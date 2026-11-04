# GO_cellular_component_0070

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0070.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — primosome complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIYHRIAVNVPLSDGLLTYSHSEPLPPGTRVLVPFRNKTVVGMVWETDIAPDMDAARILSVQTVFVEEKPLSQSWRDLLAFTSRYYHYPTGQAVFAALPQGLKETRAVEMPQPPLFYALNEAGRAQTPPPARFNKKAALWDALLSGEMTMAALKQANAQAAKLIEDWAEQGWIETTEAAKPVLRPYRGQASHSEFVLNTGQQKASDEIQTALGRFRSFLLYGITGSGKTEVYFDAMAKVLAQGRQVLFLLPEINLTPQLLKRVENRFADVPTAVLHSRMAAGRRTQDYLRAMLGQAKLVIGTRLAVFTPLPDVGLIVVDEEHDGSFKQDNELRYHARDLAVWRAKQGGCPVVLGSATPSLESWHKAQSGAYRLLQLTERAHASAQLPQVDILNIGRLKLDNGFSPQALQLLKQNFEAGGMSLVYLNRRGFAPALFCGDCGHTFGCPNCSAKMVLHQRARQLRCHHCDHREPIPFKCPDCGNQDLTAVGHGTQRVEETLRAFLPKAAVVRVDRDSTAHKNDWADLYRRIANDEIDILVGTQMLAKGHDFARLNLVIVLNADGSLYSADFRAPERLFAELMQVSGRAGRADKPGKVLIQTQLPEHPVFAAVKAQDYAVFAENELNERQMFAMPPFGFQTAVRADAPRVADAMEFLNAAKETLAPLLPESVSRFGAAPMLMVRLAERERAQVFLESTSRQDLHRAVSLWVQVLQQNRDGKIRWSVDVDPQEA

[Multiple Choices]
A. cell surface
B. primosome complex
C. microneme
D. plasma membrane
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

> The sequence-matched historical UniProt record annotates the protein to the primosome complex (H5), and identifies it as replication restart protein PriA (H1). This supports the key as a database annotation, though the GO annotation is electronic (IEA), not direct experimental evidence of localization or complex membership.

