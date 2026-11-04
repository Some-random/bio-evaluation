# GO_cellular_component_0052

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0052.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQLRKALLVIFVAYLLVTDEAEAFWGFLGKLAMKAVPSLIGGNKSSSKRKREIEDLFDPYQKDLDLQRLDRFFSQFQ

[Multiple Choices]
A. membrane
B. lipid droplet
C. host cytoskeleton
D. apicoplast
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

> The sequence-matched UniProt record describes the protein as secreted and associated with the target-cell membrane, supporting “membrane” among the offered choices. This is a localization annotation, not evidence that the peptide is an integral membrane protein; the record also annotates an extracellular location.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal segment consistent with a secretion signal, followed by a short, basic and hydrophobic peptide region. Transferable knowledge of secreted antimicrobial peptides makes interaction with target membranes a credible inference. That pattern favors membrane over lipid droplet, host cytoskeleton, or apicoplast, though it does not establish membrane residence as opposed to extracellular secretion.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A meaningful family-level inference is available from the sequence and choices; the exact protein annotation is not necessary to distinguish the membrane option probabilistically.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may be secreted rather than residing in its own membrane, but extracellular location is not offered. The membrane option is supported by the plausible target-membrane association and is not matched by another listed choice.


### Important caveats

- The reviewer-only source evidence was not part of the original model input.
- The source supports target-cell membrane association alongside secretion; it does not establish integral membrane topology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with a secretion signal, followed by a short, basic and hydrophobic peptide region. Transferable knowledge of secreted antimicrobial peptides makes interaction with target membranes a credible inference. That pattern favors membrane over lipid droplet, host cytoskeleton, or apicoplast, though it does not establish membrane residence as opposed to extracellular secretion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A meaningful family-level inference is available from the sequence and choices; the exact protein annotation is not necessary to distinguish the membrane option probabilistically."
  },
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes the protein as secreted and associated with the target-cell membrane, supporting “membrane” among the offered choices. This is a localization annotation, not evidence that the peptide is an integral membrane protein; the record also annotates an extracellular location."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original model input.",
    "The source supports target-cell membrane association alongside secretion; it does not establish integral membrane topology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may be secreted rather than residing in its own membrane, but extracellular location is not offered. The membrane option is supported by the plausible target-membrane association and is not matched by another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes the protein as secreted and associated with the target-cell membrane, supporting “membrane” among the offered choices. This is a localization annotation, not evidence that the peptide is an integral membrane protein; the record also annotates an extracellular location.",
    "evidence_ids": ["C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with a secretion signal, followed by a short, basic and hydrophobic peptide region. Transferable knowledge of secreted antimicrobial peptides makes interaction with target membranes a credible inference. That pattern favors membrane over lipid droplet, host cytoskeleton, or apicoplast, though it does not establish membrane residence as opposed to extracellular secretion.",
    "missing_item_specific_fact": "",
    "reason": "A meaningful family-level inference is available from the sequence and choices; the exact protein annotation is not necessary to distinguish the membrane option probabilistically."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may be secreted rather than residing in its own membrane, but extracellular location is not offered. The membrane option is supported by the plausible target-membrane association and is not matched by another listed choice."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original model input.",
    "The source supports target-cell membrane association alongside secretion; it does not establish integral membrane topology."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (VpAmp2.0 from scorpion) lists 'Secreted' and 'Target cell membrane' as subcellular locations. GO:0044218 ('other organism cell membrane') is annotated, which is a descendant of the broader 'membrane' term (GO:0016020). While the primary annotation is 'Secreted' / 'extracellular region' (GO:0005576), the 'Target cell membrane' annotation and the GO:0044218 term are within the membrane hierarchy, making 'membrane' a defensible broad-category answer among the four choices. The protein is an antimicrobial peptide that acts on target cell membranes, consistent with membrane association.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MQLRKALLVIFVAYLLVT, residues 1-18) is a classic signal peptide, indicating the protein enters the secretory pathway and is either secreted or membrane-associated. This immediately eliminates 'apicoplast' (D), which is a plastid organelle exclusive to apicomplexan parasites (Plasmodium, Toxoplasma) and irrelevant for an animal-derived sequence. 'Host cytoskeleton' (C) requires cytoskeleton-binding motifs (e.g., WH2 domains, actin-binding sequences) absent here. 'Lipid droplet' (B) proteins typically feature specific amphipathic helical targeting domains (e.g., PAT domain in perilipins) not present in this short peptide. The remaining 'membrane' (A) is consistent with the signal peptide directing the protein to the secretory/membrane pathway, and the overall short cationic-hydrophobic composition resembles antimicrobial peptides known to target cell membranes. Thus, transferable knowledge of signal peptides, antimicrobial peptide biology, and organelle specificity meaningfully distinguishes 'membrane' from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide and overall sequence composition provide sufficient transferable biological reasoning to select 'membrane' over apicoplast (wrong organism type), host cytoskeleton (no cytoskeleton motifs), and lipid droplet (no lipid droplet targeting features). No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other three options are clearly eliminable: apicoplast is restricted to apicomplexans, host cytoskeleton lacks relevant motifs, and lipid droplet lacks targeting features. Among the four choices, 'membrane' is the only reasonable answer, even if 'secreted/extracellular' would be more precise. The signal peptide and antimicrobial peptide-like composition make 'membrane' the best fit.


