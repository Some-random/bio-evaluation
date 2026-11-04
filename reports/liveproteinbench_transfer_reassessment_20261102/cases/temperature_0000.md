# temperature_0000

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0000.txt)

**Task:** `temperature`  
**Expected answer:** **A** — 30

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. 30
B. 40
C. 74
D. 32
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

> The matched protein sequence has an experimental UniProt annotation reporting an optimum temperature of 30 °C, supporting choice A. The archived entry reports the same value and cites experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The optimum temperature measured for this exact protein under the relevant assay conditions.


**Reason**

> The sequence may suggest a soluble eukaryotic enzyme, but that does not meaningfully distinguish an exact optimum of 30 °C from 32 °C. Choosing between those close alternatives requires the target-specific measurement or annotation, not a reliable inference from transferable sequence patterns.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited experimental annotation specifies 30 °C, so the supplied evidence identifies one listed answer. Assay conditions can affect measured optima, but no competing measurement is supplied.


### Important caveats

- The evidence supports an experimentally annotated optimum temperature, not necessarily a complete classification of the protein's thermal adaptation range.
- The exact assay conditions are not given in the excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The optimum temperature measured for this exact protein under the relevant assay conditions.",
    "reason": "The sequence may suggest a soluble eukaryotic enzyme, but that does not meaningfully distinguish an exact optimum of 30 °C from 32 °C. Choosing between those close alternatives requires the target-specific measurement or annotation, not a reliable inference from transferable sequence patterns."
  },
  "case_id": "temperature_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched protein sequence has an experimental UniProt annotation reporting an optimum temperature of 30 °C, supporting choice A. The archived entry reports the same value and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The evidence supports an experimentally annotated optimum temperature, not necessarily a complete classification of the protein's thermal adaptation range.",
    "The exact assay conditions are not given in the excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited experimental annotation specifies 30 °C, so the supplied evidence identifies one listed answer. Assay conditions can affect measured optima, but no competing measurement is supplied."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein sequence has an experimental UniProt annotation reporting an optimum temperature of 30 °C, supporting choice A. The archived entry reports the same value and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The optimum temperature measured for this exact protein under the relevant assay conditions.",
    "reason": "The sequence may suggest a soluble eukaryotic enzyme, but that does not meaningfully distinguish an exact optimum of 30 °C from 32 °C. Choosing between those close alternatives requires the target-specific measurement or annotation, not a reliable inference from transferable sequence patterns."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited experimental annotation specifies 30 °C, so the supplied evidence identifies one listed answer. Assay conditions can affect measured optima, but no competing measurement is supplied."
  },
  "important_caveats": [
    "The evidence supports an experimentally annotated optimum temperature, not necessarily a complete classification of the protein's thermal adaptation range.",
    "The exact assay conditions are not given in the excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (A0A075D654, Ajmaline N-methyltransferase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' based on experimental evidence (ECO:0000269, PubMed:27122470). The sequence matches exactly (291 AA, SHA256 confirmed). The expected answer of 30°C is directly supported by a published experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence reveals a Class I methyltransferase (Rossmann fold motif GCGIGGTC), which is a standard mesophilic enzyme architecture. The absence of thermophilic features (extreme ion-pair networks, very high proline, compact hydrophobic cores) allows elimination of 74°C. Plant enzymes generally operate at ambient temperatures (20-40°C), making 30, 32, and 40 all plausible. However, the 2-degree distinction between 30 and 32 (and even 30 vs 40) cannot be resolved from any sequence feature, amino acid composition bias, or family-level pattern. No known structural or sequence-based rule maps to a precise 2°C difference in optimum temperature.


**Missing item-specific fact**

> The experimentally determined optimum temperature of exactly 30°C (vs 32°C or 40°C) for this specific Ajmaline N-methyltransferase, as measured in the 2016 Cazares-Flores et al. study (PubMed:27122470). This is a protein-specific experimental measurement not derivable from sequence composition, fold recognition, or homolog family statistics.


**Reason**

> While 74°C can be eliminated by general knowledge (no thermophilic sequence signatures), the remaining choices 30, 32, and 40 are all within the normal mesophilic plant enzyme range. No transferable biological principle distinguishes 30 from 32 or from 40 for a methyltransferase. The precise numerical answer requires the specific experimental measurement for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> From sequence-based reasoning alone, both 30°C and 32°C are equally valid mesophilic plant enzyme optima. The 2-degree difference has no known structural or sequence-level correlate. A knowledgeable model could reasonably select either value without access to the specific experimental measurement.


### Important caveats

- The organism (Rauvolfia serpentina, a tropical plant) is not provided in the original input; only the sequence is given. Knowing the organism would narrow the range but still not distinguish 30 from 32.
- The question asks for a precise numerical temperature rather than a broad category (cold/moderate/hot), which increases the lookup dependency.
- The experimental optimum temperature (30°C) is a single measurement from one publication; actual enzyme activity may vary with assay conditions.
- The protein family (gamma-tocopherol-like N-methyltransferase) does not have a well-established temperature optimum that would allow family-level transfer to distinguish 30 from 32.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence reveals a Class I methyltransferase (Rossmann fold motif GCGIGGTC), which is a standard mesophilic enzyme architecture. The absence of thermophilic features (extreme ion-pair networks, very high proline, compact hydrophobic cores) allows elimination of 74°C. Plant enzymes generally operate at ambient temperatures (20-40°C), making 30, 32, and 40 all plausible. However, the 2-degree distinction between 30 and 32 (and even 30 vs 40) cannot be resolved from any sequence feature, amino acid composition bias, or family-level pattern. No known structural or sequence-based rule maps to a precise 2°C difference in optimum temperature.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined optimum temperature of exactly 30°C (vs 32°C or 40°C) for this specific Ajmaline N-methyltransferase, as measured in the 2016 Cazares-Flores et al. study (PubMed:27122470). This is a protein-specific experimental measurement not derivable from sequence composition, fold recognition, or homolog family statistics.",
    "reason": "While 74°C can be eliminated by general knowledge (no thermophilic sequence signatures), the remaining choices 30, 32, and 40 are all within the normal mesophilic plant enzyme range. No transferable biological principle distinguishes 30 from 32 or from 40 for a methyltransferase. The precise numerical answer requires the specific experimental measurement for this protein."
  },
  "case_id": "temperature_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A075D654, Ajmaline N-methyltransferase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' based on experimental evidence (ECO:0000269, PubMed:27122470). The sequence matches exactly (291 AA, SHA256 confirmed). The expected answer of 30°C is directly supported by a published experimental measurement."
  },
  "important_caveats": [
    "The organism (Rauvolfia serpentina, a tropical plant) is not provided in the original input; only the sequence is given. Knowing the organism would narrow the range but still not distinguish 30 from 32.",
    "The question asks for a precise numerical temperature rather than a broad category (cold/moderate/hot), which increases the lookup dependency.",
    "The experimental optimum temperature (30°C) is a single measurement from one publication; actual enzyme activity may vary with assay conditions.",
    "The protein family (gamma-tocopherol-like N-methyltransferase) does not have a well-established temperature optimum that would allow family-level transfer to distinguish 30 from 32."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "From sequence-based reasoning alone, both 30°C and 32°C are equally valid mesophilic plant enzyme optima. The 2-degree difference has no known structural or sequence-level correlate. A knowledgeable model could reasonably select either value without access to the specific experimental measurement."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A075D654, Ajmaline N-methyltransferase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' based on experimental evidence (ECO:0000269, PubMed:27122470). The sequence matches exactly (291 AA, SHA256 confirmed). The expected answer of 30°C is directly supported by a published experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence reveals a Class I methyltransferase (Rossmann fold motif GCGIGGTC), which is a standard mesophilic enzyme architecture. The absence of thermophilic features (extreme ion-pair networks, very high proline, compact hydrophobic cores) allows elimination of 74°C. Plant enzymes generally operate at ambient temperatures (20-40°C), making 30, 32, and 40 all plausible. However, the 2-degree distinction between 30 and 32 (and even 30 vs 40) cannot be resolved from any sequence feature, amino acid composition bias, or family-level pattern. No known structural or sequence-based rule maps to a precise 2°C difference in optimum temperature.",
    "missing_item_specific_fact": "The experimentally determined optimum temperature of exactly 30°C (vs 32°C or 40°C) for this specific Ajmaline N-methyltransferase, as measured in the 2016 Cazares-Flores et al. study (PubMed:27122470). This is a protein-specific experimental measurement not derivable from sequence composition, fold recognition, or homolog family statistics.",
    "reason": "While 74°C can be eliminated by general knowledge (no thermophilic sequence signatures), the remaining choices 30, 32, and 40 are all within the normal mesophilic plant enzyme range. No transferable biological principle distinguishes 30 from 32 or from 40 for a methyltransferase. The precise numerical answer requires the specific experimental measurement for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "From sequence-based reasoning alone, both 30°C and 32°C are equally valid mesophilic plant enzyme optima. The 2-degree difference has no known structural or sequence-level correlate. A knowledgeable model could reasonably select either value without access to the specific experimental measurement."
  },
  "important_caveats": [
    "The organism (Rauvolfia serpentina, a tropical plant) is not provided in the original input; only the sequence is given. Knowing the organism would narrow the range but still not distinguish 30 from 32.",
    "The question asks for a precise numerical temperature rather than a broad category (cold/moderate/hot), which increases the lookup dependency.",
    "The experimental optimum temperature (30°C) is a single measurement from one publication; actual enzyme activity may vary with assay conditions.",
    "The protein family (gamma-tocopherol-like N-methyltransferase) does not have a well-established temperature optimum that would allow family-level transfer to distinguish 30 from 32."
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
  "benchmark_sequence_length": 291,
  "benchmark_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 291,
  "current_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A075D654",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "selected_historical_source_sequence_length": 291,
  "selected_historical_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "selected_historical_version": {
    "accession": "A0A075D654",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ANMT_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A075D654\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHH02777.1\",\"source\":\"EMBL\"}],\"value\":\"Gamma-tocopherol-like methyltransferase ANMT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.393\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Ajmaline N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"RsANMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with S-adenosyl-L-methionine as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"unit\":\"pmol/sec/mg\",\"velocity\":45.7},{\"enzyme\":\"enzyme with norajmaline as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"unit\":\"pmol/sec/mg\",\"velocity\":60.3}],\"michaelisConstants\":[{\"constant\":17.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"substrate\":\"S-adenosyl-L-methionine\",\"unit\":\"uM\"},{\"constant\":184.3,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"substrate\":\"norajmaline\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"kcat is 0.7 sec(-1) with S-adenosyl-L-methionine as substrate (PubMed:27122470). kcat is 1 sec(-1) with norajmaline as substrate (PubMed:27122470).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7.5.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 30 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Cazares-Flores P.\",\"Levac D.\",\"De Luca V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27122470\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.13186\"}],\"citationType\":\"journal article\",\"firstPage\":\"335\",\"id\":\"27122470\",\"journal\":\"Plant J.\",\"lastPage\":\"342\",\"publicationDate\":\"2016\",\"title\":\"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.\",\"volume\":\"87\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   ANMT_RAUSE              Reviewed;         291 AA.\nAC   A0A075D654;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};\nDE            Short=RsANMT {ECO:0000303|PubMed:27122470};\nDE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};\nGN   Name=ANMT {ECO:0000303|PubMed:27122470};\nGN   Synonyms=Rs820 {ECO:0000312|EMBL:AHH02777.1};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRX   PubMed=27122470; DOI=10.1111/tpj.13186;\nRA   Cazares-Flores P., Levac D., De Luca V.;\nRT   \"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta\nRT   -methylajmaline biosynthesis belong to a gene family derived from gamma-\nRT   tocopherol C-methyltransferase.\";\nRL   Plant J. 87:335-342(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=17 uM for S-adenosyl-L-methionine {ECO:0000269|PubMed:27122470};\nCC         KM=184.3 uM for norajmaline {ECO:0000269|PubMed:27122470};\nCC         Vmax=45.7 pmol/sec/mg enzyme with S-adenosyl-L-methionine as\nCC         substrate {ECO:0000269|PubMed:27122470};\nCC         Vmax=60.3 pmol/sec/mg enzyme with norajmaline as substrate\nCC         {ECO:0000269|PubMed:27122470};\nCC         Note=kcat is 0.7 sec(-1) with S-adenosyl-L-methionine as substrate\nCC         (PubMed:27122470). kcat is 1 sec(-1) with norajmaline as substrate\nCC         (PubMed:27122470). {ECO:0000269|PubMed:27122470};\nCC       pH dependence:\nCC         Optimum pH is 7.5. {ECO:0000269|PubMed:27122470};\nCC       Temperature dependence:\nCC         Optimum temperature is 30 degrees Celsius.\nCC         {ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
