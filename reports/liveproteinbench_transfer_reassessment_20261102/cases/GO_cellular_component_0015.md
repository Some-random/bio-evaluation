# GO_cellular_component_0015

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0015.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — host cell cytoplasm

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDQFIKQDETGDLIETGMNVANHFLSAPIQGTNSLSKATIIPGVAPVLIGNPEQKNIQYPTASHQGSKSKGRGSGAKPIIVSSSEGGTGGTQIPEPLFAQTGQGGVVTTVYQDPTIQPTGSYRSVELAKIGKERMINRFVEKPRTSTPVTEFKRGAGNGSPRPDNPRGGHRREWSLSWVQGEVRVFEWCNPICSPITAAARFHSCKCGNCPAKCDQCERDYGPP

[Multiple Choices]
A. matrilin complex
B. glutamatergic synapse
C. host cell cytoplasm
D. endoplasmic reticulum membrane
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

> The sequence-matched UniProt record annotates this protein to the host cytoplasm, and its GO annotation assigns host cell cytoplasm. The host-cytoplasm annotation is curatorial/inferred rather than directly supported by the cited experimental evidence, which concerns virion association; nevertheless, it supports choice C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has no evident transmembrane segment or secretion signal, arguing against ER membrane and an extracellular-matrix matrilin complex. Its C-terminal cysteine-rich region is compatible with a viral accessory-protein family pattern; such intracellular viral proteins plausibly act in host cytoplasm. The glutamatergic-synapse option also lacks supporting sequence/context features. These transferable clues favor C among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Even without knowing the exact protein annotation, sequence features and transferable knowledge of intracellular viral proteins distinguish host cytoplasm from these alternatives. This is a probabilistic localization inference, not proof of the protein's exact localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice has comparable support. The protein is also annotated as a virion component, but virion is not an option and does not make another listed choice defensible.


### Important caveats

