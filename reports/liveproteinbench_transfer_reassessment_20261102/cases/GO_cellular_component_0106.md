# GO_cellular_component_0106

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0106.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — host cell cytoplasm

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDLETRVSGHEKPQRRNPEDPDCQYAKTRSSPCKPLGRFEEVASRTSAGSWTHQNGFGDTSLFEIYSNQAITGPYQQMGFRGEKRGYGNNKEVQERSCCHVENNQC

[Multiple Choices]
A. peroxisomal membrane
B. host cell cytoplasm
C. IRE1-TRAF2-ASK1 complex
D. nematocyst
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

> The sequence-matched UniProt record reports host cytoplasm with experimental evidence, and its GO annotation is host cell cytoplasm. This supports choice B; the record also mentions host cytoskeleton.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short sequence has no evident hydrophobic transmembrane segment or signal peptide, making a peroxisomal membrane location less plausible. A specific ER-associated IRE1-TRAF2-ASK1 complex or a specialized nematocyst would require contextual or interaction evidence not apparent here. Among these choices, a soluble intracellular protein is most plausibly in the host cytoplasm.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence does not establish host-specific localization, so this is a probabilistic inference rather than a direct sequence readout. But the soluble-protein pattern and the relative specificity of the alternatives meaningfully favor B without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence features and general localization patterns.


### Important caveats

- The reviewer-only annotation supports the key but was not part of the original input.
- The protein is also annotated to the host cytoskeleton; the choices do not include that location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence has no evident hydrophobic transmembrane segment or signal peptide, making a peroxisomal membrane location less plausible. A specific ER-associated IRE1-TRAF2-ASK1 complex or a specialized nematocyst would require contextual or interaction evidence not apparent here. Among these choices, a soluble intracellular protein is most plausibly in the host cytoplasm.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence does not establish host-specific localization, so this is a probabilistic inference rather than a direct sequence readout. But the soluble-protein pattern and the relative specificity of the alternatives meaningfully favor B without needing the exact protein's recorded annotation."
  },
  "case_id": "GO_cellular_component_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports host cytoplasm with experimental evidence, and its GO annotation is host cell cytoplasm. This supports choice B; the record also mentions host cytoskeleton."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original input.",
    "The protein is also annotated to the host cytoskeleton; the choices do not include that location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and general localization patterns."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports host cytoplasm with experimental evidence, and its GO annotation is host cell cytoplasm. This supports choice B; the record also mentions host cytoskeleton.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence has no evident hydrophobic transmembrane segment or signal peptide, making a peroxisomal membrane location less plausible. A specific ER-associated IRE1-TRAF2-ASK1 complex or a specialized nematocyst would require contextual or interaction evidence not apparent here. Among these choices, a soluble intracellular protein is most plausibly in the host cytoplasm.",
    "missing_item_specific_fact": "",
    "reason": "The sequence does not establish host-specific localization, so this is a probabilistic inference rather than a direct sequence readout. But the soluble-protein pattern and the relative specificity of the alternatives meaningfully favor B without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and general localization patterns."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original input.",
    "The protein is also annotated to the host cytoskeleton; the choices do not include that location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXN9 (uORF protein from Zika virus) is annotated with GO:0030430 (host cell cytoplasm) based on experimental evidence (ECO:0000269, PubMed:39394194, a 2024 Nature Communications paper). The subcellular location comment explicitly states 'Host cytoplasm' and 'Host cytoplasm, host cytoskeleton' with experimental evidence codes. The sequence match is confirmed (106 AA, SHA256 matches). The answer B (host cell cytoplasm) is directly supported by experimental annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use elimination based on absence of required targeting features plus the meaning of the GO terms. (1) Nematocyst (D) is an organelle exclusive to cnidarians (jellyfish, corals); a 106 AA protein with no cnidarian-specific features cannot reside there. (2) IRE1-TRAF2-ASK1 complex (C) is an ER membrane protein complex; the sequence lacks any N-terminal signal peptide or transmembrane helix required for ER membrane association. (3) Peroxisomal membrane (A) requires either a C-terminal PTS1 (S-K-L/S-R-L) or an N-terminal PTS2, or transmembrane domains for membrane proteins; the C-terminus 'VENNQC' has no PTS1, and no PTS2 or TM helices are present. (4) The term 'host cell cytoplasm' specifically denotes a pathogen/parasite protein in the host cytoplasm. A small (106 AA) protein with no detectable targeting signals, no signal peptide, and no membrane-spanning regions is consistent with a cytoplasmic viral protein. The combination of small size, absence of all targeting motifs, and the 'host cell' qualifier in option B provides a credible inference pathway without needing to know the exact protein identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of options A, C, and D relies on well-established, transferable knowledge: nematocyst is cnidarian-specific, IRE1-TRAF2-ASK1 is an ER membrane complex requiring signal peptides/TM domains, and peroxisomal targeting requires PTS1/PTS2 or TM domains. The remaining option B ('host cell cytoplasm') is the default location for a small pathogen-encoded protein lacking targeting signals. This reasoning uses general protein-targeting biology and the definitions of the GO terms themselves, not a memorized annotation for this specific sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D each require specific structural or contextual features (PTS signals/TM domains, ER signal peptide/TM domain, cnidarian organelle context) that are clearly absent from the sequence. Only option B is consistent with a small protein lacking all targeting signals. No ambiguity among the offered choices.


