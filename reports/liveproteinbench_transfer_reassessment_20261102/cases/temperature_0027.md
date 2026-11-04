# temperature_0027

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0027.txt)

**Task:** `temperature`  
**Expected answer:** **D** — 55

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. 79
B. 76
C. 32
D. 55
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

> The sequence-matched UniProt annotation reports an experimentally supported optimum temperature of 55 °C, matching choice D.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's measured temperature optimum, or a reliable target-specific annotation of it, is needed to select 55 °C over the other listed values.


**Reason**

> The sequence provides no clear transferable feature that reliably distinguishes a 55 °C optimum from 32, 76, or 79 °C. General sequence-based tendencies toward stability are not sufficient to infer this enzyme's specific optimum.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct temperatures, and the supplied reviewer evidence identifies 55 °C as the experimentally reported optimum.


### Important caveats

- The evidence supports 55 °C as the reported optimum, not a complete description of the protein's thermal stability or adaptation category.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's measured temperature optimum, or a reliable target-specific annotation of it, is needed to select 55 °C over the other listed values.",
    "reason": "The sequence provides no clear transferable feature that reliably distinguishes a 55 °C optimum from 32, 76, or 79 °C. General sequence-based tendencies toward stability are not sufficient to infer this enzyme's specific optimum."
  },
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an experimentally supported optimum temperature of 55 °C, matching choice D."
  },
  "important_caveats": [
    "The evidence supports 55 °C as the reported optimum, not a complete description of the protein's thermal stability or adaptation category."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct temperatures, and the supplied reviewer evidence identifies 55 °C as the experimentally reported optimum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an experimentally supported optimum temperature of 55 °C, matching choice D.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's measured temperature optimum, or a reliable target-specific annotation of it, is needed to select 55 °C over the other listed values.",
    "reason": "The sequence provides no clear transferable feature that reliably distinguishes a 55 °C optimum from 32, 76, or 79 °C. General sequence-based tendencies toward stability are not sufficient to infer this enzyme's specific optimum."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct temperatures, and the supplied reviewer evidence identifies 55 °C as the experimentally reported optimum."
  },
  "important_caveats": [
    "The evidence supports 55 °C as the reported optimum, not a complete description of the protein's thermal stability or adaptation category."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (I0AIT9, Beta-1,2-glucosyltransferase from Ignavibacterium album) explicitly states 'Optimum temperature is 55 degrees Celsius' and 'Stable up to 60 degrees Celsius after incubation for 1 hour,' both backed by experimental evidence (ECO:0000269, PubMed:35065074, J. Biol. Chem. 2022). The expected answer of 55°C is directly confirmed by experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span a wide thermal range: 32°C (psychrophilic), 55°C (moderate thermophilic), 76°C and 79°C (hyperthermophilic). A knowledgeable model can eliminate 76 and 79 because the sequence lacks the extreme signatures of hyperthermophilic proteins: it does not show the very high charged-residue fraction (>20-25%), very low thermolabile-residue content (C, Q, N), or extremely short loops characteristic of proteins from organisms growing at 75-80°C (e.g., Pyrococcus, Thermotoga). The sequence also contains numerous prolines and a moderate-to-high density of charged residues (K, E, D, R) forming potential salt bridges, features more consistent with moderate thermophily than psychrophily. For 32°C, one would expect fewer salt bridges, lower proline content, more glycine-rich flexible loops, and reduced hydrophobic packing — none of which are strongly evident here. The protein belongs to the glycosyltransferase family; while GH enzymes span all temperatures, the combination of moderate charge density, proline frequency, and absence of extreme signatures points away from both hyperthermophily and psychrophily, favoring the moderate thermophilic option (55°C). Additionally, Ignavibacterium species are known from thermal spring mats, and family-level ecological knowledge supports moderate thermophily over the 32°C option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The spread of options (32 vs 55 vs 76/79) is wide enough that general sequence-composition reasoning and family-level knowledge about glycosyltransferases and their thermal adaptations can meaningfully eliminate the extreme options. The moderate thermophilic character is inferable from the balance of charged residues, proline content, and absence of hyperthermophilic or psychrophilic extremes. While recognizing the exact organism (Ignavibacterium album, a hot-spring mat organism) would further confirm 55°C, the sequence-based elimination of 76/79 and the weak-but-reasonable discrimination against 32 provide a defensible probabilistic path to 55.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are well-separated (32, 55, 76, 79). While distinguishing 55 from 32 requires moderate sequence analysis or ecological knowledge, the combination of features (charge density, proline content, lack of psychrophilic flexibility signatures) makes 55 the most defensible choice among the four. No two options are close enough to be genuinely ambiguous.


### Important caveats

- The exact optimum temperature of 55°C is an experimental measurement (PubMed:35065074); the sequence-based reasoning supports the moderate thermophilic category but cannot pinpoint 55 to the degree.
- Recognition of Ignavibacterium as a hot-spring organism strengthens the case for 55 over 32, but this recognition from sequence alone borders on lookup; the argument is primarily supported by sequence-composition features.
- The protein's stability up to 60°C (also experimental) is consistent with the 55°C optimum but is not encoded in the sequence as a directly readable feature.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span a wide thermal range: 32°C (psychrophilic), 55°C (moderate thermophilic), 76°C and 79°C (hyperthermophilic). A knowledgeable model can eliminate 76 and 79 because the sequence lacks the extreme signatures of hyperthermophilic proteins: it does not show the very high charged-residue fraction (>20-25%), very low thermolabile-residue content (C, Q, N), or extremely short loops characteristic of proteins from organisms growing at 75-80°C (e.g., Pyrococcus, Thermotoga). The sequence also contains numerous prolines and a moderate-to-high density of charged residues (K, E, D, R) forming potential salt bridges, features more consistent with moderate thermophily than psychrophily. For 32°C, one would expect fewer salt bridges, lower proline content, more glycine-rich flexible loops, and reduced hydrophobic packing — none of which are strongly evident here. The protein belongs to the glycosyltransferase family; while GH enzymes span all temperatures, the combination of moderate charge density, proline frequency, and absence of extreme signatures points away from both hyperthermophily and psychrophily, favoring the moderate thermophilic option (55°C). Additionally, Ignavibacterium species are known from thermal spring mats, and family-level ecological knowledge supports moderate thermophily over the 32°C option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The spread of options (32 vs 55 vs 76/79) is wide enough that general sequence-composition reasoning and family-level knowledge about glycosyltransferases and their thermal adaptations can meaningfully eliminate the extreme options. The moderate thermophilic character is inferable from the balance of charged residues, proline content, and absence of hyperthermophilic or psychrophilic extremes. While recognizing the exact organism (Ignavibacterium album, a hot-spring mat organism) would further confirm 55°C, the sequence-based elimination of 76/79 and the weak-but-reasonable discrimination against 32 provide a defensible probabilistic path to 55."
  },
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (I0AIT9, Beta-1,2-glucosyltransferase from Ignavibacterium album) explicitly states 'Optimum temperature is 55 degrees Celsius' and 'Stable up to 60 degrees Celsius after incubation for 1 hour,' both backed by experimental evidence (ECO:0000269, PubMed:35065074, J. Biol. Chem. 2022). The expected answer of 55°C is directly confirmed by experimental measurement."
  },
  "important_caveats": [
    "The exact optimum temperature of 55°C is an experimental measurement (PubMed:35065074); the sequence-based reasoning supports the moderate thermophilic category but cannot pinpoint 55 to the degree.",
    "Recognition of Ignavibacterium as a hot-spring organism strengthens the case for 55 over 32, but this recognition from sequence alone borders on lookup; the argument is primarily supported by sequence-composition features.",
    "The protein's stability up to 60°C (also experimental) is consistent with the 55°C optimum but is not encoded in the sequence as a directly readable feature."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-separated (32, 55, 76, 79). While distinguishing 55 from 32 requires moderate sequence analysis or ecological knowledge, the combination of features (charge density, proline content, lack of psychrophilic flexibility signatures) makes 55 the most defensible choice among the four. No two options are close enough to be genuinely ambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (I0AIT9, Beta-1,2-glucosyltransferase from Ignavibacterium album) explicitly states 'Optimum temperature is 55 degrees Celsius' and 'Stable up to 60 degrees Celsius after incubation for 1 hour,' both backed by experimental evidence (ECO:0000269, PubMed:35065074, J. Biol. Chem. 2022). The expected answer of 55°C is directly confirmed by experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options span a wide thermal range: 32°C (psychrophilic), 55°C (moderate thermophilic), 76°C and 79°C (hyperthermophilic). A knowledgeable model can eliminate 76 and 79 because the sequence lacks the extreme signatures of hyperthermophilic proteins: it does not show the very high charged-residue fraction (>20-25%), very low thermolabile-residue content (C, Q, N), or extremely short loops characteristic of proteins from organisms growing at 75-80°C (e.g., Pyrococcus, Thermotoga). The sequence also contains numerous prolines and a moderate-to-high density of charged residues (K, E, D, R) forming potential salt bridges, features more consistent with moderate thermophily than psychrophily. For 32°C, one would expect fewer salt bridges, lower proline content, more glycine-rich flexible loops, and reduced hydrophobic packing — none of which are strongly evident here. The protein belongs to the glycosyltransferase family; while GH enzymes span all temperatures, the combination of moderate charge density, proline frequency, and absence of extreme signatures points away from both hyperthermophily and psychrophily, favoring the moderate thermophilic option (55°C). Additionally, Ignavibacterium species are known from thermal spring mats, and family-level ecological knowledge supports moderate thermophily over the 32°C option.",
    "missing_item_specific_fact": "",
    "reason": "The spread of options (32 vs 55 vs 76/79) is wide enough that general sequence-composition reasoning and family-level knowledge about glycosyltransferases and their thermal adaptations can meaningfully eliminate the extreme options. The moderate thermophilic character is inferable from the balance of charged residues, proline content, and absence of hyperthermophilic or psychrophilic extremes. While recognizing the exact organism (Ignavibacterium album, a hot-spring mat organism) would further confirm 55°C, the sequence-based elimination of 76/79 and the weak-but-reasonable discrimination against 32 provide a defensible probabilistic path to 55."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-separated (32, 55, 76, 79). While distinguishing 55 from 32 requires moderate sequence analysis or ecological knowledge, the combination of features (charge density, proline content, lack of psychrophilic flexibility signatures) makes 55 the most defensible choice among the four. No two options are close enough to be genuinely ambiguous."
  },
  "important_caveats": [
    "The exact optimum temperature of 55°C is an experimental measurement (PubMed:35065074); the sequence-based reasoning supports the moderate thermophilic category but cannot pinpoint 55 to the degree.",
    "Recognition of Ignavibacterium as a hot-spring organism strengthens the case for 55 over 32, but this recognition from sequence alone borders on lookup; the argument is primarily supported by sequence-composition features.",
    "The protein's stability up to 60°C (also experimental) is consistent with the 55°C optimum but is not encoded in the sequence as a directly readable feature."
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
  "benchmark_sequence_length": 716,
  "benchmark_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-06-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 716,
  "current_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "I0AIT9",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "selected_historical_source_sequence_length": 716,
  "selected_historical_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "selected_historical_version": {
    "accession": "I0AIT9",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "B12GT_IGNAJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"I0AIT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-06-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Ignavibacteriota\",\"Ignavibacteria\",\"Ignavibacteriales\",\"Ignavibacteriaceae\",\"Ignavibacterium\"],\"scientificName\":\"Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16)\",\"taxonId\":945713}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"IaSGT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.391\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":9.6,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"sophorose (with pNP-alpha-glucose as an acceptor)\",\"unit\":\"mM\"},{\"constant\":22.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"beta-(1->2)-glucotriose (with pNP-alpha-glucose as an acceptor)\",\"unit\":\"mM\"},{\"constant\":0.2,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"methyl-alpha-glucose\",\"unit\":\"mM\"},{\"constant\":0.044,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"ethyl-alpha-glucose\",\"unit\":\"mM\"},{\"constant\":0.22,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"phenyl-alpha-glucose\",\"unit\":\"mM\"},{\"constant\":0.38,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"alpha-arbutin\",\"unit\":\"mM\"},{\"constant\":0.13,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"pNP-alpha-glucose\",\"unit\":\"mM\"},{\"constant\":0.096,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"benzyl-alpha-glucose\",\"unit\":\"mM\"},{\"constant\":0.15,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"2-naphthyl-alpha-glucose\",\"unit\":\"mM\"},{\"constant\":0.13,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"methyl-beta-glucose\",\"unit\":\"mM\"},{\"constant\":0.026,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"beta-arbutin\",\"unit\":\"mM\"},{\"constant\":0.04,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"pNP-beta-glucose\",\"unit\":\"mM\"},{\"constant\":0.042,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"gastrodin\",\"unit\":\"mM\"},{\"constant\":0.021,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"salicin\",\"unit\":\"mM\"},{\"constant\":0.045,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"esculin\",\"unit\":\"mM\"},{\"constant\":0.15,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"substrate\":\"amygdalin\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"kcat is 70 sec(-1) with sophorose as substrate. kcat is 12 sec(-1) with beta-(1->2)-glucotriose as substrate. kcat is 1.0 sec(-1) with methyl-alpha-glucose as substrate. kcat is 0.55 sec(-1) with ethyl-alpha-glucose as substrate. kcat is 1.8 sec(-1) with phenyl-alpha-glucose as substrate. kcat is 8.7 sec(-1) with alpha-arbutin as substrate. kcat is 5.0 sec(-1) with pNP-alpha-glucose as substrate. kcat is 0.86 sec(-1) with benzyl-alpha-glucose as substrate. kcat is 3.9 sec(-1) with 2-naphthyl-alpha-glucose as substrate. kcat is 1.9 sec(-1) with methyl-beta-glucose as substrate. kcat is 1.4 sec(-1) with beta-arbutin as substrate. kcat is 0.46 sec(-1) with pNP-beta-glucose as substrate. kcat is 0.49 sec(-1) with gastrodin as substrate. kcat is 0.88 sec(-1) with salicin as substrate. kcat is 1.3 sec(-1) with esculin as substrate. kcat is 0.35 sec(-1) with amygdalin as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Shows high activity at pH 5.0 to 8.0.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 55 degrees Celsius (PubMed:35065074). Stable up to 60 degrees Celsius after incubation for 1 hour (PubMed:35065074).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kobayashi K.\",\"Shimizu H.\",\"Tanaka N.\",\"Kuramochi K.\",\"Nakai H.\",\"Nakajima M.\",\"Taguchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35065074\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2022.101606\"}],\"citationType\":\"journal article\",\"firstPage\":\"101606\",\"id\":\"35065074\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"101606\",\"publicationDate\":\"2022\",\"title\":\"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.\",\"volume\":\"298\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKW\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL0\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-176 AND GLU-343\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   B12GT_IGNAJ             Reviewed;         716 AA.\nAC   I0AIT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\nGN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};\nOS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /\nOS   Mat9-16).\nOC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;\nOC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.\nOX   NCBI_TaxID=945713;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}\nRP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;\nRP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF\nRP   GLU-176 AND GLU-343.\nRC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;\nRX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;\nRA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,\nRA   Taguchi H.;\nRT   \"Characterization and structural analyses of a novel glycosyltransferase\nRT   acting on the beta-1,2-glucosidic linkages.\";\nRL   J. Biol. Chem. 298:101606-101606(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=9.6 mM for sophorose (with pNP-alpha-glucose as an acceptor)\nCC         {ECO:0000269|PubMed:35065074};\nCC         KM=22 mM for beta-(1->2)-glucotriose (with pNP-alpha-glucose as an\nCC         acceptor) {ECO:0000269|PubMed:35065074};\nCC         KM=0.20 mM for methyl-alpha-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.044 mM for ethyl-alpha-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.22 mM for phenyl-alpha-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.38 mM for alpha-arbutin {ECO:0000269|PubMed:35065074};\nCC         KM=0.13 mM for pNP-alpha-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.096 mM for benzyl-alpha-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.15 mM for 2-naphthyl-alpha-glucose\nCC         {ECO:0000269|PubMed:35065074};\nCC         KM=0.13 mM for methyl-beta-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.026 mM for beta-arbutin {ECO:0000269|PubMed:35065074};\nCC         KM=0.040 mM for pNP-beta-glucose {ECO:0000269|PubMed:35065074};\nCC         KM=0.042 mM for gastrodin {ECO:0000269|PubMed:35065074};\nCC         KM=0.021 mM for salicin {ECO:0000269|PubMed:35065074};\nCC         KM=0.045 mM for esculin {ECO:0000269|PubMed:35065074};\nCC         KM=0.15 mM for amygdalin {ECO:0000269|PubMed:35065074};\nCC         Note=kcat is 70 sec(-1) with sophorose as substrate. kcat is 12 sec(-\nCC         1) with beta-(1->2)-glucotriose as substrate. kcat is 1.0 sec(-1)\nCC         with methyl-alpha-glucose as substrate. kcat is 0.55 sec(-1) with\nCC         ethyl-alpha-glucose as substrate. kcat is 1.8 sec(-1) with phenyl-\nCC         alpha-glucose as substrate. kcat is 8.7 sec(-1) with alpha-arbutin as\nCC         substrate. kcat is 5.0 sec(-1) with pNP-alpha-glucose as substrate.\nCC         kcat is 0.86 sec(-1) with benzyl-alpha-glucose as substrate. kcat is\nCC         3.9 sec(-1) with 2-naphthyl-alpha-glucose as substrate. kcat is 1.9\nCC         sec(-1) with methyl-beta-glucose as substrate. kcat is 1.4 sec(-1)\nCC         with beta-arbutin as substrate. kcat is 0.46 sec(-1) with pNP-beta-\nCC         glucose as substrate. kcat is 0.49 sec(-1) with gastrodin as\nCC         substrate. kcat is 0.88 sec(-1) with salicin as substrate. kcat is\nCC         1.3 sec(-1) with esculin as substrate. kcat is 0.35 sec(-1) with\nCC         amygdalin as substrate. {ECO:0000269|PubMed:35065074};\nCC       pH dependence:\nCC         Shows high activity at pH 5.0 to 8.0. {ECO:0000269|PubMed:35065074};\nCC       Temperature dependence:\nCC         Optimum temperature is 55 degrees Celsius (PubMed:35065074). Stable\nCC         up to 60 degrees Celsius after incubation for 1 hour\nCC         (PubMed:35065074). {ECO:0000269|PubMed:35065074};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
