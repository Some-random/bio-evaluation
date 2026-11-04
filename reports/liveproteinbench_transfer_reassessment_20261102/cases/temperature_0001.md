# temperature_0001

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0001.txt)

**Task:** `temperature`  
**Expected answer:** **C** — 30

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. 72
B. 40
C. 30
D. 41
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt record reports an optimum temperature of 30 °C, citing experimental evidence (ECO:0000269). This supports choice C for the supplied sequence.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence-based knowledge could make the extreme 72 °C option unlikely for a typical soluble enzyme, but the sequence and choices do not provide a credible transferable basis for distinguishing an optimum of 30 °C from 40 or 41 °C.


**Missing item-specific fact**

> The measured temperature optimum for this exact enzyme under the relevant assay conditions.


**Reason**

> The key is supported by an experimental temperature-optimum annotation, but no organism, assay context, or other input establishes that measurement. General sequence or family-level tendencies may suggest a broad temperature range, not meaningfully select 30 over the nearby alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The numeric options are distinct candidate optima; the lack of enough input to infer which is correct is an answerability limitation, not evidence that multiple options are correct.


### Important caveats

- The prompt describes thermal adaptation in terms of stability and function, whereas the supporting evidence is an experimentally annotated enzyme activity optimum; these properties are related but not identical.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence-based knowledge could make the extreme 72 °C option unlikely for a typical soluble enzyme, but the sequence and choices do not provide a credible transferable basis for distinguishing an optimum of 30 °C from 40 or 41 °C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured temperature optimum for this exact enzyme under the relevant assay conditions.",
    "reason": "The key is supported by an experimental temperature-optimum annotation, but no organism, assay context, or other input establishes that measurement. General sequence or family-level tendencies may suggest a broad temperature range, not meaningfully select 30 over the nearby alternatives."
  },
  "case_id": "temperature_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record reports an optimum temperature of 30 °C, citing experimental evidence (ECO:0000269). This supports choice C for the supplied sequence."
  },
  "important_caveats": [
    "The prompt describes thermal adaptation in terms of stability and function, whereas the supporting evidence is an experimentally annotated enzyme activity optimum; these properties are related but not identical."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The numeric options are distinct candidate optima; the lack of enough input to infer which is correct is an answerability limitation, not evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record reports an optimum temperature of 30 °C, citing experimental evidence (ECO:0000269). This supports choice C for the supplied sequence.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence-based knowledge could make the extreme 72 °C option unlikely for a typical soluble enzyme, but the sequence and choices do not provide a credible transferable basis for distinguishing an optimum of 30 °C from 40 or 41 °C.",
    "missing_item_specific_fact": "The measured temperature optimum for this exact enzyme under the relevant assay conditions.",
    "reason": "The key is supported by an experimental temperature-optimum annotation, but no organism, assay context, or other input establishes that measurement. General sequence or family-level tendencies may suggest a broad temperature range, not meaningfully select 30 over the nearby alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The numeric options are distinct candidate optima; the lack of enough input to infer which is correct is an answerability limitation, not evidence that multiple options are correct."
  },
  "important_caveats": [
    "The prompt describes thermal adaptation in terms of stability and function, whereas the supporting evidence is an experimentally annotated enzyme activity optimum; these properties are related but not identical."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A075D6M1) for this protein (Norajmaline N-methyltransferase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:27122470). The sequence matches the benchmark input exactly (292 AA, SHA256 confirmed). This is a direct experimental measurement, not computational inference.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unusually high number of Cys residues (~8-9 in 292 residues, ~3%), which is atypical for thermophilic proteins (which minimize Cys to avoid thermolability) but characteristic of plant proteins that form structural disulfide bonds. The overall amino acid composition shows moderate charged-residue content without the extreme salt-bridge density expected for 72°C thermophiles, clearly eliminating option A. The high Cys count, combined with the methyltransferase Rossmann-fold motifs (GCGVGG, VGGTCVHVAK), is more consistent with a plant enzyme than a thermotolerant bacterial enzyme. Plant enzymes cluster around 25-35°C optimal temperatures because plants are sessile mesophiles operating at ambient temperatures; 40-41°C optima are rare in plant enzymes and more typical of thermotolerant bacteria. Thus, the inference 'high Cys + methyltransferase architecture → likely plant enzyme → ~30°C optimum' meaningfully distinguishes C (30) from B (40) and D (41), though this is a probabilistic family-level inference rather than a certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of 72°C is strongly supported by absence of thermophilic sequence signatures. The distinction between 30°C and 40/41°C relies on the probabilistic inference that high Cys content and plant-like methyltransferase architecture indicate a plant enzyme with a lower mesophilic optimum. This is a legitimate family-level and composition-based transfer from knowledge of plant vs. bacterial enzyme thermal ranges, though it does not constitute a definitive proof and would benefit from organism identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B (40) and D (41) differ by only 1°C and are both within the mesophilic range. If the correct answer were in the 40s, distinguishing between them would be essentially impossible from sequence alone. Since the answer is 30, this ambiguity is less consequential, but a model uncertain about the plant-vs-bacterium inference could reasonably select either 40 or 41 as a 'mesophilic but not cold-adapted' choice.