### Important caveats

- The primary UniProt annotation is 'Secreted' (GO:0005576, extracellular region), not 'membrane' per se. The 'membrane' answer is supported via the secondary 'Target cell membrane' annotation and GO:0044218, which is a descendant of membrane terms. The answer is the best among the four choices but not the most precise annotation.
- The protein is an antimicrobial peptide from scorpion venom gland; its membrane interaction is with target (other organism) cell membranes, not with its own cellular membranes.
- The GO evidence codes for the membrane-related annotations are IEA (Inferred from Electronic Annotation) and ECO:0000305 (curator inference), not direct experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MQLRKALLVIFVAYLLVT, residues 1-18) is a classic signal peptide, indicating the protein enters the secretory pathway and is either secreted or membrane-associated. This immediately eliminates 'apicoplast' (D), which is a plastid organelle exclusive to apicomplexan parasites (Plasmodium, Toxoplasma) and irrelevant for an animal-derived sequence. 'Host cytoskeleton' (C) requires cytoskeleton-binding motifs (e.g., WH2 domains, actin-binding sequences) absent here. 'Lipid droplet' (B) proteins typically feature specific amphipathic helical targeting domains (e.g., PAT domain in perilipins) not present in this short peptide. The remaining 'membrane' (A) is consistent with the signal peptide directing the protein to the secretory/membrane pathway, and the overall short cationic-hydrophobic composition resembles antimicrobial peptides known to target cell membranes. Thus, transferable knowledge of signal peptides, antimicrobial peptide biology, and organelle specificity meaningfully distinguishes 'membrane' from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide and overall sequence composition provide sufficient transferable biological reasoning to select 'membrane' over apicoplast (wrong organism type), host cytoskeleton (no cytoskeleton motifs), and lipid droplet (no lipid droplet targeting features). No target-specific database lookup is required."
  },
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (VpAmp2.0 from scorpion) lists 'Secreted' and 'Target cell membrane' as subcellular locations. GO:0044218 ('other organism cell membrane') is annotated, which is a descendant of the broader 'membrane' term (GO:0016020). While the primary annotation is 'Secreted' / 'extracellular region' (GO:0005576), the 'Target cell membrane' annotation and the GO:0044218 term are within the membrane hierarchy, making 'membrane' a defensible broad-category answer among the four choices. The protein is an antimicrobial peptide that acts on target cell membranes, consistent with membrane association."
  },
  "important_caveats": [
    "The primary UniProt annotation is 'Secreted' (GO:0005576, extracellular region), not 'membrane' per se. The 'membrane' answer is supported via the secondary 'Target cell membrane' annotation and GO:0044218, which is a descendant of membrane terms. The answer is the best among the four choices but not the most precise annotation.",
    "The protein is an antimicrobial peptide from scorpion venom gland; its membrane interaction is with target (other organism) cell membranes, not with its own cellular membranes.",
    "The GO evidence codes for the membrane-related annotations are IEA (Inferred from Electronic Annotation) and ECO:0000305 (curator inference), not direct experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options are clearly eliminable: apicoplast is restricted to apicomplexans, host cytoskeleton lacks relevant motifs, and lipid droplet lacks targeting features. Among the four choices, 'membrane' is the only reasonable answer, even if 'secreted/extracellular' would be more precise. The signal peptide and antimicrobial peptide-like composition make 'membrane' the best fit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (VpAmp2.0 from scorpion) lists 'Secreted' and 'Target cell membrane' as subcellular locations. GO:0044218 ('other organism cell membrane') is annotated, which is a descendant of the broader 'membrane' term (GO:0016020). While the primary annotation is 'Secreted' / 'extracellular region' (GO:0005576), the 'Target cell membrane' annotation and the GO:0044218 term are within the membrane hierarchy, making 'membrane' a defensible broad-category answer among the four choices. The protein is an antimicrobial peptide that acts on target cell membranes, consistent with membrane association.",
    "evidence_ids": ["C5", "H3", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MQLRKALLVIFVAYLLVT, residues 1-18) is a classic signal peptide, indicating the protein enters the secretory pathway and is either secreted or membrane-associated. This immediately eliminates 'apicoplast' (D), which is a plastid organelle exclusive to apicomplexan parasites (Plasmodium, Toxoplasma) and irrelevant for an animal-derived sequence. 'Host cytoskeleton' (C) requires cytoskeleton-binding motifs (e.g., WH2 domains, actin-binding sequences) absent here. 'Lipid droplet' (B) proteins typically feature specific amphipathic helical targeting domains (e.g., PAT domain in perilipins) not present in this short peptide. The remaining 'membrane' (A) is consistent with the signal peptide directing the protein to the secretory/membrane pathway, and the overall short cationic-hydrophobic composition resembles antimicrobial peptides known to target cell membranes. Thus, transferable knowledge of signal peptides, antimicrobial peptide biology, and organelle specificity meaningfully distinguishes 'membrane' from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide and overall sequence composition provide sufficient transferable biological reasoning to select 'membrane' over apicoplast (wrong organism type), host cytoskeleton (no cytoskeleton motifs), and lipid droplet (no lipid droplet targeting features). No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options are clearly eliminable: apicoplast is restricted to apicomplexans, host cytoskeleton lacks relevant motifs, and lipid droplet lacks targeting features. Among the four choices, 'membrane' is the only reasonable answer, even if 'secreted/extracellular' would be more precise. The signal peptide and antimicrobial peptide-like composition make 'membrane' the best fit."
  },
  "important_caveats": [
    "The primary UniProt annotation is 'Secreted' (GO:0005576, extracellular region), not 'membrane' per se. The 'membrane' answer is supported via the secondary 'Target cell membrane' annotation and GO:0044218, which is a descendant of membrane terms. The answer is the best among the four choices but not the most precise annotation.",
    "The protein is an antimicrobial peptide from scorpion venom gland; its membrane interaction is with target (other organism) cell membranes, not with its own cellular membranes.",
    "The GO evidence codes for the membrane-related annotations are IEA (Inferred from Electronic Annotation) and ECO:0000305 (curator inference), not direct experimental evidence."
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
  "benchmark_sequence_length": 77,
  "benchmark_sequence_sha256": "14166f2627a45ea62876c122779de6778a1951ee3d6b1b252ef982499308217f",
  "current_entry_audit": {
    "entryVersion": 8,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-01-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 77,
  "current_source_sequence_sha256": "14166f2627a45ea62876c122779de6778a1951ee3d6b1b252ef982499308217f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 7,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0N7FMT9",
  "selected_historical_entry_version": 7,
  "selected_historical_record_sha256": "45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c",
  "selected_historical_source_sequence_length": 77,
  "selected_historical_source_sequence_sha256": "14166f2627a45ea62876c122779de6778a1951ee3d6b1b252ef982499308217f",
  "selected_historical_version": {
    "accession": "A0A0N7FMT9",
    "database": "Swiss-Prot",
    "entryVersion": 7,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NDB2_MESPU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0N7FMT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":8,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-01-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Scorpion\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Chelicerata\",\"Arachnida\",\"Scorpiones\",\"Iurida\",\"Chactoidea\",\"Vaejovidae\",\"Mesomexovis\"],\"scientificName\":\"Mesomexovis punctatus\",\"synonyms\":[\"Vaejovis punctatus\"],\"taxonId\":1532993}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26352292\",\"source\":\"PubMed\"}],\"value\":\"VpAmp2.0\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26352292\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0451\",\"value\":\"Target cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/2",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Ramirez-Carreto S.\",\"Jimenez-Vargas J.M.\",\"Rivas-Santiago B.\",\"Corzo G.\",\"Possani L.D.\",\"Becerril B.\",\"Ortiz E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26352292\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.peptides.2015.08.014\"}],\"citationType\":\"journal article\",\"firstPage\":\"51\",\"id\":\"26352292\",\"journal\":\"Peptides\",\"lastPage\":\"59\",\"publicationDate\":\"2015\",\"title\":\"Peptides from the scorpion Vaejovis punctatus with broad antimicrobial activity.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALG64975.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom gland\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"SYNTHESIS OF 24-48\",\"MUTAGENESIS OF 45-SER--SER-47\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:17.678372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H1",
  "excerpt": "ID   NDB2_MESPU              Reviewed;          77 AA.\nAC   A0A0N7FMT9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-JAN-2016, sequence version 1.\nDT   28-JAN-2026, entry version 7.\nDE   RecName: Full=VpAmp2.0 {ECO:0000303|PubMed:26352292};\nDE   Flags: Precursor;\nOS   Mesomexovis punctatus (Scorpion) (Vaejovis punctatus).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida;\nOC   Scorpiones; Iurida; Chactoidea; Vaejovidae; Mesomexovis.\nOX   NCBI_TaxID=1532993;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:20.060714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c",
  "url": "https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALG64975.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], SYNTHESIS OF 24-48, AND MUTAGENESIS OF\nRP   45-SER--SER-47.\nRC   TISSUE=Venom gland;\nRX   PubMed=26352292; DOI=10.1016/j.peptides.2015.08.014;\nRA   Ramirez-Carreto S., Jimenez-Vargas J.M., Rivas-Santiago B., Corzo G.,\nRA   Possani L.D., Becerril B., Ortiz E.;\nRT   \"Peptides from the scorpion Vaejovis punctatus with broad antimicrobial\nRT   activity.\";\nRL   Peptides 73:51-59(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:20.060714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 12-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c",
  "url": "https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:26352292}. Target\nCC       cell membrane {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:20.060714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c",
  "url": "https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:20.060714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c",
  "url": "https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0044218; C:other organism cell membrane; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:20.060714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c",
  "url": "https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005811\nname: lipid droplet\nnamespace: cellular_component\ndef: \"An intracellular non-membrane-bounded organelle comprising a matrix of coalesced lipids surrounded by a phospholipid monolayer. May include associated proteins.\" [GOC:mah, GOC:tb]\ncomment: Note that this term does not refer to vesicles, but instead to structures in which lipids do not necessarily form bilayers.\nsubset: goslim_chembl\nsubset: goslim_generic\nsynonym: \"adiposome\" EXACT []\nsynonym: \"lipid body\" EXACT []\nsynonym: \"lipid particle\" EXACT []\nis_a: GO:0043232 ! intracellular membraneless organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005811",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59777-59789",
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
  "excerpt": "[Term]\nid: GO:0016020\nname: membrane\nnamespace: cellular_component\nalt_id: GO:0016021\nalt_id: GO:0098589\nalt_id: GO:0098805\ndef: \"A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it.\" [GOC:dos, GOC:mah, ISBN:0815316194]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"integral component of membrane\" NARROW []\nsynonym: \"integral to membrane\" NARROW []\nsynonym: \"membrane region\" NARROW []\nsynonym: \"region of membrane\" NARROW []\nsynonym: \"transmembrane\" RELATED [GOC:mah]\nsynonym: \"whole membrane\" NARROW []\nxref: Wikipedia:Biological_membrane\nxref: Wikipedia:Transmembrane_protein\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 122626-122650",
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
  "excerpt": "[Term]\nid: GO:0020011\nname: apicoplast\nnamespace: cellular_component\ndef: \"The plastid organelle found in apicomplexans.\" [ISBN:0521664470]\nxref: Wikipedia:Apicoplast\nis_a: GO:0009536 ! plastid\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020011",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155210-155217",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
