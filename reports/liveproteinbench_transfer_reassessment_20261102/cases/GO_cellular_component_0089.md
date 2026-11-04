# GO_cellular_component_0089

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0089.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — monoatomic ion channel complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDGSHCKVIAPLLTERHQRMVTKDGHSTLQMDGAQTGLAYLRDAWGILMDMRWRWMMLVFSASFVIHWLVFAVLWYILAEMNGDLGLDHDAPPENHTICVKYITSFTAAFSFSLETQLTIGYGTMFPSGDCPSAIALLAIQMLLGLMLEAFITGAFVAKIARPKNRAFSIRFTDLAVVAHIDGKPNLIFQVANTRPSPLTNVRVSAVLYQERENGKLYQTSVDFHLDGISSEECPFFIFPLTYYHSIIPSSPLATLLQHENPPHFELVVFLSAMQEGTGETCQRRTSYLPSEIMLHHCFASLLARGSKGEYQIKMENFDKTTPEFQTPLVSKSPNRTDLDIHINGQSIDNFQISETGLTE

[Multiple Choices]
A. neuron projection
B. H3 histone acetyltransferase complex
C. host cell mitochondrion
D. monoatomic ion channel complex
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates GO:0034702, monoatomic ion channel complex, with computational evidence (IEA); an archived record has the same annotation. This supports D, but is not experimental confirmation.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple hydrophobic membrane-spanning regions and a TIGYG-like pore signature. Knowledge of conserved potassium-channel features supports identifying it as a membrane ion channel, meaning D is a meaningful match among these choices; the other options describe neuronal projections, a histone-modifying complex, or mitochondria.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable channel-family inference from the sequence distinguishes D without needing the exact protein's database annotation. It supports the channel-complex choice, though it does not independently establish all cellular localizations.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices include only one ion-channel-complex term; the sequence features support it over the unrelated alternatives.


### Important caveats