- The evidence supports host-cytoplasm annotation but does not establish that this is the protein's exclusive or experimentally demonstrated primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has no evident transmembrane segment or secretion signal, arguing against ER membrane and an extracellular-matrix matrilin complex. Its C-terminal cysteine-rich region is compatible with a viral accessory-protein family pattern; such intracellular viral proteins plausibly act in host cytoplasm. The glutamatergic-synapse option also lacks supporting sequence/context features. These transferable clues favor C among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Even without knowing the exact protein annotation, sequence features and transferable knowledge of intracellular viral proteins distinguish host cytoplasm from these alternatives. This is a probabilistic localization inference, not proof of the protein's exact localization."
  },
  "case_id": "GO_cellular_component_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the host cytoplasm, and its GO annotation assigns host cell cytoplasm. The host-cytoplasm annotation is curatorial/inferred rather than directly supported by the cited experimental evidence, which concerns virion association; nevertheless, it supports choice C."
  },
  "important_caveats": [
    "The evidence supports host-cytoplasm annotation but does not establish that this is the protein's exclusive or experimentally demonstrated primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support. The protein is also annotated as a virion component, but virion is not an option and does not make another listed choice defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the host cytoplasm, and its GO annotation assigns host cell cytoplasm. The host-cytoplasm annotation is curatorial/inferred rather than directly supported by the cited experimental evidence, which concerns virion association; nevertheless, it supports choice C.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has no evident transmembrane segment or secretion signal, arguing against ER membrane and an extracellular-matrix matrilin complex. Its C-terminal cysteine-rich region is compatible with a viral accessory-protein family pattern; such intracellular viral proteins plausibly act in host cytoplasm. The glutamatergic-synapse option also lacks supporting sequence/context features. These transferable clues favor C among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "Even without knowing the exact protein annotation, sequence features and transferable knowledge of intracellular viral proteins distinguish host cytoplasm from these alternatives. This is a probabilistic localization inference, not proof of the protein's exact localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support. The protein is also annotated as a virion component, but virion is not an option and does not make another listed choice defensible."
  },
  "important_caveats": [
    "The evidence supports host-cytoplasm annotation but does not establish that this is the protein's exclusive or experimentally demonstrated primary location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (Mumps virus Non-structural protein V, Q5SC47) explicitly annotates 'Host cytoplasm' with GO:0030430 (host cell cytoplasm). The evidence code for this subcellular location is ECO:0000305 (inferred by curator), while experimental mass spectrometry evidence (ECO:0000269) supports 'Virion' localization. The curator inference to host cytoplasm is biologically consistent for a non-structural viral protein that functions during infection. The GO annotation (IEA:UniProtKB-SubCell) directly matches option C. The annotation is not contradicted by any evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable sequence and biological features distinguish C from the alternatives: (1) The N-terminus lacks a signal peptide (no hydrophobic leader sequence), ruling out secreted/extracellular localization (option A, matrilin complex, which requires a signal peptide and specific EGF-like/collagen-binding domains). (2) No hydrophobic transmembrane segments are present in the 224-residue sequence, making ER membrane insertion (option D) implausible. (3) The protein lacks features of synaptic proteins (no PDZ domains, no vesicle-associated motifs, no neurotransmitter receptor architecture), ruling out option B. (4) The C-terminal cysteine-rich motif (CNPICSPITAAARFHSCKCGNCPAKCDQCERDYGPP) resembles zinc-binding domains common in viral proteins (e.g., paramyxovirus V proteins), and the small size (224 AA) with absence of eukaryotic domain architecture suggests a viral non-structural protein. (5) General virology knowledge: non-structural viral proteins function in the host cytoplasm during infection, and the GO term 'host cell cytoplasm' specifically denotes viral proteins within a host cell. These features collectively and credibly point to C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence lacks signal peptides, transmembrane domains, and eukaryotic domain architectures that would support options A, B, or D. The cysteine-rich C-terminal motif and small size are consistent with viral zinc-binding proteins. General knowledge that viral non-structural proteins reside in host cytoplasm, combined with the specific meaning of the GO term 'host cell cytoplasm' (implying viral context), provides a concrete transferable inference distinguishing C from the other options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated in biological context. Matrilin complex (extracellular matrix), glutamatergic synapse (neuronal), and ER membrane (transmembrane protein) each require specific structural features entirely absent from this sequence. Only 'host cell cytoplasm' is consistent with a small, non-secreted, non-membrane protein with viral-like features.


### Important caveats

- The 'host cytoplasm' annotation carries curator-inferred evidence (ECO:0000305), not direct experimental localization evidence. Experimental mass spectrometry evidence supports 'Virion' location, which is not among the choices.
- Recognizing the specific paramyxovirus V protein identity would strengthen the argument but is not strictly necessary; the absence of eukaryotic targeting signals and presence of viral-like zinc-binding motifs suffice for a probabilistic inference.
- The GO term 'host cell cytoplasm' specifically implies a viral/pathogen context; if the model cannot recognize viral features, it might hesitate between a generic 'cytoplasm' and 'host cell cytoplasm,' but no generic cytoplasm option is offered.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable sequence and biological features distinguish C from the alternatives: (1) The N-terminus lacks a signal peptide (no hydrophobic leader sequence), ruling out secreted/extracellular localization (option A, matrilin complex, which requires a signal peptide and specific EGF-like/collagen-binding domains). (2) No hydrophobic transmembrane segments are present in the 224-residue sequence, making ER membrane insertion (option D) implausible. (3) The protein lacks features of synaptic proteins (no PDZ domains, no vesicle-associated motifs, no neurotransmitter receptor architecture), ruling out option B. (4) The C-terminal cysteine-rich motif (CNPICSPITAAARFHSCKCGNCPAKCDQCERDYGPP) resembles zinc-binding domains common in viral proteins (e.g., paramyxovirus V proteins), and the small size (224 AA) with absence of eukaryotic domain architecture suggests a viral non-structural protein. (5) General virology knowledge: non-structural viral proteins function in the host cytoplasm during infection, and the GO term 'host cell cytoplasm' specifically denotes viral proteins within a host cell. These features collectively and credibly point to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence lacks signal peptides, transmembrane domains, and eukaryotic domain architectures that would support options A, B, or D. The cysteine-rich C-terminal motif and small size are consistent with viral zinc-binding proteins. General knowledge that viral non-structural proteins reside in host cytoplasm, combined with the specific meaning of the GO term 'host cell cytoplasm' (implying viral context), provides a concrete transferable inference distinguishing C from the other options."
  },
  "case_id": "GO_cellular_component_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Mumps virus Non-structural protein V, Q5SC47) explicitly annotates 'Host cytoplasm' with GO:0030430 (host cell cytoplasm). The evidence code for this subcellular location is ECO:0000305 (inferred by curator), while experimental mass spectrometry evidence (ECO:0000269) supports 'Virion' localization. The curator inference to host cytoplasm is biologically consistent for a non-structural viral protein that functions during infection. The GO annotation (IEA:UniProtKB-SubCell) directly matches option C. The annotation is not contradicted by any evidence."
  },
  "important_caveats": [
    "The 'host cytoplasm' annotation carries curator-inferred evidence (ECO:0000305), not direct experimental localization evidence. Experimental mass spectrometry evidence supports 'Virion' location, which is not among the choices.",
    "Recognizing the specific paramyxovirus V protein identity would strengthen the argument but is not strictly necessary; the absence of eukaryotic targeting signals and presence of viral-like zinc-binding motifs suffice for a probabilistic inference.",
    "The GO term 'host cell cytoplasm' specifically implies a viral/pathogen context; if the model cannot recognize viral features, it might hesitate between a generic 'cytoplasm' and 'host cell cytoplasm,' but no generic cytoplasm option is offered."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated in biological context. Matrilin complex (extracellular matrix), glutamatergic synapse (neuronal), and ER membrane (transmembrane protein) each require specific structural features entirely absent from this sequence. Only 'host cell cytoplasm' is consistent with a small, non-secreted, non-membrane protein with viral-like features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Mumps virus Non-structural protein V, Q5SC47) explicitly annotates 'Host cytoplasm' with GO:0030430 (host cell cytoplasm). The evidence code for this subcellular location is ECO:0000305 (inferred by curator), while experimental mass spectrometry evidence (ECO:0000269) supports 'Virion' localization. The curator inference to host cytoplasm is biologically consistent for a non-structural viral protein that functions during infection. The GO annotation (IEA:UniProtKB-SubCell) directly matches option C. The annotation is not contradicted by any evidence.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable sequence and biological features distinguish C from the alternatives: (1) The N-terminus lacks a signal peptide (no hydrophobic leader sequence), ruling out secreted/extracellular localization (option A, matrilin complex, which requires a signal peptide and specific EGF-like/collagen-binding domains). (2) No hydrophobic transmembrane segments are present in the 224-residue sequence, making ER membrane insertion (option D) implausible. (3) The protein lacks features of synaptic proteins (no PDZ domains, no vesicle-associated motifs, no neurotransmitter receptor architecture), ruling out option B. (4) The C-terminal cysteine-rich motif (CNPICSPITAAARFHSCKCGNCPAKCDQCERDYGPP) resembles zinc-binding domains common in viral proteins (e.g., paramyxovirus V proteins), and the small size (224 AA) with absence of eukaryotic domain architecture suggests a viral non-structural protein. (5) General virology knowledge: non-structural viral proteins function in the host cytoplasm during infection, and the GO term 'host cell cytoplasm' specifically denotes viral proteins within a host cell. These features collectively and credibly point to C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence lacks signal peptides, transmembrane domains, and eukaryotic domain architectures that would support options A, B, or D. The cysteine-rich C-terminal motif and small size are consistent with viral zinc-binding proteins. General knowledge that viral non-structural proteins reside in host cytoplasm, combined with the specific meaning of the GO term 'host cell cytoplasm' (implying viral context), provides a concrete transferable inference distinguishing C from the other options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated in biological context. Matrilin complex (extracellular matrix), glutamatergic synapse (neuronal), and ER membrane (transmembrane protein) each require specific structural features entirely absent from this sequence. Only 'host cell cytoplasm' is consistent with a small, non-secreted, non-membrane protein with viral-like features."
  },
  "important_caveats": [
    "The 'host cytoplasm' annotation carries curator-inferred evidence (ECO:0000305), not direct experimental localization evidence. Experimental mass spectrometry evidence supports 'Virion' location, which is not among the choices.",
    "Recognizing the specific paramyxovirus V protein identity would strengthen the argument but is not strictly necessary; the absence of eukaryotic targeting signals and presence of viral-like zinc-binding motifs suffice for a probabilistic inference.",
    "The GO term 'host cell cytoplasm' specifically implies a viral/pathogen context; if the model cannot recognize viral features, it might hesitate between a generic 'cytoplasm' and 'host cell cytoplasm,' but no generic cytoplasm option is offered."
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
  "benchmark_sequence_length": 224,
  "benchmark_sequence_sha256": "aff41f3cad17bade9393d7af0a012fd40440ec7d65de5a925100ff82a30e1fed",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 224,
  "current_source_sequence_sha256": "aff41f3cad17bade9393d7af0a012fd40440ec7d65de5a925100ff82a30e1fed",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5SC47",
  "selected_historical_entry_version": 45,
  "selected_historical_record_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "selected_historical_source_sequence_length": 224,
  "selected_historical_source_sequence_sha256": "aff41f3cad17bade9393d7af0a012fd40440ec7d65de5a925100ff82a30e1fed",
  "selected_historical_version": {
    "accession": "Q5SC47",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "V_MUMPZ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5SC47\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Non-structural protein NS1\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Non-structural protein V\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26768080\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30326905\",\"source\":\"PubMed\"}],\"id\":\"SL-0274\",\"value\":\"Virion\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0381\",\"value\":\"Host cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030430\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:host cell cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Brgles M.\",\"Bonta M.\",\"Santak M.\",\"Jagusic M.\",\"Forcic D.\",\"Halassy B.\",\"Allmaier G.\",\"Marchetti-Deschmann M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26768080\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12985-016-0463-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"9\",\"id\":\"26768080\",\"journal\":\"Virol. J.\",\"lastPage\":\"9\",\"publicationDate\":\"2016\",\"title\":\"Identification of mumps virus protein and lipid composition by mass spectrometry.\",\"volume\":\"13\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"L-Zagreb vaccine\"}],\"referenceNumber\":3,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC47.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sviben D.\",\"Forcic D.\",\"Halassy B.\",\"Allmaier G.\",\"Marchetti-Deschmann M.\",\"Brgles M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30326905\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12985-018-1073-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"160\",\"id\":\"30326905\",\"journal\":\"Virol. J.\",\"lastPage\":\"160\",\"publicationDate\":\"2018\",\"title\":\"Mass spectrometry-based investigation of measles and mumps virus proteome.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"L-Zagreb vaccine\"}],\"referenceNumber\":4,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:25.927504+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d72d1bfef91f83edc604e803c3745ab3e35339dd94ab21f7e9f2f0685a89f29",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC47.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H1",
  "excerpt": "ID   V_MUMPZ                 Reviewed;         224 AA.\nAC   Q5SC47;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Non-structural protein V;\nDE   AltName: Full=Non-structural protein NS1;\nGN   Name=P/V/I {ECO:0000305};\nGN   and\nGN   Name=P;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.135943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "url": "https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.\nRC   STRAIN=L-Zagreb vaccine;\nRX   PubMed=26768080; DOI=10.1186/s12985-016-0463-0;\nRA   Brgles M., Bonta M., Santak M., Jagusic M., Forcic D., Halassy B.,\nRA   Allmaier G., Marchetti-Deschmann M.;\nRT   \"Identification of mumps virus protein and lipid composition by mass\nRT   spectrometry.\";\nRL   Virol. J. 13:9-9(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.135943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "url": "https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.\nRC   STRAIN=L-Zagreb vaccine;\nRX   PubMed=30326905; DOI=10.1186/s12985-018-1073-9;\nRA   Sviben D., Forcic D., Halassy B., Allmaier G., Marchetti-Deschmann M.,\nRA   Brgles M.;\nRT   \"Mass spectrometry-based investigation of measles and mumps virus\nRT   proteome.\";\nRL   Virol. J. 15:160-160(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.135943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "url": "https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000269|PubMed:26768080,\nCC       ECO:0000269|PubMed:30326905}. Host cytoplasm {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.135943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "url": "https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0030430; C:host cell cytoplasm; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.135943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "url": "https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0044423; C:virion component; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.135943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9b10c0e61fcd2db01a967b45f0328f76163c11791f76112a4d924c43addec41",
  "url": "https://rest.uniprot.org/unisave/Q5SC47?format=txt&versions=45"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005789\nname: endoplasmic reticulum membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the endoplasmic reticulum.\" [GOC:mah]\nsynonym: \"ER membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0042175 ! nuclear outer membrane-endoplasmic reticulum membrane network\nrelationship: part_of GO:0098827 ! endoplasmic reticulum subcompartment\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005789",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59526-59535",
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
  "excerpt": "[Term]\nid: GO:0098978\nname: glutamatergic synapse\nnamespace: cellular_component\ndef: \"A synapse that uses glutamate as a neurotransmitter.\" [GOC:dos]\nsubset: goslim_synapse\nis_a: GO:0045202 ! synapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098978",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 412689-412696",
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
  "excerpt": "[Term]\nid: GO:0120216\nname: matrilin complex\nnamespace: cellular_component\ndef: \"A cartilage extracellular matrix complex that mediates interactions between major components of the extracellular matrix such as collagens and proteoglycans and contributes to their fibrillar network. Exists as an obligate homotrimer.\" [PMID:10367731, PMID:15075323, PMID:29310791, PMID:9699631]\nsynonym: \"matrilin family complex\" RELATED [GOC:bhm]\nsynonym: \"matrilin-1 complex\" NARROW [GOC:bhm]\nsynonym: \"matrilin-2 complex\" NARROW [GOC:bhm]\nsynonym: \"matrilin-3 complex\" NARROW [GOC:bhm]\nsynonym: \"matrilin-4 complex\" NARROW [GOC:bhm]\nis_a: GO:0140392 ! extracellular protein-containing complex\nrelationship: part_of GO:0140149 ! non-collagenous component of interstitial matrix\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0120216",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 434047-434059",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
