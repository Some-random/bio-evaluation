# temperature_0032

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0032.txt)

**Task:** `temperature`  
**Expected answer:** **A** — 30

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTPQDLIDASIPFLNELKNRTAGEDLEKWLNDAYGPGSEFYERVAGLVKDGVRDGWAANIEVDGPRYRRSRLAEPCEELNYFSITAVYMDSVEPYRGQYHQHPYGELNMVVPLNEGAELAGPRGWCGGGWTAPDPASHHYPEVRGGAIIALFYLPAGRISYDITPPAE

[Multiple Choices]
A. 30
B. 79
C. 23
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

> The sequence-matched UniProt annotation reports an optimum temperature of 30 °C, with experimental evidence attributed to PubMed 34554625. This supports choice A, though the underlying paper was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The experimentally determined optimum temperature for this exact protein; sequence patterns alone do not meaningfully distinguish 30 °C from the other plausible moderate-temperature choices, 23 °C and 41 °C.


**Reason**

> The sequence provides no reliable basis for selecting the specific optimum among the nearby moderate-temperature options. General sequence or family-level tendencies might make 79 °C less plausible, but do not distinguish choice A from C or D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct numerical temperatures, and the sequence-matched annotation reports a specific optimum. The limitation is that this value is not meaningfully inferable from the original sequence alone, rather than that multiple options are established as correct.


### Important caveats

