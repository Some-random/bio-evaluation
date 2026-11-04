# temperature_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0028.txt)

**Task:** `temperature`  
**Expected answer:** **B** — 70

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSIALALAAAPAVLAQSQLWGQCGGIGWNGPTTCVSGATCTKINDWYHQCLPGGNNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGGNTLHEKFKARGKQYFGTEIDHYHLNNNQLMEIARREFGQITHENSMKWDATEPSRGSFSFGNADRVVDWATSNGKLIRGHTLLWHSQLPQWVQNINDRNTLTQVIENHVKTIMTRYKGKIFHYDVVNEILDENGGLRNSVFSRVLGEDFVGIAFRAARATDPDAKLYINDYNLDSANYAKTRGMINLVNKWVSQGVPIDGIGTQAHLAGPGGWNPASGVPAALQALAGANVKEVAITELDIQGAGANDYVTVANACLNVQKCVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL

[Multiple Choices]
A. 58
B. 70
C. 74
D. 27-37
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

> The sequence-matched UniProt annotation reports an optimum temperature of 70°C, citing experimental evidence (PubMed 23306124), which supports choice B.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The experimentally measured temperature optimum for this particular protein, under the relevant assay conditions.


**Reason**

> The sequence may support recognizing a secreted enzyme, but general sequence or family-level patterns do not reliably distinguish an optimum of 70°C from nearby alternatives such as 58°C or 74°C. The exact optimum is an item-specific experimental property not given in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited sequence-matched annotation reports one optimum, 70°C. The original sequence alone may not determine it, but that does not make multiple choices equally defensible as the reported optimum.


### Important caveats

