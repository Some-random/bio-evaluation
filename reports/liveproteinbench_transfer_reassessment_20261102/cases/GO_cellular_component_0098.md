# GO_cellular_component_0098

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0098.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSNITSTSIIFLLTGVPGLEAFHTWISIPFCFLSVTALLGNSLILFATITQPSLHEPMYYFLSMLSATDLGLSISTLVTMLSIFWFNVREISFNACLSHMFFIKFFTVMESSVLLAMAFDRFVAVSNPLRYAMILTDSRIAQIGVASVIRGLLMLTPMVALLIRLSYCHSQVLHHSYCYHPDVMKLSCTDTRINSAVGLTAMFSTVGVDLLLILLSYVLIIRTVLSVASPEERKETFSTCVSHIVAFAIYYIPLISLSIVHRFGKQAPAYVHTMIANTYLLISPLMNPVIYSVKTKQIRRAVIKILHSKET

[Multiple Choices]
A. plasma membrane
B. Dbf4-dependent protein kinase complex
C. chromatin
D. synapse
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

> The exact-sequence-matched UniProt record annotates the protein as a multipass membrane protein and assigns GO:0005886 (plasma membrane) with IBA evidence. These are computational or ontology-based annotations, not direct experimental localization evidence, but they support the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous long hydrophobic segments consistent with a seven-transmembrane GPCR. Transferable knowledge of GPCRs, including olfactory receptors, supports localization at the cell surface. That distinguishes plasma membrane from the nuclear chromatin and Dbf4-dependent kinase-complex options; the sequence offers no comparable basis for the specialized synapse option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The membrane-spanning pattern and GPCR-family inference provide a meaningful basis for choosing plasma membrane without needing this exact protein's database record. The sequence alone does not establish precise tissue distribution or prove experimental localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A multipass cell-surface receptor could occur in particular cellular contexts, but the offered synapse choice is more specific than the broad plasma-membrane localization supported by the sequence.


### Important caveats

- The supplied source annotations include computational or inferred evidence; they should not be described as direct experimental confirmation.
- Reviewer-only protein identity and annotations were not part of the original model input and are not used as the transferability argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic segments consistent with a seven-transmembrane GPCR. Transferable knowledge of GPCRs, including olfactory receptors, supports localization at the cell surface. That distinguishes plasma membrane from the nuclear chromatin and Dbf4-dependent kinase-complex options; the sequence offers no comparable basis for the specialized synapse option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The membrane-spanning pattern and GPCR-family inference provide a meaningful basis for choosing plasma membrane without needing this exact protein's database record. The sequence alone does not establish precise tissue distribution or prove experimental localization."
  },
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates the protein as a multipass membrane protein and assigns GO:0005886 (plasma membrane) with IBA evidence. These are computational or ontology-based annotations, not direct experimental localization evidence, but they support the expected answer."
  },
  "important_caveats": [
    "The supplied source annotations include computational or inferred evidence; they should not be described as direct experimental confirmation.",
    "Reviewer-only protein identity and annotations were not part of the original model input and are not used as the transferability argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A multipass cell-surface receptor could occur in particular cellular contexts, but the offered synapse choice is more specific than the broad plasma-membrane localization supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates the protein as a multipass membrane protein and assigns GO:0005886 (plasma membrane) with IBA evidence. These are computational or ontology-based annotations, not direct experimental localization evidence, but they support the expected answer.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic segments consistent with a seven-transmembrane GPCR. Transferable knowledge of GPCRs, including olfactory receptors, supports localization at the cell surface. That distinguishes plasma membrane from the nuclear chromatin and Dbf4-dependent kinase-complex options; the sequence offers no comparable basis for the specialized synapse option.",
    "missing_item_specific_fact": "",
    "reason": "The membrane-spanning pattern and GPCR-family inference provide a meaningful basis for choosing plasma membrane without needing this exact protein's database record. The sequence alone does not establish precise tissue distribution or prove experimental localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A multipass cell-surface receptor could occur in particular cellular contexts, but the offered synapse choice is more specific than the broad plasma-membrane localization supported by the sequence."
  },
  "important_caveats": [
    "The supplied source annotations include computational or inferred evidence; they should not be described as direct experimental confirmation.",
    "Reviewer-only protein identity and annotations were not part of the original model input and are not used as the transferability argument."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A3B3IT45, Olfactory receptor OR51C1) annotates the protein as 'Membrane; Multi-pass membrane protein' with GO:0005886 (plasma membrane) via IBA:GO_Central. The sequence itself displays canonical 7-transmembrane GPCR topology with the DRY motif (AFDRFVAVSN) and NPxxY motif (NPLRY), confirming a multi-pass membrane protein at the plasma membrane. The GO annotation evidence code is IBA (inferred by biological aspect), which is a computational/phylogenetic transfer rather than direct experimental localization, but it is consistent with the well-established biology of olfactory receptors as plasma membrane GPCRs.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately 7 hydrophobic stretches of ~20-25 residues characteristic of G-protein-coupled receptor (GPCR) transmembrane helices. Two hallmark GPCR motifs are identifiable: the DRY motif (D-R-Y in 'AFDRFVAVSN' around position 130) and the NPxxY motif (N-P-L-R-Y in 'SNPLRY' around position 145). GPCRs are, by definition and fundamental cell biology, integral plasma membrane proteins. This eliminates B (Dbf4-dependent kinase complex: no kinase catalytic domain, no nuclear localization signal), C (chromatin: no DNA-binding domain, no histone-like folds, no NLS), and D (synapse: while some GPCRs localize to synaptic membranes, this requires specific synaptic targeting motifs absent here; the generic location of a multi-pass TM receptor without synaptic targeting signals is the plasma membrane). The distinction between A and D is supported by the general principle that a 7-TM receptor without synaptic scaffolding motifs or neurotransmitter-receptor-specific features resides at the plasma membrane rather than a specialized synaptic junction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7-TM topology, DRY motif, and NPxxY motif are well-known GPCR signatures transferable from general knowledge of receptor biology. The assignment of multi-pass transmembrane receptors to the plasma membrane is a fundamental principle of cell biology. The other three options (nuclear kinase complex, chromatin, synapse) are eliminated by the absence of corresponding domain features (kinase domains, DNA-binding motifs, synaptic targeting sequences). No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While 'synapse' (D) is a membrane-associated location and some GPCRs do localize to synapses, the sequence lacks any synaptic targeting motifs and the general biology of olfactory receptors places them at the plasma membrane of sensory cilia. The 7-TM GPCR architecture without synaptic scaffolding features makes A clearly the best answer among the four choices.


