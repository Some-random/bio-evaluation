# GO_cellular_component_0141

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0141.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — cytoplasm

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFNNFLNMYMCTLAEKLCKFKKNNFNNIHRNNNFYRDNNFYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNLYTNNNLYRDNNFYNITLRKFHFIQTISNNNFNFEIIKKYGDVINKIMFIHTQKKNKQERFMFNNKKYIKRKEYILNDLNEFISIIPHPEINNEITNNSNQKKNKDNKQNVLSTNQQIITNYNLNHKENVTSNLNFNNKEEDEKKLDKLLKKRNIKKRDIVTITEEAKEELKKIISINKKENNNNYNNMNTICSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK

[Multiple Choices]
A. endoplasmic reticulum
B. perinuclear region of cytoplasm
C. cytoplasm
D. cytosolic small ribosomal subunit
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

> The matched sequence has a GO cytoplasm annotation (IBA), supporting choice C as a broad cellular-component annotation. However, the source also reports experimentally supported mitochondrial localization, which is more specific; mitochondrion is not an offered choice and is part of the cytoplasm in the supplied ontology hierarchy.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a long, low-complexity N-terminal region followed by a more conserved protein-like region, plausibly consistent with an organellar Fe-S assembly protein rather than an ER secretory protein or ribosomal subunit. Transferable knowledge that eukaryotic IscA-like Fe-S assembly proteins commonly localize to mitochondria makes the broad cytoplasm choice the best fit among these options; mitochondrial residence is within the cytoplasm in the supplied GO hierarchy.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the contrast with ER-targeting and ribosomal features provide a meaningful basis for preferring C among the actual options. The inference is probabilistic, and the exact mitochondrial localization is not established from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Mitochondrion would be a more specific localization, but it is not an option. The supplied choices do not offer another clearly supported localization for this protein.


### Important caveats

