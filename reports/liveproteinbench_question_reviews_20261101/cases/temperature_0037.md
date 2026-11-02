# temperature_0037

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **B** — 37-42

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 26-37
B. 37-42
C. 22-33
D. 40-54
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

> The sequence matches the UniProt entry, whose experimentally supported temperature annotation reports an optimum between 37 and 42 °C, matching choice B. The entry also reports relatively constant activity from 37 to 56 °C, which is distinct from the stated optimum.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein’s temperature range cannot be read directly from its sequence. General biological knowledge might suggest a mesophilic context, but the original input supplies neither organism nor experimental temperature data and does not distinguish these precise ranges.


**Missing item-specific fact**

> The experimentally reported optimum temperature range for this specific protein.


**Reason**

> Selecting B requires a protein-specific measurement or annotation absent from the input; generic sequence-based thermal-adaptation heuristics do not justify this precise interval.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The reported optimum range, 37–42 °C, matches B, but overlaps D at 40–42 °C. Without a single optimum value or a rule for choosing among overlapping ranges, a value within that overlap fits both.


### Important caveats

- The experimental annotation applies to the sequence-matched protein; the exact author source snapshot is unknown.
- The annotation also reports relatively constant activity over a broader range, which should not be conflated with the optimum.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein’s temperature range cannot be read directly from its sequence. General biological knowledge might suggest a mesophilic context, but the original input supplies neither organism nor experimental temperature data and does not distinguish these precise ranges.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally reported optimum temperature range for this specific protein.",
    "reason": "Selecting B requires a protein-specific measurement or annotation absent from the input; generic sequence-based thermal-adaptation heuristics do not justify this precise interval."
  },
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose experimentally supported temperature annotation reports an optimum between 37 and 42 °C, matching choice B. The entry also reports relatively constant activity from 37 to 56 °C, which is distinct from the stated optimum."
  },
  "important_caveats": [
    "The experimental annotation applies to the sequence-matched protein; the exact author source snapshot is unknown.",
    "The annotation also reports relatively constant activity over a broader range, which should not be conflated with the optimum."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The reported optimum range, 37–42 °C, matches B, but overlaps D at 40–42 °C. Without a single optimum value or a rule for choosing among overlapping ranges, a value within that overlap fits both."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose experimentally supported temperature annotation reports an optimum between 37 and 42 °C, matching choice B. The entry also reports relatively constant activity from 37 to 56 °C, which is distinct from the stated optimum.",
    "evidence_ids": ["C1", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein’s temperature range cannot be read directly from its sequence. General biological knowledge might suggest a mesophilic context, but the original input supplies neither organism nor experimental temperature data and does not distinguish these precise ranges.",
    "missing_item_specific_fact": "The experimentally reported optimum temperature range for this specific protein.",
    "reason": "Selecting B requires a protein-specific measurement or annotation absent from the input; generic sequence-based thermal-adaptation heuristics do not justify this precise interval."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The reported optimum range, 37–42 °C, matches B, but overlaps D at 40–42 °C. Without a single optimum value or a rule for choosing among overlapping ranges, a value within that overlap fits both."
  },
  "important_caveats": [
    "The experimental annotation applies to the sequence-matched protein; the exact author source snapshot is unknown.",
    "The annotation also reports relatively constant activity over a broader range, which should not be conflated with the optimum."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9RHD7 (WbpO, Pseudomonas aeruginosa) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is between 37 and 42 degrees Celsius' (ECO:0000269, PubMed:18065759). The sequence SHA256 matches the benchmark sequence exactly. This is experimental evidence (ECO:0000269), not computational inference. Choice B (37-42) matches this annotation verbatim.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that P. aeruginosa is a mesophilic organism (optimal growth ~37°C), so its enzymes should have optima near 37°C, favoring B over C (psychrophilic 22-33) and D (thermophilic 40-54). However, this reasoning cannot cleanly distinguish B (37-42) from A (26-37), since both ranges overlap with mesophilic biology. Moreover, the UniProt annotation notes activity is 'relatively constant over 37 to 56°C,' which makes D partially defensible without the specific 'optimum' qualifier. The precise boundary at 37 vs 26 as the lower end of the optimum is an experimental measurement.


**Missing item-specific fact**

> The specific experimental finding (PubMed:18065759) that the optimum temperature of WbpO is 'between 37 and 42 degrees Celsius' rather than 'between 26 and 37 degrees Celsius.' The organism identity (P. aeruginosa) is not provided in the question input, and even if inferred, the fine-grained distinction between 26-37 and 37-42 requires the item-specific experimental measurement.


**Reason**

> While general knowledge that P. aeruginosa is mesophilic could eliminate extreme ranges (C, D), the critical discrimination between A (26-37) and B (37-42) depends on a specific experimental optimum-temperature measurement not derivable from sequence composition heuristics alone. The sequence does not encode a precise 37°C lower boundary for the optimum.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Choice A (26-37) overlaps with the mesophilic growth range of P. aeruginosa and is a plausible inference for a mesophilic enzyme without the specific experimental optimum. Choice D (40-54) is partially defensible because the annotation states activity is 'relatively constant over 37 to 56°C,' meaning the enzyme functions well in that range, even though the stated optimum is 37-42. The question asks for 'thermal adaptation category' which could be interpreted as the functional range rather than the narrow optimum.


### Important caveats

- The organism identity (Pseudomonas aeruginosa) is not stated in the question; the model must infer it from sequence, which itself is a lookup/memorization task.
- The UniProt annotation distinguishes 'optimum temperature' (37-42°C) from the broader functional range (37-56°C). The question's phrasing 'thermal adaptation category' is ambiguous between these two concepts.
- The evidence codes are ECO:0000269 (experimental evidence), confirming this is a measured value, not a prediction.
- The historical UniProt entry (version 111, released 2026-01-28) already contained this annotation, so it was available at the benchmark construction date.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that P. aeruginosa is a mesophilic organism (optimal growth ~37°C), so its enzymes should have optima near 37°C, favoring B over C (psychrophilic 22-33) and D (thermophilic 40-54). However, this reasoning cannot cleanly distinguish B (37-42) from A (26-37), since both ranges overlap with mesophilic biology. Moreover, the UniProt annotation notes activity is 'relatively constant over 37 to 56°C,' which makes D partially defensible without the specific 'optimum' qualifier. The precise boundary at 37 vs 26 as the lower end of the optimum is an experimental measurement.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental finding (PubMed:18065759) that the optimum temperature of WbpO is 'between 37 and 42 degrees Celsius' rather than 'between 26 and 37 degrees Celsius.' The organism identity (P. aeruginosa) is not provided in the question input, and even if inferred, the fine-grained distinction between 26-37 and 37-42 requires the item-specific experimental measurement.",
    "reason": "While general knowledge that P. aeruginosa is mesophilic could eliminate extreme ranges (C, D), the critical discrimination between A (26-37) and B (37-42) depends on a specific experimental optimum-temperature measurement not derivable from sequence composition heuristics alone. The sequence does not encode a precise 37°C lower boundary for the optimum."
  },
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9RHD7 (WbpO, Pseudomonas aeruginosa) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is between 37 and 42 degrees Celsius' (ECO:0000269, PubMed:18065759). The sequence SHA256 matches the benchmark sequence exactly. This is experimental evidence (ECO:0000269), not computational inference. Choice B (37-42) matches this annotation verbatim."
  },
  "important_caveats": [
    "The organism identity (Pseudomonas aeruginosa) is not stated in the question; the model must infer it from sequence, which itself is a lookup/memorization task.",
    "The UniProt annotation distinguishes 'optimum temperature' (37-42°C) from the broader functional range (37-56°C). The question's phrasing 'thermal adaptation category' is ambiguous between these two concepts.",
    "The evidence codes are ECO:0000269 (experimental evidence), confirming this is a measured value, not a prediction.",
    "The historical UniProt entry (version 111, released 2026-01-28) already contained this annotation, so it was available at the benchmark construction date."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Choice A (26-37) overlaps with the mesophilic growth range of P. aeruginosa and is a plausible inference for a mesophilic enzyme without the specific experimental optimum. Choice D (40-54) is partially defensible because the annotation states activity is 'relatively constant over 37 to 56°C,' meaning the enzyme functions well in that range, even though the stated optimum is 37-42. The question asks for 'thermal adaptation category' which could be interpreted as the functional range rather than the narrow optimum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9RHD7 (WbpO, Pseudomonas aeruginosa) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is between 37 and 42 degrees Celsius' (ECO:0000269, PubMed:18065759). The sequence SHA256 matches the benchmark sequence exactly. This is experimental evidence (ECO:0000269), not computational inference. Choice B (37-42) matches this annotation verbatim.",
    "evidence_ids": ["C5", "C6", "C7", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that P. aeruginosa is a mesophilic organism (optimal growth ~37°C), so its enzymes should have optima near 37°C, favoring B over C (psychrophilic 22-33) and D (thermophilic 40-54). However, this reasoning cannot cleanly distinguish B (37-42) from A (26-37), since both ranges overlap with mesophilic biology. Moreover, the UniProt annotation notes activity is 'relatively constant over 37 to 56°C,' which makes D partially defensible without the specific 'optimum' qualifier. The precise boundary at 37 vs 26 as the lower end of the optimum is an experimental measurement.",
    "missing_item_specific_fact": "The specific experimental finding (PubMed:18065759) that the optimum temperature of WbpO is 'between 37 and 42 degrees Celsius' rather than 'between 26 and 37 degrees Celsius.' The organism identity (P. aeruginosa) is not provided in the question input, and even if inferred, the fine-grained distinction between 26-37 and 37-42 requires the item-specific experimental measurement.",
    "reason": "While general knowledge that P. aeruginosa is mesophilic could eliminate extreme ranges (C, D), the critical discrimination between A (26-37) and B (37-42) depends on a specific experimental optimum-temperature measurement not derivable from sequence composition heuristics alone. The sequence does not encode a precise 37°C lower boundary for the optimum."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Choice A (26-37) overlaps with the mesophilic growth range of P. aeruginosa and is a plausible inference for a mesophilic enzyme without the specific experimental optimum. Choice D (40-54) is partially defensible because the annotation states activity is 'relatively constant over 37 to 56°C,' meaning the enzyme functions well in that range, even though the stated optimum is 37-42. The question asks for 'thermal adaptation category' which could be interpreted as the functional range rather than the narrow optimum."
  },
  "important_caveats": [
    "The organism identity (Pseudomonas aeruginosa) is not stated in the question; the model must infer it from sequence, which itself is a lookup/memorization task.",
    "The UniProt annotation distinguishes 'optimum temperature' (37-42°C) from the broader functional range (37-56°C). The question's phrasing 'thermal adaptation category' is ambiguous between these two concepts.",
    "The evidence codes are ECO:0000269 (experimental evidence), confirming this is a measured value, not a prediction.",
    "The historical UniProt entry (version 111, released 2026-01-28) already contained this annotation, so it was available at the benchmark construction date."
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

**Accession:** `Q9RHD7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
"Q9RHD7"
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"michaelisConstants":[{"constant":0.047,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"UDP-GlcNAc","unit":"mM"},{"constant":22.2,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"UDP-GlcNAc (refolded enzyme, in the presence of NAD(+))","unit":"mM"},{"constant":0.27,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"UDP-GalNAc","unit":"mM"},{"constant":7.79,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"UDP-GalNAc (refolded enzyme, in the presence of NAD(+))","unit":"mM"},{"constant":0.23,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"NAD(+)","unit":"mM"},{"constant":0.65,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"NAD(+) (refolded enzyme)","unit":"mM"},{"constant":3.7,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"NADP(+)","unit":"mM"},{"constant":0.44,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"NADP(+) (refolded enzyme)","unit":"mM"}],"note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"kcat is 110 min(-1) with UDP-GlcNAc as substrate. kcat is 0.69 min(-1) with UDP-GalNAc as substrate. kcat is 110 min(-1) with NAD(+) as substrate. kcat is 0.71 min(-1) with NADP(+) as substrate (PubMed:18065759). kcat is 5.5 min(-1) with UDP-GlcNAc as substrate (refolded enzyme, in the presence of NAD(+)). kcat is 47.8 min(-1) with UDP-GalNAc as substrate (refolded enzyme, in the presence of NAD(+)). kcat is 26.8 min(-1) with NAD(+) as substrate (refolded enzyme). kcat is 16.9 min(-1) with NADP(+) as substrate (refolded enzyme) (PubMed:10931835)."}]}},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"Optimum pH is 8.5."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"Activity is relatively constant over a wide temperature range from 37 to 56 degrees Celsius (PubMed:10931835). Optimum temperature is between 37 and 42 degrees Celsius (PubMed:18065759)."}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Zhao X.","Creuzenet C.","Belanger M.","Egbosimba E.","Li J.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"10931835"},{"database":"DOI","id":"10.1074/jbc.m004191200"}],"citationType":"journal article","firstPage":"33252","id":"10931835","journal":"J. Biol. Chem.","lastPage":"33259","publicationDate":"2000","title":"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas aeruginosa serotype O6.","volume":"275"},"referenceComments":[{"type":"STRAIN","value":"Serotype O6"}],"referenceNumber":4,"referencePositions":["FUNCTION","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Miller W.L.","Matewish M.J.","McNally D.J.","Ishiyama N.","Anderson E.M.","Brewer D.","Brisson J.R.","Berghuis A.M.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"18065759"},{"database":"DOI","id":"10.1074/jbc.m708894200"}],"citationType":"journal article","firstPage":"3507","id":"18065759","journal":"J. Biol. Chem.","lastPage":"3518","publicationDate":"2008","title":"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.","volume":"283"},"referenceComments":[{"type":"STRAIN","value":"PAK / Serotype O6"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 78-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=0.047 mM for UDP-GlcNAc {ECO:0000269|PubMed:18065759};
CC         KM=22.2 mM for UDP-GlcNAc (refolded enzyme, in the presence of
CC         NAD(+)) {ECO:0000269|PubMed:10931835};
CC         KM=0.27 mM for UDP-GalNAc {ECO:0000269|PubMed:18065759};
CC         KM=7.79 mM for UDP-GalNAc (refolded enzyme, in the presence of
CC         NAD(+)) {ECO:0000269|PubMed:10931835};
CC         KM=0.23 mM for NAD(+) {ECO:0000269|PubMed:18065759};
CC         KM=0.65 mM for NAD(+) (refolded enzyme)
CC         {ECO:0000269|PubMed:10931835};
CC         KM=3.7 mM for NADP(+) {ECO:0000269|PubMed:18065759};
CC         KM=0.44 mM for NADP(+) (refolded enzyme)
CC         {ECO:0000269|PubMed:10931835};
CC         Note=kcat is 110 min(-1) with UDP-GlcNAc as substrate. kcat is 0.69
CC         min(-1) with UDP-GalNAc as substrate. kcat is 110 min(-1) with NAD(+)
CC         as substrate. kcat is 0.71 min(-1) with NADP(+) as substrate
CC         (PubMed:18065759). kcat is 5.5 min(-1) with UDP-GlcNAc as substrate
CC         (refolded enzyme, in the presence of NAD(+)). kcat is 47.8 min(-1)
CC         with UDP-GalNAc as substrate (refolded enzyme, in the presence of
CC         NAD(+)). kcat is 26.8 min(-1) with NAD(+) as substrate (refolded
CC         enzyme). kcat is 16.9 min(-1) with NADP(+) as substrate (refolded
CC         enzyme) (PubMed:10931835). {ECO:0000269|PubMed:10931835,
CC         ECO:0000269|PubMed:18065759};
CC       pH dependence:
CC         Optimum pH is 8.5. {ECO:0000269|PubMed:10931835,
CC         ECO:0000269|PubMed:18065759};
CC       Temperature dependence:
CC         Activity is relatively constant over a wide temperature range from 37
CC         to 56 degrees Celsius (PubMed:10931835). Optimum temperature is
CC         between 37 and 42 degrees Celsius (PubMed:18065759).
CC         {ECO:0000269|PubMed:10931835, ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
