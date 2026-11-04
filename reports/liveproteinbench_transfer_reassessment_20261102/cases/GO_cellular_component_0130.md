# GO_cellular_component_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0130.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — cytosolic large ribosomal subunit

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIMLKTQRRIAAELLKCGENRIWIDPERIEDVAAAITREDIKRLIHDGVIKKKPIKGQSRARARAFQEARKKGRHRGPGSKKGKKTARMGKKEVWMMTIRALRKELRKLKAEGKLDAHTYRRLYIRAKGGQFKNKRQLYMFMQEHGILKE

[Multiple Choices]
A. host cytoskeleton
B. virion component
C. histone deacetylase complex
D. cytosolic large ribosomal subunit
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

> The supplied sequence matches a UniProt entry annotated as large ribosomal subunit protein eL19, and that entry assigns it to the cytosolic large ribosomal subunit. The protein name is supported by a HAMAP rule and the GO annotation by IBA, so this is computational/phylogenetic annotation rather than direct experimental localization evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a small, strongly basic protein with the profile of an archaeal/eukaryotic-type large-subunit ribosomal protein such as eL19. Such proteins associate with ribosomal RNA and the large ribosomal subunit. That family-level inference meaningfully favors D over a host cytoskeleton protein, virion component, or histone deacetylase complex; the broad D option also encompasses prokaryotic large ribosomal subunits.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable ribosomal-protein family inference from the sequence distinguishes the offered choices without needing the exact protein's database record. The assignment is credible but is not an independent experimental determination of localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these alternatives, the ribosomal-protein sequence profile points to D; none of the other choices is comparably supported.


### Important caveats

- The reviewer-only evidence identifies the organism as an archaeon, but that identity was not part of the original input and is not needed for the family-level inference.
- The source GO annotation is IBA, and the protein name is assigned by a HAMAP rule; neither excerpt establishes direct experimental localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a small, strongly basic protein with the profile of an archaeal/eukaryotic-type large-subunit ribosomal protein such as eL19. Such proteins associate with ribosomal RNA and the large ribosomal subunit. That family-level inference meaningfully favors D over a host cytoskeleton protein, virion component, or histone deacetylase complex; the broad D option also encompasses prokaryotic large ribosomal subunits.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable ribosomal-protein family inference from the sequence distinguishes the offered choices without needing the exact protein's database record. The assignment is credible but is not an independent experimental determination of localization."
  },
  "case_id": "GO_cellular_component_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches a UniProt entry annotated as large ribosomal subunit protein eL19, and that entry assigns it to the cytosolic large ribosomal subunit. The protein name is supported by a HAMAP rule and the GO annotation by IBA, so this is computational/phylogenetic annotation rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the organism as an archaeon, but that identity was not part of the original input and is not needed for the family-level inference.",
    "The source GO annotation is IBA, and the protein name is assigned by a HAMAP rule; neither excerpt establishes direct experimental localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, the ribosomal-protein sequence profile points to D; none of the other choices is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches a UniProt entry annotated as large ribosomal subunit protein eL19, and that entry assigns it to the cytosolic large ribosomal subunit. The protein name is supported by a HAMAP rule and the GO annotation by IBA, so this is computational/phylogenetic annotation rather than direct experimental localization evidence.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a small, strongly basic protein with the profile of an archaeal/eukaryotic-type large-subunit ribosomal protein such as eL19. Such proteins associate with ribosomal RNA and the large ribosomal subunit. That family-level inference meaningfully favors D over a host cytoskeleton protein, virion component, or histone deacetylase complex; the broad D option also encompasses prokaryotic large ribosomal subunits.",
    "missing_item_specific_fact": "",
    "reason": "A transferable ribosomal-protein family inference from the sequence distinguishes the offered choices without needing the exact protein's database record. The assignment is credible but is not an independent experimental determination of localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, the ribosomal-protein sequence profile points to D; none of the other choices is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the organism as an archaeon, but that identity was not part of the original input and is not needed for the family-level inference.",
    "The source GO annotation is IBA, and the protein name is assigned by a HAMAP rule; neither excerpt establishes direct experimental localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5JJG6 annotates this 150 AA sequence as 'Large ribosomal subunit protein eL19' (HAMAP-Rule MF_01475) with GO:0022625 (cytosolic large ribosomal subunit, evidence IBA:GO_Central). The sequence matches exactly. The GO term applies to archaea (includes 'prokaryotic large ribosomal subunit' as a NARROW synonym). The evidence is computational (HAMAP rule + IBA:GO_Central) rather than experimental, but the sequence composition (extreme basicity, small size, no enzymatic domains) is consistent with ribosomal protein characteristics, supporting the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-residue sequence exhibits an extraordinarily high density of basic residues (Lys and Arg comprise roughly 35% of the sequence), with clusters such as 'KKKPIKGQSRARARAFQEARKKGRHRGPGSKKGKKTARMGKKEVWMM'. This extreme basicity is a hallmark of ribosomal proteins across all domains of life, reflecting their need to interact electrostatically with negatively charged rRNA. Ribosomal proteins are also characteristically small (50–300 AA) and lack enzymatic or structural domains. Among the choices: (A) cytoskeletal proteins are typically 300–500+ AA with different sequence architecture; (B) viral capsid proteins vary but rarely show this specific pattern of clustered basic residues without hydrophobic capsid motifs; (C) HDAC complex subunits contain recognizable enzymatic domains (zinc-binding for classical HDACs, Rossmann-fold for sirtuins) absent here. The combination of small size, extreme basicity, and absence of any enzymatic or structural domain motif provides a concrete, transferable inference from general ribosomal-protein biology (learned from eukaryotic and bacterial homologs) that meaningfully distinguishes option D from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence's extreme basic character (~35% K+R), small length (150 AA), and lack of enzymatic domains are well-known hallmarks of ribosomal proteins learned from homologs across domains. This transferable pattern distinguishes D from the other three choices without needing to recall the specific annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The extreme basicity and small size strongly and specifically point to ribosomal proteins. Cytoskeletal proteins are much larger, HDAC subunits require enzymatic domains, and while some viral proteins are small, they lack this specific pattern of clustered basic residues without hydrophobic capsid motifs. No alternative is genuinely defensible given the sequence features.