- The cited annotation is experimental-evidence-coded, but the primary paper was not independently reviewed here.
- An enzyme's measured optimum can depend on assay conditions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured temperature optimum for this particular protein, under the relevant assay conditions.",
    "reason": "The sequence may support recognizing a secreted enzyme, but general sequence or family-level patterns do not reliably distinguish an optimum of 70°C from nearby alternatives such as 58°C or 74°C. The exact optimum is an item-specific experimental property not given in the original input."
  },
  "case_id": "temperature_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 70°C, citing experimental evidence (PubMed 23306124), which supports choice B."
  },
  "important_caveats": [
    "The cited annotation is experimental-evidence-coded, but the primary paper was not independently reviewed here.",
    "An enzyme's measured optimum can depend on assay conditions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited sequence-matched annotation reports one optimum, 70°C. The original sequence alone may not determine it, but that does not make multiple choices equally defensible as the reported optimum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 70°C, citing experimental evidence (PubMed 23306124), which supports choice B.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The experimentally measured temperature optimum for this particular protein, under the relevant assay conditions.",
    "reason": "The sequence may support recognizing a secreted enzyme, but general sequence or family-level patterns do not reliably distinguish an optimum of 70°C from nearby alternatives such as 58°C or 74°C. The exact optimum is an item-specific experimental property not given in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited sequence-matched annotation reports one optimum, 70°C. The original sequence alone may not determine it, but that does not make multiple choices equally defensible as the reported optimum."
  },
  "important_caveats": [
    "The cited annotation is experimental-evidence-coded, but the primary paper was not independently reviewed here.",
    "An enzyme's measured optimum can depend on assay conditions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C5, H4) from UniProt entry M4MEY9 (XYNC_HUMIN) explicitly states 'Optimum temperature is 70 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:23306124 (Du et al., 2013, Bioresour. Technol. 130:161-167). The sequence matches exactly (390 AA, identical SHA256). This is a directly measured experimental value for Endo-1,4-beta-xylanase C from Humicola insolens Y1.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model could recognize the GH11 xylanase fold from the catalytic domain sequence and identify thermophilic indicators (Pro-rich linker regions, moderate salt-bridge-forming residues, secreted protein architecture), which would eliminate option D (27-37, mesophilic). However, the remaining three options (58, 70, 74) all fall within the thermophilic range for fungal GH11 xylanases. No sequence-level feature (charge ratio, hydrophobicity, Pro content, thermolabile residue count) reliably distinguishes 70 from 58 or 74. Family-level knowledge of thermophilic fungal xylanases places optima broadly in the 55-75°C range, which encompasses all three thermophilic choices. The specific value of 70°C is an experimentally determined measurement for this particular enzyme variant (XynC from strain Y1), not a predictable consequence of sequence features or family-level trends.


**Missing item-specific fact**

> The experimentally measured optimum temperature of 70°C for this specific xylanase variant (Endo-1,4-beta-xylanase C, XynC, from Humicola insolens Y1), as reported in Du et al. 2013. The three thermophilic options (58, 70, 74) are not separable by any sequence-derived feature or family-level generalization.


**Reason**

> While the sequence permits elimination of the mesophilic option (D) through recognition of thermophilic structural signatures, the three remaining thermophilic temperatures (58, 70, 74) cannot be distinguished by sequence composition, family-level patterns, or mechanistic reasoning. The correct answer depends on the specific experimental measurement for this exact protein variant.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C"
]
```

> All three thermophilic options (58, 70, 74) are plausible optima for a thermophilic fungal GH11 xylanase. Without the specific experimental measurement, a knowledgeable model could reasonably select any of these three based on family-level expectations for thermophilic xylanases. The sequence does not encode a clear discriminator between these close values.


### Important caveats

- The question asks for a specific temperature value rather than a broad category (cold/moderate/hot), making it harder to answer from general principles.
- The Pro-rich and Asn/Gln-rich linker regions in the sequence might weakly suggest moderate rather than extreme thermophily, but this is too speculative to reliably distinguish 58 from 70.
- The protein is a precursor (390 AA including signal peptide); the mature enzyme's thermal properties are what were experimentally measured.
- Humicola insolens is a thermophilic fungus (growth optimum ~45°C), but this organism-level information is not directly derivable from the sequence without recognizing the specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the GH11 xylanase fold from the catalytic domain sequence and identify thermophilic indicators (Pro-rich linker regions, moderate salt-bridge-forming residues, secreted protein architecture), which would eliminate option D (27-37, mesophilic). However, the remaining three options (58, 70, 74) all fall within the thermophilic range for fungal GH11 xylanases. No sequence-level feature (charge ratio, hydrophobicity, Pro content, thermolabile residue count) reliably distinguishes 70 from 58 or 74. Family-level knowledge of thermophilic fungal xylanases places optima broadly in the 55-75°C range, which encompasses all three thermophilic choices. The specific value of 70°C is an experimentally determined measurement for this particular enzyme variant (XynC from strain Y1), not a predictable consequence of sequence features or family-level trends.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of 70°C for this specific xylanase variant (Endo-1,4-beta-xylanase C, XynC, from Humicola insolens Y1), as reported in Du et al. 2013. The three thermophilic options (58, 70, 74) are not separable by any sequence-derived feature or family-level generalization.",
    "reason": "While the sequence permits elimination of the mesophilic option (D) through recognition of thermophilic structural signatures, the three remaining thermophilic temperatures (58, 70, 74) cannot be distinguished by sequence composition, family-level patterns, or mechanistic reasoning. The correct answer depends on the specific experimental measurement for this exact protein variant."
  },
  "case_id": "temperature_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) from UniProt entry M4MEY9 (XYNC_HUMIN) explicitly states 'Optimum temperature is 70 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:23306124 (Du et al., 2013, Bioresour. Technol. 130:161-167). The sequence matches exactly (390 AA, identical SHA256). This is a directly measured experimental value for Endo-1,4-beta-xylanase C from Humicola insolens Y1."
  },
  "important_caveats": [
    "The question asks for a specific temperature value rather than a broad category (cold/moderate/hot), making it harder to answer from general principles.",
    "The Pro-rich and Asn/Gln-rich linker regions in the sequence might weakly suggest moderate rather than extreme thermophily, but this is too speculative to reliably distinguish 58 from 70.",
    "The protein is a precursor (390 AA including signal peptide); the mature enzyme's thermal properties are what were experimentally measured.",
    "Humicola insolens is a thermophilic fungus (growth optimum ~45°C), but this organism-level information is not directly derivable from the sequence without recognizing the specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C"
    ],
    "reason": "All three thermophilic options (58, 70, 74) are plausible optima for a thermophilic fungal GH11 xylanase. Without the specific experimental measurement, a knowledgeable model could reasonably select any of these three based on family-level expectations for thermophilic xylanases. The sequence does not encode a clear discriminator between these close values."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) from UniProt entry M4MEY9 (XYNC_HUMIN) explicitly states 'Optimum temperature is 70 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:23306124 (Du et al., 2013, Bioresour. Technol. 130:161-167). The sequence matches exactly (390 AA, identical SHA256). This is a directly measured experimental value for Endo-1,4-beta-xylanase C from Humicola insolens Y1.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model could recognize the GH11 xylanase fold from the catalytic domain sequence and identify thermophilic indicators (Pro-rich linker regions, moderate salt-bridge-forming residues, secreted protein architecture), which would eliminate option D (27-37, mesophilic). However, the remaining three options (58, 70, 74) all fall within the thermophilic range for fungal GH11 xylanases. No sequence-level feature (charge ratio, hydrophobicity, Pro content, thermolabile residue count) reliably distinguishes 70 from 58 or 74. Family-level knowledge of thermophilic fungal xylanases places optima broadly in the 55-75°C range, which encompasses all three thermophilic choices. The specific value of 70°C is an experimentally determined measurement for this particular enzyme variant (XynC from strain Y1), not a predictable consequence of sequence features or family-level trends.",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of 70°C for this specific xylanase variant (Endo-1,4-beta-xylanase C, XynC, from Humicola insolens Y1), as reported in Du et al. 2013. The three thermophilic options (58, 70, 74) are not separable by any sequence-derived feature or family-level generalization.",
    "reason": "While the sequence permits elimination of the mesophilic option (D) through recognition of thermophilic structural signatures, the three remaining thermophilic temperatures (58, 70, 74) cannot be distinguished by sequence composition, family-level patterns, or mechanistic reasoning. The correct answer depends on the specific experimental measurement for this exact protein variant."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C"],
    "reason": "All three thermophilic options (58, 70, 74) are plausible optima for a thermophilic fungal GH11 xylanase. Without the specific experimental measurement, a knowledgeable model could reasonably select any of these three based on family-level expectations for thermophilic xylanases. The sequence does not encode a clear discriminator between these close values."
  },
  "important_caveats": [
    "The question asks for a specific temperature value rather than a broad category (cold/moderate/hot), making it harder to answer from general principles.",
    "The Pro-rich and Asn/Gln-rich linker regions in the sequence might weakly suggest moderate rather than extreme thermophily, but this is too speculative to reliably distinguish 58 from 70.",
    "The protein is a precursor (390 AA including signal peptide); the mature enzyme's thermal properties are what were experimentally measured.",
    "Humicola insolens is a thermophilic fungus (growth optimum ~45°C), but this organism-level information is not directly derivable from the sequence without recognizing the specific protein."
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
  "benchmark_sequence_length": 390,
  "benchmark_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 390,
  "current_source_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MEY9",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "selected_historical_source_sequence_length": 390,
  "selected_historical_source_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "selected_historical_version": {
    "accession": "M4MEY9",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNC_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MEY9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase C\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase C\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme towards birchwood xylan\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":287.7}],\"michaelisConstants\":[{\"constant\":2.1,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"substrate\":\"birchwood xylan\",\"unit\":\"mM\"}]},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 6.0.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 70 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   XYNC_HUMIN              Reviewed;         390 AA.\nAC   M4MEY9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynC {ECO:0000303|PubMed:23306124};\nGN   Synonyms=Xyl3 {ECO:0000303|PubMed:8190078},\nGN   XynW {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION.\nRX   PubMed=8190078; DOI=10.1007/bf00301060;\nRA   Dalboege H., Hansen H.P.H.;\nRT   \"A novel method for efficient expression cloning of fungal enzyme genes.\";\nRL   Mol. Gen. Genet. 243:253-260(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=2.1 mM for birchwood xylan {ECO:0000269|PubMed:23306124};\nCC         Vmax=287.7 umol/min/mg enzyme towards birchwood xylan\nCC         {ECO:0000269|PubMed:23306124};\nCC       pH dependence:\nCC         Optimum pH is 6.0. {ECO:0000269|PubMed:23306124};\nCC       Temperature dependence:\nCC         Optimum temperature is 70 degrees Celsius.\nCC         {ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
