# temperature_0017

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0017.txt)

**Task:** `temperature`  
**Expected answer:** **C** — 90

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

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

> The sequence-matched UniProt annotation reports an optimum temperature of 90°C for phosphoglucose isomerase activity, citing experimental evidence. This supports choice C; the supplied excerpts do not independently validate the cited paper.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence composition can provide probabilistic clues about thermal adaptation, but no clear transferable feature in the supplied sequence distinguishes an optimum of 90°C from 59°C. Those choices require a more specific temperature inference than a general thermophile-versus-mesophile tendency supplies.


**Missing item-specific fact**

> The experimentally reported optimum temperature for this exact protein, or other target-specific evidence sufficient to distinguish 90°C from the other offered values.


**Reason**

> The input gives only a sequence and numeric alternatives, with no organism or assay context. A broad sequence-based estimate may be possible, but selecting the precise optimum depends on target-specific information absent from the input; recalling this protein's record would not count as transfer from related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct numeric temperatures, and the supplied evidence identifies one measured optimum. The input alone leaves the precise value uncertain, but no particular pair of choices is established as equally defensible.


### Important caveats

- The temperature annotation is curated and cites experimental evidence; the cited primary study was not independently reviewed here.
- The reviewer evidence reports a sequence match, but its accession and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence composition can provide probabilistic clues about thermal adaptation, but no clear transferable feature in the supplied sequence distinguishes an optimum of 90°C from 59°C. Those choices require a more specific temperature inference than a general thermophile-versus-mesophile tendency supplies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein, or other target-specific evidence sufficient to distinguish 90°C from the other offered values.",
    "reason": "The input gives only a sequence and numeric alternatives, with no organism or assay context. A broad sequence-based estimate may be possible, but selecting the precise optimum depends on target-specific information absent from the input; recalling this protein's record would not count as transfer from related proteins."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 90°C for phosphoglucose isomerase activity, citing experimental evidence. This supports choice C; the supplied excerpts do not independently validate the cited paper."
  },
  "important_caveats": [
    "The temperature annotation is curated and cites experimental evidence; the cited primary study was not independently reviewed here.",
    "The reviewer evidence reports a sequence match, but its accession and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numeric temperatures, and the supplied evidence identifies one measured optimum. The input alone leaves the precise value uncertain, but no particular pair of choices is established as equally defensible."
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
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 90°C for phosphoglucose isomerase activity, citing experimental evidence. This supports choice C; the supplied excerpts do not independently validate the cited paper.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence composition can provide probabilistic clues about thermal adaptation, but no clear transferable feature in the supplied sequence distinguishes an optimum of 90°C from 59°C. Those choices require a more specific temperature inference than a general thermophile-versus-mesophile tendency supplies.",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein, or other target-specific evidence sufficient to distinguish 90°C from the other offered values.",
    "reason": "The input gives only a sequence and numeric alternatives, with no organism or assay context. A broad sequence-based estimate may be possible, but selecting the precise optimum depends on target-specific information absent from the input; recalling this protein's record would not count as transfer from related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numeric temperatures, and the supplied evidence identifies one measured optimum. The input alone leaves the precise value uncertain, but no particular pair of choices is established as equally defensible."
  },
  "important_caveats": [
    "The temperature annotation is curated and cites experimental evidence; the cited primary study was not independently reviewed here.",
    "The reviewer evidence reports a sequence match, but its accession and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A3MTR6 (sequence matched, 299 AA) records an experimentally determined optimum temperature of 90°C for phosphoglucose isomerase activity (ECO:0000269, PubMed:39208883), with thermostability half-life of ~50 min at 100°C. The sequence from Pyrobaculum calidifontis (a hyperthermophilic archaeon in Thermoproteota) is confirmed as the source. The answer of 90°C is directly supported by experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits extreme amino acid composition features learned from other hyperthermophilic proteins: (1) Very high Arg content (~8-10%) with a markedly elevated Arg/Lys ratio, consistent with bidentate salt-bridge networks characteristic of hyperthermophiles rather than moderate thermophiles; (2) High Glu content providing counter-charges for salt bridges; (3) Near-complete absence of thermolabile residues (no Cys, very few Gln, Asn, Ser, Thr); (4) High hydrophobic content (I, V, L) indicating a tightly packed core. The TIM-barrel 'GG' motif and overall architecture identify this as a phosphoglucose isomerase family member. The EXTREMITY of the composition bias—particularly the very high Arg/Lys ratio and near-zero thermolabile residues—distinguishes hyperthermophilic adaptation (90°C) from moderate thermophilic adaptation (59°C), where enrichment is present but less extreme. Mesophilic options (25, 41) are easily excluded by the high charged and hydrophobic content.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the PGI/TIM-barrel family from the GG motif and sequence architecture, then apply learned composition patterns from other hyperthermophilic proteins (extreme Arg enrichment, high R/K ratio, absence of Cys/Q/N, high hydrophobicity) to distinguish 90°C from 59°C. While the 90-vs-59 distinction is probabilistic rather than certain, the extremity of the composition bias provides a meaningful and defensible inference consistent with known hyperthermophile signatures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Distinguishing 90°C from 59°C purely from sequence composition is inherently probabilistic. A model recognizing thermophilic composition might select 59°C (moderate thermophile) if it judges the composition as 'thermophilic but not extreme.' However, the very high Arg/Lys ratio and near-absence of all thermolabile residues tip the balance toward hyperthermophilic (90°C). The distinction is defensible but not absolute from sequence alone.


### Important caveats

- The 90°C value is an experimental measurement (PubMed:39208883), not a computational prediction; the benchmark task frames this as prediction from sequence.
- The distinction between 90°C and 59°C from sequence composition alone is probabilistic; the argument relies on the extremity of composition bias matching known hyperthermophile patterns.
- The organism (Pyrobaculum calidifontis, a hyperthermophilic archaeon) is not provided in the model input; the inference must come from sequence features alone.
- The UniProt annotation was added in 2025 (first public date 2025-02-05), so the experimental characterization is relatively recent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits extreme amino acid composition features learned from other hyperthermophilic proteins: (1) Very high Arg content (~8-10%) with a markedly elevated Arg/Lys ratio, consistent with bidentate salt-bridge networks characteristic of hyperthermophiles rather than moderate thermophiles; (2) High Glu content providing counter-charges for salt bridges; (3) Near-complete absence of thermolabile residues (no Cys, very few Gln, Asn, Ser, Thr); (4) High hydrophobic content (I, V, L) indicating a tightly packed core. The TIM-barrel 'GG' motif and overall architecture identify this as a phosphoglucose isomerase family member. The EXTREMITY of the composition bias—particularly the very high Arg/Lys ratio and near-zero thermolabile residues—distinguishes hyperthermophilic adaptation (90°C) from moderate thermophilic adaptation (59°C), where enrichment is present but less extreme. Mesophilic options (25, 41) are easily excluded by the high charged and hydrophobic content.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PGI/TIM-barrel family from the GG motif and sequence architecture, then apply learned composition patterns from other hyperthermophilic proteins (extreme Arg enrichment, high R/K ratio, absence of Cys/Q/N, high hydrophobicity) to distinguish 90°C from 59°C. While the 90-vs-59 distinction is probabilistic rather than certain, the extremity of the composition bias provides a meaningful and defensible inference consistent with known hyperthermophile signatures."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A3MTR6 (sequence matched, 299 AA) records an experimentally determined optimum temperature of 90°C for phosphoglucose isomerase activity (ECO:0000269, PubMed:39208883), with thermostability half-life of ~50 min at 100°C. The sequence from Pyrobaculum calidifontis (a hyperthermophilic archaeon in Thermoproteota) is confirmed as the source. The answer of 90°C is directly supported by experimental measurement."
  },
  "important_caveats": [
    "The 90°C value is an experimental measurement (PubMed:39208883), not a computational prediction; the benchmark task frames this as prediction from sequence.",
    "The distinction between 90°C and 59°C from sequence composition alone is probabilistic; the argument relies on the extremity of composition bias matching known hyperthermophile patterns.",
    "The organism (Pyrobaculum calidifontis, a hyperthermophilic archaeon) is not provided in the model input; the inference must come from sequence features alone.",
    "The UniProt annotation was added in 2025 (first public date 2025-02-05), so the experimental characterization is relatively recent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Distinguishing 90°C from 59°C purely from sequence composition is inherently probabilistic. A model recognizing thermophilic composition might select 59°C (moderate thermophile) if it judges the composition as 'thermophilic but not extreme.' However, the very high Arg/Lys ratio and near-absence of all thermolabile residues tip the balance toward hyperthermophilic (90°C). The distinction is defensible but not absolute from sequence alone."
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
    "reason": "The UniProt entry A3MTR6 (sequence matched, 299 AA) records an experimentally determined optimum temperature of 90°C for phosphoglucose isomerase activity (ECO:0000269, PubMed:39208883), with thermostability half-life of ~50 min at 100°C. The sequence from Pyrobaculum calidifontis (a hyperthermophilic archaeon in Thermoproteota) is confirmed as the source. The answer of 90°C is directly supported by experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits extreme amino acid composition features learned from other hyperthermophilic proteins: (1) Very high Arg content (~8-10%) with a markedly elevated Arg/Lys ratio, consistent with bidentate salt-bridge networks characteristic of hyperthermophiles rather than moderate thermophiles; (2) High Glu content providing counter-charges for salt bridges; (3) Near-complete absence of thermolabile residues (no Cys, very few Gln, Asn, Ser, Thr); (4) High hydrophobic content (I, V, L) indicating a tightly packed core. The TIM-barrel 'GG' motif and overall architecture identify this as a phosphoglucose isomerase family member. The EXTREMITY of the composition bias—particularly the very high Arg/Lys ratio and near-zero thermolabile residues—distinguishes hyperthermophilic adaptation (90°C) from moderate thermophilic adaptation (59°C), where enrichment is present but less extreme. Mesophilic options (25, 41) are easily excluded by the high charged and hydrophobic content.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PGI/TIM-barrel family from the GG motif and sequence architecture, then apply learned composition patterns from other hyperthermophilic proteins (extreme Arg enrichment, high R/K ratio, absence of Cys/Q/N, high hydrophobicity) to distinguish 90°C from 59°C. While the 90-vs-59 distinction is probabilistic rather than certain, the extremity of the composition bias provides a meaningful and defensible inference consistent with known hyperthermophile signatures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Distinguishing 90°C from 59°C purely from sequence composition is inherently probabilistic. A model recognizing thermophilic composition might select 59°C (moderate thermophile) if it judges the composition as 'thermophilic but not extreme.' However, the very high Arg/Lys ratio and near-absence of all thermolabile residues tip the balance toward hyperthermophilic (90°C). The distinction is defensible but not absolute from sequence alone."
  },
  "important_caveats": [
    "The 90°C value is an experimental measurement (PubMed:39208883), not a computational prediction; the benchmark task frames this as prediction from sequence.",
    "The distinction between 90°C and 59°C from sequence composition alone is probabilistic; the argument relies on the extremity of composition bias matching known hyperthermophile patterns.",
    "The organism (Pyrobaculum calidifontis, a hyperthermophilic archaeon) is not provided in the model input; the inference must come from sequence features alone.",
    "The UniProt annotation was added in 2025 (first public date 2025-02-05), so the experimental characterization is relatively recent."
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
  "benchmark_sequence_length": 299,
  "benchmark_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_entry_audit": {
    "entryVersion": 75,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 299,
  "current_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A3MTR6",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "selected_historical_source_sequence_length": 299,
  "selected_historical_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "selected_historical_version": {
    "accession": "A3MTR6",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGMI_PYRCJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A3MTR6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":75,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Thermoproteales\",\"Thermoproteaceae\",\"Pyrobaculum\"],\"scientificName\":\"Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1)\",\"taxonId\":410359}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Glucose-6-phosphate isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"GPI\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mannose-6-phosphate isomerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.8\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional phosphoglucose/phosphomannose isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Bifunctional PGI/PMI\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with glucose 6-phosphate as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":290.0},{\"enzyme\":\"enzyme with mannose 6-phosphate as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":235.0},{\"enzyme\":\"enzyme with fructose 6-phosphate as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":240.0}],\"michaelisConstants\":[{\"constant\":0.33,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"substrate\":\"glucose 6-phosphate\",\"unit\":\"mM\"},{\"constant\":0.34,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"substrate\":\"mannose 6-phosphate\",\"unit\":\"mM\"},{\"constant\":0.29,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"substrate\":\"fructose 6-phosphate\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"kcat is 315 sec(-1) with glucose 6-phosphate as substrate. kcat is 240 sec(-1) with mannose 6-phosphate as substrate. kcat is 265 sec(-1) with fructose 6-phosphate as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 8.5 (for phosphoglucose isomerase activity) (PubMed:39208883). Activity is reduced significantly below pH 8.0 and above 9.0 (PubMed:39208883).\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity) (PubMed:39208883). Displays high thermostability with a half-life of about 50 minutes at 100 degrees Celsius (PubMed:39208883).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Maqsood A.\",\"Shakir N.A.\",\"Aslam M.\",\"Rahman M.\",\"Rashid N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39208883\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.135127\"}],\"citationType\":\"journal article\",\"firstPage\":\"135127\",\"id\":\"39208883\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"135127\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\",\"volume\":\"279\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 21063 / JCM 11548 / VA1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   PGMI_PYRCJ              Reviewed;         299 AA.\nAC   A3MTR6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\nGN   OrderedLocusNames=Pcal_0606 {ECO:0000312|EMBL:ABO08033.1};\nOS   Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1).\nOC   Archaea; Thermoproteota; Thermoprotei; Thermoproteales; Thermoproteaceae;\nOC   Pyrobaculum.\nOX   NCBI_TaxID=410359;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 21063 / JCM 11548 / VA1;\nRX   PubMed=39208883; DOI=10.1016/j.ijbiomac.2024.135127;\nRA   Maqsood A., Shakir N.A., Aslam M., Rahman M., Rashid N.;\nRT   \"Structural and functional investigations of Pcal_0606, a bifunctional\nRT   phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\";\nRL   Int. J. Biol. Macromol. 279:135127-135127(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=0.33 mM for glucose 6-phosphate {ECO:0000269|PubMed:39208883};\nCC         KM=0.34 mM for mannose 6-phosphate {ECO:0000269|PubMed:39208883};\nCC         KM=0.29 mM for fructose 6-phosphate {ECO:0000269|PubMed:39208883};\nCC         Vmax=290 umol/min/mg enzyme with glucose 6-phosphate as substrate\nCC         {ECO:0000269|PubMed:39208883};\nCC         Vmax=235 umol/min/mg enzyme with mannose 6-phosphate as substrate\nCC         {ECO:0000269|PubMed:39208883};\nCC         Vmax=240 umol/min/mg enzyme with fructose 6-phosphate as substrate\nCC         {ECO:0000269|PubMed:39208883};\nCC         Note=kcat is 315 sec(-1) with glucose 6-phosphate as substrate. kcat\nCC         is 240 sec(-1) with mannose 6-phosphate as substrate. kcat is 265\nCC         sec(-1) with fructose 6-phosphate as substrate.\nCC         {ECO:0000269|PubMed:39208883};\nCC       pH dependence:\nCC         Optimum pH is 8.5 (for phosphoglucose isomerase activity)\nCC         (PubMed:39208883). Activity is reduced significantly below pH 8.0 and\nCC         above 9.0 (PubMed:39208883). {ECO:0000269|PubMed:39208883};\nCC       Temperature dependence:\nCC         Optimum temperature is 90 degrees Celsius (for phosphoglucose\nCC         isomerase activity) (PubMed:39208883). Displays high thermostability\nCC         with a half-life of about 50 minutes at 100 degrees Celsius\nCC         (PubMed:39208883). {ECO:0000269|PubMed:39208883};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
