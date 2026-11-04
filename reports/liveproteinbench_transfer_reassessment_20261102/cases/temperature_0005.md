# temperature_0005

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0005.txt)

**Task:** `temperature`  
**Expected answer:** **A** — 37

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. 37
B. 20
C. 49
D. 21
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

> The sequence-matched UniProt record reports an optimum temperature of 37 °C, with experimental evidence (ECO:0000269, PubMed:12391554), supporting choice A.

Citations as saved: [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing a soluble reductase-like enzyme, and ordinary mesophilic biology makes 49 less compelling. But that does not meaningfully distinguish 37 from 20 or 21: sequence composition and enzyme class do not reliably specify this enzyme's measured optimum.


**Missing item-specific fact**

> The experimentally reported optimum temperature for this exact protein is 37 °C.


**Reason**

> The choices are specific temperatures, not broad adaptation categories. The exact optimum is an empirical property absent from the input; transferable sequence and family knowledge does not reliably resolve the close alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched experimental annotation supports a unique listed value, 37 °C. The sequence alone may not identify it, but that is an answerability limitation rather than ambiguity in the recorded value.


### Important caveats

- The source reports an enzyme optimum temperature; that measurement is not necessarily equivalent to a broad thermal-adaptation category.
- The supplied evidence supports the key through a database annotation citing experimental evidence; the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognizing a soluble reductase-like enzyme, and ordinary mesophilic biology makes 49 less compelling. But that does not meaningfully distinguish 37 from 20 or 21: sequence composition and enzyme class do not reliably specify this enzyme's measured optimum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein is 37 °C.",
    "reason": "The choices are specific temperatures, not broad adaptation categories. The exact optimum is an empirical property absent from the input; transferable sequence and family knowledge does not reliably resolve the close alternatives."
  },
  "case_id": "temperature_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 37 °C, with experimental evidence (ECO:0000269, PubMed:12391554), supporting choice A."
  },
  "important_caveats": [
    "The source reports an enzyme optimum temperature; that measurement is not necessarily equivalent to a broad thermal-adaptation category.",
    "The supplied evidence supports the key through a database annotation citing experimental evidence; the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched experimental annotation supports a unique listed value, 37 °C. The sequence alone may not identify it, but that is an answerability limitation rather than ambiguity in the recorded value."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 37 °C, with experimental evidence (ECO:0000269, PubMed:12391554), supporting choice A.",
    "evidence_ids": ["H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing a soluble reductase-like enzyme, and ordinary mesophilic biology makes 49 less compelling. But that does not meaningfully distinguish 37 from 20 or 21: sequence composition and enzyme class do not reliably specify this enzyme's measured optimum.",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein is 37 °C.",
    "reason": "The choices are specific temperatures, not broad adaptation categories. The exact optimum is an empirical property absent from the input; transferable sequence and family knowledge does not reliably resolve the close alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched experimental annotation supports a unique listed value, 37 °C. The sequence alone may not identify it, but that is an answerability limitation rather than ambiguity in the recorded value."
  },
  "important_caveats": [
    "The source reports an enzyme optimum temperature; that measurement is not necessarily equivalent to a broad thermal-adaptation category.",
    "The supplied evidence supports the key through a database annotation citing experimental evidence; the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 37 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:12391554. The benchmark sequence matches the source sequence (SHA256 confirmed, 363 aa). The answer 37°C is directly annotated from experimental measurement.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical Rossmann-fold NAD(P)-binding motifs (GATMGS, GKSTK) identifying it as an oxidoreductase. Composition analysis provides a chain of elimination: (1) 49°C is ruled out because the protein has multiple Cys residues (~5-6), a low Arg-to-Lys ratio (Lys-rich, Arg-poor), and lacks the high charge density, short loops, and reduced thermolabile residues characteristic of thermophilic proteins. (2) 20°C and 21°C are argued against because the protein lacks the extreme cold-adaptation signatures: it does not show very high Gly content, very low Pro, very low overall hydrophobicity, or the excessive loop flexibility typical of psychrophilic enzymes. The canonical, well-conserved Rossmann motifs and moderate hydrophobic core packing suggest a stable mesophilic enzyme. (3) With 49 eliminated by composition and 20/21 weakened by absence of extreme cold-adaptation features, 37°C is the reasonable mesophilic default. Additionally, the simultaneous presence of both 20 and 21 as separate options creates near-equivalence for cold-adapted answers, making a single unambiguous mesophilic answer (37) more likely by test design logic.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate the thermophilic option (49°C) from clear compositional absences (multiple Cys, low Arg, no salt-bridge enrichment) and argue against extreme cold-adaptation (20/21°C) from the absence of psychrophilic signatures (no extreme Gly excess, no very low hydrophobicity, canonical stable motifs). The remaining mesophilic default of 37°C is the most defensible choice. The argument is probabilistic rather than definitive for 37 vs 20, but the dual 20/21 options and the absence of any cold-adaptation signature make 37 the most distinguishable answer among the four.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B (20°C) and D (21°C) represent essentially the same thermal category (room-temperature/temperate). If the protein were cold-adapted, both would be equally defensible, creating an internal ambiguity. However, since the evidence supports 37°C and the composition lacks cold-adaptation features, this ambiguity does not affect the correct answer.


### Important caveats

- The distinction between 37°C and 20°C from sequence composition alone is subtle; the argument relies primarily on the absence of extreme cold-adaptation features rather than positive evidence uniquely indicating 37°C.
- The presence of both 20 and 21 as separate options is a design choice that effectively penalizes cold-adapted answers (since both would be equally valid), which may be intentional or may reflect a data artifact.
- The experimental optimum temperature (37°C) reflects in vitro assay conditions from a 2002 publication; the in vivo physiological temperature of the tropical plant Rauvolfia serpentina may differ.
- The model does not receive organism identity from the sequence; the tropical-plant context that would naturally suggest ~37°C must be inferred from composition or family knowledge rather than stated explicitly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical Rossmann-fold NAD(P)-binding motifs (GATMGS, GKSTK) identifying it as an oxidoreductase. Composition analysis provides a chain of elimination: (1) 49°C is ruled out because the protein has multiple Cys residues (~5-6), a low Arg-to-Lys ratio (Lys-rich, Arg-poor), and lacks the high charge density, short loops, and reduced thermolabile residues characteristic of thermophilic proteins. (2) 20°C and 21°C are argued against because the protein lacks the extreme cold-adaptation signatures: it does not show very high Gly content, very low Pro, very low overall hydrophobicity, or the excessive loop flexibility typical of psychrophilic enzymes. The canonical, well-conserved Rossmann motifs and moderate hydrophobic core packing suggest a stable mesophilic enzyme. (3) With 49 eliminated by composition and 20/21 weakened by absence of extreme cold-adaptation features, 37°C is the reasonable mesophilic default. Additionally, the simultaneous presence of both 20 and 21 as separate options creates near-equivalence for cold-adapted answers, making a single unambiguous mesophilic answer (37) more likely by test design logic.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate the thermophilic option (49°C) from clear compositional absences (multiple Cys, low Arg, no salt-bridge enrichment) and argue against extreme cold-adaptation (20/21°C) from the absence of psychrophilic signatures (no extreme Gly excess, no very low hydrophobicity, canonical stable motifs). The remaining mesophilic default of 37°C is the most defensible choice. The argument is probabilistic rather than definitive for 37 vs 20, but the dual 20/21 options and the absence of any cold-adaptation signature make 37 the most distinguishable answer among the four."
  },
  "case_id": "temperature_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 37 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:12391554. The benchmark sequence matches the source sequence (SHA256 confirmed, 363 aa). The answer 37°C is directly annotated from experimental measurement."
  },
  "important_caveats": [
    "The distinction between 37°C and 20°C from sequence composition alone is subtle; the argument relies primarily on the absence of extreme cold-adaptation features rather than positive evidence uniquely indicating 37°C.",
    "The presence of both 20 and 21 as separate options is a design choice that effectively penalizes cold-adapted answers (since both would be equally valid), which may be intentional or may reflect a data artifact.",
    "The experimental optimum temperature (37°C) reflects in vitro assay conditions from a 2002 publication; the in vivo physiological temperature of the tropical plant Rauvolfia serpentina may differ.",
    "The model does not receive organism identity from the sequence; the tropical-plant context that would naturally suggest ~37°C must be inferred from composition or family knowledge rather than stated explicitly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B (20°C) and D (21°C) represent essentially the same thermal category (room-temperature/temperate). If the protein were cold-adapted, both would be equally defensible, creating an internal ambiguity. However, since the evidence supports 37°C and the composition lacks cold-adaptation features, this ambiguity does not affect the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 37 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:12391554. The benchmark sequence matches the source sequence (SHA256 confirmed, 363 aa). The answer 37°C is directly annotated from experimental measurement.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical Rossmann-fold NAD(P)-binding motifs (GATMGS, GKSTK) identifying it as an oxidoreductase. Composition analysis provides a chain of elimination: (1) 49°C is ruled out because the protein has multiple Cys residues (~5-6), a low Arg-to-Lys ratio (Lys-rich, Arg-poor), and lacks the high charge density, short loops, and reduced thermolabile residues characteristic of thermophilic proteins. (2) 20°C and 21°C are argued against because the protein lacks the extreme cold-adaptation signatures: it does not show very high Gly content, very low Pro, very low overall hydrophobicity, or the excessive loop flexibility typical of psychrophilic enzymes. The canonical, well-conserved Rossmann motifs and moderate hydrophobic core packing suggest a stable mesophilic enzyme. (3) With 49 eliminated by composition and 20/21 weakened by absence of extreme cold-adaptation features, 37°C is the reasonable mesophilic default. Additionally, the simultaneous presence of both 20 and 21 as separate options creates near-equivalence for cold-adapted answers, making a single unambiguous mesophilic answer (37) more likely by test design logic.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate the thermophilic option (49°C) from clear compositional absences (multiple Cys, low Arg, no salt-bridge enrichment) and argue against extreme cold-adaptation (20/21°C) from the absence of psychrophilic signatures (no extreme Gly excess, no very low hydrophobicity, canonical stable motifs). The remaining mesophilic default of 37°C is the most defensible choice. The argument is probabilistic rather than definitive for 37 vs 20, but the dual 20/21 options and the absence of any cold-adaptation signature make 37 the most distinguishable answer among the four."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B (20°C) and D (21°C) represent essentially the same thermal category (room-temperature/temperate). If the protein were cold-adapted, both would be equally defensible, creating an internal ambiguity. However, since the evidence supports 37°C and the composition lacks cold-adaptation features, this ambiguity does not affect the correct answer."
  },
  "important_caveats": [
    "The distinction between 37°C and 20°C from sequence composition alone is subtle; the argument relies primarily on the absence of extreme cold-adaptation features rather than positive evidence uniquely indicating 37°C.",
    "The presence of both 20 and 21 as separate options is a design choice that effectively penalizes cold-adapted answers (since both would be equally valid), which may be intentional or may reflect a data artifact.",
    "The experimental optimum temperature (37°C) reflects in vitro assay conditions from a 2002 publication; the in vivo physiological temperature of the tropical plant Rauvolfia serpentina may differ.",
    "The model does not receive organism identity from the sequence; the tropical-plant context that would naturally suggest ~37°C must be inferred from composition or family knowledge rather than stated explicitly."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
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
  "requested_accession": "A0A0U3S9Q3",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "selected_historical_version": {
    "accession": "A0A0U3S9Q3",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHVOR_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3S9Q3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsRR4\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsVR2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.73\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1,2-Dihydrovomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsDHVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":43.16,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"substrate\":\"vomilenine\",\"unit\":\"uM\"},{\"constant\":1089.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"substrate\":\"vomilenine\",\"unit\":\"uM\"},{\"constant\":32.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"substrate\":\"1,2-dihydrovomilenine\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"kcat is 0.2 sec(-1) with vomilenine as substrate (PubMed:38212296). kcat is 10.4 sec(-1) with 1,2-dihydrovomilenine as substrate (PubMed:38212296).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 6.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 37 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82981.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1)\",\"PROTEIN SEQUENCE OF 5-13 AND 298-308\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61918.1\",\"source\":\"EMBL\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Gao S.\",\"von Schumann G.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12391554\"},{\"database\":\"DOI\",\"id\":\"10.1055/s-2002-34935\"}],\"citationType\":\"journal article\",\"firstPage\":\"906\",\"id\":\"12391554\",\"journal\":\"Planta Med.\",\"lastPage\":\"911\",\"publicationDate\":\"2002\",\"title\":\"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis of the antiarrhythmic alkaloid ajmaline.\",\"volume\":\"68\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   DHVOR_RAUSE             Reviewed;         363 AA.\nAC   A0A0U3S9Q3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RsDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR4 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\nGN   Name=DHVR {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR4 {ECO:0000303|PubMed:26715562},\nGN   VR2 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82981.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1), PROTEIN SEQUENCE OF 5-13 AND\nRP   298-308, FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:WKU61918.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=12391554; DOI=10.1055/s-2002-34935;\nRA   Gao S., von Schumann G., Stoeckigt J.;\nRT   \"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis\nRT   of the antiarrhythmic alkaloid ajmaline.\";\nRL   Planta Med. 68:906-911(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=43.16 uM for vomilenine {ECO:0000269|PubMed:26715562};\nCC         KM=1089 uM for vomilenine {ECO:0000269|PubMed:38212296};\nCC         KM=32 uM for 1,2-dihydrovomilenine {ECO:0000269|PubMed:38212296};\nCC         Note=kcat is 0.2 sec(-1) with vomilenine as substrate\nCC         (PubMed:38212296). kcat is 10.4 sec(-1) with 1,2-dihydrovomilenine as\nCC         substrate (PubMed:38212296). {ECO:0000269|PubMed:38212296};\nCC       pH dependence:\nCC         Optimum pH is 6. {ECO:0000269|PubMed:12391554};\nCC       Temperature dependence:\nCC         Optimum temperature is 37 degrees Celsius.\nCC         {ECO:0000269|PubMed:12391554};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