- An optimum catalytic activity temperature is not necessarily equivalent to a protein's thermal stability or broader thermal-adaptation category, and may depend on assay conditions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined optimum temperature for this exact protein; sequence patterns alone do not meaningfully distinguish 30 °C from the other plausible moderate-temperature choices, 23 °C and 41 °C.",
    "reason": "The sequence provides no reliable basis for selecting the specific optimum among the nearby moderate-temperature options. General sequence or family-level tendencies might make 79 °C less plausible, but do not distinguish choice A from C or D."
  },
  "case_id": "temperature_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 30 °C, with experimental evidence attributed to PubMed 34554625. This supports choice A, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "An optimum catalytic activity temperature is not necessarily equivalent to a protein's thermal stability or broader thermal-adaptation category, and may depend on assay conditions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numerical temperatures, and the sequence-matched annotation reports a specific optimum. The limitation is that this value is not meaningfully inferable from the original sequence alone, rather than that multiple options are established as correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 30 °C, with experimental evidence attributed to PubMed 34554625. This supports choice A, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The experimentally determined optimum temperature for this exact protein; sequence patterns alone do not meaningfully distinguish 30 °C from the other plausible moderate-temperature choices, 23 °C and 41 °C.",
    "reason": "The sequence provides no reliable basis for selecting the specific optimum among the nearby moderate-temperature options. General sequence or family-level tendencies might make 79 °C less plausible, but do not distinguish choice A from C or D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numerical temperatures, and the sequence-matched annotation reports a specific optimum. The limitation is that this value is not meaningfully inferable from the original sequence alone, rather than that multiple options are established as correct."
  },
  "important_caveats": [
    "An optimum catalytic activity temperature is not necessarily equivalent to a protein's thermal stability or broader thermal-adaptation category, and may depend on assay conditions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXG7 (4-hydroxylaminobenzoate lyase, Nocardioides sp. LMS-CY) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:34554625). The sequence matches the benchmark sequence exactly (169 aa, SHA256 confirmed). The answer 30°C is directly annotated from experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (169 aa) shows a Pro content of approximately 10.7% (18/169), which is elevated above the typical mesophilic average (~5-7%). This elevated Pro disfavors option C (23°C, psychrotolerant), as cold-adapted proteins typically have reduced Pro to maintain flexibility. The absence of extreme thermophilic signatures—no very high charged-residue density, no extreme Pro (>13%), no depletion of Asn/Gln/Ser—clearly eliminates option B (79°C, thermophilic). Between A (30°C) and D (41°C), the presence of a GGG flexibility motif (G-G-G-W-T), moderate (not elevated) Arg/Lys/Glu content, and overall 'balanced' mesophilic composition favor the standard mesophilic optimum. Additionally, 30°C is the most frequently reported optimal temperature for mesophilic soil Actinobacteria in the literature, a statistical regularity learned from many related proteins. The sequence lacks the additional stabilization features (higher salt-bridge potential, more Pro, fewer flexible Gly/Ser) that would shift the optimum toward 41°C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use sequence composition features (Pro content, charged residue density, Gly-rich motifs) and learned patterns about mesophilic vs. thermophilic vs. psychrophilic protein adaptations to eliminate 79 and make 23 less probable. The 30 vs 41 distinction relies on the overall 'standard mesophilic' pattern and the statistical prior that 30°C is the modal optimal temperature for soil mesophiles. While the 30-vs-41 margin is narrow, the combination of moderate stabilization features and flexibility motifs provides a defensible probabilistic argument for 30°C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> 79 is clearly eliminated by absence of thermophilic features. 23 is disfavored by elevated Pro. The 30-vs-41 distinction is the closest call, but the overall composition pattern (moderate Pro, GGG flexibility motif, non-extreme charged residues) and the strong statistical prior for 30°C as the modal mesophilic optimum provide a reasonable basis to prefer A over D. No other option is equally defensible.


### Important caveats

- The 30-vs-41 distinction from sequence alone is the weakest link in the reasoning; the difference between these two mesophilic optima is subtle and may not be reliably separable by composition features alone.
- The elevated Pro content (~10.7%) is based on a 169-aa sequence, so percentage estimates carry sampling noise.
- The statistical prior that 30°C is the modal optimum for soil Actinobacteria is a legitimate learned pattern but is not a sequence-derived feature per se.
- The UniProt annotation is experimental (ECO:0000269) from a single study (PubMed:34554625), providing a single measured optimum rather than a range.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (169 aa) shows a Pro content of approximately 10.7% (18/169), which is elevated above the typical mesophilic average (~5-7%). This elevated Pro disfavors option C (23°C, psychrotolerant), as cold-adapted proteins typically have reduced Pro to maintain flexibility. The absence of extreme thermophilic signatures—no very high charged-residue density, no extreme Pro (>13%), no depletion of Asn/Gln/Ser—clearly eliminates option B (79°C, thermophilic). Between A (30°C) and D (41°C), the presence of a GGG flexibility motif (G-G-G-W-T), moderate (not elevated) Arg/Lys/Glu content, and overall 'balanced' mesophilic composition favor the standard mesophilic optimum. Additionally, 30°C is the most frequently reported optimal temperature for mesophilic soil Actinobacteria in the literature, a statistical regularity learned from many related proteins. The sequence lacks the additional stabilization features (higher salt-bridge potential, more Pro, fewer flexible Gly/Ser) that would shift the optimum toward 41°C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence composition features (Pro content, charged residue density, Gly-rich motifs) and learned patterns about mesophilic vs. thermophilic vs. psychrophilic protein adaptations to eliminate 79 and make 23 less probable. The 30 vs 41 distinction relies on the overall 'standard mesophilic' pattern and the statistical prior that 30°C is the modal optimal temperature for soil mesophiles. While the 30-vs-41 margin is narrow, the combination of moderate stabilization features and flexibility motifs provides a defensible probabilistic argument for 30°C."
  },
  "case_id": "temperature_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXG7 (4-hydroxylaminobenzoate lyase, Nocardioides sp. LMS-CY) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:34554625). The sequence matches the benchmark sequence exactly (169 aa, SHA256 confirmed). The answer 30°C is directly annotated from experimental measurement."
  },
  "important_caveats": [
    "The 30-vs-41 distinction from sequence alone is the weakest link in the reasoning; the difference between these two mesophilic optima is subtle and may not be reliably separable by composition features alone.",
    "The elevated Pro content (~10.7%) is based on a 169-aa sequence, so percentage estimates carry sampling noise.",
    "The statistical prior that 30°C is the modal optimum for soil Actinobacteria is a legitimate learned pattern but is not a sequence-derived feature per se.",
    "The UniProt annotation is experimental (ECO:0000269) from a single study (PubMed:34554625), providing a single measured optimum rather than a range."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "79 is clearly eliminated by absence of thermophilic features. 23 is disfavored by elevated Pro. The 30-vs-41 distinction is the closest call, but the overall composition pattern (moderate Pro, GGG flexibility motif, non-extreme charged residues) and the strong statistical prior for 30°C as the modal mesophilic optimum provide a reasonable basis to prefer A over D. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXG7 (4-hydroxylaminobenzoate lyase, Nocardioides sp. LMS-CY) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:34554625). The sequence matches the benchmark sequence exactly (169 aa, SHA256 confirmed). The answer 30°C is directly annotated from experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (169 aa) shows a Pro content of approximately 10.7% (18/169), which is elevated above the typical mesophilic average (~5-7%). This elevated Pro disfavors option C (23°C, psychrotolerant), as cold-adapted proteins typically have reduced Pro to maintain flexibility. The absence of extreme thermophilic signatures—no very high charged-residue density, no extreme Pro (>13%), no depletion of Asn/Gln/Ser—clearly eliminates option B (79°C, thermophilic). Between A (30°C) and D (41°C), the presence of a GGG flexibility motif (G-G-G-W-T), moderate (not elevated) Arg/Lys/Glu content, and overall 'balanced' mesophilic composition favor the standard mesophilic optimum. Additionally, 30°C is the most frequently reported optimal temperature for mesophilic soil Actinobacteria in the literature, a statistical regularity learned from many related proteins. The sequence lacks the additional stabilization features (higher salt-bridge potential, more Pro, fewer flexible Gly/Ser) that would shift the optimum toward 41°C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence composition features (Pro content, charged residue density, Gly-rich motifs) and learned patterns about mesophilic vs. thermophilic vs. psychrophilic protein adaptations to eliminate 79 and make 23 less probable. The 30 vs 41 distinction relies on the overall 'standard mesophilic' pattern and the statistical prior that 30°C is the modal optimal temperature for soil mesophiles. While the 30-vs-41 margin is narrow, the combination of moderate stabilization features and flexibility motifs provides a defensible probabilistic argument for 30°C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "79 is clearly eliminated by absence of thermophilic features. 23 is disfavored by elevated Pro. The 30-vs-41 distinction is the closest call, but the overall composition pattern (moderate Pro, GGG flexibility motif, non-extreme charged residues) and the strong statistical prior for 30°C as the modal mesophilic optimum provide a reasonable basis to prefer A over D. No other option is equally defensible."
  },
  "important_caveats": [
    "The 30-vs-41 distinction from sequence alone is the weakest link in the reasoning; the difference between these two mesophilic optima is subtle and may not be reliably separable by composition features alone.",
    "The elevated Pro content (~10.7%) is based on a 169-aa sequence, so percentage estimates carry sampling noise.",
    "The statistical prior that 30°C is the modal optimum for soil Actinobacteria is a legitimate learned pattern but is not a sequence-derived feature per se.",
    "The UniProt annotation is experimental (ECO:0000269) from a single study (PubMed:34554625), providing a single measured optimum rather than a range."
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
  "benchmark_sequence_length": 169,
  "benchmark_sequence_sha256": "9de4ba2d1c4af2aa958494d811cfc11376a18b8e31621a5c7b5d64582a12fddf",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 169,
  "current_source_sequence_sha256": "9de4ba2d1c4af2aa958494d811cfc11376a18b8e31621a5c7b5d64582a12fddf",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXG7",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "4b6b05a8fd223aed01be2d76992876667425e7e6437694f1ae97efd975cb1310",
  "selected_historical_source_sequence_length": 169,
  "selected_historical_source_sequence_sha256": "9de4ba2d1c4af2aa958494d811cfc11376a18b8e31621a5c7b5d64582a12fddf",
  "selected_historical_version": {
    "accession": "P0DXG7",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PNBB_NOCS0",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXG7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:26.682490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:26.682490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Propionibacteriales\",\"Nocardioidaceae\",\"Nocardioides\"],\"scientificName\":\"Nocardioides sp. (strain LMS-CY)\",\"taxonId\":2840457}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:26.682490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"4.3.3.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"4-hydroxylaminobenzoate lyase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:26.682490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":162.3,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"substrate\":\"4-hydroxylaminobenzoate\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"kcat is 37.1 sec(-1) with 4-hydroxylaminobenzoate as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7.0.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 30 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:26.682490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheng M.\",\"Qian Y.\",\"Xing Z.\",\"Zylstra G.J.\",\"Huang X.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34554625\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.15787\"}],\"citationType\":\"journal article\",\"firstPage\":\"7028\",\"id\":\"34554625\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"7041\",\"publicationDate\":\"2021\",\"title\":\"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.\",\"volume\":\"23\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"LMS-CY\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:26.682490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "57c25dc0f5e72db0aceee8bcfa906ebadbeffb5160e6ae1db79832af6c832afa",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   PNBB_NOCS0              Reviewed;         169 AA.\nAC   P0DXG7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=4-hydroxylaminobenzoate lyase {ECO:0000303|PubMed:34554625};\nDE            EC=4.3.3.- {ECO:0000269|PubMed:34554625};\nGN   Name=pnbB {ECO:0000303|PubMed:34554625};\nGN   ORFNames=KM427_00690 {ECO:0000312|EMBL:QWF22306.1};\nOS   Nocardioides sp. (strain LMS-CY).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Propionibacteriales;\nOC   Nocardioidaceae; Nocardioides.\nOX   NCBI_TaxID=2840457;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:28.436556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b6b05a8fd223aed01be2d76992876667425e7e6437694f1ae97efd975cb1310",
  "url": "https://rest.uniprot.org/unisave/P0DXG7?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA], FUNCTION, CATALYTIC\nRP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND INDUCTION.\nRC   STRAIN=LMS-CY;\nRX   PubMed=34554625; DOI=10.1111/1462-2920.15787;\nRA   Cheng M., Qian Y., Xing Z., Zylstra G.J., Huang X.;\nRT   \"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively\nRT   regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.\";\nRL   Environ. Microbiol. 23:7028-7041(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:28.436556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b6b05a8fd223aed01be2d76992876667425e7e6437694f1ae97efd975cb1310",
  "url": "https://rest.uniprot.org/unisave/P0DXG7?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=162.3 uM for 4-hydroxylaminobenzoate\nCC         {ECO:0000269|PubMed:34554625};\nCC         Note=kcat is 37.1 sec(-1) with 4-hydroxylaminobenzoate as substrate.\nCC         {ECO:0000269|PubMed:34554625};\nCC       pH dependence:\nCC         Optimum pH is 7.0. {ECO:0000269|PubMed:34554625};\nCC       Temperature dependence:\nCC         Optimum temperature is 30 degrees Celsius.\nCC         {ECO:0000269|PubMed:34554625};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:28.436556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b6b05a8fd223aed01be2d76992876667425e7e6437694f1ae97efd975cb1310",
  "url": "https://rest.uniprot.org/unisave/P0DXG7?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
