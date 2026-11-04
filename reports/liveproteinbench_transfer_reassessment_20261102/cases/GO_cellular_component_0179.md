# GO_cellular_component_0179

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0179.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — extracellular region

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIKMLQLPFNKKGQVSFDFIIAMLFLLLIFAFMGQNVLNMAKSFRDSETAEHAHAILDSFENYAIMAYSKDVTVNATFEPIGNLNYTIMLSNKSISVNSSTNIIFQPETDANGDYVSIKCNNVDNSVNTIPLNAVRISFGDFTVSKDEMEVNIR

[Multiple Choices]
A. NF-kappaB p50/p65 complex
B. peroxisomal matrix
C. extracellular region
D. cytoplasm
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

> The sequence-matched record annotates the protein as secreted, at the cell surface, and in a fimbrium; it also carries an extracellular-region GO annotation. These support C as the best offered location, though the cited location annotations are curator-inferred rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal basic segment followed by a strongly hydrophobic region, a pattern consistent with a processed export signal in pilin-like proteins. Transferable knowledge of pilin assembly and export makes an external or surface-associated destination more likely than cytoplasm or peroxisomal matrix; NF-kappaB complex is also not a plausible compartment for this sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal-like N terminus and compact protein sequence provide a meaningful family-pattern inference favoring the extracellular choice among these alternatives. This supports a probabilistic prediction without requiring recall of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may also be cell-surface or fimbrium-associated, but those locations are not offered. Among the listed options, extracellular region is the best match to the export/pilin inference.


### Important caveats