### Important caveats

- The organism identity (Rauvolfia serpentina, a tropical plant) was not provided to the evaluated model; the inference that this is a plant protein relies on sequence composition features (high Cys, methyltransferase motifs) rather than explicit organism labeling.
- The distinction between 30°C and 40/41°C is probabilistic: some plant enzymes can have optima near 35-40°C, and some mesophilic bacteria have optima near 30°C. The argument favors 30 but does not exclude 40/41 with certainty.
- The experimental measurement (30°C) comes from in vitro enzyme assays (PubMed:27122470) and represents the measured optimum under specific assay conditions, which may differ from the organism's native thermal environment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unusually high number of Cys residues (~8-9 in 292 residues, ~3%), which is atypical for thermophilic proteins (which minimize Cys to avoid thermolability) but characteristic of plant proteins that form structural disulfide bonds. The overall amino acid composition shows moderate charged-residue content without the extreme salt-bridge density expected for 72°C thermophiles, clearly eliminating option A. The high Cys count, combined with the methyltransferase Rossmann-fold motifs (GCGVGG, VGGTCVHVAK), is more consistent with a plant enzyme than a thermotolerant bacterial enzyme. Plant enzymes cluster around 25-35°C optimal temperatures because plants are sessile mesophiles operating at ambient temperatures; 40-41°C optima are rare in plant enzymes and more typical of thermotolerant bacteria. Thus, the inference 'high Cys + methyltransferase architecture → likely plant enzyme → ~30°C optimum' meaningfully distinguishes C (30) from B (40) and D (41), though this is a probabilistic family-level inference rather than a certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of 72°C is strongly supported by absence of thermophilic sequence signatures. The distinction between 30°C and 40/41°C relies on the probabilistic inference that high Cys content and plant-like methyltransferase architecture indicate a plant enzyme with a lower mesophilic optimum. This is a legitimate family-level and composition-based transfer from knowledge of plant vs. bacterial enzyme thermal ranges, though it does not constitute a definitive proof and would benefit from organism identification."
  },
  "case_id": "temperature_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A075D6M1) for this protein (Norajmaline N-methyltransferase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:27122470). The sequence matches the benchmark input exactly (292 AA, SHA256 confirmed). This is a direct experimental measurement, not computational inference."
  },
  "important_caveats": [
    "The organism identity (Rauvolfia serpentina, a tropical plant) was not provided to the evaluated model; the inference that this is a plant protein relies on sequence composition features (high Cys, methyltransferase motifs) rather than explicit organism labeling.",
    "The distinction between 30°C and 40/41°C is probabilistic: some plant enzymes can have optima near 35-40°C, and some mesophilic bacteria have optima near 30°C. The argument favors 30 but does not exclude 40/41 with certainty.",
    "The experimental measurement (30°C) comes from in vitro enzyme assays (PubMed:27122470) and represents the measured optimum under specific assay conditions, which may differ from the organism's native thermal environment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B (40) and D (41) differ by only 1°C and are both within the mesophilic range. If the correct answer were in the 40s, distinguishing between them would be essentially impossible from sequence alone. Since the answer is 30, this ambiguity is less consequential, but a model uncertain about the plant-vs-bacterium inference could reasonably select either 40 or 41 as a 'mesophilic but not cold-adapted' choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A075D6M1) for this protein (Norajmaline N-methyltransferase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:27122470). The sequence matches the benchmark input exactly (292 AA, SHA256 confirmed). This is a direct experimental measurement, not computational inference.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unusually high number of Cys residues (~8-9 in 292 residues, ~3%), which is atypical for thermophilic proteins (which minimize Cys to avoid thermolability) but characteristic of plant proteins that form structural disulfide bonds. The overall amino acid composition shows moderate charged-residue content without the extreme salt-bridge density expected for 72°C thermophiles, clearly eliminating option A. The high Cys count, combined with the methyltransferase Rossmann-fold motifs (GCGVGG, VGGTCVHVAK), is more consistent with a plant enzyme than a thermotolerant bacterial enzyme. Plant enzymes cluster around 25-35°C optimal temperatures because plants are sessile mesophiles operating at ambient temperatures; 40-41°C optima are rare in plant enzymes and more typical of thermotolerant bacteria. Thus, the inference 'high Cys + methyltransferase architecture → likely plant enzyme → ~30°C optimum' meaningfully distinguishes C (30) from B (40) and D (41), though this is a probabilistic family-level inference rather than a certainty.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of 72°C is strongly supported by absence of thermophilic sequence signatures. The distinction between 30°C and 40/41°C relies on the probabilistic inference that high Cys content and plant-like methyltransferase architecture indicate a plant enzyme with a lower mesophilic optimum. This is a legitimate family-level and composition-based transfer from knowledge of plant vs. bacterial enzyme thermal ranges, though it does not constitute a definitive proof and would benefit from organism identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B (40) and D (41) differ by only 1°C and are both within the mesophilic range. If the correct answer were in the 40s, distinguishing between them would be essentially impossible from sequence alone. Since the answer is 30, this ambiguity is less consequential, but a model uncertain about the plant-vs-bacterium inference could reasonably select either 40 or 41 as a 'mesophilic but not cold-adapted' choice."
  },
  "important_caveats": [
    "The organism identity (Rauvolfia serpentina, a tropical plant) was not provided to the evaluated model; the inference that this is a plant protein relies on sequence composition features (high Cys, methyltransferase motifs) rather than explicit organism labeling.",
    "The distinction between 30°C and 40/41°C is probabilistic: some plant enzymes can have optima near 35-40°C, and some mesophilic bacteria have optima near 30°C. The argument favors 30 but does not exclude 40/41 with certainty.",
    "The experimental measurement (30°C) comes from in vitro enzyme assays (PubMed:27122470) and represents the measured optimum under specific assay conditions, which may differ from the organism's native thermal environment."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 292,
  "benchmark_sequence_sha256": "1d64f8836757be86aab995d1a14b3feb88531eb4212b35fbfd7dbdc62567e997",
  "current_entry_audit": {
    "entryVersion": 38,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 292,
  "current_source_sequence_sha256": "1d64f8836757be86aab995d1a14b3feb88531eb4212b35fbfd7dbdc62567e997",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A075D6M1",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "selected_historical_source_sequence_length": 292,
  "selected_historical_source_sequence_sha256": "1d64f8836757be86aab995d1a14b3feb88531eb4212b35fbfd7dbdc62567e997",
  "selected_historical_version": {
    "accession": "A0A075D6M1",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NNMT_RAUSE",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A075D6M1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":38,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHH02781.1\",\"source\":\"EMBL\"}],\"value\":\"Gamma-tocopherol-like methyltransferase NNMT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.392\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Norajmaline N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsNNMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with S-adenosyl-L-methionine as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"unit\":\"pmol/sec/mg\",\"velocity\":96.9},{\"enzyme\":\"enzyme with norajmaline as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"unit\":\"pmol/sec/mg\",\"velocity\":111.2}],\"michaelisConstants\":[{\"constant\":3.5,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"substrate\":\"S-adenosyl-L-methionine\",\"unit\":\"uM\"},{\"constant\":4.4,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"substrate\":\"norajmaline\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"kcat is 1.8 sec(-1) with S-adenosyl-L-methionine as substrate (PubMed:27122470). kcat is 2.1 sec(-1) with norajmaline as substrate (PubMed:27122470).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7.5.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 30 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Cazares-Flores P.\",\"Levac D.\",\"De Luca V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27122470\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.13186\"}],\"citationType\":\"journal article\",\"firstPage\":\"335\",\"id\":\"27122470\",\"journal\":\"Plant J.\",\"lastPage\":\"342\",\"publicationDate\":\"2016\",\"title\":\"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.\",\"volume\":\"87\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   NNMT_RAUSE              Reviewed;         292 AA.\nAC   A0A075D6M1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};\nDE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};\nDE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};\nGN   Name=NNMT {ECO:0000303|PubMed:38212296};\nGN   Synonyms=Rs9447 {ECO:0000312|EMBL:AHH02781.1};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRX   PubMed=27122470; DOI=10.1111/tpj.13186;\nRA   Cazares-Flores P., Levac D., De Luca V.;\nRT   \"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta\nRT   -methylajmaline biosynthesis belong to a gene family derived from gamma-\nRT   tocopherol C-methyltransferase.\";\nRL   Plant J. 87:335-342(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=3.5 uM for S-adenosyl-L-methionine {ECO:0000269|PubMed:27122470};\nCC         KM=4.4 uM for norajmaline {ECO:0000269|PubMed:27122470};\nCC         Vmax=96.9 pmol/sec/mg enzyme with S-adenosyl-L-methionine as\nCC         substrate {ECO:0000269|PubMed:27122470};\nCC         Vmax=111.2 pmol/sec/mg enzyme with norajmaline as substrate\nCC         {ECO:0000269|PubMed:27122470};\nCC         Note=kcat is 1.8 sec(-1) with S-adenosyl-L-methionine as substrate\nCC         (PubMed:27122470). kcat is 2.1 sec(-1) with norajmaline as substrate\nCC         (PubMed:27122470). {ECO:0000269|PubMed:27122470};\nCC       pH dependence:\nCC         Optimum pH is 7.5. {ECO:0000269|PubMed:27122470};\nCC       Temperature dependence:\nCC         Optimum temperature is 30 degrees Celsius.\nCC         {ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
