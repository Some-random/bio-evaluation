# GO_cellular_component_0005

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0005.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — extracellular region

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTKLTLTVALVSALLASGASAQQPTGTGNGPDPRATTDLNRNQPTKSWTQWQPKATYAFSQLPDQYMGANRIESGEGGQPGGEPQSGYNTCARNTWNQDSKCQTAWINSLEDFCLWAPAEYGTVGEKERSGVAYCTTDRHGTRLIPDGTIQGAHFVRTRDYVQVTGVGDFTSILIPDGDDGGEFDPHGADDLGNPIGGIVYTTANPASNGEPFFVSEWTNFMSYNQFCLRACWGERAAAQCEHIYDVMGCRWNIPANYEPGVFETCDGDIGQLQGIYSGSTFRQGDPVTPPAHPAPSSSQCSSVSTIGHGLLARSASASTSSVETSSSSAASSAATDSSASTNSASSMTRVTNSAVSTNVGSGTGSGSGSGSGSGSGSGSGSSSGSSSSGSSSNTQGAASSASSLTISVGLAGLVAIGAAAFAL

[Multiple Choices]
A. acrosomal membrane
B. extracellular region
C. viral envelope
D. fungal-type cell wall
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

> The sequence matches the protein in the source record. That record reports secretion and an experimentally supported GO annotation to extracellular region; it also reports cell-membrane localization, so extracellular region is supported but not the only reported localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic segment consistent with a secretion signal and a hydrophobic segment near the C terminus consistent with membrane anchoring. Together these features support entry into the secretory pathway and an extracellular or cell-surface destination, making B more plausible than the acrosomal or viral alternatives. Secretion alone does not prove a fungal cell-wall location; that would require additional localization or retention evidence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence-based inference meaningfully favors the extracellular option among those offered. It is probabilistic, and the sequence does not by itself resolve the protein’s precise distribution between extracellular and membrane-associated locations.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence suggests secretory-pathway targeting and possible membrane anchoring, but provides no specific evidence for fungal cell-wall localization. The unlisted membrane location complicates the word “primary” without making another offered choice equally supported.


### Important caveats