Citations as saved: [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a large ATP-dependent helicase-like architecture, including a recognizable P-loop-like nucleotide-binding motif and a C-terminal cysteine-rich region consistent with DNA-binding features of bacterial PriA-family replication restart helicases. Transferable knowledge that PriA helicases act at stalled replication forks and participate in replication-restart/primosome machinery supports B. The sequence also lacks an evident membrane-spanning region or secretory targeting signal, making the membrane and cell-surface options poor fits; micronemes are specialized apicomplexan parasite organelles.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known role of PriA-like helicases meaningfully distinguish the offered primosome-complex choice without requiring recall of this exact protein's database entry. The inference supports association with replication machinery, not necessarily permanent residence in a complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these alternatives, the replication-associated complex is meaningfully distinguished from cell-surface or membrane locations and from a microneme.


### Important caveats

- The supporting GO annotation is electronic (IEA), so it should not be represented as direct experimental localization evidence.
- A PriA-family role supports primosome association but does not establish that the protein is permanently bound to the complex.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a large ATP-dependent helicase-like architecture, including a recognizable P-loop-like nucleotide-binding motif and a C-terminal cysteine-rich region consistent with DNA-binding features of bacterial PriA-family replication restart helicases. Transferable knowledge that PriA helicases act at stalled replication forks and participate in replication-restart/primosome machinery supports B. The sequence also lacks an evident membrane-spanning region or secretory targeting signal, making the membrane and cell-surface options poor fits; micronemes are specialized apicomplexan parasite organelles.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known role of PriA-like helicases meaningfully distinguish the offered primosome-complex choice without requiring recall of this exact protein's database entry. The inference supports association with replication machinery, not necessarily permanent residence in a complex."
  },
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates the protein to the primosome complex (H5), and identifies it as replication restart protein PriA (H1). This supports the key as a database annotation, though the GO annotation is electronic (IEA), not direct experimental evidence of localization or complex membership."
  },
  "important_caveats": [
    "The supporting GO annotation is electronic (IEA), so it should not be represented as direct experimental localization evidence.",
    "A PriA-family role supports primosome association but does not establish that the protein is permanently bound to the complex."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, the replication-associated complex is meaningfully distinguished from cell-surface or membrane locations and from a microneme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates the protein to the primosome complex (H5), and identifies it as replication restart protein PriA (H1). This supports the key as a database annotation, though the GO annotation is electronic (IEA), not direct experimental evidence of localization or complex membership.",
    "evidence_ids": ["H1", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a large ATP-dependent helicase-like architecture, including a recognizable P-loop-like nucleotide-binding motif and a C-terminal cysteine-rich region consistent with DNA-binding features of bacterial PriA-family replication restart helicases. Transferable knowledge that PriA helicases act at stalled replication forks and participate in replication-restart/primosome machinery supports B. The sequence also lacks an evident membrane-spanning region or secretory targeting signal, making the membrane and cell-surface options poor fits; micronemes are specialized apicomplexan parasite organelles.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known role of PriA-like helicases meaningfully distinguish the offered primosome-complex choice without requiring recall of this exact protein's database entry. The inference supports association with replication machinery, not necessarily permanent residence in a complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, the replication-associated complex is meaningfully distinguished from cell-surface or membrane locations and from a microneme."
  },
  "important_caveats": [
    "The supporting GO annotation is electronic (IEA), so it should not be represented as direct experimental localization evidence.",
    "A PriA-family role supports primosome association but does not establish that the protein is permanently bound to the complex."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q5F6V8) annotates this protein as GO:1990077 (primosome complex) via IEA:UniProtKB-UniRule. The protein is identified as PriA (Replication restart protein, EC 5.6.2.4) from Neisseria gonorrhoeae, confirmed by multiple experimental references (PubMed:16030229, 21861872, 23193948) characterizing its helicase and ATPase functions in replication restart. PriA is a well-established component of the primosome complex. The sequence contains characteristic DEAD-box helicase motifs and zinc-binding motifs consistent with PriA.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear DEAD-box helicase Walker B motif ('VDEEHDGSFKQDNELRYHARDLAVWRAKQ') and a multi-cysteine zinc-binding motif ('CGDCGHTFGCPNCSAKMVLHQRARQLRCHHCDHREPIPFKCPDCGN'), which together are hallmarks of replication/recombination DNA helicases (e.g., PriA, Rep, DnaB homologs). The protein lacks any N-terminal signal peptide, transmembrane helix, or lipoprotein cysteine anchor, eliminating membrane-associated compartments (A: cell surface, D: plasma membrane). The sequence architecture is bacterial (no eukaryotic organelle-targeting signals), eliminating C: microneme, which is exclusive to apicomplexan parasites. A DNA helicase with zinc fingers involved in replication restart is a canonical primosome component, making B the only biologically coherent choice among the four alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of (1) recognizable DEAD-box helicase motifs learned from many other helicases, (2) the zinc-finger motif characteristic of replication restart helicases, (3) absence of any membrane-targeting signal eliminating A and D, and (4) the bacterial context eliminating the apicomplexan-specific microneme (C), provides a concrete transferable-knowledge chain that meaningfully distinguishes B from the other three options without requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive and biologically incompatible with the sequence features: A and D require membrane-targeting signals absent here; C requires an apicomplexan-specific organelle incompatible with a bacterial protein; only B is consistent with a cytoplasmic DNA helicase involved in replication.


### Important caveats

- The GO annotation for primosome complex is IEA (Inferred from Electronic Annotation via UniRule), a computational assignment, but the protein's identity as PriA is supported by experimental literature (helicase/ATPase assays, disruption phenotypes).
- The reviewer identified the accession from dataset metadata not available to the evaluated model; the reasoning above relies solely on sequence features and general biological knowledge.
- The GO term 'primosome complex' is a protein-DNA complex annotation rather than a classical 'location' (e.g., cytoplasm, nucleus); the question frames it as a cellular component, which is technically valid under GO's cellular_component namespace but somewhat unconventional for a complex rather than a compartment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear DEAD-box helicase Walker B motif ('VDEEHDGSFKQDNELRYHARDLAVWRAKQ') and a multi-cysteine zinc-binding motif ('CGDCGHTFGCPNCSAKMVLHQRARQLRCHHCDHREPIPFKCPDCGN'), which together are hallmarks of replication/recombination DNA helicases (e.g., PriA, Rep, DnaB homologs). The protein lacks any N-terminal signal peptide, transmembrane helix, or lipoprotein cysteine anchor, eliminating membrane-associated compartments (A: cell surface, D: plasma membrane). The sequence architecture is bacterial (no eukaryotic organelle-targeting signals), eliminating C: microneme, which is exclusive to apicomplexan parasites. A DNA helicase with zinc fingers involved in replication restart is a canonical primosome component, making B the only biologically coherent choice among the four alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) recognizable DEAD-box helicase motifs learned from many other helicases, (2) the zinc-finger motif characteristic of replication restart helicases, (3) absence of any membrane-targeting signal eliminating A and D, and (4) the bacterial context eliminating the apicomplexan-specific microneme (C), provides a concrete transferable-knowledge chain that meaningfully distinguishes B from the other three options without requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q5F6V8) annotates this protein as GO:1990077 (primosome complex) via IEA:UniProtKB-UniRule. The protein is identified as PriA (Replication restart protein, EC 5.6.2.4) from Neisseria gonorrhoeae, confirmed by multiple experimental references (PubMed:16030229, 21861872, 23193948) characterizing its helicase and ATPase functions in replication restart. PriA is a well-established component of the primosome complex. The sequence contains characteristic DEAD-box helicase motifs and zinc-binding motifs consistent with PriA."
  },
  "important_caveats": [
    "The GO annotation for primosome complex is IEA (Inferred from Electronic Annotation via UniRule), a computational assignment, but the protein's identity as PriA is supported by experimental literature (helicase/ATPase assays, disruption phenotypes).",
    "The reviewer identified the accession from dataset metadata not available to the evaluated model; the reasoning above relies solely on sequence features and general biological knowledge.",
    "The GO term 'primosome complex' is a protein-DNA complex annotation rather than a classical 'location' (e.g., cytoplasm, nucleus); the question frames it as a cellular component, which is technically valid under GO's cellular_component namespace but somewhat unconventional for a complex rather than a compartment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and biologically incompatible with the sequence features: A and D require membrane-targeting signals absent here; C requires an apicomplexan-specific organelle incompatible with a bacterial protein; only B is consistent with a cytoplasmic DNA helicase involved in replication."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q5F6V8) annotates this protein as GO:1990077 (primosome complex) via IEA:UniProtKB-UniRule. The protein is identified as PriA (Replication restart protein, EC 5.6.2.4) from Neisseria gonorrhoeae, confirmed by multiple experimental references (PubMed:16030229, 21861872, 23193948) characterizing its helicase and ATPase functions in replication restart. PriA is a well-established component of the primosome complex. The sequence contains characteristic DEAD-box helicase motifs and zinc-binding motifs consistent with PriA.",
    "evidence_ids": ["C4", "C5", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear DEAD-box helicase Walker B motif ('VDEEHDGSFKQDNELRYHARDLAVWRAKQ') and a multi-cysteine zinc-binding motif ('CGDCGHTFGCPNCSAKMVLHQRARQLRCHHCDHREPIPFKCPDCGN'), which together are hallmarks of replication/recombination DNA helicases (e.g., PriA, Rep, DnaB homologs). The protein lacks any N-terminal signal peptide, transmembrane helix, or lipoprotein cysteine anchor, eliminating membrane-associated compartments (A: cell surface, D: plasma membrane). The sequence architecture is bacterial (no eukaryotic organelle-targeting signals), eliminating C: microneme, which is exclusive to apicomplexan parasites. A DNA helicase with zinc fingers involved in replication restart is a canonical primosome component, making B the only biologically coherent choice among the four alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) recognizable DEAD-box helicase motifs learned from many other helicases, (2) the zinc-finger motif characteristic of replication restart helicases, (3) absence of any membrane-targeting signal eliminating A and D, and (4) the bacterial context eliminating the apicomplexan-specific microneme (C), provides a concrete transferable-knowledge chain that meaningfully distinguishes B from the other three options without requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and biologically incompatible with the sequence features: A and D require membrane-targeting signals absent here; C requires an apicomplexan-specific organelle incompatible with a bacterial protein; only B is consistent with a cytoplasmic DNA helicase involved in replication."
  },
  "important_caveats": [
    "The GO annotation for primosome complex is IEA (Inferred from Electronic Annotation via UniRule), a computational assignment, but the protein's identity as PriA is supported by experimental literature (helicase/ATPase assays, disruption phenotypes).",
    "The reviewer identified the accession from dataset metadata not available to the evaluated model; the reasoning above relies solely on sequence features and general biological knowledge.",
    "The GO term 'primosome complex' is a protein-DNA complex annotation rather than a classical 'location' (e.g., cytoplasm, nucleus); the question frames it as a cellular component, which is technically valid under GO's cellular_component namespace but somewhat unconventional for a complex rather than a compartment."
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
  "benchmark_sequence_length": 729,
  "benchmark_sequence_sha256": "ef6c3ffe7dc37bec3d2529c78a1850288bf6360f53389681bff488df263499ab",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-03-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 729,
  "current_source_sequence_sha256": "ef6c3ffe7dc37bec3d2529c78a1850288bf6360f53389681bff488df263499ab",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 129,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5F6V8",
  "selected_historical_entry_version": 129,
  "selected_historical_record_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "selected_historical_source_sequence_length": 729,
  "selected_historical_source_sequence_sha256": "ef6c3ffe7dc37bec3d2529c78a1850288bf6360f53389681bff488df263499ab",
  "selected_historical_version": {
    "accession": "Q5F6V8",
    "database": "Swiss-Prot",
    "entryVersion": 129,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PRIA_NEIG1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5F6V8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-03-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090)\",\"taxonId\":242231}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21861872\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23193948\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"ATP-dependent DNA helicase PriA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"DNA 3'-5' helicase PriA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16030229\",\"source\":\"PubMed\"}],\"value\":\"Helicase PriA\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Replication restart protein PriA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990077\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:primosome complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kline K.A.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16030229\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.15.5347-5355.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"5347\",\"id\":\"16030229\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"5355\",\"publicationDate\":\"2005\",\"title\":\"Mutation of the priA gene of Neisseria gonorrhoeae affects DNA transformation and DNA repair.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Feng C.\",\"Sunchu B.\",\"Greenwood M.E.\",\"Lopper M.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21861872\"},{\"database\":\"DOI\",\"id\":\"10.1186/1471-2180-11-189\"}],\"citationType\":\"journal article\",\"firstPage\":\"189\",\"id\":\"21861872\",\"journal\":\"BMC Microbiol.\",\"lastPage\":\"189\",\"publicationDate\":\"2011\",\"title\":\"A bacterial PriB with weak single-stranded DNA binding activity can stimulate the DNA unwinding activity of its cognate PriA helicase.\",\"volume\":\"11\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION AS A HELICASE\",\"FUNCTION AS AN ATPASE\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DNA-BINDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sunchu B.\",\"Berg L.\",\"Ward H.E.\",\"Lopper M.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23193948\"},{\"database\":\"DOI\",\"id\":\"10.1021/bi301100w\"}],\"citationType\":\"journal article\",\"firstPage\":\"10137\",\"id\":\"23193948\",\"journal\":\"Biochemistry\",\"lastPage\":\"10146\",\"publicationDate\":\"2012\",\"title\":\"Identification of a small molecule PriA helicase inhibitor.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H1",
  "excerpt": "ID   PRIA_NEIG1              Reviewed;         729 AA.\nAC   Q5F6V8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-MAR-2005, sequence version 1.\nDT   28-JAN-2026, entry version 129.\nDE   RecName: Full=Replication restart protein PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE   AltName: Full=ATP-dependent DNA helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE            EC=5.6.2.4 {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305|PubMed:21861872, ECO:0000305|PubMed:23193948};\nDE   AltName: Full=DNA 3'-5' helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE   AltName: Full=Helicase PriA {ECO:0000303|PubMed:16030229};\nGN   Name=priA {ECO:0000255|HAMAP-Rule:MF_00983};\nGN   OrderedLocusNames=NGO_1437 {ECO:0000312|EMBL:AAW90079.1};\nOS   Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=242231;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700825 / FA 1090;\nRX   PubMed=16030229; DOI=10.1128/jb.187.15.5347-5355.2005;\nRA   Kline K.A., Seifert H.S.;\nRT   \"Mutation of the priA gene of Neisseria gonorrhoeae affects DNA\nRT   transformation and DNA repair.\";\nRL   J. Bacteriol. 187:5347-5355(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY, ACTIVITY\nRP   REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND DNA-BINDING.\nRC   STRAIN=ATCC 700825 / FA 1090;\nRX   PubMed=21861872; DOI=10.1186/1471-2180-11-189;\nRA   Feng C., Sunchu B., Greenwood M.E., Lopper M.E.;\nRT   \"A bacterial PriB with weak single-stranded DNA binding activity can\nRT   stimulate the DNA unwinding activity of its cognate PriA helicase.\";\nRL   BMC Microbiol. 11:189-189(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H4",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRC   STRAIN=ATCC 700825 / FA 1090;\nRX   PubMed=23193948; DOI=10.1021/bi301100w;\nRA   Sunchu B., Berg L., Ward H.E., Lopper M.E.;\nRT   \"Identification of a small molecule PriA helicase inhibitor.\";\nRL   Biochemistry 51:10137-10146(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:1990077; C:primosome complex; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
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

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0009986\nname: cell surface\nnamespace: cellular_component\nalt_id: GO:0009928\nalt_id: GO:0009929\ndef: \"The external part of the cell wall and/or plasma membrane.\" [GOC:jl, GOC:mtg_sensu, GOC:sm]\ncomment: Note that this term is intended to annotate gene products that are attached (integrated or loosely bound) to the plasma membrane or cell wall.\nsubset: goslim_pir\nsynonym: \"cell associated\" EXACT []\nsynonym: \"cell bound\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009986",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 101772-101784",
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
  "excerpt": "[Term]\nid: GO:0020009\nname: microneme\nnamespace: cellular_component\ndef: \"A small, elongated secretory organelle that forms part of the apical complex, located along the main axis of an apicomplexan parasite cell within the extreme apical region and at the periphery under the inner membrane complex. Of the specialized secretory compartments identified in apicomplexans, micronemes discharge their contents first, during initial contact of the parasite's apical pole with the host cell surface. Micronemal proteins function during parasite attachment and penetration into the target cell.\" [ISBN:0521664470, PMID:11801218]\nsynonym: \"sarconeme\" RELATED []\nxref: Wikipedia:Microneme\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0020007 ! apical complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020009",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155191-155200",
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
  "excerpt": "[Term]\nid: GO:1990077\nname: primosome complex\nnamespace: cellular_component\ndef: \"Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart.\" [GOC:bhm, GOC:mah, PMID:21856207]\nsynonym: \"primosome\" EXACT []\nis_a: GO:0032993 ! protein-DNA complex\nrelationship: part_of GO:0030894 ! replisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990077",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 549032-549040",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
