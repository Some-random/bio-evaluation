# temperature_0025

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0025.txt)

**Task:** `temperature`  
**Expected answer:** **D** — 80

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. 32
B. 23
C. 64
D. 80
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

> A sequence-matched UniProt annotation reports an optimum temperature of 80°C for this enzyme’s oxidation of hexanal, citing experimental evidence. This supports choice D for the measured reaction, though it is not necessarily a universal optimum across substrates or conditions.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The measured temperature optimum for this exact protein under a specified assay; the supplied evidence gives 80°C for hexanal oxidation.


**Reason**

> Sequence or family-level clues might suggest a thermostable enzyme, but they do not meaningfully distinguish 80°C from the also-high 64°C option. Choosing the exact value requires a fact about this protein’s measured temperature dependence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct numeric temperatures, and the reported optimum for the cited reaction matches only 80°C.


### Important caveats

- The evidence supports 80°C specifically for oxidation of hexanal; the question does not specify substrate or assay conditions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured temperature optimum for this exact protein under a specified assay; the supplied evidence gives 80°C for hexanal oxidation.",
    "reason": "Sequence or family-level clues might suggest a thermostable enzyme, but they do not meaningfully distinguish 80°C from the also-high 64°C option. Choosing the exact value requires a fact about this protein’s measured temperature dependence."
  },
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "A sequence-matched UniProt annotation reports an optimum temperature of 80°C for this enzyme’s oxidation of hexanal, citing experimental evidence. This supports choice D for the measured reaction, though it is not necessarily a universal optimum across substrates or conditions."
  },
  "important_caveats": [
    "The evidence supports 80°C specifically for oxidation of hexanal; the question does not specify substrate or assay conditions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numeric temperatures, and the reported optimum for the cited reaction matches only 80°C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "A sequence-matched UniProt annotation reports an optimum temperature of 80°C for this enzyme’s oxidation of hexanal, citing experimental evidence. This supports choice D for the measured reaction, though it is not necessarily a universal optimum across substrates or conditions.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The measured temperature optimum for this exact protein under a specified assay; the supplied evidence gives 80°C for hexanal oxidation.",
    "reason": "Sequence or family-level clues might suggest a thermostable enzyme, but they do not meaningfully distinguish 80°C from the also-high 64°C option. Choosing the exact value requires a fact about this protein’s measured temperature dependence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numeric temperatures, and the reported optimum for the cited reaction matches only 80°C."
  },
  "important_caveats": [
    "The evidence supports 80°C specifically for oxidation of hexanal; the question does not specify substrate or assay conditions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FHH1 (sequence matched exactly) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is 80 degrees Celsius for the oxidation of hexanal,' supported by experimental evidence (ECO:0000269, PubMed:16199576). The protein is from Pyrococcus furiosus, an extremely thermophilic archaeon. The expected answer of 80°C is directly confirmed by experimental measurement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the tungsten-containing aldehyde oxidoreductase (AOR) family, including the 'GAGGYS' tungstopterin-binding motif and the characteristic fold architecture. Transferable family-level knowledge establishes that tungsten-containing AORs are found almost exclusively in hyperthermophilic archaea (Pyrococcus, Thermococcus, Thermotoga), with optimal temperatures in the 80–100°C range. Additionally, the sequence shows an extremely high density of charged residues (K, E, R, D) throughout, with clusters like 'EKVKEVELSEDVLKK', 'KLLKEVHEEIRKKEKLKG', and 'KREVKRIKKRLNL', which is a well-documented signature of hyperthermophilic proteins (salt-bridge networks for thermostability). The very low content of thermolabile residues (only two Cys in the entire 624-aa sequence) further supports extreme thermophily. These features collectively distinguish the hyperthermophilic range (80°C) from moderate thermophily (64°C) and mesophily (23°C, 32°C): the AOR family association with hyperthermophiles, combined with the extreme charge enrichment, makes 80°C the most defensible choice over 64°C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the tungsten-AOR family from sequence motifs and apply the well-established family-level association of tungsten AORs with hyperthermophilic archaea (80–100°C). The extreme charged-residue density and near-absence of thermolabile residues further support the hyperthermophilic category. This is legitimate transferable knowledge from other proteins in the AOR family, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options (23, 32, 64, 80°C) span mesophilic to hyperthermophilic ranges. The tungsten-AOR family association with hyperthermophiles and the extreme sequence composition features clearly favor 80°C over 64°C (moderate thermophile) and the mesophilic options. No genuine ambiguity exists among the offered choices.


### Important caveats

- The exact distinction between 80°C and 64°C relies on family-level knowledge that tungsten AORs are exclusively hyperthermophilic; a model without this specific family knowledge might find 64°C marginally more defensible based on charge content alone.
- The UniProt annotation reports 80°C specifically for hexanal oxidation; the optimal temperature may vary slightly with substrate, but 80°C is the stated experimental optimum.
- The reviewer-only evidence confirms the sequence matches UniProt E7FHH1 exactly (624 AA, SHA-256 match), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the tungsten-containing aldehyde oxidoreductase (AOR) family, including the 'GAGGYS' tungstopterin-binding motif and the characteristic fold architecture. Transferable family-level knowledge establishes that tungsten-containing AORs are found almost exclusively in hyperthermophilic archaea (Pyrococcus, Thermococcus, Thermotoga), with optimal temperatures in the 80–100°C range. Additionally, the sequence shows an extremely high density of charged residues (K, E, R, D) throughout, with clusters like 'EKVKEVELSEDVLKK', 'KLLKEVHEEIRKKEKLKG', and 'KREVKRIKKRLNL', which is a well-documented signature of hyperthermophilic proteins (salt-bridge networks for thermostability). The very low content of thermolabile residues (only two Cys in the entire 624-aa sequence) further supports extreme thermophily. These features collectively distinguish the hyperthermophilic range (80°C) from moderate thermophily (64°C) and mesophily (23°C, 32°C): the AOR family association with hyperthermophiles, combined with the extreme charge enrichment, makes 80°C the most defensible choice over 64°C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the tungsten-AOR family from sequence motifs and apply the well-established family-level association of tungsten AORs with hyperthermophilic archaea (80–100°C). The extreme charged-residue density and near-absence of thermolabile residues further support the hyperthermophilic category. This is legitimate transferable knowledge from other proteins in the AOR family, not a lookup of this specific protein's annotation."
  },
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FHH1 (sequence matched exactly) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is 80 degrees Celsius for the oxidation of hexanal,' supported by experimental evidence (ECO:0000269, PubMed:16199576). The protein is from Pyrococcus furiosus, an extremely thermophilic archaeon. The expected answer of 80°C is directly confirmed by experimental measurement."
  },
  "important_caveats": [
    "The exact distinction between 80°C and 64°C relies on family-level knowledge that tungsten AORs are exclusively hyperthermophilic; a model without this specific family knowledge might find 64°C marginally more defensible based on charge content alone.",
    "The UniProt annotation reports 80°C specifically for hexanal oxidation; the optimal temperature may vary slightly with substrate, but 80°C is the stated experimental optimum.",
    "The reviewer-only evidence confirms the sequence matches UniProt E7FHH1 exactly (624 AA, SHA-256 match), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options (23, 32, 64, 80°C) span mesophilic to hyperthermophilic ranges. The tungsten-AOR family association with hyperthermophiles and the extreme sequence composition features clearly favor 80°C over 64°C (moderate thermophile) and the mesophilic options. No genuine ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E7FHH1 (sequence matched exactly) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is 80 degrees Celsius for the oxidation of hexanal,' supported by experimental evidence (ECO:0000269, PubMed:16199576). The protein is from Pyrococcus furiosus, an extremely thermophilic archaeon. The expected answer of 80°C is directly confirmed by experimental measurement.",
    "evidence_ids": ["C5", "C6", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the tungsten-containing aldehyde oxidoreductase (AOR) family, including the 'GAGGYS' tungstopterin-binding motif and the characteristic fold architecture. Transferable family-level knowledge establishes that tungsten-containing AORs are found almost exclusively in hyperthermophilic archaea (Pyrococcus, Thermococcus, Thermotoga), with optimal temperatures in the 80–100°C range. Additionally, the sequence shows an extremely high density of charged residues (K, E, R, D) throughout, with clusters like 'EKVKEVELSEDVLKK', 'KLLKEVHEEIRKKEKLKG', and 'KREVKRIKKRLNL', which is a well-documented signature of hyperthermophilic proteins (salt-bridge networks for thermostability). The very low content of thermolabile residues (only two Cys in the entire 624-aa sequence) further supports extreme thermophily. These features collectively distinguish the hyperthermophilic range (80°C) from moderate thermophily (64°C) and mesophily (23°C, 32°C): the AOR family association with hyperthermophiles, combined with the extreme charge enrichment, makes 80°C the most defensible choice over 64°C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the tungsten-AOR family from sequence motifs and apply the well-established family-level association of tungsten AORs with hyperthermophilic archaea (80–100°C). The extreme charged-residue density and near-absence of thermolabile residues further support the hyperthermophilic category. This is legitimate transferable knowledge from other proteins in the AOR family, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options (23, 32, 64, 80°C) span mesophilic to hyperthermophilic ranges. The tungsten-AOR family association with hyperthermophiles and the extreme sequence composition features clearly favor 80°C over 64°C (moderate thermophile) and the mesophilic options. No genuine ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The exact distinction between 80°C and 64°C relies on family-level knowledge that tungsten AORs are exclusively hyperthermophilic; a model without this specific family knowledge might find 64°C marginally more defensible based on charge content alone.",
    "The UniProt annotation reports 80°C specifically for hexanal oxidation; the optimal temperature may vary slightly with substrate, but 80°C is the stated experimental optimum.",
    "The reviewer-only evidence confirms the sequence matches UniProt E7FHH1 exactly (624 AA, SHA-256 match), so the annotation applies directly to the supplied sequence."
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
  "benchmark_sequence_length": 624,
  "benchmark_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_entry_audit": {
    "entryVersion": 61,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 624,
  "current_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E7FHH1",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "selected_historical_source_sequence_length": 624,
  "selected_historical_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "selected_historical_version": {
    "accession": "E7FHH1",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASOR_PYRFU",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E7FHH1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":61,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Aliphatic sulfonate ferredoxin oxidoreductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"ASOR\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"Tungsten-containing aldehyde oxidoreductase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"WOR5\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5 large subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5-L\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aliphatic sulfonate oxidoreductase, WOR-like subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with taurine as substrate (with benzyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":14.9},{\"enzyme\":\"enzyme with hexanal as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":15.6},{\"enzyme\":\"enzyme with hexanal as substrate (with benzyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":30.0},{\"enzyme\":\"enzyme with hydratropaldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":9.3},{\"enzyme\":\"enzyme with 2-ethylhexanal as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":8.3},{\"enzyme\":\"enzyme with 2-methylvaleraldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":12.7},{\"enzyme\":\"enzyme with 3-phenylbutyraldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":8.0},{\"enzyme\":\"enzyme with 2-methylbutyraldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":7.7},{\"enzyme\":\"enzyme with isobutyraldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":11.8},{\"enzyme\":\"enzyme with 2-naphthaldehyde(beta) as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":7.7},{\"enzyme\":\"enzyme with acetaldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":0.34},{\"enzyme\":\"enzyme with cinnamaldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":7.4},{\"enzyme\":\"enzyme with propionaldehyde as substrate (with benzyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":26.2},{\"enzyme\":\"enzyme with 2-methoxybenzaldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":15.1},{\"enzyme\":\"enzyme with glutaraldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":1.4},{\"enzyme\":\"enzyme with formaldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":8.5},{\"enzyme\":\"enzyme with crotonaldehyde as substrate (with methyl viologen as electron acceptor)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":1.1}],\"michaelisConstants\":[{\"constant\":0.112,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"substrate\":\"taurine\",\"unit\":\"mM\"},{\"constant\":0.18,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"hexanal\",\"unit\":\"mM\"},{\"constant\":0.23,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"substrate\":\"hexanal\",\"unit\":\"mM\"},{\"constant\":0.12,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"hydratropaldehyde\",\"unit\":\"mM\"},{\"constant\":0.17,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"2-ethylhexanal\",\"unit\":\"mM\"},{\"constant\":0.27,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"2-methylvaleraldehyde\",\"unit\":\"mM\"},{\"constant\":0.42,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"3-phenylbutyraldehyde\",\"unit\":\"mM\"},{\"constant\":0.43,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"2-methylbutyraldehyde\",\"unit\":\"mM\"},{\"constant\":0.79,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"isobutyraldehyde\",\"unit\":\"mM\"},{\"constant\":1.3,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"2-naphthaldehyde(beta)\",\"unit\":\"mM\"},{\"constant\":1.5,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"acetaldehyde\",\"unit\":\"mM\"},{\"constant\":1.6,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"cinnamaldehyde\",\"unit\":\"mM\"},{\"constant\":2.047,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"substrate\":\"propionaldehyde\",\"unit\":\"mM\"},{\"constant\":4.8,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"2-methoxybenzaldehyde\",\"unit\":\"mM\"},{\"constant\":9.4,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"glutaraldehyde\",\"unit\":\"mM\"},{\"constant\":45.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"formaldehyde\",\"unit\":\"mM\"},{\"constant\":46.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"substrate\":\"crotonaldehyde\",\"unit\":\"mM\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 80 degrees Celsius for the oxidation of hexanal.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/9",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bevers L.E.\",\"Bol E.\",\"Hagedoorn P.L.\",\"Hagen W.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16199576\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.20.7056-7061.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"7056\",\"id\":\"16199576\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"7061\",\"publicationDate\":\"2005\",\"title\":\"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus furiosus with a broad substrate specificity.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 43587 / DSM 3638 / JCM 8422 / Vc1\"}],\"referenceNumber\":3,\"referencePositions\":[\"PROTEIN SEQUENCE OF 1-21\",\"FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Mathew L.G.\",\"Haja D.K.\",\"Pritchett C.\",\"McCormick W.\",\"Zeineddine R.\",\"Fontenot L.S.\",\"Rivera M.E.\",\"Glushka J.\",\"Adams M.W.W.\",\"Lanzilotta W.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36269456\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00775-022-01965-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"747\",\"id\":\"36269456\",\"journal\":\"J. Biol. Inorg. Chem.\",\"lastPage\":\"758\",\"publicationDate\":\"2022\",\"title\":\"An unprecedented function for a tungsten-containing oxidoreductase.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X1O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X6U\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   ASOR_PYRFU              Reviewed;         624 AA.\nAC   E7FHH1; A0A5C0XQU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\nGN   Name=wor5 {ECO:0000303|PubMed:16199576};\nGN   OrderedLocusNames=PF1480 {ECO:0000312|EMBL:AAL81604.1};\nGN   ORFNames=PFDSM3638_07420 {ECO:0000312|EMBL:QEK79109.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   PROTEIN SEQUENCE OF 1-21, FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 43587 / DSM 3638 / JCM 8422 / Vc1;\nRX   PubMed=16199576; DOI=10.1128/jb.187.20.7056-7061.2005;\nRA   Bevers L.E., Bol E., Hagedoorn P.L., Hagen W.R.;\nRT   \"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus\nRT   furiosus with a broad substrate specificity.\";\nRL   J. Bacteriol. 187:7056-7061(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}\nRP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR\nRP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.\nRC   STRAIN=COM1;\nRX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;\nRA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,\nRA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;\nRT   \"An unprecedented function for a tungsten-containing oxidoreductase.\";\nRL   J. Biol. Inorg. Chem. 27:747-758(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=0.112 mM for taurine {ECO:0000269|PubMed:36269456};\nCC         KM=0.18 mM for hexanal {ECO:0000269|PubMed:16199576};\nCC         KM=0.230 mM for hexanal {ECO:0000269|PubMed:36269456};\nCC         KM=0.12 mM for hydratropaldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=0.17 mM for 2-ethylhexanal {ECO:0000269|PubMed:16199576};\nCC         KM=0.27 mM for 2-methylvaleraldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=0.42 mM for 3-phenylbutyraldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=0.43 mM for 2-methylbutyraldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=0.79 mM for isobutyraldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=1.3 mM for 2-naphthaldehyde(beta) {ECO:0000269|PubMed:16199576};\nCC         KM=1.5 mM for acetaldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=1.6 mM for cinnamaldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=2.047 mM for propionaldehyde {ECO:0000269|PubMed:36269456};\nCC         KM=4.8 mM for 2-methoxybenzaldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=9.4 mM for glutaraldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=45 mM for formaldehyde {ECO:0000269|PubMed:16199576};\nCC         KM=46 mM for crotonaldehyde {ECO:0000269|PubMed:16199576};\nCC         Vmax=14.9 umol/min/mg enzyme with taurine as substrate (with benzyl\nCC         viologen as electron acceptor) {ECO:0000269|PubMed:36269456};\nCC         Vmax=15.6 umol/min/mg enzyme with hexanal as substrate (with methyl\nCC         viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=30.0 umol/min/mg enzyme with hexanal as substrate (with benzyl\nCC         viologen as electron acceptor) {ECO:0000269|PubMed:36269456};\nCC         Vmax=9.3 umol/min/mg enzyme with hydratropaldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=8.3 umol/min/mg enzyme with 2-ethylhexanal as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=12.7 umol/min/mg enzyme with 2-methylvaleraldehyde as substrate\nCC         (with methyl viologen as electron acceptor)\nCC         {ECO:0000269|PubMed:16199576};\nCC         Vmax=8.0 umol/min/mg enzyme with 3-phenylbutyraldehyde as substrate\nCC         (with methyl viologen as electron acceptor)\nCC         {ECO:0000269|PubMed:16199576};\nCC         Vmax=7.7 umol/min/mg enzyme with 2-methylbutyraldehyde as substrate\nCC         (with methyl viologen as electron acceptor)\nCC         {ECO:0000269|PubMed:16199576};\nCC         Vmax=11.8 umol/min/mg enzyme with isobutyraldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=7.7 umol/min/mg enzyme with 2-naphthaldehyde(beta) as substrate\nCC         (with methyl viologen as electron acceptor)\nCC         {ECO:0000269|PubMed:16199576};\nCC         Vmax=0.34 umol/min/mg enzyme with acetaldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=7.4 umol/min/mg enzyme with cinnamaldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=26.2 umol/min/mg enzyme with propionaldehyde as substrate (with\nCC         benzyl viologen as electron acceptor) {ECO:0000269|PubMed:36269456};\nCC         Vmax=15.1 umol/min/mg enzyme with 2-methoxybenzaldehyde as substrate\nCC         (with methyl viologen as electron acceptor)\nCC         {ECO:0000269|PubMed:16199576};\nCC         Vmax=1.4 umol/min/mg enzyme with glutaraldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=8.5 umol/min/mg enzyme with formaldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC         Vmax=1.1 umol/min/mg enzyme with crotonaldehyde as substrate (with\nCC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};\nCC       Temperature dependence:\nCC         Optimum temperature is 80 degrees Celsius for the oxidation of\nCC         hexanal. {ECO:0000269|PubMed:16199576};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-184",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