### Important caveats

- The protein is the Zika virus uORF protein (P0DXN9), a 106 AA protein first annotated in 2025. The model does not need to identify it as ZIKV specifically; the reasoning works from absence of targeting features and the meaning of GO term names.
- The UniProt annotation also includes 'host cytoskeleton' (GO:0044163), but this is not offered as an alternative, so it does not create ambiguity among the four choices.
- The experimental evidence (PubMed:39394194) is from a 2024 paper; the entry was only integrated into Swiss-Prot in February 2025. The benchmark sequence and annotation are consistent.
- The 'host cell cytoplasm' GO term inherently implies a pathogen/parasite context, which the model can infer from the term definition itself without knowing the organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use elimination based on absence of required targeting features plus the meaning of the GO terms. (1) Nematocyst (D) is an organelle exclusive to cnidarians (jellyfish, corals); a 106 AA protein with no cnidarian-specific features cannot reside there. (2) IRE1-TRAF2-ASK1 complex (C) is an ER membrane protein complex; the sequence lacks any N-terminal signal peptide or transmembrane helix required for ER membrane association. (3) Peroxisomal membrane (A) requires either a C-terminal PTS1 (S-K-L/S-R-L) or an N-terminal PTS2, or transmembrane domains for membrane proteins; the C-terminus 'VENNQC' has no PTS1, and no PTS2 or TM helices are present. (4) The term 'host cell cytoplasm' specifically denotes a pathogen/parasite protein in the host cytoplasm. A small (106 AA) protein with no detectable targeting signals, no signal peptide, and no membrane-spanning regions is consistent with a cytoplasmic viral protein. The combination of small size, absence of all targeting motifs, and the 'host cell' qualifier in option B provides a credible inference pathway without needing to know the exact protein identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of options A, C, and D relies on well-established, transferable knowledge: nematocyst is cnidarian-specific, IRE1-TRAF2-ASK1 is an ER membrane complex requiring signal peptides/TM domains, and peroxisomal targeting requires PTS1/PTS2 or TM domains. The remaining option B ('host cell cytoplasm') is the default location for a small pathogen-encoded protein lacking targeting signals. This reasoning uses general protein-targeting biology and the definitions of the GO terms themselves, not a memorized annotation for this specific sequence."
  },
  "case_id": "GO_cellular_component_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXN9 (uORF protein from Zika virus) is annotated with GO:0030430 (host cell cytoplasm) based on experimental evidence (ECO:0000269, PubMed:39394194, a 2024 Nature Communications paper). The subcellular location comment explicitly states 'Host cytoplasm' and 'Host cytoplasm, host cytoskeleton' with experimental evidence codes. The sequence match is confirmed (106 AA, SHA256 matches). The answer B (host cell cytoplasm) is directly supported by experimental annotation."
  },
  "important_caveats": [
    "The protein is the Zika virus uORF protein (P0DXN9), a 106 AA protein first annotated in 2025. The model does not need to identify it as ZIKV specifically; the reasoning works from absence of targeting features and the meaning of GO term names.",
    "The UniProt annotation also includes 'host cytoskeleton' (GO:0044163), but this is not offered as an alternative, so it does not create ambiguity among the four choices.",
    "The experimental evidence (PubMed:39394194) is from a 2024 paper; the entry was only integrated into Swiss-Prot in February 2025. The benchmark sequence and annotation are consistent.",
    "The 'host cell cytoplasm' GO term inherently implies a pathogen/parasite context, which the model can infer from the term definition itself without knowing the organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D each require specific structural or contextual features (PTS signals/TM domains, ER signal peptide/TM domain, cnidarian organelle context) that are clearly absent from the sequence. Only option B is consistent with a small protein lacking all targeting signals. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXN9 (uORF protein from Zika virus) is annotated with GO:0030430 (host cell cytoplasm) based on experimental evidence (ECO:0000269, PubMed:39394194, a 2024 Nature Communications paper). The subcellular location comment explicitly states 'Host cytoplasm' and 'Host cytoplasm, host cytoskeleton' with experimental evidence codes. The sequence match is confirmed (106 AA, SHA256 matches). The answer B (host cell cytoplasm) is directly supported by experimental annotation.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use elimination based on absence of required targeting features plus the meaning of the GO terms. (1) Nematocyst (D) is an organelle exclusive to cnidarians (jellyfish, corals); a 106 AA protein with no cnidarian-specific features cannot reside there. (2) IRE1-TRAF2-ASK1 complex (C) is an ER membrane protein complex; the sequence lacks any N-terminal signal peptide or transmembrane helix required for ER membrane association. (3) Peroxisomal membrane (A) requires either a C-terminal PTS1 (S-K-L/S-R-L) or an N-terminal PTS2, or transmembrane domains for membrane proteins; the C-terminus 'VENNQC' has no PTS1, and no PTS2 or TM helices are present. (4) The term 'host cell cytoplasm' specifically denotes a pathogen/parasite protein in the host cytoplasm. A small (106 AA) protein with no detectable targeting signals, no signal peptide, and no membrane-spanning regions is consistent with a cytoplasmic viral protein. The combination of small size, absence of all targeting motifs, and the 'host cell' qualifier in option B provides a credible inference pathway without needing to know the exact protein identity.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of options A, C, and D relies on well-established, transferable knowledge: nematocyst is cnidarian-specific, IRE1-TRAF2-ASK1 is an ER membrane complex requiring signal peptides/TM domains, and peroxisomal targeting requires PTS1/PTS2 or TM domains. The remaining option B ('host cell cytoplasm') is the default location for a small pathogen-encoded protein lacking targeting signals. This reasoning uses general protein-targeting biology and the definitions of the GO terms themselves, not a memorized annotation for this specific sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D each require specific structural or contextual features (PTS signals/TM domains, ER signal peptide/TM domain, cnidarian organelle context) that are clearly absent from the sequence. Only option B is consistent with a small protein lacking all targeting signals. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The protein is the Zika virus uORF protein (P0DXN9), a 106 AA protein first annotated in 2025. The model does not need to identify it as ZIKV specifically; the reasoning works from absence of targeting features and the meaning of GO term names.",
    "The UniProt annotation also includes 'host cytoskeleton' (GO:0044163), but this is not offered as an alternative, so it does not create ambiguity among the four choices.",
    "The experimental evidence (PubMed:39394194) is from a 2024 paper; the entry was only integrated into Swiss-Prot in February 2025. The benchmark sequence and annotation are consistent.",
    "The 'host cell cytoplasm' GO term inherently implies a pathogen/parasite context, which the model can infer from the term definition itself without knowing the organism."
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
  "benchmark_sequence_length": 106,
  "benchmark_sequence_sha256": "bb1330e3da6cb7b23bd6441a52b14512607cdface881df5fceb29428642b68f5",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 106,
  "current_source_sequence_sha256": "bb1330e3da6cb7b23bd6441a52b14512607cdface881df5fceb29428642b68f5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXN9",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "90a67f397b92566241bb9702f74606e2f512999e3e9d14874cb790b018ebbf88",
  "selected_historical_source_sequence_length": 106,
  "selected_historical_source_sequence_sha256": "bb1330e3da6cb7b23bd6441a52b14512607cdface881df5fceb29428642b68f5",
  "selected_historical_version": {
    "accession": "P0DXN9",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "UORF_ZIKV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXN9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"ZIKV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Kitrinoviricota\",\"Flasuviricetes\",\"Amarillovirales\",\"Flaviviridae\",\"Orthoflavivirus\",\"Orthoflavivirus zikaense\"],\"scientificName\":\"Zika virus\",\"taxonId\":64320}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"uORF protein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39394194\",\"source\":\"PubMed\"}],\"id\":\"SL-0381\",\"value\":\"Host cytoplasm\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39394194\",\"source\":\"PubMed\"}],\"id\":\"SL-0383\",\"value\":\"Host cytoplasm, host cytoskeleton\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39394194\",\"source\":\"PubMed\"}],\"id\":\"GO:0030430\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:host cell cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0044163\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:host cytoskeleton\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Lefevre C.\",\"Cook G.M.\",\"Dinan A.M.\",\"Torii S.\",\"Stewart H.\",\"Gibbons G.\",\"Nicholson A.S.\",\"Echavarria-Consuegra L.\",\"Meredith L.W.\",\"Lulla V.\",\"McGovern N.\",\"Kenyon J.C.\",\"Goodfellow I.\",\"Deane J.E.\",\"Graham S.C.\",\"Lakatos A.\",\"Lambrechts L.\",\"Brierley I.\",\"Irigoyen N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39394194\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-53085-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"8822\",\"id\":\"39394194\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"8822\",\"publicationDate\":\"2024\",\"title\":\"Zika viruses encode 5' upstream open reading frames affecting infection of human brain cells.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Isolate Dak84\"}],\"referenceNumber\":3,\"referencePositions\":[\"ALTERNATIVE INITIATION (ISOFORM UORF)\",\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:35.516881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03987561a35d3bea68d2033cf08aaec1ae9f6b461d9fdcf13af7db8c7358f810",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   UORF_ZIKV               Reviewed;         106 AA.\nAC   P0DXN9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=uORF protein;\nOS   Zika virus (ZIKV).\nOC   Viruses; Riboviria; Orthornavirae; Kitrinoviricota; Flasuviricetes;\nOC   Amarillovirales; Flaviviridae; Orthoflavivirus; Orthoflavivirus zikaense.\nOX   NCBI_TaxID=64320;\nOH   NCBI_TaxID=7159; Aedes aegypti (Yellowfever mosquito) (Culex aegypti).\nOH   NCBI_TaxID=7160; Aedes albopictus (Asian tiger mosquito) (Stegomyia albopicta).\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\nOH   NCBI_TaxID=9544; Macaca mulatta (Rhesus macaque).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.226210+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90a67f397b92566241bb9702f74606e2f512999e3e9d14874cb790b018ebbf88",
  "url": "https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   ALTERNATIVE INITIATION (ISOFORM UORF), FUNCTION, AND SUBCELLULAR LOCATION.\nRC   STRAIN=Isolate Dak84;\nRX   PubMed=39394194; DOI=10.1038/s41467-024-53085-9;\nRA   Lefevre C., Cook G.M., Dinan A.M., Torii S., Stewart H., Gibbons G.,\nRA   Nicholson A.S., Echavarria-Consuegra L., Meredith L.W., Lulla V.,\nRA   McGovern N., Kenyon J.C., Goodfellow I., Deane J.E., Graham S.C.,\nRA   Lakatos A., Lambrechts L., Brierley I., Irigoyen N.;\nRT   \"Zika viruses encode 5' upstream open reading frames affecting infection of\nRT   human brain cells.\";\nRL   Nat. Commun. 15:8822-8822(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.226210+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90a67f397b92566241bb9702f74606e2f512999e3e9d14874cb790b018ebbf88",
  "url": "https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Host cytoplasm {ECO:0000269|PubMed:39394194}.\nCC       Host cytoplasm, host cytoskeleton {ECO:0000269|PubMed:39394194}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.226210+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90a67f397b92566241bb9702f74606e2f512999e3e9d14874cb790b018ebbf88",
  "url": "https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0030430; C:host cell cytoplasm; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.226210+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90a67f397b92566241bb9702f74606e2f512999e3e9d14874cb790b018ebbf88",
  "url": "https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0044163; C:host cytoskeleton; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.226210+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90a67f397b92566241bb9702f74606e2f512999e3e9d14874cb790b018ebbf88",
  "url": "https://rest.uniprot.org/unisave/P0DXN9?format=txt&versions=3"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005778\nname: peroxisomal membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding a peroxisome.\" [GOC:mah]\nsynonym: \"peroxisome membrane\" EXACT []\nis_a: GO:0031903 ! microbody membrane\nrelationship: part_of GO:0005777 ! peroxisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005778",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59400-59408",
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
  "excerpt": "[Term]\nid: GO:0030430\nname: host cell cytoplasm\nnamespace: cellular_component\nalt_id: GO:0097679\ndef: \"The cytoplasm of a host cell.\" [GOC:mah]\nsynonym: \"other organism cytoplasm\" RELATED []\nis_a: GO:0033646 ! host intracellular part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030430",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 166128-166136",
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
  "excerpt": "[Term]\nid: GO:0042151\nname: nematocyst\nnamespace: cellular_component\ndef: \"An organelle found in cnidoblast (nematoblast) cells. When matured, these stinging organelles store toxins and can deliver them when the cnidocil (a short extension of the cnidocyst) is stimulated by a prey or another stimulus.\" [DOI:10.1139/z02-135, GOC:jl]\nsynonym: \"cnidocyst\" EXACT []\nxref: Wikipedia:Cnidocyte\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0005938 ! cell cortex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042151",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 234754-234763",
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
  "excerpt": "[Term]\nid: GO:1990604\nname: IRE1-TRAF2-ASK1 complex\nnamespace: cellular_component\ndef: \"A protein complex of the endoplasmic reticulum membrane that consists of IRE1 (Inositol-requiring enzyme-1), TRAF2 (TNF receptor-associated factor 2) and ASK1 (Apoptosis signal-regulating kinase 1, a MAP3K).\" [GOC:bf, GOC:PARL, PMID:12050113, PMID:23000344]\nsynonym: \"ERN1-TRAF2-ASK1 complex\" RELATED [HGNC:3449]\nis_a: GO:0098796 ! membrane protein complex\nis_a: GO:0140534 ! endoplasmic reticulum protein-containing complex\nrelationship: part_of GO:0005789 ! endoplasmic reticulum membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990604",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 553487-553496",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
