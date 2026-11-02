# temperature_0017

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **C** — 90

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. 25
B. 41
C. 90
D. 59
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

> The exact 299-aa sequence matches the UniProt entry, which reports an optimum temperature of 90°C for phosphoglucose isomerase activity, with experimental evidence attributed to PubMed 39208883. This supports choice C, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a defensible way to distinguish an exact optimum of 90°C from the other listed temperatures. General sequence-based thermal tendencies would not establish this particular measured value.


**Missing item-specific fact**

> The protein-specific experimental temperature optimum (reported as 90°C), or an external identification of the protein and its associated measurement.


**Reason**

> The protein identity, organism, and temperature measurement are absent from the evaluated input. Recognizing or looking up this sequence could supply the answer, but that is item-specific lookup rather than reasoning from the provided information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The system wording describes thermal categories, but the choices are numeric temperatures. Interpreting them as candidate optimum temperatures, the cited evidence distinguishes 90°C.


### Important caveats

- The reported optimum is specifically for phosphoglucose isomerase activity, not an unrestricted measure of stability or thermal category.
- The source sequence match is exact, including in the checked historical entry; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to distinguish an exact optimum of 90°C from the other listed temperatures. General sequence-based thermal tendencies would not establish this particular measured value.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental temperature optimum (reported as 90°C), or an external identification of the protein and its associated measurement.",
    "reason": "The protein identity, organism, and temperature measurement are absent from the evaluated input. Recognizing or looking up this sequence could supply the answer, but that is item-specific lookup rather than reasoning from the provided information."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact 299-aa sequence matches the UniProt entry, which reports an optimum temperature of 90°C for phosphoglucose isomerase activity, with experimental evidence attributed to PubMed 39208883. This supports choice C, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reported optimum is specifically for phosphoglucose isomerase activity, not an unrestricted measure of stability or thermal category.",
    "The source sequence match is exact, including in the checked historical entry; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The system wording describes thermal categories, but the choices are numeric temperatures. Interpreting them as candidate optimum temperatures, the cited evidence distinguishes 90°C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 299-aa sequence matches the UniProt entry, which reports an optimum temperature of 90°C for phosphoglucose isomerase activity, with experimental evidence attributed to PubMed 39208883. This supports choice C, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to distinguish an exact optimum of 90°C from the other listed temperatures. General sequence-based thermal tendencies would not establish this particular measured value.",
    "missing_item_specific_fact": "The protein-specific experimental temperature optimum (reported as 90°C), or an external identification of the protein and its associated measurement.",
    "reason": "The protein identity, organism, and temperature measurement are absent from the evaluated input. Recognizing or looking up this sequence could supply the answer, but that is item-specific lookup rather than reasoning from the provided information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The system wording describes thermal categories, but the choices are numeric temperatures. Interpreting them as candidate optimum temperatures, the cited evidence distinguishes 90°C."
  },
  "important_caveats": [
    "The reported optimum is specifically for phosphoglucose isomerase activity, not an unrestricted measure of stability or thermal category.",
    "The source sequence match is exact, including in the checked historical entry; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry A3MTR6 (PGMI_PYRCJ) from Pyrobaculum calidifontis explicitly annotates: 'Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity)' with experimental evidence code ECO:0000269 from PubMed:39208883 (Maqsood et al., 2024). The sequence matches perfectly (SHA256 identical, 299 AA). The 90°C value is an experimentally determined optimum, not a computational prediction.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence shows elevated charged-residue content (K, E, R, D) and patterns consistent with thermophilic salt-bridge networks, which could narrow the answer away from 25°C (mesophilic) and 41°C (moderate thermophilic). However, distinguishing 90°C (hyperthermophilic) from 59°C (thermophilic) requires knowing the organism is Pyrobaculum calidifontis, a hyperthermophilic archaeon growing at ~90°C, or having access to the specific experimental measurement. General sequence-composition heuristics (charged residue ratio, proline content, loop length) can indicate 'thermophilic' broadly but cannot reliably separate 59 from 90 without organism context.


**Missing item-specific fact**

> The organism identity (Pyrobaculum calidifontis, a hyperthermophilic archaeon) or the experimentally determined optimum temperature of 90°C from PubMed:39208883. Without knowing the source organism is a hyperthermophile, the sequence alone does not provide a general-biology argument that cleanly separates 90°C from 59°C.


**Reason**

> While the sequence exhibits thermophilic signatures (high charged-residue density, salt-bridge-forming patterns), the precise distinction between 59°C and 90°C depends on organism-specific knowledge (Pyrobaculum is a known hyperthermophile) or the experimental measurement itself. This is not derivable from general biological reasoning about amino acid composition alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C (90)",
  "D (59)"
]
```

> Both 90°C and 59°C represent thermophilic optima. From sequence composition alone, without organism identification, a knowledgeable model could reasonably argue for either a thermophilic (59°C) or hyperthermophilic (90°C) assignment based on the degree of charged-residue enrichment. The question does not provide organism context, making the 59 vs 90 distinction dependent on external knowledge.


### Important caveats

- The UniProt annotation of 90°C is experimentally determined (ECO:0000269, PubMed:39208883, 2024 paper), not a computational prediction.
- The organism identity (Pyrobaculum calidifontis, hyperthermophilic archaeon) is not provided in the question input, making organism-based reasoning unavailable to the evaluated model.
- The sequence was deposited in 2007 but the experimental characterization (including the 90°C optimum) was published in 2024, so the annotation is relatively recent.
- The question's framing ('subtle patterns in the amino acid sequence') implies sequence-based reasoning should suffice, but in practice the precise temperature value requires organism or experimental knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows elevated charged-residue content (K, E, R, D) and patterns consistent with thermophilic salt-bridge networks, which could narrow the answer away from 25°C (mesophilic) and 41°C (moderate thermophilic). However, distinguishing 90°C (hyperthermophilic) from 59°C (thermophilic) requires knowing the organism is Pyrobaculum calidifontis, a hyperthermophilic archaeon growing at ~90°C, or having access to the specific experimental measurement. General sequence-composition heuristics (charged residue ratio, proline content, loop length) can indicate 'thermophilic' broadly but cannot reliably separate 59 from 90 without organism context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The organism identity (Pyrobaculum calidifontis, a hyperthermophilic archaeon) or the experimentally determined optimum temperature of 90°C from PubMed:39208883. Without knowing the source organism is a hyperthermophile, the sequence alone does not provide a general-biology argument that cleanly separates 90°C from 59°C.",
    "reason": "While the sequence exhibits thermophilic signatures (high charged-residue density, salt-bridge-forming patterns), the precise distinction between 59°C and 90°C depends on organism-specific knowledge (Pyrobaculum is a known hyperthermophile) or the experimental measurement itself. This is not derivable from general biological reasoning about amino acid composition alone."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (PGMI_PYRCJ) from Pyrobaculum calidifontis explicitly annotates: 'Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity)' with experimental evidence code ECO:0000269 from PubMed:39208883 (Maqsood et al., 2024). The sequence matches perfectly (SHA256 identical, 299 AA). The 90°C value is an experimentally determined optimum, not a computational prediction."
  },
  "important_caveats": [
    "The UniProt annotation of 90°C is experimentally determined (ECO:0000269, PubMed:39208883, 2024 paper), not a computational prediction.",
    "The organism identity (Pyrobaculum calidifontis, hyperthermophilic archaeon) is not provided in the question input, making organism-based reasoning unavailable to the evaluated model.",
    "The sequence was deposited in 2007 but the experimental characterization (including the 90°C optimum) was published in 2024, so the annotation is relatively recent.",
    "The question's framing ('subtle patterns in the amino acid sequence') implies sequence-based reasoning should suffice, but in practice the precise temperature value requires organism or experimental knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C (90)",
      "D (59)"
    ],
    "reason": "Both 90°C and 59°C represent thermophilic optima. From sequence composition alone, without organism identification, a knowledgeable model could reasonably argue for either a thermophilic (59°C) or hyperthermophilic (90°C) assignment based on the degree of charged-residue enrichment. The question does not provide organism context, making the 59 vs 90 distinction dependent on external knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (PGMI_PYRCJ) from Pyrobaculum calidifontis explicitly annotates: 'Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity)' with experimental evidence code ECO:0000269 from PubMed:39208883 (Maqsood et al., 2024). The sequence matches perfectly (SHA256 identical, 299 AA). The 90°C value is an experimentally determined optimum, not a computational prediction.",
    "evidence_ids": ["C5", "H3", "C1", "C3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence shows elevated charged-residue content (K, E, R, D) and patterns consistent with thermophilic salt-bridge networks, which could narrow the answer away from 25°C (mesophilic) and 41°C (moderate thermophilic). However, distinguishing 90°C (hyperthermophilic) from 59°C (thermophilic) requires knowing the organism is Pyrobaculum calidifontis, a hyperthermophilic archaeon growing at ~90°C, or having access to the specific experimental measurement. General sequence-composition heuristics (charged residue ratio, proline content, loop length) can indicate 'thermophilic' broadly but cannot reliably separate 59 from 90 without organism context.",
    "missing_item_specific_fact": "The organism identity (Pyrobaculum calidifontis, a hyperthermophilic archaeon) or the experimentally determined optimum temperature of 90°C from PubMed:39208883. Without knowing the source organism is a hyperthermophile, the sequence alone does not provide a general-biology argument that cleanly separates 90°C from 59°C.",
    "reason": "While the sequence exhibits thermophilic signatures (high charged-residue density, salt-bridge-forming patterns), the precise distinction between 59°C and 90°C depends on organism-specific knowledge (Pyrobaculum is a known hyperthermophile) or the experimental measurement itself. This is not derivable from general biological reasoning about amino acid composition alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C (90)", "D (59)"],
    "reason": "Both 90°C and 59°C represent thermophilic optima. From sequence composition alone, without organism identification, a knowledgeable model could reasonably argue for either a thermophilic (59°C) or hyperthermophilic (90°C) assignment based on the degree of charged-residue enrichment. The question does not provide organism context, making the 59 vs 90 distinction dependent on external knowledge."
  },
  "important_caveats": [
    "The UniProt annotation of 90°C is experimentally determined (ECO:0000269, PubMed:39208883, 2024 paper), not a computational prediction.",
    "The organism identity (Pyrobaculum calidifontis, hyperthermophilic archaeon) is not provided in the question input, making organism-based reasoning unavailable to the evaluated model.",
    "The sequence was deposited in 2007 but the experimental characterization (including the 90°C optimum) was published in 2024, so the annotation is relatively recent.",
    "The question's framing ('subtle patterns in the amino acid sequence') implies sequence-based reasoning should suffice, but in practice the precise temperature value requires organism or experimental knowledge."
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

**Accession:** `A3MTR6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
"A3MTR6"
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"lineage":["Archaea","Thermoproteota","Thermoprotei","Thermoproteales","Thermoproteaceae","Pyrobaculum"],"scientificName":"Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1)","taxonId":410359}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39208883","source":"PubMed"}],"value":"Glucose-6-phosphate isomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"GPI"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Mannose-6-phosphate isomerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"5.3.1.8"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"5.3.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39208883","source":"PubMed"}],"value":"Bifunctional phosphoglucose/phosphomannose isomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Bifunctional PGI/PMI"}]}}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"maximumVelocities":[{"enzyme":"enzyme with glucose 6-phosphate as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"unit":"umol/min/mg","velocity":290.0},{"enzyme":"enzyme with mannose 6-phosphate as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"unit":"umol/min/mg","velocity":235.0},{"enzyme":"enzyme with fructose 6-phosphate as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"unit":"umol/min/mg","velocity":240.0}],"michaelisConstants":[{"constant":0.33,"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"substrate":"glucose 6-phosphate","unit":"mM"},{"constant":0.34,"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"substrate":"mannose 6-phosphate","unit":"mM"},{"constant":0.29,"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"substrate":"fructose 6-phosphate","unit":"mM"}],"note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"kcat is 315 sec(-1) with glucose 6-phosphate as substrate. kcat is 240 sec(-1) with mannose 6-phosphate as substrate. kcat is 265 sec(-1) with fructose 6-phosphate as substrate."}]}},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"Optimum pH is 8.5 (for phosphoglucose isomerase activity) (PubMed:39208883). Activity is reduced significantly below pH 8.0 and above 9.0 (PubMed:39208883)."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity) (PubMed:39208883). Displays high thermostability with a half-life of about 50 minutes at 100 degrees Celsius (PubMed:39208883)."}]}}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)  
**Locator:** `lines 55-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:27:04.156488+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=0.33 mM for glucose 6-phosphate {ECO:0000269|PubMed:39208883};
CC         KM=0.34 mM for mannose 6-phosphate {ECO:0000269|PubMed:39208883};
CC         KM=0.29 mM for fructose 6-phosphate {ECO:0000269|PubMed:39208883};
CC         Vmax=290 umol/min/mg enzyme with glucose 6-phosphate as substrate
CC         {ECO:0000269|PubMed:39208883};
CC         Vmax=235 umol/min/mg enzyme with mannose 6-phosphate as substrate
CC         {ECO:0000269|PubMed:39208883};
CC         Vmax=240 umol/min/mg enzyme with fructose 6-phosphate as substrate
CC         {ECO:0000269|PubMed:39208883};
CC         Note=kcat is 315 sec(-1) with glucose 6-phosphate as substrate. kcat
CC         is 240 sec(-1) with mannose 6-phosphate as substrate. kcat is 265
CC         sec(-1) with fructose 6-phosphate as substrate.
CC         {ECO:0000269|PubMed:39208883};
CC       pH dependence:
CC         Optimum pH is 8.5 (for phosphoglucose isomerase activity)
CC         (PubMed:39208883). Activity is reduced significantly below pH 8.0 and
CC         above 9.0 (PubMed:39208883). {ECO:0000269|PubMed:39208883};
CC       Temperature dependence:
CC         Optimum temperature is 90 degrees Celsius (for phosphoglucose
CC         isomerase activity) (PubMed:39208883). Displays high thermostability
CC         with a half-life of about 50 minutes at 100 degrees Celsius
CC         (PubMed:39208883). {ECO:0000269|PubMed:39208883};
```

Source SHA-256: `9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