### Important caveats

- The GO annotation evidence is IBA:GO_Central (computational inference), and the protein name derives from HAMAP-Rule (proteome-wide computational annotation), not direct experimental localization.
- The protein is from Thermococcus kodakarensis (Archaea); the GO term 'cytosolic large ribosomal subunit' (GO:0022625) includes 'prokaryotic large ribosomal subunit' as a NARROW synonym, making it applicable to archaeal ribosomes.
- The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on sequence composition and general ribosomal-protein biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-residue sequence exhibits an extraordinarily high density of basic residues (Lys and Arg comprise roughly 35% of the sequence), with clusters such as 'KKKPIKGQSRARARAFQEARKKGRHRGPGSKKGKKTARMGKKEVWMM'. This extreme basicity is a hallmark of ribosomal proteins across all domains of life, reflecting their need to interact electrostatically with negatively charged rRNA. Ribosomal proteins are also characteristically small (50–300 AA) and lack enzymatic or structural domains. Among the choices: (A) cytoskeletal proteins are typically 300–500+ AA with different sequence architecture; (B) viral capsid proteins vary but rarely show this specific pattern of clustered basic residues without hydrophobic capsid motifs; (C) HDAC complex subunits contain recognizable enzymatic domains (zinc-binding for classical HDACs, Rossmann-fold for sirtuins) absent here. The combination of small size, extreme basicity, and absence of any enzymatic or structural domain motif provides a concrete, transferable inference from general ribosomal-protein biology (learned from eukaryotic and bacterial homologs) that meaningfully distinguishes option D from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence's extreme basic character (~35% K+R), small length (150 AA), and lack of enzymatic domains are well-known hallmarks of ribosomal proteins learned from homologs across domains. This transferable pattern distinguishes D from the other three choices without needing to recall the specific annotation of this exact protein."
  },
  "case_id": "GO_cellular_component_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5JJG6 annotates this 150 AA sequence as 'Large ribosomal subunit protein eL19' (HAMAP-Rule MF_01475) with GO:0022625 (cytosolic large ribosomal subunit, evidence IBA:GO_Central). The sequence matches exactly. The GO term applies to archaea (includes 'prokaryotic large ribosomal subunit' as a NARROW synonym). The evidence is computational (HAMAP rule + IBA:GO_Central) rather than experimental, but the sequence composition (extreme basicity, small size, no enzymatic domains) is consistent with ribosomal protein characteristics, supporting the annotation."
  },
  "important_caveats": [
    "The GO annotation evidence is IBA:GO_Central (computational inference), and the protein name derives from HAMAP-Rule (proteome-wide computational annotation), not direct experimental localization.",
    "The protein is from Thermococcus kodakarensis (Archaea); the GO term 'cytosolic large ribosomal subunit' (GO:0022625) includes 'prokaryotic large ribosomal subunit' as a NARROW synonym, making it applicable to archaeal ribosomes.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on sequence composition and general ribosomal-protein biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The extreme basicity and small size strongly and specifically point to ribosomal proteins. Cytoskeletal proteins are much larger, HDAC subunits require enzymatic domains, and while some viral proteins are small, they lack this specific pattern of clustered basic residues without hydrophobic capsid motifs. No alternative is genuinely defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5JJG6 annotates this 150 AA sequence as 'Large ribosomal subunit protein eL19' (HAMAP-Rule MF_01475) with GO:0022625 (cytosolic large ribosomal subunit, evidence IBA:GO_Central). The sequence matches exactly. The GO term applies to archaea (includes 'prokaryotic large ribosomal subunit' as a NARROW synonym). The evidence is computational (HAMAP rule + IBA:GO_Central) rather than experimental, but the sequence composition (extreme basicity, small size, no enzymatic domains) is consistent with ribosomal protein characteristics, supporting the annotation.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-residue sequence exhibits an extraordinarily high density of basic residues (Lys and Arg comprise roughly 35% of the sequence), with clusters such as 'KKKPIKGQSRARARAFQEARKKGRHRGPGSKKGKKTARMGKKEVWMM'. This extreme basicity is a hallmark of ribosomal proteins across all domains of life, reflecting their need to interact electrostatically with negatively charged rRNA. Ribosomal proteins are also characteristically small (50–300 AA) and lack enzymatic or structural domains. Among the choices: (A) cytoskeletal proteins are typically 300–500+ AA with different sequence architecture; (B) viral capsid proteins vary but rarely show this specific pattern of clustered basic residues without hydrophobic capsid motifs; (C) HDAC complex subunits contain recognizable enzymatic domains (zinc-binding for classical HDACs, Rossmann-fold for sirtuins) absent here. The combination of small size, extreme basicity, and absence of any enzymatic or structural domain motif provides a concrete, transferable inference from general ribosomal-protein biology (learned from eukaryotic and bacterial homologs) that meaningfully distinguishes option D from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence's extreme basic character (~35% K+R), small length (150 AA), and lack of enzymatic domains are well-known hallmarks of ribosomal proteins learned from homologs across domains. This transferable pattern distinguishes D from the other three choices without needing to recall the specific annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The extreme basicity and small size strongly and specifically point to ribosomal proteins. Cytoskeletal proteins are much larger, HDAC subunits require enzymatic domains, and while some viral proteins are small, they lack this specific pattern of clustered basic residues without hydrophobic capsid motifs. No alternative is genuinely defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation evidence is IBA:GO_Central (computational inference), and the protein name derives from HAMAP-Rule (proteome-wide computational annotation), not direct experimental localization.",
    "The protein is from Thermococcus kodakarensis (Archaea); the GO term 'cytosolic large ribosomal subunit' (GO:0022625) includes 'prokaryotic large ribosomal subunit' as a NARROW synonym, making it applicable to archaeal ribosomes.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on sequence composition and general ribosomal-protein biology."
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
  "benchmark_sequence_length": 150,
  "benchmark_sequence_sha256": "fd07dbf9bfb5cb23c30118d25ae54d0b10bd6ce7e6599f4edef4712571d4789e",
  "current_entry_audit": {
    "entryVersion": 115,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-02-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 150,
  "current_source_sequence_sha256": "fd07dbf9bfb5cb23c30118d25ae54d0b10bd6ce7e6599f4edef4712571d4789e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 113,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5JJG6",
  "selected_historical_entry_version": 113,
  "selected_historical_record_sha256": "89f2058191e5c852afb7a552db1ff6204bc8ed83b2550cad9f645c365cf70da9",
  "selected_historical_source_sequence_length": 150,
  "selected_historical_source_sequence_sha256": "fd07dbf9bfb5cb23c30118d25ae54d0b10bd6ce7e6599f4edef4712571d4789e",
  "selected_historical_version": {
    "accession": "Q5JJG6",
    "database": "Swiss-Prot",
    "entryVersion": 113,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RL19E_THEKO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5JJG6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:21.208051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JJG6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":115,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-02-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:21.208051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JJG6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Pyrococcus kodakaraensis (strain KOD1)\",\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Thermococcus\"],\"scientificName\":\"Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\",\"taxonId\":69014}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:21.208051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JJG6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01475\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Large ribosomal subunit protein eL19\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:21.208051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JJG6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0022625\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosolic large ribosomal subunit\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "retrieved_utc": "2026-11-02T04:31:21.208051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JJG6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113)

```json
{
  "entry_version": 113,
  "evidence_id": "H1",
  "excerpt": "ID   RL19E_THEKO             Reviewed;         150 AA.\nAC   Q5JJG6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-FEB-2005, sequence version 1.\nDT   28-JAN-2026, entry version 113.\nDE   RecName: Full=Large ribosomal subunit protein eL19 {ECO:0000255|HAMAP-Rule:MF_01475};\nGN   Name=rpl19e {ECO:0000255|HAMAP-Rule:MF_01475};\nGN   OrderedLocusNames=TK1523 {ECO:0000312|EMBL:BAD85712.1};\nOS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\nOS   (Pyrococcus kodakaraensis (strain KOD1)).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Thermococcus.\nOX   NCBI_TaxID=69014;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.628071+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89f2058191e5c852afb7a552db1ff6204bc8ed83b2550cad9f645c365cf70da9",
  "url": "https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113)

```json
{
  "entry_version": 113,
  "evidence_id": "H2",
  "excerpt": "DR   GO; GO:0022625; C:cytosolic large ribosomal subunit; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:30.628071+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89f2058191e5c852afb7a552db1ff6204bc8ed83b2550cad9f645c365cf70da9",
  "url": "https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000118\nname: histone deacetylase complex\nnamespace: cellular_component\ndef: \"A protein complex that possesses histone deacetylase activity.\" [GOC:mah]\ncomment: Note that this term represents a location, not a function; the activity possessed by this complex is mentioned in the definition for the purpose of describing and distinguishing the complex. The function of this complex is represented by the molecular function term 'histone deacetylase activity ; GO:0004407'.\nsynonym: \"HDAC complex\" EXACT []\nis_a: GO:0140513 ! nuclear protein-containing complex\nis_a: GO:1902494 ! catalytic complex\nrelationship: part_of GO:0005654 ! nucleoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000118",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1175-1185",
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
  "excerpt": "[Term]\nid: GO:0000180\nname: obsolete cytosolic large ribosomal subunit\nnamespace: cellular_component\ndef: \"OBSOLETE. (Was not defined before being made obsolete).\" [GOC:ai]\ncomment: This term was made obsolete because more specific children exist.\nsynonym: \"cytosolic large ribosomal subunit\" EXACT []\nis_obsolete: true\nconsider: GO:0022625\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000180",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1791-1800",
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
  "excerpt": "[Term]\nid: GO:0022625\nname: cytosolic large ribosomal subunit\nnamespace: cellular_component\nalt_id: GO:0005842\nalt_id: GO:0009282\nalt_id: GO:0030498\nalt_id: GO:0030872\ndef: \"The large subunit of a ribosome located in the cytosol.\" [GOC:mtg_sensu]\nsynonym: \"50S ribosomal subunit\" NARROW []\nsynonym: \"60S ribosomal subunit\" NARROW []\nsynonym: \"eukaryotic ribosomal LSU\" NARROW []\nsynonym: \"prokaryotic large ribosomal subunit\" NARROW []\nis_a: GO:0015934 ! large ribosomal subunit\nrelationship: part_of GO:0022626 ! cytosolic ribosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0022625",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 160556-160571",
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
  "excerpt": "[Term]\nid: GO:0044163\nname: host cytoskeleton\nnamespace: cellular_component\ndef: \"A cellular structure that forms the internal framework of eukaryotic and prokaryotic host cells. The cytoskeleton includes intermediate filaments, microfilaments, microtubules, the microtrabecular lattice, and other structures characterized by a polymeric filamentous nature and long-range order within the cell. The various elements of the cytoskeleton not only serve in the maintenance of cellular shape but also have roles in other cellular functions, including cellular movement, cell division, endocytosis, and movement of organelles.\" [GOC:rph]\nis_a: GO:0033647 ! host intracellular organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044163",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 254829-254835",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0044423\nname: virion component\nnamespace: cellular_component\nalt_id: GO:0019012\ndef: \"Any constituent part of a virion, a complete fully infectious extracellular virus particle.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"complete virus particle\" RELATED []\nsynonym: \"virion\" RELATED []\nsynonym: \"virion part\" EXACT []\nxref: Wikipedia:Virus\nis_a: GO:0005575 ! cellular_component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044423",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 257048-257062",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