- The record also lists cell-surface and fimbrium localization, so extracellular region is not the only description of the protein's location.
- The GO extracellular-region annotation is IEA:UniProtKB-SubCell, and the cited excerpts do not establish direct experimental evidence for that specific GO assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal basic segment followed by a strongly hydrophobic region, a pattern consistent with a processed export signal in pilin-like proteins. Transferable knowledge of pilin assembly and export makes an external or surface-associated destination more likely than cytoplasm or peroxisomal matrix; NF-kappaB complex is also not a plausible compartment for this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal-like N terminus and compact protein sequence provide a meaningful family-pattern inference favoring the extracellular choice among these alternatives. This supports a probabilistic prediction without requiring recall of this exact protein's annotation."
  },
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as secreted, at the cell surface, and in a fimbrium; it also carries an extracellular-region GO annotation. These support C as the best offered location, though the cited location annotations are curator-inferred rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The record also lists cell-surface and fimbrium localization, so extracellular region is not the only description of the protein's location.",
    "The GO extracellular-region annotation is IEA:UniProtKB-SubCell, and the cited excerpts do not establish direct experimental evidence for that specific GO assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also be cell-surface or fimbrium-associated, but those locations are not offered. Among the listed options, extracellular region is the best match to the export/pilin inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as secreted, at the cell surface, and in a fimbrium; it also carries an extracellular-region GO annotation. These support C as the best offered location, though the cited location annotations are curator-inferred rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal basic segment followed by a strongly hydrophobic region, a pattern consistent with a processed export signal in pilin-like proteins. Transferable knowledge of pilin assembly and export makes an external or surface-associated destination more likely than cytoplasm or peroxisomal matrix; NF-kappaB complex is also not a plausible compartment for this sequence.",
    "missing_item_specific_fact": "",
    "reason": "The signal-like N terminus and compact protein sequence provide a meaningful family-pattern inference favoring the extracellular choice among these alternatives. This supports a probabilistic prediction without requiring recall of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also be cell-surface or fimbrium-associated, but those locations are not offered. Among the listed options, extracellular region is the best match to the export/pilin inference."
  },
  "important_caveats": [
    "The record also lists cell-surface and fimbrium localization, so extracellular region is not the only description of the protein's location.",
    "The GO extracellular-region annotation is IEA:UniProtKB-SubCell, and the cited excerpts do not establish direct experimental evidence for that specific GO assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q6M0N3) annotates this protein with GO:0005576 (extracellular region) via IEA:UniProtKB-SubCell, and the subcellular location comment states 'Secreted; Cell surface; Fimbrium' with experimental evidence from PubMed:17114255 and PubMed:21075925. The protein is a minor structural pilin (EpdC) that is secreted and incorporated into fimbriae on the cell surface, consistent with the extracellular region annotation. The GO term definition notes a preference for 'external side of plasma membrane' for surface-attached products, but the extracellular region annotation is present and the answer is supported.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region of the sequence (residues ~12-28: FIIAMLFLLLIFAFMGQ) is a classic hydrophobic signal peptide, strongly indicating the protein is targeted for secretion/export across the membrane. This immediately rules out cytoplasm (D) and peroxisomal matrix (B), since peroxisomal matrix proteins use PTS1 (C-terminal SKL-like) or PTS2 signals and lack transmembrane signal peptides. The C-terminus ends in 'NIR' with no PTS1 motif. Option A (NF-kappaB p50/p65 complex) is a vertebrate-specific transcription factor complex composed of Rel-homology-domain proteins; this 154-aa sequence bears no resemblance to NF-kappaB subunits and the organism context (small archaeal protein with a signal peptide) is incompatible. The remaining option, extracellular region (C), is the natural destination for a secreted protein bearing a signal peptide. A knowledgeable model can follow this standard signal-peptide → secretion → extracellular inference without knowing this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The N-terminal signal peptide is directly visible in the supplied sequence and is a universally recognized feature of secreted proteins. Combined with the absence of peroxisomal targeting signals, the absence of NF-kappaB-like Rel-homology domains, and the small size of the protein, a model with general biology knowledge can confidently eliminate A, B, and D and select C. This relies on transferable knowledge of signal peptides and protein targeting, not on memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, the N-terminal signal peptide cleanly directs to a secreted/extracellular destination. The GO definition's note preferring 'external side of plasma membrane' for surface-attached products introduces a minor technical nuance, but no such alternative is offered among the choices. Options A, B, and D are clearly incompatible with the sequence features. No ambiguity in selecting C.


### Important caveats

- The GO term definition for extracellular region (GO:0005576) notes it is intended for gene products not attached to the cell surface, while surface-attached products should use GO:0009897 (external side of plasma membrane). A pilin is technically surface-attached, creating a minor terminological imprecision, but the annotation is present in UniProt and no better alternative is offered among the choices.
- The GO annotation is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, derived from the experimental subcellular location comment. The underlying experimental evidence (PubMed:17114255, PubMed:21075925) supports secretion and fimbrial incorporation.
- The reviewer-only accession and organism identity (Methanococcus maripaludis, archaeon) were not provided to the evaluated model; the reasoning relies solely on sequence features visible in the input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region of the sequence (residues ~12-28: FIIAMLFLLLIFAFMGQ) is a classic hydrophobic signal peptide, strongly indicating the protein is targeted for secretion/export across the membrane. This immediately rules out cytoplasm (D) and peroxisomal matrix (B), since peroxisomal matrix proteins use PTS1 (C-terminal SKL-like) or PTS2 signals and lack transmembrane signal peptides. The C-terminus ends in 'NIR' with no PTS1 motif. Option A (NF-kappaB p50/p65 complex) is a vertebrate-specific transcription factor complex composed of Rel-homology-domain proteins; this 154-aa sequence bears no resemblance to NF-kappaB subunits and the organism context (small archaeal protein with a signal peptide) is incompatible. The remaining option, extracellular region (C), is the natural destination for a secreted protein bearing a signal peptide. A knowledgeable model can follow this standard signal-peptide → secretion → extracellular inference without knowing this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal signal peptide is directly visible in the supplied sequence and is a universally recognized feature of secreted proteins. Combined with the absence of peroxisomal targeting signals, the absence of NF-kappaB-like Rel-homology domains, and the small size of the protein, a model with general biology knowledge can confidently eliminate A, B, and D and select C. This relies on transferable knowledge of signal peptides and protein targeting, not on memorizing this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q6M0N3) annotates this protein with GO:0005576 (extracellular region) via IEA:UniProtKB-SubCell, and the subcellular location comment states 'Secreted; Cell surface; Fimbrium' with experimental evidence from PubMed:17114255 and PubMed:21075925. The protein is a minor structural pilin (EpdC) that is secreted and incorporated into fimbriae on the cell surface, consistent with the extracellular region annotation. The GO term definition notes a preference for 'external side of plasma membrane' for surface-attached products, but the extracellular region annotation is present and the answer is supported."
  },
  "important_caveats": [
    "The GO term definition for extracellular region (GO:0005576) notes it is intended for gene products not attached to the cell surface, while surface-attached products should use GO:0009897 (external side of plasma membrane). A pilin is technically surface-attached, creating a minor terminological imprecision, but the annotation is present in UniProt and no better alternative is offered among the choices.",
    "The GO annotation is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, derived from the experimental subcellular location comment. The underlying experimental evidence (PubMed:17114255, PubMed:21075925) supports secretion and fimbrial incorporation.",
    "The reviewer-only accession and organism identity (Methanococcus maripaludis, archaeon) were not provided to the evaluated model; the reasoning relies solely on sequence features visible in the input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, the N-terminal signal peptide cleanly directs to a secreted/extracellular destination. The GO definition's note preferring 'external side of plasma membrane' for surface-attached products introduces a minor technical nuance, but no such alternative is offered among the choices. Options A, B, and D are clearly incompatible with the sequence features. No ambiguity in selecting C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q6M0N3) annotates this protein with GO:0005576 (extracellular region) via IEA:UniProtKB-SubCell, and the subcellular location comment states 'Secreted; Cell surface; Fimbrium' with experimental evidence from PubMed:17114255 and PubMed:21075925. The protein is a minor structural pilin (EpdC) that is secreted and incorporated into fimbriae on the cell surface, consistent with the extracellular region annotation. The GO term definition notes a preference for 'external side of plasma membrane' for surface-attached products, but the extracellular region annotation is present and the answer is supported.",
    "evidence_ids": ["C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region of the sequence (residues ~12-28: FIIAMLFLLLIFAFMGQ) is a classic hydrophobic signal peptide, strongly indicating the protein is targeted for secretion/export across the membrane. This immediately rules out cytoplasm (D) and peroxisomal matrix (B), since peroxisomal matrix proteins use PTS1 (C-terminal SKL-like) or PTS2 signals and lack transmembrane signal peptides. The C-terminus ends in 'NIR' with no PTS1 motif. Option A (NF-kappaB p50/p65 complex) is a vertebrate-specific transcription factor complex composed of Rel-homology-domain proteins; this 154-aa sequence bears no resemblance to NF-kappaB subunits and the organism context (small archaeal protein with a signal peptide) is incompatible. The remaining option, extracellular region (C), is the natural destination for a secreted protein bearing a signal peptide. A knowledgeable model can follow this standard signal-peptide → secretion → extracellular inference without knowing this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal signal peptide is directly visible in the supplied sequence and is a universally recognized feature of secreted proteins. Combined with the absence of peroxisomal targeting signals, the absence of NF-kappaB-like Rel-homology domains, and the small size of the protein, a model with general biology knowledge can confidently eliminate A, B, and D and select C. This relies on transferable knowledge of signal peptides and protein targeting, not on memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, the N-terminal signal peptide cleanly directs to a secreted/extracellular destination. The GO definition's note preferring 'external side of plasma membrane' for surface-attached products introduces a minor technical nuance, but no such alternative is offered among the choices. Options A, B, and D are clearly incompatible with the sequence features. No ambiguity in selecting C."
  },
  "important_caveats": [
    "The GO term definition for extracellular region (GO:0005576) notes it is intended for gene products not attached to the cell surface, while surface-attached products should use GO:0009897 (external side of plasma membrane). A pilin is technically surface-attached, creating a minor terminological imprecision, but the annotation is present in UniProt and no better alternative is offered among the choices.",
    "The GO annotation is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, derived from the experimental subcellular location comment. The underlying experimental evidence (PubMed:17114255, PubMed:21075925) supports secretion and fimbrial incorporation.",
    "The reviewer-only accession and organism identity (Methanococcus maripaludis, archaeon) were not provided to the evaluated model; the reasoning relies solely on sequence features visible in the input."
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
  "benchmark_sequence_length": 154,
  "benchmark_sequence_sha256": "0f3be7d235562e4dffce23d4823c076daff4e18aa4e7ccd079ac7522f404b26c",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 154,
  "current_source_sequence_sha256": "0f3be7d235562e4dffce23d4823c076daff4e18aa4e7ccd079ac7522f404b26c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 69,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6M0N3",
  "selected_historical_entry_version": 69,
  "selected_historical_record_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "selected_historical_source_sequence_length": 154,
  "selected_historical_source_sequence_sha256": "0f3be7d235562e4dffce23d4823c076daff4e18aa4e7ccd079ac7522f404b26c",
  "selected_historical_version": {
    "accession": "Q6M0N3",
    "database": "Swiss-Prot",
    "entryVersion": 69,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "EPDC_METMP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6M0N3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17114255\",\"source\":\"PubMed\"}],\"value\":\"EppA-dependent protein C\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Minor structural pilin EpdC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17114255\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17114255\",\"source\":\"PubMed\"}],\"id\":\"SL-0310\",\"value\":\"Cell surface\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17114255\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21075925\",\"source\":\"PubMed\"}],\"id\":\"SL-0113\",\"value\":\"Fimbrium\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009986\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cell surface\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Szabo Z.\",\"Stahl A.O.\",\"Albers S.V.\",\"Kissinger J.C.\",\"Driessen A.J.\",\"Pohlschroeder M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17114255\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01547-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"772\",\"id\":\"17114255\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"778\",\"publicationDate\":\"2007\",\"title\":\"Identification of diverse archaeal proteins with class III signal peptides cleaved by distinct archaeal prepilin peptidases.\",\"volume\":\"189\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":2,\"referencePositions\":[\"CLEAVAGE BY EPPA\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Ng S.Y.\",\"Wu J.\",\"Nair D.B.\",\"Logan S.M.\",\"Robotham A.\",\"Tessier L.\",\"Kelly J.F.\",\"Uchida K.\",\"Aizawa S.\",\"Jarrell K.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21075925\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.00822-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"804\",\"id\":\"21075925\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"814\",\"publicationDate\":\"2011\",\"title\":\"Genetic and mass spectrometry analyses of the unusual type IV-like pili of the archaeon Methanococcus maripaludis.\",\"volume\":\"193\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:40.884710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H1",
  "excerpt": "ID   EPDC_METMP              Reviewed;         154 AA.\nAC   Q6M0N3;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 69.\nDE   RecName: Full=Minor structural pilin EpdC {ECO:0000305};\nDE   AltName: Full=EppA-dependent protein C {ECO:0000303|PubMed:17114255};\nDE   Flags: Precursor;\nGN   Name=epdC {ECO:0000303|PubMed:17114255};\nGN   OrderedLocusNames=MMP0237 {ECO:0000312|EMBL:CAF29793.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:42.932189+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "url": "https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   CLEAVAGE BY EPPA, AND DOMAIN.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=17114255; DOI=10.1128/jb.01547-06;\nRA   Szabo Z., Stahl A.O., Albers S.V., Kissinger J.C., Driessen A.J.,\nRA   Pohlschroeder M.;\nRT   \"Identification of diverse archaeal proteins with class III signal peptides\nRT   cleaved by distinct archaeal prepilin peptidases.\";\nRL   J. Bacteriol. 189:772-778(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:42.932189+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "url": "https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=21075925; DOI=10.1128/jb.00822-10;\nRA   Ng S.Y., Wu J., Nair D.B., Logan S.M., Robotham A., Tessier L., Kelly J.F.,\nRA   Uchida K., Aizawa S., Jarrell K.F.;\nRT   \"Genetic and mass spectrometry analyses of the unusual type IV-like pili of\nRT   the archaeon Methanococcus maripaludis.\";\nRL   J. Bacteriol. 193:804-814(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:42.932189+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "url": "https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:17114255}. Cell\nCC       surface {ECO:0000305|PubMed:17114255}. Fimbrium\nCC       {ECO:0000305|PubMed:17114255, ECO:0000305|PubMed:21075925}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:42.932189+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "url": "https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0009986; C:cell surface; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:42.932189+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "url": "https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:42.932189+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa",
  "url": "https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005576\nname: extracellular region\nnamespace: cellular_component\ndef: \"The space external to the outermost structure of a cell. For cells without external protective or external encapsulating structures this refers to space outside of the plasma membrane. This term covers the host cell environment outside an intracellular parasite.\" [GOC:curators]\ncomment: Note that this term is intended to annotate gene products that are not attached to the cell surface. For gene products at the cell surface, consider annotating to external side of plasma membrane ; GO:0009897.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"extracellular\" EXACT []\nxref: Wikipedia:Extracellular\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005576",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57481-57505",
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
  "excerpt": "[Term]\nid: GO:0005737\nname: cytoplasm\nnamespace: cellular_component\ndef: \"The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures.\" [ISBN:0198547684]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nxref: Wikipedia:Cytoplasm\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005622 ! intracellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005737",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58957-58974",
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
  "excerpt": "[Term]\nid: GO:0005782\nname: peroxisomal matrix\nnamespace: cellular_component\nalt_id: GO:0031909\ndef: \"The volume contained within the membranes of a peroxisome; in many cells the matrix contains a crystalloid core largely composed of urate oxidase.\" [GOC:curators, ISBN:0815316194]\nsynonym: \"peroxisomal lumen\" EXACT []\nis_a: GO:0031907 ! microbody lumen\nrelationship: part_of GO:0005777 ! peroxisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005782",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59440-59449",
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
  "excerpt": "[Term]\nid: GO:0035525\nname: NF-kappaB p50/p65 complex\nnamespace: cellular_component\ndef: \"A heterodimer of NF-kappa B p50 and p65 subunits.\" [GO:add, PMID:20393192, PMID:9299584]\ncomment: Note that the p50 subunit is encoded by NFKB1 gene in human and the p65 subunit is encoded by the RELA gene in human. Similar nomenclature is used in other vertebrate species. The p50 subunit has a precursor form p105 in some publications.\nsynonym: \"NF-kappa B1/p65 complex\" EXACT [PMID:9299584]\nsynonym: \"NF-kappa B1/RelA complex\" EXACT [PMID:9299584]\nsynonym: \"NF-kappa p105/p65 complex\" RELATED [PMID:9299584]\nsynonym: \"NF-kappa p105/RelA complex\" RELATED [PMID:9299584]\nsynonym: \"NF-kappa p50/RelA complex\" EXACT [PMID:9299584]\nis_a: GO:0071159 ! NF-kappaB complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035525",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 218851-218863",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
