# temperature_0034

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0034.txt)

**Task:** `temperature`  
**Expected answer:** **C** — 37-42

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMSRYEELRKELPAQPKVWLITGVAGFIGSNLLETLLKLDQKVVGLDNFATGHQRNLDEVRSLVSEKQWSNFKFIQGDIRNLDDCNNACAGVDYVLHQAALGSVPRSINDPITSNATNIDGFLNMLIAARDAKVQSFTYAASSSTYGDHPGLPKVEDTIGKPLSPYAVTKYVNELYADVFSRCYGFSTIGLRYFNVFGRRQDPNGAYAAVIPKWTSSMIQGDDVYINGDGETSRDFCYIENTVQANLLAATAGLDARNQVYNIAVGGRTSLNQLFFALRDGLAENGVSYHREPVYRDFREGDVRHSLADISKAAKLLGYAPKYDVSAGVALAMPWYIMFLK

[Multiple Choices]
A. 49-61
B. 31-45
C. 37-42
D. 42-50
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

> The sequence matches the historical UniProt record, which reports an experimentally supported optimum temperature between 37 and 42 °C. This supports choice C as the reported range.

Citations as saved: [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The experimentally measured optimum temperature range for this exact protein.


**Reason**

> The sequence may support a broad expectation of a non-extremophilic enzyme, but that does not distinguish the narrow 37–42 °C interval from the broader overlapping 31–45 °C option. Selecting the specifically reported range requires a measurement or annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> If an option is interpreted as a temperature band containing the optimum, both 31–45 °C and 37–42 °C contain the reported range. Choice C is the exact reported interval, but the question does not clarify whether broader containing bands should be rejected.


### Important caveats

- The evidence is a database annotation citing biochemical characterization; it is not evidence that the evaluated model saw that annotation.
- The reviewer source sequence matches the input, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature range for this exact protein.",
    "reason": "The sequence may support a broad expectation of a non-extremophilic enzyme, but that does not distinguish the narrow 37–42 °C interval from the broader overlapping 31–45 °C option. Selecting the specifically reported range requires a measurement or annotation for this protein."
  },
  "case_id": "temperature_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, which reports an experimentally supported optimum temperature between 37 and 42 °C. This supports choice C as the reported range."
  },
  "important_caveats": [
    "The evidence is a database annotation citing biochemical characterization; it is not evidence that the evaluated model saw that annotation.",
    "The reviewer source sequence matches the input, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "If an option is interpreted as a temperature band containing the optimum, both 31–45 °C and 37–42 °C contain the reported range. Choice C is the exact reported interval, but the question does not clarify whether broader containing bands should be rejected."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, which reports an experimentally supported optimum temperature between 37 and 42 °C. This supports choice C as the reported range.",
    "evidence_ids": ["H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The experimentally measured optimum temperature range for this exact protein.",
    "reason": "The sequence may support a broad expectation of a non-extremophilic enzyme, but that does not distinguish the narrow 37–42 °C interval from the broader overlapping 31–45 °C option. Selecting the specifically reported range requires a measurement or annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "If an option is interpreted as a temperature band containing the optimum, both 31–45 °C and 37–42 °C contain the reported range. Choice C is the exact reported interval, but the question does not clarify whether broader containing bands should be rejected."
  },
  "important_caveats": [
    "The evidence is a database annotation citing biochemical characterization; it is not evidence that the evaluated model saw that annotation.",
    "The reviewer source sequence matches the input, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8KN66 (WbpP from Pseudomonas aeruginosa) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is between 37 and 42 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:10747995, J. Biol. Chem. 2000). The sequence matches (SHA256 confirmed, 341 AA). This is experimental data, not computational inference. Choice C (37-42) is directly supported.

Citations as saved: [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> From the sequence, one can identify a Rossmann-fold NAD-binding motif (GVAGFIGS) and a UDP-sugar 4-epimerase family, plus GC-rich composition suggestive of a mesophilic gamma-proteobacterium. This rules out A (49-61, thermophilic). However, distinguishing C (37-42) from D (42-50) and from B (31-45) requires knowing the specific organism's growth optimum (P. aeruginosa at 37°C, max 42°C) or the experimental measurement. The 5°C shift in boundaries between C and D is not reliably encoded in sequence features (salt bridges, hydrophobic packing, loop length) at this resolution.


**Missing item-specific fact**

> The experimental measurement showing optimum activity at 37-42°C for this specific protein (WbpP), or equivalently, knowledge that the source organism is P. aeruginosa with optimal growth at 37°C and maximum at 42°C. The precise lower bound (37 vs 31) and upper bound (42 vs 45 vs 50) cannot be derived from sequence composition alone.


**Reason**

> While sequence features can establish 'mesophilic' and rule out thermophilic (A), the specific boundaries distinguishing 37-42 from 42-50 or 31-45 depend on knowing the organism's exact growth temperature or the experimental assay result. Recognizing P. aeruginosa from sequence is possible but uncertain, and even then the precise 37-42 range reflects an experimental measurement rather than a sequence-derivable property.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Choice B (31-45) fully encompasses C (37-42). A model reasoning 'mesophilic, roughly 30-45°C' could select B. Choice D (42-50) also overlaps C at the boundary (42). Without knowing the exact organism or experimental range, B and C are both defensible for a mesophilic protein.


### Important caveats

- The UniProt annotation is experimental (ECO:0000269, PubMed:10747995), not computational, lending high confidence to the key.
- P. aeruginosa identification from sequence alone is possible via GC-rich composition and family motifs but is not guaranteed; the organism name was not provided in the original input.
- The choices B and C overlap substantially, creating genuine ambiguity for a model reasoning only from 'mesophilic.'
- The 5°C difference between C's upper bound (42) and D's upper bound (50) is at the threshold of sequence-derivable inference for mesophilic proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the sequence, one can identify a Rossmann-fold NAD-binding motif (GVAGFIGS) and a UDP-sugar 4-epimerase family, plus GC-rich composition suggestive of a mesophilic gamma-proteobacterium. This rules out A (49-61, thermophilic). However, distinguishing C (37-42) from D (42-50) and from B (31-45) requires knowing the specific organism's growth optimum (P. aeruginosa at 37°C, max 42°C) or the experimental measurement. The 5°C shift in boundaries between C and D is not reliably encoded in sequence features (salt bridges, hydrophobic packing, loop length) at this resolution.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental measurement showing optimum activity at 37-42°C for this specific protein (WbpP), or equivalently, knowledge that the source organism is P. aeruginosa with optimal growth at 37°C and maximum at 42°C. The precise lower bound (37 vs 31) and upper bound (42 vs 45 vs 50) cannot be derived from sequence composition alone.",
    "reason": "While sequence features can establish 'mesophilic' and rule out thermophilic (A), the specific boundaries distinguishing 37-42 from 42-50 or 31-45 depend on knowing the organism's exact growth temperature or the experimental assay result. Recognizing P. aeruginosa from sequence is possible but uncertain, and even then the precise 37-42 range reflects an experimental measurement rather than a sequence-derivable property."
  },
  "case_id": "temperature_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (WbpP from Pseudomonas aeruginosa) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is between 37 and 42 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:10747995, J. Biol. Chem. 2000). The sequence matches (SHA256 confirmed, 341 AA). This is experimental data, not computational inference. Choice C (37-42) is directly supported."
  },
  "important_caveats": [
    "The UniProt annotation is experimental (ECO:0000269, PubMed:10747995), not computational, lending high confidence to the key.",
    "P. aeruginosa identification from sequence alone is possible via GC-rich composition and family motifs but is not guaranteed; the organism name was not provided in the original input.",
    "The choices B and C overlap substantially, creating genuine ambiguity for a model reasoning only from 'mesophilic.'",
    "The 5°C difference between C's upper bound (42) and D's upper bound (50) is at the threshold of sequence-derivable inference for mesophilic proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Choice B (31-45) fully encompasses C (37-42). A model reasoning 'mesophilic, roughly 30-45°C' could select B. Choice D (42-50) also overlaps C at the boundary (42). Without knowing the exact organism or experimental range, B and C are both defensible for a mesophilic protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"temperature_0034","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry Q8KN66 (WbpP from Pseudomonas aeruginosa) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is between 37 and 42 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:10747995, J. Biol. Chem. 2000). The sequence matches (SHA256 confirmed, 341 AA). This is experimental data, not computational inference. Choice C (37-42) is directly supported.","evidence_ids":["C5","H8"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"From the sequence, one can identify a Rossmann-fold NAD-binding motif (GVAGFIGS) and a UDP-sugar 4-epimerase family, plus GC-rich composition suggestive of a mesophilic gamma-proteobacterium. This rules out A (49-61, thermophilic). However, distinguishing C (37-42) from D (42-50) and from B (31-45) requires knowing the specific organism's growth optimum (P. aeruginosa at 37°C, max 42°C) or the experimental measurement. The 5°C shift in boundaries between C and D is not reliably encoded in sequence features (salt bridges, hydrophobic packing, loop length) at this resolution.","missing_item_specific_fact":"The experimental measurement showing optimum activity at 37-42°C for this specific protein (WbpP), or equivalently, knowledge that the source organism is P. aeruginosa with optimal growth at 37°C and maximum at 42°C. The precise lower bound (37 vs 31) and upper bound (42 vs 45 vs 50) cannot be derived from sequence composition alone.","reason":"While sequence features can establish 'mesophilic' and rule out thermophilic (A), the specific boundaries distinguishing 37-42 from 42-50 or 31-45 depend on knowing the organism's exact growth temperature or the experimental assay result. Recognizing P. aeruginosa from sequence is possible but uncertain, and even then the precise 37-42 range reflects an experimental measurement rather than a sequence-derivable property."},"question_ambiguity":{"multiple_defensible_options":["B","C"],"reason":"Choice B (31-45) fully encompasses C (37-42). A model reasoning 'mesophilic, roughly 30-45°C' could select B. Choice D (42-50) also overlaps C at the boundary (42). Without knowing the exact organism or experimental range, B and C are both defensible for a mesophilic protein."},"important_caveats":["The UniProt annotation is experimental (ECO:0000269, PubMed:10747995), not computational, lending high confidence to the key.","P. aeruginosa identification from sequence alone is possible via GC-rich composition and family motifs but is not guaranteed; the organism name was not provided in the original input.","The choices B and C overlap substantially, creating genuine ambiguity for a model reasoning only from 'mesophilic.'","The 5°C difference between C's upper bound (42) and D's upper bound (50) is at the threshold of sequence-derivable inference for mesophilic proteins."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 341,
  "benchmark_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 341,
  "current_source_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8KN66",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "selected_historical_source_sequence_length": 341,
  "selected_historical_source_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "selected_historical_version": {
    "accession": "Q8KN66",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPP_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8KN66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15016816\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetylglucosamine C4 epimerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc C4 epimerase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.45\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAcA 4-epimerase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":197.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-N-acetylgalactosamine\",\"unit\":\"uM\"},{\"constant\":224.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-N-acetylglucosamine\",\"unit\":\"uM\"},{\"constant\":251.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-galactose\",\"unit\":\"uM\"},{\"constant\":237.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-glucose\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"value\":\"kcat is 271 min(-1) with UDP-N-acetylgalactosamine as substrate. kcat is 120 min(-1) with UDP-N-acetylglucosamine as substrate. kcat is 0.188 min(-1) with UDP-galactose as substrate. kcat is 0.124 min(-1) with UDP-glucose as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is between 7 and 8.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is between 37 and 42 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Creuzenet C.\",\"Belanger M.\",\"Wakarchuk W.W.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10747995\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m001171200\"}],\"citationType\":\"journal article\",\"firstPage\":\"19060\",\"id\":\"10747995\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"19067\",\"publicationDate\":\"2000\",\"title\":\"Expression, purification, and biochemical characterization of WbpP, a new UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.\",\"volume\":\"275\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Demendi M.\",\"Ishiyama N.\",\"Lam J.S.\",\"Berghuis A.M.\",\"Creuzenet C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15752069\"},{\"database\":\"DOI\",\"id\":\"10.1042/bj20050263\"}],\"citationType\":\"journal article\",\"firstPage\":\"173\",\"id\":\"15752069\",\"journal\":\"Biochem. J.\",\"lastPage\":\"180\",\"publicationDate\":\"2005\",\"title\":\"Towards a better understanding of the substrate specificity of the UDP-N-acetylglucosamine C4 epimerase WbpP.\",\"volume\":\"389\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF GLY-102; SER-143; SER-144; GLN-201 AND ALA-209\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Ishiyama N.\",\"Creuzenet C.\",\"Lam J.S.\",\"Berghuis A.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15016816\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m401642200\"}],\"citationType\":\"journal article\",\"firstPage\":\"22635\",\"id\":\"15016816\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"22642\",\"publicationDate\":\"2004\",\"title\":\"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-epimerases.\",\"volume\":\"279\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"1SB8\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"1SB9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+); UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF ALA-209 AND SER-306\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   WBPP_PSEAI              Reviewed;         341 AA.\nAC   Q8KN66; Q9RHD6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};\nDE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};\nDE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};\nDE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};\nDE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};\nDE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\nGN   Name=wbpP {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23998.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27817.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBUNIT.\nRC   STRAIN=Serotype O6;\nRX   PubMed=10747995; DOI=10.1074/jbc.m001171200;\nRA   Creuzenet C., Belanger M., Wakarchuk W.W., Lam J.S.;\nRT   \"Expression, purification, and biochemical characterization of WbpP, a new\nRT   UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.\";\nRL   J. Biol. Chem. 275:19060-19067(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H5",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF GLY-102; SER-143; SER-144;\nRP   GLN-201 AND ALA-209.\nRC   STRAIN=Serotype O6;\nRX   PubMed=15752069; DOI=10.1042/bj20050263;\nRA   Demendi M., Ishiyama N., Lam J.S., Berghuis A.M., Creuzenet C.;\nRT   \"Towards a better understanding of the substrate specificity of the UDP-N-\nRT   acetylglucosamine C4 epimerase WbpP.\";\nRL   Biochem. J. 389:173-180(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H6",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H7",
  "excerpt": "RN   [6] {ECO:0007744|PDB:1SB8, ECO:0007744|PDB:1SB9}\nRP   X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+);\nRP   UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE, FUNCTION, CATALYTIC\nRP   ACTIVITY, COFACTOR, SUBUNIT, AND MUTAGENESIS OF ALA-209 AND SER-306.\nRC   STRAIN=Serotype O6;\nRX   PubMed=15016816; DOI=10.1074/jbc.m401642200;\nRA   Ishiyama N., Creuzenet C., Lam J.S., Berghuis A.M.;\nRT   \"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase\nRT   from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-\nRT   epimerases.\";\nRL   J. Biol. Chem. 279:22635-22642(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H8",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=197 uM for UDP-N-acetylgalactosamine\nCC         {ECO:0000269|PubMed:10747995};\nCC         KM=224 uM for UDP-N-acetylglucosamine {ECO:0000269|PubMed:10747995};\nCC         KM=251 uM for UDP-galactose {ECO:0000269|PubMed:10747995};\nCC         KM=237 uM for UDP-glucose {ECO:0000269|PubMed:10747995};\nCC         Note=kcat is 271 min(-1) with UDP-N-acetylgalactosamine as substrate.\nCC         kcat is 120 min(-1) with UDP-N-acetylglucosamine as substrate. kcat\nCC         is 0.188 min(-1) with UDP-galactose as substrate. kcat is 0.124 min(-\nCC         1) with UDP-glucose as substrate. {ECO:0000269|PubMed:10747995};\nCC       pH dependence:\nCC         Optimum pH is between 7 and 8. {ECO:0000269|PubMed:10747995};\nCC       Temperature dependence:\nCC         Optimum temperature is between 37 and 42 degrees Celsius.\nCC         {ECO:0000269|PubMed:10747995};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