- The experimental source evidence supports mitochondrial localization, while the cytoplasm annotation is IBA; these are different levels and types of evidence.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a long, low-complexity N-terminal region followed by a more conserved protein-like region, plausibly consistent with an organellar Fe-S assembly protein rather than an ER secretory protein or ribosomal subunit. Transferable knowledge that eukaryotic IscA-like Fe-S assembly proteins commonly localize to mitochondria makes the broad cytoplasm choice the best fit among these options; mitochondrial residence is within the cytoplasm in the supplied GO hierarchy.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the contrast with ER-targeting and ribosomal features provide a meaningful basis for preferring C among the actual options. The inference is probabilistic, and the exact mitochondrial localization is not established from sequence alone."
  },
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a GO cytoplasm annotation (IBA), supporting choice C as a broad cellular-component annotation. However, the source also reports experimentally supported mitochondrial localization, which is more specific; mitochondrion is not an offered choice and is part of the cytoplasm in the supplied ontology hierarchy."
  },
  "important_caveats": [
    "The experimental source evidence supports mitochondrial localization, while the cytoplasm annotation is IBA; these are different levels and types of evidence.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mitochondrion would be a more specific localization, but it is not an option. The supplied choices do not offer another clearly supported localization for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a GO cytoplasm annotation (IBA), supporting choice C as a broad cellular-component annotation. However, the source also reports experimentally supported mitochondrial localization, which is more specific; mitochondrion is not an offered choice and is part of the cytoplasm in the supplied ontology hierarchy.",
    "evidence_ids": ["C5", "C6", "C7", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a long, low-complexity N-terminal region followed by a more conserved protein-like region, plausibly consistent with an organellar Fe-S assembly protein rather than an ER secretory protein or ribosomal subunit. Transferable knowledge that eukaryotic IscA-like Fe-S assembly proteins commonly localize to mitochondria makes the broad cytoplasm choice the best fit among these options; mitochondrial residence is within the cytoplasm in the supplied GO hierarchy.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the contrast with ER-targeting and ribosomal features provide a meaningful basis for preferring C among the actual options. The inference is probabilistic, and the exact mitochondrial localization is not established from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mitochondrion would be a more specific localization, but it is not an option. The supplied choices do not offer another clearly supported localization for this protein."
  },
  "important_caveats": [
    "The experimental source evidence supports mitochondrial localization, while the cytoplasm annotation is IBA; these are different levels and types of evidence.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for O97297 (PfIscA2) carries a GO:0005737 (cytoplasm) annotation with IBA:GO_Central evidence (C6/H4). The primary experimental SUBCELLULAR LOCATION is 'Mitochondrion' (SL-0173, ECO:0000269), but mitochondrion is part_of cytoplasm in the GO ontology (GO3). Since 'mitochondrion' is not among the offered choices, 'cytoplasm' (C) is the correct parent category in the GO hierarchy and is directly annotated in the database. The author's answer C is supported by the existing GO annotation, though it is a computational (IBA) rather than experimental annotation.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [GO3](#evidence-go3), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish C from the alternatives through multiple converging lines of reasoning: (1) Elimination of A (ER): the sequence lacks a cleavable N-terminal signal peptide and transmembrane domains characteristic of ER-resident or secreted proteins. (2) Elimination of D (cytosolic small ribosomal subunit): the protein is 404 aa with a composition inconsistent with ribosomal proteins (which are typically smaller, highly basic, and have distinct RNA-binding motifs). (3) Elimination of B (perinuclear region of cytoplasm): this is a highly specific annotation requiring evidence of perinuclear enrichment; no such targeting signal is apparent. (4) Positive support for C: the C-terminal 'ICPCG' motif (Cys-Pro-Cys) is a hallmark of Fe-S cluster-binding proteins in the ISC pathway. In eukaryotes, ISC proteins are mitochondrial, but mitochondrion is part_of cytoplasm in GO. Since mitochondrion is not offered, cytoplasm is the correct encompassing term. Additionally, the overall sequence composition (high Asn content, no strong organelle-targeting signals for ER or nucleus) is consistent with a broadly cytoplasmic/intracellular localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of motif recognition (Fe-S cluster CXXC motifs indicating ISC pathway), elimination of incompatible alternatives (no ER signal peptide, not a ribosomal protein, no perinuclear-specific features), and the GO ontology hierarchy (mitochondrion ⊂ cytoplasm) provides a concrete transferable argument that meaningfully distinguishes C from the other three options without requiring memorization of this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the true primary location is mitochondrion (not offered), among the four given choices only C (cytoplasm) is defensible. A, B, and D are eliminated by clear sequence and structural reasoning. The GO hierarchy makes cytoplasm the correct parent term for a mitochondrial protein when mitochondrion is unavailable as a choice.


### Important caveats

- The primary experimental subcellular location annotation is 'Mitochondrion' (ECO:0000269, experimental), while the 'cytoplasm' annotation is IBA:GO_Central (computational inference). The author's answer relies on the computational GO annotation and the ontology parent-child relationship.
- The question asks for the 'primary' cellular component, yet the most precise answer (mitochondrion) is not offered. Cytoplasm is correct only as the broader parent category.
- The protein is from Plasmodium falciparum, an apicomplexan with unusual organelle biology; however, the reasoning for choosing C does not depend on Plasmodium-specific knowledge.
- The GO:0000181 term in option D is obsolete (replaced by GO:0022627), which further weakens D as a viable distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish C from the alternatives through multiple converging lines of reasoning: (1) Elimination of A (ER): the sequence lacks a cleavable N-terminal signal peptide and transmembrane domains characteristic of ER-resident or secreted proteins. (2) Elimination of D (cytosolic small ribosomal subunit): the protein is 404 aa with a composition inconsistent with ribosomal proteins (which are typically smaller, highly basic, and have distinct RNA-binding motifs). (3) Elimination of B (perinuclear region of cytoplasm): this is a highly specific annotation requiring evidence of perinuclear enrichment; no such targeting signal is apparent. (4) Positive support for C: the C-terminal 'ICPCG' motif (Cys-Pro-Cys) is a hallmark of Fe-S cluster-binding proteins in the ISC pathway. In eukaryotes, ISC proteins are mitochondrial, but mitochondrion is part_of cytoplasm in GO. Since mitochondrion is not offered, cytoplasm is the correct encompassing term. Additionally, the overall sequence composition (high Asn content, no strong organelle-targeting signals for ER or nucleus) is consistent with a broadly cytoplasmic/intracellular localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of motif recognition (Fe-S cluster CXXC motifs indicating ISC pathway), elimination of incompatible alternatives (no ER signal peptide, not a ribosomal protein, no perinuclear-specific features), and the GO ontology hierarchy (mitochondrion ⊂ cytoplasm) provides a concrete transferable argument that meaningfully distinguishes C from the other three options without requiring memorization of this specific protein's database record."
  },
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "GO3",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for O97297 (PfIscA2) carries a GO:0005737 (cytoplasm) annotation with IBA:GO_Central evidence (C6/H4). The primary experimental SUBCELLULAR LOCATION is 'Mitochondrion' (SL-0173, ECO:0000269), but mitochondrion is part_of cytoplasm in the GO ontology (GO3). Since 'mitochondrion' is not among the offered choices, 'cytoplasm' (C) is the correct parent category in the GO hierarchy and is directly annotated in the database. The author's answer C is supported by the existing GO annotation, though it is a computational (IBA) rather than experimental annotation."
  },
  "important_caveats": [
    "The primary experimental subcellular location annotation is 'Mitochondrion' (ECO:0000269, experimental), while the 'cytoplasm' annotation is IBA:GO_Central (computational inference). The author's answer relies on the computational GO annotation and the ontology parent-child relationship.",
    "The question asks for the 'primary' cellular component, yet the most precise answer (mitochondrion) is not offered. Cytoplasm is correct only as the broader parent category.",
    "The protein is from Plasmodium falciparum, an apicomplexan with unusual organelle biology; however, the reasoning for choosing C does not depend on Plasmodium-specific knowledge.",
    "The GO:0000181 term in option D is obsolete (replaced by GO:0022627), which further weakens D as a viable distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the true primary location is mitochondrion (not offered), among the four given choices only C (cytoplasm) is defensible. A, B, and D are eliminated by clear sequence and structural reasoning. The GO hierarchy makes cytoplasm the correct parent term for a mitochondrial protein when mitochondrion is unavailable as a choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for O97297 (PfIscA2) carries a GO:0005737 (cytoplasm) annotation with IBA:GO_Central evidence (C6/H4). The primary experimental SUBCELLULAR LOCATION is 'Mitochondrion' (SL-0173, ECO:0000269), but mitochondrion is part_of cytoplasm in the GO ontology (GO3). Since 'mitochondrion' is not among the offered choices, 'cytoplasm' (C) is the correct parent category in the GO hierarchy and is directly annotated in the database. The author's answer C is supported by the existing GO annotation, though it is a computational (IBA) rather than experimental annotation.",
    "evidence_ids": ["C6", "H4", "GO3", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish C from the alternatives through multiple converging lines of reasoning: (1) Elimination of A (ER): the sequence lacks a cleavable N-terminal signal peptide and transmembrane domains characteristic of ER-resident or secreted proteins. (2) Elimination of D (cytosolic small ribosomal subunit): the protein is 404 aa with a composition inconsistent with ribosomal proteins (which are typically smaller, highly basic, and have distinct RNA-binding motifs). (3) Elimination of B (perinuclear region of cytoplasm): this is a highly specific annotation requiring evidence of perinuclear enrichment; no such targeting signal is apparent. (4) Positive support for C: the C-terminal 'ICPCG' motif (Cys-Pro-Cys) is a hallmark of Fe-S cluster-binding proteins in the ISC pathway. In eukaryotes, ISC proteins are mitochondrial, but mitochondrion is part_of cytoplasm in GO. Since mitochondrion is not offered, cytoplasm is the correct encompassing term. Additionally, the overall sequence composition (high Asn content, no strong organelle-targeting signals for ER or nucleus) is consistent with a broadly cytoplasmic/intracellular localization.",
    "missing_item_specific_fact": "",
    "reason": "The combination of motif recognition (Fe-S cluster CXXC motifs indicating ISC pathway), elimination of incompatible alternatives (no ER signal peptide, not a ribosomal protein, no perinuclear-specific features), and the GO ontology hierarchy (mitochondrion ⊂ cytoplasm) provides a concrete transferable argument that meaningfully distinguishes C from the other three options without requiring memorization of this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the true primary location is mitochondrion (not offered), among the four given choices only C (cytoplasm) is defensible. A, B, and D are eliminated by clear sequence and structural reasoning. The GO hierarchy makes cytoplasm the correct parent term for a mitochondrial protein when mitochondrion is unavailable as a choice."
  },
  "important_caveats": [
    "The primary experimental subcellular location annotation is 'Mitochondrion' (ECO:0000269, experimental), while the 'cytoplasm' annotation is IBA:GO_Central (computational inference). The author's answer relies on the computational GO annotation and the ontology parent-child relationship.",
    "The question asks for the 'primary' cellular component, yet the most precise answer (mitochondrion) is not offered. Cytoplasm is correct only as the broader parent category.",
    "The protein is from Plasmodium falciparum, an apicomplexan with unusual organelle biology; however, the reasoning for choosing C does not depend on Plasmodium-specific knowledge.",
    "The GO:0000181 term in option D is obsolete (replaced by GO:0022627), which further weakens D as a viable distractor."
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
  "benchmark_sequence_length": 404,
  "benchmark_sequence_sha256": "1acf9cb41bfaea25908ce91d1c41f1ea1fac9268947da35d853e46258389584e",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 404,
  "current_source_sequence_sha256": "1acf9cb41bfaea25908ce91d1c41f1ea1fac9268947da35d853e46258389584e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 128,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O97297",
  "selected_historical_entry_version": 128,
  "selected_historical_record_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "selected_historical_source_sequence_length": 404,
  "selected_historical_source_sequence_sha256": "1acf9cb41bfaea25908ce91d1c41f1ea1fac9268947da35d853e46258389584e",
  "selected_historical_version": {
    "accession": "O97297",
    "database": "Swiss-Prot",
    "entryVersion": 128,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCA2_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O97297\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Iron-sulfur assembly protein IscA2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIscA2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"id\":\"SL-0173\",\"value\":\"Mitochondrion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005739\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrion\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H1",
  "excerpt": "ID   ISCA2_PLAF7             Reviewed;         404 AA.\nAC   O97297;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-1999, sequence version 1.\nDT   28-JAN-2026, entry version 128.\nDE   RecName: Full=Iron-sulfur assembly protein IscA2 {ECO:0000305};\nDE            Short=PfIscA2 {ECO:0000303|PubMed:34032321};\nGN   Name=IscA2 {ECO:0000305};\nGN   ORFNames=PF3D7_0322500 {ECO:0000312|EMBL:CAB39044.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:34032321}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005739; C:mitochondrion; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000181\nname: obsolete cytosolic small ribosomal subunit\nnamespace: cellular_component\ndef: \"OBSOLETE. (Was not defined before being made obsolete).\" [GOC:ai]\ncomment: This term was made obsolete because more specific children exist.\nsynonym: \"cytosolic small ribosomal subunit\" EXACT []\nis_obsolete: true\nconsider: GO:0022627\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000181",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1801-1810",
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
  "excerpt": "[Term]\nid: GO:0005739\nname: mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration.\" [GOC:giardia, ISBN:0198506732]\ncomment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"mitochondria\" EXACT []\nxref: NIF_Subcellular:sao1860313010\nxref: Wikipedia:Mitochondrion\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005739",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58975-58998",
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
  "excerpt": "[Term]\nid: GO:0005783\nname: endoplasmic reticulum\nnamespace: cellular_component\ndef: \"The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached).\" [ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"ER\" EXACT []\nxref: NIF_Subcellular:sao1036339110\nxref: Wikipedia:Endoplasmic_reticulum\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59450-59472",
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
  "excerpt": "[Term]\nid: GO:0022627\nname: cytosolic small ribosomal subunit\nnamespace: cellular_component\nalt_id: GO:0005843\nalt_id: GO:0009283\nalt_id: GO:0030499\nalt_id: GO:0030873\ndef: \"The small subunit of a ribosome located in the cytosol.\" [GOC:mtg_sensu]\nsynonym: \"30S ribosomal subunit\" NARROW []\nsynonym: \"40S ribosomal subunit\" NARROW []\nsynonym: \"eukaryotic ribosomal SSU\" NARROW []\nsynonym: \"prokaryotic small ribosomal subunit\" NARROW []\nis_a: GO:0015935 ! small ribosomal subunit\nrelationship: part_of GO:0022626 ! cytosolic ribosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0022627",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 160585-160600",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0048471\nname: perinuclear region of cytoplasm\nnamespace: cellular_component\ndef: \"Cytoplasm situated near, or occurring around, the nucleus.\" [GOC:jid]\ncomment: Note that this term should not be confused with the cellular component term 'nuclear membrane lumen ; GO:0005641', which has the synonym 'perinuclear space'.\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048471",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 303515-303523",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