- The supplied GO annotation is computational (IEA), not evidence of experimental validation.
- The prompt asks for a primary cellular component, while D names a protein complex rather than a location such as the plasma membrane.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions and a TIGYG-like pore signature. Knowledge of conserved potassium-channel features supports identifying it as a membrane ion channel, meaning D is a meaningful match among these choices; the other options describe neuronal projections, a histone-modifying complex, or mitochondria.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable channel-family inference from the sequence distinguishes D without needing the exact protein's database annotation. It supports the channel-complex choice, though it does not independently establish all cellular localizations."
  },
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates GO:0034702, monoatomic ion channel complex, with computational evidence (IEA); an archived record has the same annotation. This supports D, but is not experimental confirmation."
  },
  "important_caveats": [
    "The supplied GO annotation is computational (IEA), not evidence of experimental validation.",
    "The prompt asks for a primary cellular component, while D names a protein complex rather than a location such as the plasma membrane."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices include only one ion-channel-complex term; the sequence features support it over the unrelated alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates GO:0034702, monoatomic ion channel complex, with computational evidence (IEA); an archived record has the same annotation. This supports D, but is not experimental confirmation.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions and a TIGYG-like pore signature. Knowledge of conserved potassium-channel features supports identifying it as a membrane ion channel, meaning D is a meaningful match among these choices; the other options describe neuronal projections, a histone-modifying complex, or mitochondria.",
    "missing_item_specific_fact": "",
    "reason": "A transferable channel-family inference from the sequence distinguishes D without needing the exact protein's database annotation. It supports the channel-complex choice, though it does not independently establish all cellular localizations."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices include only one ion-channel-complex term; the sequence features support it over the unrelated alternatives."
  },
  "important_caveats": [
    "The supplied GO annotation is computational (IEA), not evidence of experimental validation.",
    "The prompt asks for a primary cellular component, while D names a protein complex rather than a location such as the plasma membrane."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (E1BN00, KCNJ13_BOVIN) identifies this protein as Inward rectifier potassium channel 13 (Kir7.1), a multi-pass membrane protein. GO:0034702 (monoatomic ion channel complex) is annotated with IEA evidence. The protein is a potassium channel that forms a water-filled ion-conducting pore, consistent with the GO definition. The annotation is computationally inferred (IEA:Ensembl / IEA:UniProtKB-KW) rather than experimentally determined, but the protein's identity as a K+ channel is well-established by homology to O60928 (human Kir7.1) and the presence of the canonical selectivity filter motif in the sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the well-known GYG selectivity filter motif (visible as 'IGYG' in the region 'TQLTIGYGTMFPSGDCPSAIALLAIQMLLGLMLEAFITGAFVAKI'), which is the hallmark signature of potassium channels across all eukaryotic K+ channel families. Combined with the multi-pass transmembrane topology (multiple hydrophobic stretches consistent with 2TM + pore loop + C-terminal cytoplasmic domain architecture of Kir channels), a knowledgeable model can infer this is a potassium ion channel. This directly maps to 'monoatomic ion channel complex' (D). It eliminates B (histone acetyltransferase complex: nuclear, no TM domains, no GYG), C (host cell mitochondrion: no mitochondrial targeting presequence, wrong architecture), and A (neuron projection: a subcellular location, not a functional complex; and the GYG/TM architecture identifies the protein as an ion channel regardless of which cell type expresses it). The GYG motif is one of the most universally recognized sequence signatures in ion channel biology, making this a legitimate family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GYG selectivity filter motif and multi-pass TM topology are transferable knowledge about potassium channel families. Recognizing these features allows identification of the protein as an ion channel complex without needing to recall this specific bovine Kir7.1 entry. The four options are well-separated: only D is consistent with a multi-pass membrane protein bearing a K+ selectivity filter.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GYG motif and TM architecture uniquely identify an ion channel. Option A (neuron projection) is a location not a complex, and while some Kir channels localize to neurons, the GO annotation for this protein does not include neuron projection. Options B and C are clearly incompatible with the sequence features. No ambiguity among the offered choices.


### Important caveats

- The GO:0034702 annotation is IEA (inferred from electronic annotation), not experimentally verified for this specific bovine entry. It is propagated from human Kir7.1 (O60928) and keyword-based assignment.
- The protein's primary GO cellular component annotation also includes plasma membrane (GO:0005886, ISS), but this was not offered as a choice.
- The sequence is from Bos taurus; the reviewer identified the accession from dataset metadata not available to the evaluated model. However, the GYG motif and Kir architecture are species-independent transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the well-known GYG selectivity filter motif (visible as 'IGYG' in the region 'TQLTIGYGTMFPSGDCPSAIALLAIQMLLGLMLEAFITGAFVAKI'), which is the hallmark signature of potassium channels across all eukaryotic K+ channel families. Combined with the multi-pass transmembrane topology (multiple hydrophobic stretches consistent with 2TM + pore loop + C-terminal cytoplasmic domain architecture of Kir channels), a knowledgeable model can infer this is a potassium ion channel. This directly maps to 'monoatomic ion channel complex' (D). It eliminates B (histone acetyltransferase complex: nuclear, no TM domains, no GYG), C (host cell mitochondrion: no mitochondrial targeting presequence, wrong architecture), and A (neuron projection: a subcellular location, not a functional complex; and the GYG/TM architecture identifies the protein as an ion channel regardless of which cell type expresses it). The GYG motif is one of the most universally recognized sequence signatures in ion channel biology, making this a legitimate family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GYG selectivity filter motif and multi-pass TM topology are transferable knowledge about potassium channel families. Recognizing these features allows identification of the protein as an ion channel complex without needing to recall this specific bovine Kir7.1 entry. The four options are well-separated: only D is consistent with a multi-pass membrane protein bearing a K+ selectivity filter."
  },
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (E1BN00, KCNJ13_BOVIN) identifies this protein as Inward rectifier potassium channel 13 (Kir7.1), a multi-pass membrane protein. GO:0034702 (monoatomic ion channel complex) is annotated with IEA evidence. The protein is a potassium channel that forms a water-filled ion-conducting pore, consistent with the GO definition. The annotation is computationally inferred (IEA:Ensembl / IEA:UniProtKB-KW) rather than experimentally determined, but the protein's identity as a K+ channel is well-established by homology to O60928 (human Kir7.1) and the presence of the canonical selectivity filter motif in the sequence."
  },
  "important_caveats": [
    "The GO:0034702 annotation is IEA (inferred from electronic annotation), not experimentally verified for this specific bovine entry. It is propagated from human Kir7.1 (O60928) and keyword-based assignment.",
    "The protein's primary GO cellular component annotation also includes plasma membrane (GO:0005886, ISS), but this was not offered as a choice.",
    "The sequence is from Bos taurus; the reviewer identified the accession from dataset metadata not available to the evaluated model. However, the GYG motif and Kir architecture are species-independent transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GYG motif and TM architecture uniquely identify an ion channel. Option A (neuron projection) is a location not a complex, and while some Kir channels localize to neurons, the GO annotation for this protein does not include neuron projection. Options B and C are clearly incompatible with the sequence features. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (E1BN00, KCNJ13_BOVIN) identifies this protein as Inward rectifier potassium channel 13 (Kir7.1), a multi-pass membrane protein. GO:0034702 (monoatomic ion channel complex) is annotated with IEA evidence. The protein is a potassium channel that forms a water-filled ion-conducting pore, consistent with the GO definition. The annotation is computationally inferred (IEA:Ensembl / IEA:UniProtKB-KW) rather than experimentally determined, but the protein's identity as a K+ channel is well-established by homology to O60928 (human Kir7.1) and the presence of the canonical selectivity filter motif in the sequence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the well-known GYG selectivity filter motif (visible as 'IGYG' in the region 'TQLTIGYGTMFPSGDCPSAIALLAIQMLLGLMLEAFITGAFVAKI'), which is the hallmark signature of potassium channels across all eukaryotic K+ channel families. Combined with the multi-pass transmembrane topology (multiple hydrophobic stretches consistent with 2TM + pore loop + C-terminal cytoplasmic domain architecture of Kir channels), a knowledgeable model can infer this is a potassium ion channel. This directly maps to 'monoatomic ion channel complex' (D). It eliminates B (histone acetyltransferase complex: nuclear, no TM domains, no GYG), C (host cell mitochondrion: no mitochondrial targeting presequence, wrong architecture), and A (neuron projection: a subcellular location, not a functional complex; and the GYG/TM architecture identifies the protein as an ion channel regardless of which cell type expresses it). The GYG motif is one of the most universally recognized sequence signatures in ion channel biology, making this a legitimate family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "The GYG selectivity filter motif and multi-pass TM topology are transferable knowledge about potassium channel families. Recognizing these features allows identification of the protein as an ion channel complex without needing to recall this specific bovine Kir7.1 entry. The four options are well-separated: only D is consistent with a multi-pass membrane protein bearing a K+ selectivity filter."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GYG motif and TM architecture uniquely identify an ion channel. Option A (neuron projection) is a location not a complex, and while some Kir channels localize to neurons, the GO annotation for this protein does not include neuron projection. Options B and C are clearly incompatible with the sequence features. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The GO:0034702 annotation is IEA (inferred from electronic annotation), not experimentally verified for this specific bovine entry. It is propagated from human Kir7.1 (O60928) and keyword-based assignment.",
    "The protein's primary GO cellular component annotation also includes plasma membrane (GO:0005886, ISS), but this was not offered as a choice.",
    "The sequence is from Bos taurus; the reviewer identified the accession from dataset metadata not available to the evaluated model. However, the GYG motif and Kir architecture are species-independent transferable knowledge."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "feb9d6140c91f297df4e1b3bf9a9bd39d203ad60b8fd9106c95f00ca1a7abda5",
  "current_entry_audit": {
    "entryVersion": 87,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "feb9d6140c91f297df4e1b3bf9a9bd39d203ad60b8fd9106c95f00ca1a7abda5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 85,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E1BN00",
  "selected_historical_entry_version": 85,
  "selected_historical_record_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "feb9d6140c91f297df4e1b3bf9a9bd39d203ad60b8fd9106c95f00ca1a7abda5",
  "selected_historical_version": {
    "accession": "E1BN00",
    "database": "Swiss-Prot",
    "entryVersion": 85,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KCJ13_BOVIN",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E1BN00\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":87,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bovine\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Laurasiatheria\",\"Artiodactyla\",\"Ruminantia\",\"Pecora\",\"Bovidae\",\"Bovinae\",\"Bos\"],\"scientificName\":\"Bos taurus\",\"taxonId\":9913}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60928\",\"source\":\"UniProtKB\"}],\"value\":\"Inward rectifier K(+) channel Kir7.1\"}},{\"fullName\":{\"value\":\"Potassium channel, inwardly rectifying subfamily J member 13\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60928\",\"source\":\"UniProtKB\"}],\"value\":\"Inward rectifier potassium channel 13\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P86046\",\"source\":\"UniProtKB\"}],\"value\":\"Localized at the retinal pigmented epithelium (RPE) apical microvilli\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-0162\",\"value\":\"Membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P86046\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0034702\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:monoatomic ion channel complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:Ensembl\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H1",
  "excerpt": "ID   KCJ13_BOVIN             Reviewed;         360 AA.\nAC   E1BN00;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 85.\nDE   RecName: Full=Inward rectifier potassium channel 13 {ECO:0000250|UniProtKB:O60928};\nDE   AltName: Full=Inward rectifier K(+) channel Kir7.1 {ECO:0000250|UniProtKB:O60928};\nDE   AltName: Full=Potassium channel, inwardly rectifying subfamily J member 13;\nGN   Name=KCNJ13;\nOS   Bos taurus (Bovine).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Laurasiatheria; Artiodactyla; Ruminantia; Pecora; Bovidae;\nOC   Bovinae; Bos.\nOX   NCBI_TaxID=9913;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane\nCC       protein {ECO:0000255}. Cell membrane {ECO:0000250|UniProtKB:P86046}.\nCC       Note=Localized at the retinal pigmented epithelium (RPE) apical\nCC       microvilli. {ECO:0000250|UniProtKB:P86046}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0034702; C:monoatomic ion channel complex; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; ISS:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0033650\nname: host cell mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle as found in host cells that occurs in varying numbers, shapes, and sizes in the cell cytoplasm. The host is defined as the larger of the organisms involved in a symbiotic interaction.\" [GOC:pamgo_curators]\nsynonym: \"host mitochondria\" EXACT []\nis_a: GO:0033648 ! host intracellular membrane-bounded organelle\nis_a: GO:0033655 ! host cell cytoplasm part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0033650",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 199319-199327",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0034702\nname: monoatomic ion channel complex\nnamespace: cellular_component\ndef: \"A protein complex that spans a membrane and forms a water-filled channel across the phospholipid bilayer allowing selective monoatomic ion transport down its electrochemical gradient.\" [GOC:mah, ISBN:071673706X]\nis_a: GO:1902495 ! transmembrane transporter complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034702",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 211424-211430",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0043005\nname: neuron projection\nnamespace: cellular_component\ndef: \"A prolongation or process extending from a nerve cell, e.g. an axon or dendrite.\" [GOC:jl, PMID:3077060]\nsubset: goslim_pir\nsynonym: \"nerve fiber\" RELATED [GOC:dph]\nsynonym: \"neurite\" NARROW []\nsynonym: \"neuron process\" EXACT []\nsynonym: \"neuron protrusion\" EXACT [NIF_Subcellular:sao250931889]\nsynonym: \"neuronal cell projection\" EXACT []\nxref: NIF_Subcellular:sao867568886\nis_a: GO:0120025 ! plasma membrane bounded cell projection\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043005",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 243106-243119",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0070775\nname: H3 histone acetyltransferase complex\nnamespace: cellular_component\ndef: \"A multisubunit complex that catalyzes the acetylation of histone H3.\" [GOC:mah]\nsynonym: \"H3 HAT complex\" EXACT [GOC:mah]\nis_a: GO:0000123 ! histone acetyltransferase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070775",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 370959-370966",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