### Important caveats

- The GO:0005886 annotation is via IBA:GO_Central (phylogenetic inference), not direct experimental localization, though this is consistent with established olfactory receptor biology.
- The reviewer-only evidence identifies the protein as OR51C1 (olfactory receptor), but the model must infer GPCR identity from sequence features alone; this inference is well-supported by the DRY and NPxxY motifs and 7-TM topology.
- The distinction between 'plasma membrane' and 'synapse' relies on the general principle that generic 7-TM receptors without synaptic targeting motifs are annotated to the plasma membrane, which is standard GO practice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately 7 hydrophobic stretches of ~20-25 residues characteristic of G-protein-coupled receptor (GPCR) transmembrane helices. Two hallmark GPCR motifs are identifiable: the DRY motif (D-R-Y in 'AFDRFVAVSN' around position 130) and the NPxxY motif (N-P-L-R-Y in 'SNPLRY' around position 145). GPCRs are, by definition and fundamental cell biology, integral plasma membrane proteins. This eliminates B (Dbf4-dependent kinase complex: no kinase catalytic domain, no nuclear localization signal), C (chromatin: no DNA-binding domain, no histone-like folds, no NLS), and D (synapse: while some GPCRs localize to synaptic membranes, this requires specific synaptic targeting motifs absent here; the generic location of a multi-pass TM receptor without synaptic targeting signals is the plasma membrane). The distinction between A and D is supported by the general principle that a 7-TM receptor without synaptic scaffolding motifs or neurotransmitter-receptor-specific features resides at the plasma membrane rather than a specialized synaptic junction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM topology, DRY motif, and NPxxY motif are well-known GPCR signatures transferable from general knowledge of receptor biology. The assignment of multi-pass transmembrane receptors to the plasma membrane is a fundamental principle of cell biology. The other three options (nuclear kinase complex, chromatin, synapse) are eliminated by the absence of corresponding domain features (kinase domains, DNA-binding motifs, synaptic targeting sequences). No target-specific database lookup is required."
  },
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A3B3IT45, Olfactory receptor OR51C1) annotates the protein as 'Membrane; Multi-pass membrane protein' with GO:0005886 (plasma membrane) via IBA:GO_Central. The sequence itself displays canonical 7-transmembrane GPCR topology with the DRY motif (AFDRFVAVSN) and NPxxY motif (NPLRY), confirming a multi-pass membrane protein at the plasma membrane. The GO annotation evidence code is IBA (inferred by biological aspect), which is a computational/phylogenetic transfer rather than direct experimental localization, but it is consistent with the well-established biology of olfactory receptors as plasma membrane GPCRs."
  },
  "important_caveats": [
    "The GO:0005886 annotation is via IBA:GO_Central (phylogenetic inference), not direct experimental localization, though this is consistent with established olfactory receptor biology.",
    "The reviewer-only evidence identifies the protein as OR51C1 (olfactory receptor), but the model must infer GPCR identity from sequence features alone; this inference is well-supported by the DRY and NPxxY motifs and 7-TM topology.",
    "The distinction between 'plasma membrane' and 'synapse' relies on the general principle that generic 7-TM receptors without synaptic targeting motifs are annotated to the plasma membrane, which is standard GO practice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'synapse' (D) is a membrane-associated location and some GPCRs do localize to synapses, the sequence lacks any synaptic targeting motifs and the general biology of olfactory receptors places them at the plasma membrane of sensory cilia. The 7-TM GPCR architecture without synaptic scaffolding features makes A clearly the best answer among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A3B3IT45, Olfactory receptor OR51C1) annotates the protein as 'Membrane; Multi-pass membrane protein' with GO:0005886 (plasma membrane) via IBA:GO_Central. The sequence itself displays canonical 7-transmembrane GPCR topology with the DRY motif (AFDRFVAVSN) and NPxxY motif (NPLRY), confirming a multi-pass membrane protein at the plasma membrane. The GO annotation evidence code is IBA (inferred by biological aspect), which is a computational/phylogenetic transfer rather than direct experimental localization, but it is consistent with the well-established biology of olfactory receptors as plasma membrane GPCRs.",
    "evidence_ids": ["C5", "C6", "H2", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately 7 hydrophobic stretches of ~20-25 residues characteristic of G-protein-coupled receptor (GPCR) transmembrane helices. Two hallmark GPCR motifs are identifiable: the DRY motif (D-R-Y in 'AFDRFVAVSN' around position 130) and the NPxxY motif (N-P-L-R-Y in 'SNPLRY' around position 145). GPCRs are, by definition and fundamental cell biology, integral plasma membrane proteins. This eliminates B (Dbf4-dependent kinase complex: no kinase catalytic domain, no nuclear localization signal), C (chromatin: no DNA-binding domain, no histone-like folds, no NLS), and D (synapse: while some GPCRs localize to synaptic membranes, this requires specific synaptic targeting motifs absent here; the generic location of a multi-pass TM receptor without synaptic targeting signals is the plasma membrane). The distinction between A and D is supported by the general principle that a 7-TM receptor without synaptic scaffolding motifs or neurotransmitter-receptor-specific features resides at the plasma membrane rather than a specialized synaptic junction.",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM topology, DRY motif, and NPxxY motif are well-known GPCR signatures transferable from general knowledge of receptor biology. The assignment of multi-pass transmembrane receptors to the plasma membrane is a fundamental principle of cell biology. The other three options (nuclear kinase complex, chromatin, synapse) are eliminated by the absence of corresponding domain features (kinase domains, DNA-binding motifs, synaptic targeting sequences). No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'synapse' (D) is a membrane-associated location and some GPCRs do localize to synapses, the sequence lacks any synaptic targeting motifs and the general biology of olfactory receptors places them at the plasma membrane of sensory cilia. The 7-TM GPCR architecture without synaptic scaffolding features makes A clearly the best answer among the four choices."
  },
  "important_caveats": [
    "The GO:0005886 annotation is via IBA:GO_Central (phylogenetic inference), not direct experimental localization, though this is consistent with established olfactory receptor biology.",
    "The reviewer-only evidence identifies the protein as OR51C1 (olfactory receptor), but the model must infer GPCR identity from sequence features alone; this inference is well-supported by the DRY and NPxxY motifs and 7-TM topology.",
    "The distinction between 'plasma membrane' and 'synapse' relies on the general principle that generic 7-TM receptors without synaptic targeting motifs are annotated to the plasma membrane, which is standard GO practice."
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
  "benchmark_sequence_length": 312,
  "benchmark_sequence_sha256": "2e8788df8496584049759195f5fde6a8aa4eb5ba3967d17a73b09b64771bfd14",
  "current_entry_audit": {
    "entryVersion": 35,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-12-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 312,
  "current_source_sequence_sha256": "2e8788df8496584049759195f5fde6a8aa4eb5ba3967d17a73b09b64771bfd14",
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
  "requested_accession": "A0A3B3IT45",
  "selected_historical_entry_version": 33,
  "selected_historical_record_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "selected_historical_source_sequence_length": 312,
  "selected_historical_source_sequence_sha256": "2e8788df8496584049759195f5fde6a8aa4eb5ba3967d17a73b09b64771bfd14",
  "selected_historical_version": {
    "accession": "A0A3B3IT45",
    "database": "Swiss-Prot",
    "entryVersion": 33,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "O51C1_HUMAN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A3B3IT45\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":35,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-12-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Human\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Primates\",\"Haplorrhini\",\"Catarrhini\",\"Hominidae\",\"Homo\"],\"scientificName\":\"Homo sapiens\",\"taxonId\":9606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"HGNC:15191\",\"source\":\"HGNC\"}],\"value\":\"Olfactory receptor OR51C1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0162\",\"value\":\"Membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H1",
  "excerpt": "ID   O51C1_HUMAN             Reviewed;         312 AA.\nAC   A0A3B3IT45; Q8NH68;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-DEC-2018, sequence version 1.\nDT   28-JAN-2026, entry version 33.\nDE   RecName: Full=Olfactory receptor OR51C1 {ECO:0000312|HGNC:HGNC:15191};\nGN   Name=OR51C1 {ECO:0000312|HGNC:HGNC:15191};\nGN   Synonyms=OR51C1P {ECO:0000312|HGNC:HGNC:15191}, OR51C3P, OST734;\nOS   Homo sapiens (Human).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;\nOC   Homo.\nOX   NCBI_TaxID=9606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Multi-pass membrane\nCC       protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000785\nname: chromatin\nnamespace: cellular_component\nalt_id: GO:0000789\nalt_id: GO:0000790\nalt_id: GO:0005717\ndef: \"The ordered and organized complex of DNA, protein, and sometimes RNA, that forms the chromosome.\" [GOC:elh, PMID:20404130]\ncomment: Chromosomes include parts that are not part of the chromatin. Examples include the kinetochore.\nsynonym: \"chromosome scaffold\" RELATED []\nsynonym: \"cytoplasmic chromatin\" NARROW []\nsynonym: \"nuclear chromatin\" NARROW []\nxref: NIF_Subcellular:sao1615953555\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005694 ! chromosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000785",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 5903-5918",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0031431\nname: Dbf4-dependent protein kinase complex\nnamespace: cellular_component\ndef: \"A heterodimeric protein complex required for the activation of DNA replication origins; comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins.\" [PMID:12045100]\nsynonym: \"Cdc7-Dbf4 complex\" NARROW []\nsynonym: \"DDK\" EXACT []\nsynonym: \"Hsk1-Dfp1 kinase complex\" NARROW []\nis_a: GO:0140513 ! nuclear protein-containing complex\nis_a: GO:1902554 ! serine/threonine protein kinase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031431",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 176442-176452",
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
  "excerpt": "[Term]\nid: GO:0045202\nname: synapse\nnamespace: cellular_component\ndef: \"The junction between an axon of one neuron and a dendrite of another neuron, a muscle fiber or a glial cell. As the axon approaches the synapse it enlarges into a specialized structure, the presynaptic terminal bouton, which contains mitochondria and synaptic vesicles. At the tip of the terminal bouton is the presynaptic membrane; facing it, and separated from it by a minute cleft (the synaptic cleft) is a specialized area of membrane on the receiving cell, known as the postsynaptic membrane. In response to the arrival of nerve impulses, the presynaptic terminal bouton secretes molecules of neurotransmitters into the synaptic cleft. These diffuse across the cleft and transmit the signal to the postsynaptic membrane.\" [GOC:aruk, ISBN:0198506732, PMID:24619342, PMID:29383328, PMID:31998110]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_synapse\nsynonym: \"electrotonic synapse\" RELATED [NIF_Subcellular:sao1311109124]\nsynonym: \"mixed synapse\" NARROW [NIF_Subcellular:sao1506103497]\nsynonym: \"synaptic junction\" EXACT []\nxref: NIF_Subcellular:sao914572699\nxref: Wikipedia:Chemical_synapse\nis_a: GO:0030054 ! cell junction\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045202",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 262894-262912",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