- The source record supports both extracellular and plasma-membrane localization; the benchmark asks for a single primary component.
- The source annotation is evidence about this exact protein, not evidence available to the model from the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic segment consistent with a secretion signal and a hydrophobic segment near the C terminus consistent with membrane anchoring. Together these features support entry into the secretory pathway and an extracellular or cell-surface destination, making B more plausible than the acrosomal or viral alternatives. Secretion alone does not prove a fungal cell-wall location; that would require additional localization or retention evidence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-based inference meaningfully favors the extracellular option among those offered. It is probabilistic, and the sequence does not by itself resolve the protein’s precise distribution between extracellular and membrane-associated locations."
  },
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein in the source record. That record reports secretion and an experimentally supported GO annotation to extracellular region; it also reports cell-membrane localization, so extracellular region is supported but not the only reported localization."
  },
  "important_caveats": [
    "The source record supports both extracellular and plasma-membrane localization; the benchmark asks for a single primary component.",
    "The source annotation is evidence about this exact protein, not evidence available to the model from the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence suggests secretory-pathway targeting and possible membrane anchoring, but provides no specific evidence for fungal cell-wall localization. The unlisted membrane location complicates the word “primary” without making another offered choice equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein in the source record. That record reports secretion and an experimentally supported GO annotation to extracellular region; it also reports cell-membrane localization, so extracellular region is supported but not the only reported localization.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic segment consistent with a secretion signal and a hydrophobic segment near the C terminus consistent with membrane anchoring. Together these features support entry into the secretory pathway and an extracellular or cell-surface destination, making B more plausible than the acrosomal or viral alternatives. Secretion alone does not prove a fungal cell-wall location; that would require additional localization or retention evidence.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-based inference meaningfully favors the extracellular option among those offered. It is probabilistic, and the sequence does not by itself resolve the protein’s precise distribution between extracellular and membrane-associated locations."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence suggests secretory-pathway targeting and possible membrane anchoring, but provides no specific evidence for fungal cell-wall localization. The unlisted membrane location complicates the word “primary” without making another offered choice equally supported."
  },
  "important_caveats": [
    "The source record supports both extracellular and plasma-membrane localization; the benchmark asks for a single primary component.",
    "The source annotation is evidence about this exact protein, not evidence available to the model from the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0D1E921) directly annotates this protein with GO:0005576 (extracellular region) with IDA evidence (Inferred from Direct Assay, PubMed:38742361). The protein is also described as 'Secreted' in the subcellular location comment. The experimental paper (Pejenaute-Ochoa et al. 2024, New Phytol.) provides direct evidence for this localization. The expected answer B is directly supported by the database annotation with experimental evidence code.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MTKLTLTVALVSALLASGASA' exhibits a classic signal peptide architecture: a short positively-charged N-region (MTK), a hydrophobic H-region (LTLTVALVSALLASGASA), and a small-residue C-region at the cleavage site. This is a universally conserved feature of proteins entering the secretory pathway, directing them toward the extracellular space. Among the four options: (A) acrosomal membrane is specific to animal sperm cells and has no relevance to a protein with this architecture; (C) viral envelope requires viral origin and characteristic viral glycoprotein motifs absent here; (D) fungal-type cell wall proteins typically possess cell-wall anchoring domains (LysM, chitin-binding, WSC domains) or GPI-anchor signals with a specific ω-site, none of which are evident. The C-terminal hydrophobic stretch 'LTISVGLAGLVAIGAAAFAL' is consistent with a single-pass TM anchor (as annotated) but does not resemble a GPI anchor signal or cell-wall binding domain. The signal peptide → secretion pathway argument is a well-established, transferable principle in cell biology that meaningfully distinguishes B (extracellular region) from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The N-terminal signal peptide is a directly observable sequence feature that invokes the universal secretory pathway logic. A knowledgeable model can recognize this feature and apply the general principle that signal peptide-containing proteins are secreted to the extracellular space, which directly maps to GO:0005576. The absence of cell-wall anchoring domains, viral motifs, or sperm-specific features allows elimination of A, C, and D through standard biological reasoning applicable to any protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the protein is also annotated as a plasma membrane protein (GO:0005886), this option is not among the choices. Between B and D, the signal peptide pattern and absence of fungal cell-wall anchoring domains make B clearly preferable. The C-terminal hydrophobic stretch could theoretically suggest membrane association, but among the four offered choices, 'extracellular region' is the best fit for a secreted protein, and 'fungal-type cell wall' would require specific wall-binding features not present.


### Important caveats

- The protein is annotated as both 'Secreted' and 'Cell membrane; Single-pass membrane protein' in UniProt. The GO extracellular region annotation (IDA) and the GO plasma membrane annotation (IDA) coexist. The question asks for the 'primary' compartment, and the extracellular region annotation is the one matching option B.
- The GO term definition for extracellular region notes it is intended for gene products 'not attached to the cell surface,' yet this protein is also a membrane protein. The IDA annotation to GO:0005576 from the primary paper resolves this in favor of the extracellular annotation.
- The protein's alternative name 'Remodeling of fungal cell wall 1' refers to its biological function (remodeling the wall) rather than its physical location within the wall, which could mislead a model toward option D.
- The organism (Mycosarcoma maydis, a fungus) is not stated in the original input; a model must infer fungal origin from sequence features or not use it at all.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MTKLTLTVALVSALLASGASA' exhibits a classic signal peptide architecture: a short positively-charged N-region (MTK), a hydrophobic H-region (LTLTVALVSALLASGASA), and a small-residue C-region at the cleavage site. This is a universally conserved feature of proteins entering the secretory pathway, directing them toward the extracellular space. Among the four options: (A) acrosomal membrane is specific to animal sperm cells and has no relevance to a protein with this architecture; (C) viral envelope requires viral origin and characteristic viral glycoprotein motifs absent here; (D) fungal-type cell wall proteins typically possess cell-wall anchoring domains (LysM, chitin-binding, WSC domains) or GPI-anchor signals with a specific ω-site, none of which are evident. The C-terminal hydrophobic stretch 'LTISVGLAGLVAIGAAAFAL' is consistent with a single-pass TM anchor (as annotated) but does not resemble a GPI anchor signal or cell-wall binding domain. The signal peptide → secretion pathway argument is a well-established, transferable principle in cell biology that meaningfully distinguishes B (extracellular region) from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal signal peptide is a directly observable sequence feature that invokes the universal secretory pathway logic. A knowledgeable model can recognize this feature and apply the general principle that signal peptide-containing proteins are secreted to the extracellular space, which directly maps to GO:0005576. The absence of cell-wall anchoring domains, viral motifs, or sperm-specific features allows elimination of A, C, and D through standard biological reasoning applicable to any protein."
  },
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0D1E921) directly annotates this protein with GO:0005576 (extracellular region) with IDA evidence (Inferred from Direct Assay, PubMed:38742361). The protein is also described as 'Secreted' in the subcellular location comment. The experimental paper (Pejenaute-Ochoa et al. 2024, New Phytol.) provides direct evidence for this localization. The expected answer B is directly supported by the database annotation with experimental evidence code."
  },
  "important_caveats": [
    "The protein is annotated as both 'Secreted' and 'Cell membrane; Single-pass membrane protein' in UniProt. The GO extracellular region annotation (IDA) and the GO plasma membrane annotation (IDA) coexist. The question asks for the 'primary' compartment, and the extracellular region annotation is the one matching option B.",
    "The GO term definition for extracellular region notes it is intended for gene products 'not attached to the cell surface,' yet this protein is also a membrane protein. The IDA annotation to GO:0005576 from the primary paper resolves this in favor of the extracellular annotation.",
    "The protein's alternative name 'Remodeling of fungal cell wall 1' refers to its biological function (remodeling the wall) rather than its physical location within the wall, which could mislead a model toward option D.",
    "The organism (Mycosarcoma maydis, a fungus) is not stated in the original input; a model must infer fungal origin from sequence features or not use it at all."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein is also annotated as a plasma membrane protein (GO:0005886), this option is not among the choices. Between B and D, the signal peptide pattern and absence of fungal cell-wall anchoring domains make B clearly preferable. The C-terminal hydrophobic stretch could theoretically suggest membrane association, but among the four offered choices, 'extracellular region' is the best fit for a secreted protein, and 'fungal-type cell wall' would require specific wall-binding features not present."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0D1E921) directly annotates this protein with GO:0005576 (extracellular region) with IDA evidence (Inferred from Direct Assay, PubMed:38742361). The protein is also described as 'Secreted' in the subcellular location comment. The experimental paper (Pejenaute-Ochoa et al. 2024, New Phytol.) provides direct evidence for this localization. The expected answer B is directly supported by the database annotation with experimental evidence code.",
    "evidence_ids": ["C6", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MTKLTLTVALVSALLASGASA' exhibits a classic signal peptide architecture: a short positively-charged N-region (MTK), a hydrophobic H-region (LTLTVALVSALLASGASA), and a small-residue C-region at the cleavage site. This is a universally conserved feature of proteins entering the secretory pathway, directing them toward the extracellular space. Among the four options: (A) acrosomal membrane is specific to animal sperm cells and has no relevance to a protein with this architecture; (C) viral envelope requires viral origin and characteristic viral glycoprotein motifs absent here; (D) fungal-type cell wall proteins typically possess cell-wall anchoring domains (LysM, chitin-binding, WSC domains) or GPI-anchor signals with a specific ω-site, none of which are evident. The C-terminal hydrophobic stretch 'LTISVGLAGLVAIGAAAFAL' is consistent with a single-pass TM anchor (as annotated) but does not resemble a GPI anchor signal or cell-wall binding domain. The signal peptide → secretion pathway argument is a well-established, transferable principle in cell biology that meaningfully distinguishes B (extracellular region) from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal signal peptide is a directly observable sequence feature that invokes the universal secretory pathway logic. A knowledgeable model can recognize this feature and apply the general principle that signal peptide-containing proteins are secreted to the extracellular space, which directly maps to GO:0005576. The absence of cell-wall anchoring domains, viral motifs, or sperm-specific features allows elimination of A, C, and D through standard biological reasoning applicable to any protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein is also annotated as a plasma membrane protein (GO:0005886), this option is not among the choices. Between B and D, the signal peptide pattern and absence of fungal cell-wall anchoring domains make B clearly preferable. The C-terminal hydrophobic stretch could theoretically suggest membrane association, but among the four offered choices, 'extracellular region' is the best fit for a secreted protein, and 'fungal-type cell wall' would require specific wall-binding features not present."
  },
  "important_caveats": [
    "The protein is annotated as both 'Secreted' and 'Cell membrane; Single-pass membrane protein' in UniProt. The GO extracellular region annotation (IDA) and the GO plasma membrane annotation (IDA) coexist. The question asks for the 'primary' compartment, and the extracellular region annotation is the one matching option B.",
    "The GO term definition for extracellular region notes it is intended for gene products 'not attached to the cell surface,' yet this protein is also a membrane protein. The IDA annotation to GO:0005576 from the primary paper resolves this in favor of the extracellular annotation.",
    "The protein's alternative name 'Remodeling of fungal cell wall 1' refers to its biological function (remodeling the wall) rather than its physical location within the wall, which could mislead a model toward option D.",
    "The organism (Mycosarcoma maydis, a fungus) is not stated in the original input; a model must infer fungal origin from sequence features or not use it at all."
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
  "benchmark_sequence_length": 424,
  "benchmark_sequence_sha256": "ecd8bcb54da5af6d4e36cc7f7a0f827ff0d4f6ec76497905d24506de9c2f5b68",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-04-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 424,
  "current_source_sequence_sha256": "ecd8bcb54da5af6d4e36cc7f7a0f827ff0d4f6ec76497905d24506de9c2f5b68",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 33,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0D1E921",
  "selected_historical_entry_version": 33,
  "selected_historical_record_sha256": "8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8",
  "selected_historical_source_sequence_length": 424,
  "selected_historical_source_sequence_sha256": "ecd8bcb54da5af6d4e36cc7f7a0f827ff0d4f6ec76497905d24506de9c2f5b68",
  "selected_historical_version": {
    "accession": "A0A0D1E921",
    "database": "Swiss-Prot",
    "entryVersion": 33,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ROW1_MYCMD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0D1E921\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-04-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Corn smut fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Ustilaginomycotina\",\"Ustilaginomycetes\",\"Ustilaginales\",\"Ustilaginales incertae sedis\",\"Mycosarcoma\"],\"scientificName\":\"Mycosarcoma maydis\",\"synonyms\":[\"Ustilago maydis\"],\"taxonId\":5270}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38742361\",\"source\":\"PubMed\"}],\"value\":\"Remodeling of fungal cell wall 1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Appressorium protein ROW1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38742361\",\"source\":\"PubMed\"}],\"value\":\"Localizes to the appressorium\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38742361\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9904\",\"value\":\"Single-pass membrane protein\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38742361\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38742361\",\"source\":\"PubMed\"}],\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38742361\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Pejenaute-Ochoa M.D.\",\"Tomas-Gallardo L.\",\"Ibeas J.I.\",\"Barrales R.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38742361\"},{\"database\":\"DOI\",\"id\":\"10.1111/nph.19798\"}],\"citationType\":\"journal article\",\"firstPage\":\"1101\",\"id\":\"38742361\",\"journal\":\"New Phytol.\",\"lastPage\":\"1122\",\"publicationDate\":\"2024\",\"title\":\"Row1, a member of a new family of conserved fungal proteins involved in infection, is required for appressoria functionality in Ustilago maydis.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:39.233517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0D1E921.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H1",
  "excerpt": "ID   ROW1_MYCMD              Reviewed;         424 AA.\nAC   A0A0D1E921;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-APR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 33.\nDE   RecName: Full=Appressorium protein ROW1 {ECO:0000305};\nDE   AltName: Full=Remodeling of fungal cell wall 1 {ECO:0000303|PubMed:38742361};\nDE   Flags: Precursor;\nGN   Name=ROW1 {ECO:0000303|PubMed:38742361};\nGN   ORFNames=UMAG_00309 {ECO:0000312|EMBL:KIS71881.1};\nOS   Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Ustilaginomycotina;\nOC   Ustilaginomycetes; Ustilaginales; Ustilaginaceae; Mycosarcoma.\nOX   NCBI_TaxID=5270;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:17.968792+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8",
  "url": "https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=38742361; DOI=10.1111/nph.19798;\nRA   Pejenaute-Ochoa M.D., Tomas-Gallardo L., Ibeas J.I., Barrales R.R.;\nRT   \"Row1, a member of a new family of conserved fungal proteins involved in\nRT   infection, is required for appressoria functionality in Ustilago maydis.\";\nRL   New Phytol. 243:1101-1122(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:17.968792+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8",
  "url": "https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:38742361};\nCC       Single-pass membrane protein {ECO:0000255}. Secreted\nCC       {ECO:0000269|PubMed:38742361}. Note=Localizes to the appressorium.\nCC       {ECO:0000269|PubMed:38742361}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:17.968792+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8",
  "url": "https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:17.968792+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8",
  "url": "https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:17.968792+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8",
  "url": "https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0002080\nname: acrosomal membrane\nnamespace: cellular_component\ndef: \"The membrane that surrounds the acrosomal lumen. The acrosome is a special type of lysosome in the head of a spermatozoon that contains acid hydrolases and is concerned with the breakdown of the outer membrane of the ovum during fertilization.\" [GOC:dph]\nis_a: GO:0030667 ! secretory granule membrane\nrelationship: part_of GO:0001669 ! acrosomal vesicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0002080",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 14812-14819",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0009277\nname: fungal-type cell wall\nnamespace: cellular_component\ndef: \"A rigid yet dynamic structure surrounding the plasma membrane that affords protection from stresses and contributes to cell morphogenesis, consisting of extensively cross-linked glycoproteins and carbohydrates. The glycoproteins may be modified with N- or O-linked carbohydrates, or glycosylphosphatidylinositol (GPI) anchors; the polysaccharides are primarily branched glucans, including beta-linked and alpha-linked glucans, and may also include chitin and other carbohydrate polymers, but not cellulose or pectin. Enzymes involved in cell wall biosynthesis are also found in the cell wall. Note that some forms of fungi develop a capsule outside of the cell wall under certain circumstances; this is considered a separate structure.\" [GOC:mcc, GOC:mtg_sensu, ISBN:3540601864, PMID:11283274, PMID:16927300, PMID:3319422, PMID:36266346]\nsynonym: \"beta-glucan-containing cell wall\" RELATED []\nsynonym: \"chitin- and beta-glucan-containing cell wall\" NARROW []\nsynonym: \"chitin-containing cell wall\" RELATED []\nis_a: GO:0005618 ! cell wall\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009277",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 94765-94774",
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
  "excerpt": "[Term]\nid: GO:0019031\nname: viral envelope\nnamespace: cellular_component\ndef: \"The lipid bilayer of a virion that surrounds the protein capsid. May also contain glycoproteins.\" [GOC:bf, GOC:bm, GOC:jl, ISBN:0781718325, Wikipedia:Viral_envelope]\nsubset: goslim_chembl\nsynonym: \"viral glycoprotein\" RELATED []\nsynonym: \"viral outside membrane\" EXACT []\nxref: Wikipedia:Viral_envelope\nis_a: GO:0036338 ! viral membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019031",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 144681-144691",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
