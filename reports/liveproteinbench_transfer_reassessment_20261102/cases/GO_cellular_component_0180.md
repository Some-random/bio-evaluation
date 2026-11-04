# GO_cellular_component_0180

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0180.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIEKSNNPFLSIDPIVERTKSNGEGLPLLSEKTKKGFDFTQIVVYLVGLSDGLTHLASLAIYYLFKDYFRLTPYQVSLILMYPYIPFILKPVIALITDSFSIFGMRRKPYLFLFSLFQSLNFLALAFLNLSVIQASLILFFISLCASFCTTVAEALVVESSMGQTYSQGTNKVTEFIASKAIGSLSVAYFSGYFLEKMPREYIFIATSIFPLIISLSCLFLKEKEYSTNRNIFNQLSDLIKFINTPIFLGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIIYRVFLKNCSLRKTLIITTLVSFPIYISPIILTEHINKFLGISNELFVLSGGFLIEAITEIQLLPLFILTANICQPGLEASVFATILSVKNLGSLTKKGTSSFITYLMKIDSYNFDNLSLYILTCGFFLLFSLTLVPLLPNEEHIEKLKNKETSKG

[Multiple Choices]
A. lipid droplet
B. cytoplasmic vesicle
C. plasma membrane
D. endoplasmic reticulum
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

> The sequence-matched annotation reports plasma-membrane localization and some intracellular vesicular localization; the plasma membrane is specifically supported by a GO annotation with experimental evidence. This supports C as the primary location, though it does not imply exclusive localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an extensive multi-pass transmembrane architecture, consistent with an integral membrane transporter. As a transferable biological pattern, nutrient transporters commonly reside at the cell surface, making plasma membrane a reasonable choice over lipid droplets and a more likely primary location than ER or intracellular vesicles. This is probabilistic: the sequence alone does not establish the transporter’s substrate or localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The membrane-protein architecture and general cell-surface transporter pattern provide a meaningful basis for choosing plasma membrane among these options, even though they do not prove the exact localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence allows some vesicular localization, but describes it as secondary to plasma-membrane localization; it does not make cytoplasmic vesicle equally defensible as the primary location.


### Important caveats

- Reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- Localization is not exclusive: some intracellular vesicular localization is also reported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an extensive multi-pass transmembrane architecture, consistent with an integral membrane transporter. As a transferable biological pattern, nutrient transporters commonly reside at the cell surface, making plasma membrane a reasonable choice over lipid droplets and a more likely primary location than ER or intracellular vesicles. This is probabilistic: the sequence alone does not establish the transporter’s substrate or localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The membrane-protein architecture and general cell-surface transporter pattern provide a meaningful basis for choosing plasma membrane among these options, even though they do not prove the exact localization."
  },
  "case_id": "GO_cellular_component_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation reports plasma-membrane localization and some intracellular vesicular localization; the plasma membrane is specifically supported by a GO annotation with experimental evidence. This supports C as the primary location, though it does not imply exclusive localization."
  },
  "important_caveats": [
    "Reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "Localization is not exclusive: some intracellular vesicular localization is also reported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence allows some vesicular localization, but describes it as secondary to plasma-membrane localization; it does not make cytoplasmic vesicle equally defensible as the primary location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation reports plasma-membrane localization and some intracellular vesicular localization; the plasma membrane is specifically supported by a GO annotation with experimental evidence. This supports C as the primary location, though it does not imply exclusive localization.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an extensive multi-pass transmembrane architecture, consistent with an integral membrane transporter. As a transferable biological pattern, nutrient transporters commonly reside at the cell surface, making plasma membrane a reasonable choice over lipid droplets and a more likely primary location than ER or intracellular vesicles. This is probabilistic: the sequence alone does not establish the transporter’s substrate or localization.",
    "missing_item_specific_fact": "",
    "reason": "The membrane-protein architecture and general cell-surface transporter pattern provide a meaningful basis for choosing plasma membrane among these options, even though they do not prove the exact localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence allows some vesicular localization, but describes it as secondary to plasma-membrane localization; it does not make cytoplasmic vesicle equally defensible as the primary location."
  },
  "important_caveats": [
    "Reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "Localization is not exclusive: some intracellular vesicular localization is also reported."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IIK1 (Folate transporter 2, PfFT2) is annotated with experimental evidence (ECO:0000269, PubMed:21998306, a 2011 JBC paper) stating localization to the plasma membrane (Cell membrane, Multi-pass membrane protein). The GO annotation GO:0005886 (plasma membrane) carries IDA:GeneDB evidence. The note mentions 'plasma membrane and some intracellular vesicular structures,' confirming plasma membrane as the primary location. Both current (C5, C6) and historical (H3, H4) records confirm this.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 455-aa sequence encodes a multi-pass membrane protein with approximately 11-12 hydrophobic TM segments arranged in an alternating topology, consistent with the Major Facilitator Superfamily (MFS) of secondary active transporters. This architecture immediately eliminates lipid droplet (A), which is a phospholipid monolayer organelle whose associated proteins use amphipathic helices, not multi-pass TM domains. Among the remaining three membrane-bound compartments (B, C, D), the MFS transporter family is overwhelmingly associated with plasma membrane nutrient uptake (e.g., GLUT sugar transporters, bacterial sugar/amino-acid permeases). The biological logic of folate transport in Plasmodium—which cannot synthesize folate de novo and must import it from the host erythrocyte—requires a plasma membrane localization for external nutrient acquisition. ER-resident transporters (e.g., G6PT) typically carry ER-targeting signal peptides or KDEL/HDEL retention motifs absent here. Vesicular transporters (e.g., VMAT, VGLUT) transport substrates INTO vesicles rather than importing from the extracellular space. The combination of MFS-like 12-TM architecture, absence of ER retention signals, and the nutrient-import function of folate transporters provides a credible inference pathway to plasma membrane (C) over ER (D) or vesicle (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the multi-pass membrane architecture and MFS-like topology can apply family-level knowledge (MFS transporters are predominantly plasma membrane nutrient importers) and biological reasoning (folate must be imported from outside the cell) to distinguish C from the other options. The sequence lacks ER retention signals, and the transporter function logic disfavors vesicular localization. While not mathematically certain, this constitutes a defensible probabilistic inference from transferable knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt note mentions 'some intracellular vesicular structures' as a secondary localization, the question asks for the PRIMARY cellular component. The primary experimental localization is unambiguously the plasma membrane. The multi-pass TM architecture excludes lipid droplet, and the transporter-import logic plus absence of ER signals make B and D less defensible as the primary compartment.


### Important caveats

- The UniProt note mentions secondary localization to 'some intracellular vesicular structures,' but the question asks for the primary component, making C the correct choice.
- MFS family assignment is inferred from hydrophobicity pattern and approximate TM count (~12); without structural data, the family assignment is probabilistic rather than definitive.
- The organism (Plasmodium falciparum) and protein name (Folate transporter 2) are reviewer-only information not available to the evaluated model; the reasoning above relies on sequence-derived features and general biology.
- Distinguishing plasma membrane from ER for multi-pass membrane proteins purely from sequence is inherently uncertain; the argument relies on the convergence of multiple weak-to-moderate signals (MFS topology, absence of ER signals, nutrient-import biology).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 455-aa sequence encodes a multi-pass membrane protein with approximately 11-12 hydrophobic TM segments arranged in an alternating topology, consistent with the Major Facilitator Superfamily (MFS) of secondary active transporters. This architecture immediately eliminates lipid droplet (A), which is a phospholipid monolayer organelle whose associated proteins use amphipathic helices, not multi-pass TM domains. Among the remaining three membrane-bound compartments (B, C, D), the MFS transporter family is overwhelmingly associated with plasma membrane nutrient uptake (e.g., GLUT sugar transporters, bacterial sugar/amino-acid permeases). The biological logic of folate transport in Plasmodium—which cannot synthesize folate de novo and must import it from the host erythrocyte—requires a plasma membrane localization for external nutrient acquisition. ER-resident transporters (e.g., G6PT) typically carry ER-targeting signal peptides or KDEL/HDEL retention motifs absent here. Vesicular transporters (e.g., VMAT, VGLUT) transport substrates INTO vesicles rather than importing from the extracellular space. The combination of MFS-like 12-TM architecture, absence of ER retention signals, and the nutrient-import function of folate transporters provides a credible inference pathway to plasma membrane (C) over ER (D) or vesicle (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the multi-pass membrane architecture and MFS-like topology can apply family-level knowledge (MFS transporters are predominantly plasma membrane nutrient importers) and biological reasoning (folate must be imported from outside the cell) to distinguish C from the other options. The sequence lacks ER retention signals, and the transporter function logic disfavors vesicular localization. While not mathematically certain, this constitutes a defensible probabilistic inference from transferable knowledge."
  },
  "case_id": "GO_cellular_component_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IIK1 (Folate transporter 2, PfFT2) is annotated with experimental evidence (ECO:0000269, PubMed:21998306, a 2011 JBC paper) stating localization to the plasma membrane (Cell membrane, Multi-pass membrane protein). The GO annotation GO:0005886 (plasma membrane) carries IDA:GeneDB evidence. The note mentions 'plasma membrane and some intracellular vesicular structures,' confirming plasma membrane as the primary location. Both current (C5, C6) and historical (H3, H4) records confirm this."
  },
  "important_caveats": [
    "The UniProt note mentions secondary localization to 'some intracellular vesicular structures,' but the question asks for the primary component, making C the correct choice.",
    "MFS family assignment is inferred from hydrophobicity pattern and approximate TM count (~12); without structural data, the family assignment is probabilistic rather than definitive.",
    "The organism (Plasmodium falciparum) and protein name (Folate transporter 2) are reviewer-only information not available to the evaluated model; the reasoning above relies on sequence-derived features and general biology.",
    "Distinguishing plasma membrane from ER for multi-pass membrane proteins purely from sequence is inherently uncertain; the argument relies on the convergence of multiple weak-to-moderate signals (MFS topology, absence of ER signals, nutrient-import biology)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt note mentions 'some intracellular vesicular structures' as a secondary localization, the question asks for the PRIMARY cellular component. The primary experimental localization is unambiguously the plasma membrane. The multi-pass TM architecture excludes lipid droplet, and the transporter-import logic plus absence of ER signals make B and D less defensible as the primary compartment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IIK1 (Folate transporter 2, PfFT2) is annotated with experimental evidence (ECO:0000269, PubMed:21998306, a 2011 JBC paper) stating localization to the plasma membrane (Cell membrane, Multi-pass membrane protein). The GO annotation GO:0005886 (plasma membrane) carries IDA:GeneDB evidence. The note mentions 'plasma membrane and some intracellular vesicular structures,' confirming plasma membrane as the primary location. Both current (C5, C6) and historical (H3, H4) records confirm this.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 455-aa sequence encodes a multi-pass membrane protein with approximately 11-12 hydrophobic TM segments arranged in an alternating topology, consistent with the Major Facilitator Superfamily (MFS) of secondary active transporters. This architecture immediately eliminates lipid droplet (A), which is a phospholipid monolayer organelle whose associated proteins use amphipathic helices, not multi-pass TM domains. Among the remaining three membrane-bound compartments (B, C, D), the MFS transporter family is overwhelmingly associated with plasma membrane nutrient uptake (e.g., GLUT sugar transporters, bacterial sugar/amino-acid permeases). The biological logic of folate transport in Plasmodium—which cannot synthesize folate de novo and must import it from the host erythrocyte—requires a plasma membrane localization for external nutrient acquisition. ER-resident transporters (e.g., G6PT) typically carry ER-targeting signal peptides or KDEL/HDEL retention motifs absent here. Vesicular transporters (e.g., VMAT, VGLUT) transport substrates INTO vesicles rather than importing from the extracellular space. The combination of MFS-like 12-TM architecture, absence of ER retention signals, and the nutrient-import function of folate transporters provides a credible inference pathway to plasma membrane (C) over ER (D) or vesicle (B).",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the multi-pass membrane architecture and MFS-like topology can apply family-level knowledge (MFS transporters are predominantly plasma membrane nutrient importers) and biological reasoning (folate must be imported from outside the cell) to distinguish C from the other options. The sequence lacks ER retention signals, and the transporter function logic disfavors vesicular localization. While not mathematically certain, this constitutes a defensible probabilistic inference from transferable knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt note mentions 'some intracellular vesicular structures' as a secondary localization, the question asks for the PRIMARY cellular component. The primary experimental localization is unambiguously the plasma membrane. The multi-pass TM architecture excludes lipid droplet, and the transporter-import logic plus absence of ER signals make B and D less defensible as the primary compartment."
  },
  "important_caveats": [
    "The UniProt note mentions secondary localization to 'some intracellular vesicular structures,' but the question asks for the primary component, making C the correct choice.",
    "MFS family assignment is inferred from hydrophobicity pattern and approximate TM count (~12); without structural data, the family assignment is probabilistic rather than definitive.",
    "The organism (Plasmodium falciparum) and protein name (Folate transporter 2) are reviewer-only information not available to the evaluated model; the reasoning above relies on sequence-derived features and general biology.",
    "Distinguishing plasma membrane from ER for multi-pass membrane proteins purely from sequence is inherently uncertain; the argument relies on the convergence of multiple weak-to-moderate signals (MFS topology, absence of ER signals, nutrient-import biology)."
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
  "benchmark_sequence_length": 455,
  "benchmark_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 455,
  "current_source_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IIK1",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "selected_historical_source_sequence_length": 455,
  "selected_historical_source_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "selected_historical_version": {
    "accession": "Q8IIK1",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FT2_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IIK1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"Folate transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"PfFT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"In intraerythrocytic stage parasites, localizes to the plasma membrane and some intracellular vesicular structures\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Salcedo-Sora J.E.\",\"Ochong E.\",\"Beveridge S.\",\"Johnson D.\",\"Nzila A.\",\"Biagini G.A.\",\"Stocks P.A.\",\"O'Neill P.M.\",\"Krishna S.\",\"Bray P.G.\",\"Ward S.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21998306\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.286054\"}],\"citationType\":\"journal article\",\"firstPage\":\"44659\",\"id\":\"21998306\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"44668\",\"publicationDate\":\"2011\",\"title\":\"The molecular basis of folate salvage in Plasmodium falciparum: characterization of two folate transporters.\",\"volume\":\"286\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   FT2_PLAF7               Reviewed;         455 AA.\nAC   Q8IIK1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Folate transporter 2 {ECO:0000303|PubMed:21998306};\nDE            Short=PfFT2 {ECO:0000303|PubMed:21998306};\nGN   ORFNames=PF3D7_1116500 {ECO:0000312|EMBL:CZT98826.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, ACTIVITY REGULATION, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=21998306; DOI=10.1074/jbc.m111.286054;\nRA   Salcedo-Sora J.E., Ochong E., Beveridge S., Johnson D., Nzila A.,\nRA   Biagini G.A., Stocks P.A., O'Neill P.M., Krishna S., Bray P.G., Ward S.A.;\nRT   \"The molecular basis of folate salvage in Plasmodium falciparum:\nRT   characterization of two folate transporters.\";\nRL   J. Biol. Chem. 286:44659-44668(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:21998306};\nCC       Multi-pass membrane protein {ECO:0000255}. Note=In intraerythrocytic\nCC       stage parasites, localizes to the plasma membrane and some\nCC       intracellular vesicular structures. {ECO:0000269|PubMed:21998306}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
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

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0031410\nname: cytoplasmic vesicle\nnamespace: cellular_component\nalt_id: GO:0016023\ndef: \"A vesicle found in the cytoplasm of a cell.\" [GOC:ai, GOC:mah, GOC:vesicles]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_yeast\nsynonym: \"cytoplasmic membrane bounded vesicle\" RELATED []\nsynonym: \"cytoplasmic membrane-enclosed vesicle\" RELATED []\nsynonym: \"cytoplasmic, membrane-bounded vesicle\" RELATED []\nxref: NIF_Subcellular:sao180601769\nis_a: GO:0097708 ! intracellular vesicle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031410",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 176239-176257",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
