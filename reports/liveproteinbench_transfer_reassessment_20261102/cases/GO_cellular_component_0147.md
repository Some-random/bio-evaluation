# GO_cellular_component_0147

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0147.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — virus tail, tube

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTVIQDTADVYFKRKSDGKLVFTAEAQTASFSQAISEEKLRGGIGNKPLYILKSEKEINLTVKNAFFDLEWLAMTQGETIQEETKVKVFDREHGLIVDDTNKVTLKGKPVSDVTFYNKKGLTYKIAVSTDGTYTIPTAFAAAKDKLTAVYQIEKVGRRLAIKASKFSERYEVEYRTIAYNPDTEEVYSDIYIQFPNVSPSGEFEMSLENGNALAPEIKFEALADTDTDEMAVVIEASRDENTAAPVEDTTGSTQSSDLGGTTE

[Multiple Choices]
A. virus tail, tube
B. actin cytoskeleton
C. host cell plasma membrane
D. microvillus membrane
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

> The matched UniProt record names the protein as a tail tube protein and annotates it to the virus tail, tube GO term. The GO annotation is computationally assigned via UniProtKB-KW, so it supports the key but is not direct experimental localization evidence.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 264-aa sequence is a compact soluble-protein candidate, with no obvious transmembrane segment or eukaryotic membrane-targeting signal; it also does not resemble a canonical actin protein. Phage tail-tube proteins are commonly soluble virion structural proteins, and transferable family-level sequence recognition can make A more plausible than the host-cell cytoskeleton or membrane choices. This is a probabilistic inference, not a definitive identification from sequence composition alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices contrast a phage structural component with host-cell compartments. Sequence-based family recognition and the lack of membrane or actin-like features provide a meaningful basis for preferring A without needing the exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the supplied sequence and choices.


### Important caveats

- The supplied input contains no organism or viral context, and sequence composition alone does not prove that the protein is a tail-tube component.
- The supporting GO annotation is computational; the supplied evidence does not establish direct experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 264-aa sequence is a compact soluble-protein candidate, with no obvious transmembrane segment or eukaryotic membrane-targeting signal; it also does not resemble a canonical actin protein. Phage tail-tube proteins are commonly soluble virion structural proteins, and transferable family-level sequence recognition can make A more plausible than the host-cell cytoskeleton or membrane choices. This is a probabilistic inference, not a definitive identification from sequence composition alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices contrast a phage structural component with host-cell compartments. Sequence-based family recognition and the lack of membrane or actin-like features provide a meaningful basis for preferring A without needing the exact protein's database annotation."
  },
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record names the protein as a tail tube protein and annotates it to the virus tail, tube GO term. The GO annotation is computationally assigned via UniProtKB-KW, so it supports the key but is not direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied input contains no organism or viral context, and sequence composition alone does not prove that the protein is a tail-tube component.",
    "The supporting GO annotation is computational; the supplied evidence does not establish direct experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the supplied sequence and choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record names the protein as a tail tube protein and annotates it to the virus tail, tube GO term. The GO annotation is computationally assigned via UniProtKB-KW, so it supports the key but is not direct experimental localization evidence.",
    "evidence_ids": ["C4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 264-aa sequence is a compact soluble-protein candidate, with no obvious transmembrane segment or eukaryotic membrane-targeting signal; it also does not resemble a canonical actin protein. Phage tail-tube proteins are commonly soluble virion structural proteins, and transferable family-level sequence recognition can make A more plausible than the host-cell cytoskeleton or membrane choices. This is a probabilistic inference, not a definitive identification from sequence composition alone.",
    "missing_item_specific_fact": "",
    "reason": "The choices contrast a phage structural component with host-cell compartments. Sequence-based family recognition and the lack of membrane or actin-like features provide a meaningful basis for preferring A without needing the exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the supplied sequence and choices."
  },
  "important_caveats": [
    "The supplied input contains no organism or viral context, and sequence composition alone does not prove that the protein is a tail-tube component.",
    "The supporting GO annotation is computational; the supplied evidence does not establish direct experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0AAE9G628) names this protein 'Tail tube protein' from Bacillus phage SPR (Caudoviricetes, Spbetavirus). The GO annotation GO:0098026 'virus tail, tube' is present (evidence IEA:UniProtKB-KW), and the subcellular location is annotated as 'Virion' (ECO:0000305, curator inference). The protein name directly corresponds to the GO term. The GO annotation is keyword-derived rather than experimentally validated, but the protein's identity as a phage tail tube structural protein is well-established by its naming and organism context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (264 AA) can be evaluated against the defining structural requirements of each option. Options C (host cell plasma membrane) and D (microvillus membrane) require transmembrane domains or lipid-anchor motifs; the sequence lacks any hydrophobic stretch of ~20+ residues characteristic of a transmembrane helix, and lacks signal peptides or GPI-anchor signals. Option B (actin cytoskeleton) requires actin-binding motifs (WH2, profilin-like, or similar); none are present. Option A (virus tail, tube) is a small, beta-sheet-rich structural protein forming the virion tube; the sequence's compact size, absence of membrane/secretion signals, and alternating hydrophobic-polar composition consistent with beta-strand packing align with phage tail tube proteins (e.g., gp19 of T4, gp7 of lambda). By elimination of B, C, D and positive match to small viral structural protein features, A is distinguished.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B (no actin-binding motifs), C and D (no transmembrane domains or membrane-association signals) based on well-established structural requirements for those compartments. The remaining option A is the only one consistent with a small, non-membrane, non-cytoskeletal protein. The beta-sheet-like composition and absence of eukaryotic targeting signals further support a viral structural protein assignment. This is a legitimate elimination-plus-positive-feature argument using transferable knowledge of membrane protein architecture, actin-binding domains, and phage structural biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally distinct compartments. B requires actin-binding capability, C and D require membrane integration, and A requires virion structural assembly. The sequence clearly lacks features for B, C, and D, leaving A as the only consistent choice.


### Important caveats

- The GO annotation is IEA:UniProtKB-KW (keyword-based electronic inference) rather than direct experimental evidence; the subcellular location 'Virion' uses ECO:0000305 (curator inference).
- The primary discriminating argument is elimination of B, C, D by absence of their defining structural features; positive identification of 'tail tube' specifically (vs. other phage structural roles like head or baseplate) relies on general phage protein composition patterns rather than a unique sequence motif.
- The protein's identity as a phage tail tube protein is established by its UniProt name and organism context, which were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (264 AA) can be evaluated against the defining structural requirements of each option. Options C (host cell plasma membrane) and D (microvillus membrane) require transmembrane domains or lipid-anchor motifs; the sequence lacks any hydrophobic stretch of ~20+ residues characteristic of a transmembrane helix, and lacks signal peptides or GPI-anchor signals. Option B (actin cytoskeleton) requires actin-binding motifs (WH2, profilin-like, or similar); none are present. Option A (virus tail, tube) is a small, beta-sheet-rich structural protein forming the virion tube; the sequence's compact size, absence of membrane/secretion signals, and alternating hydrophobic-polar composition consistent with beta-strand packing align with phage tail tube proteins (e.g., gp19 of T4, gp7 of lambda). By elimination of B, C, D and positive match to small viral structural protein features, A is distinguished.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B (no actin-binding motifs), C and D (no transmembrane domains or membrane-association signals) based on well-established structural requirements for those compartments. The remaining option A is the only one consistent with a small, non-membrane, non-cytoskeletal protein. The beta-sheet-like composition and absence of eukaryotic targeting signals further support a viral structural protein assignment. This is a legitimate elimination-plus-positive-feature argument using transferable knowledge of membrane protein architecture, actin-binding domains, and phage structural biology."
  },
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAE9G628) names this protein 'Tail tube protein' from Bacillus phage SPR (Caudoviricetes, Spbetavirus). The GO annotation GO:0098026 'virus tail, tube' is present (evidence IEA:UniProtKB-KW), and the subcellular location is annotated as 'Virion' (ECO:0000305, curator inference). The protein name directly corresponds to the GO term. The GO annotation is keyword-derived rather than experimentally validated, but the protein's identity as a phage tail tube structural protein is well-established by its naming and organism context."
  },
  "important_caveats": [
    "The GO annotation is IEA:UniProtKB-KW (keyword-based electronic inference) rather than direct experimental evidence; the subcellular location 'Virion' uses ECO:0000305 (curator inference).",
    "The primary discriminating argument is elimination of B, C, D by absence of their defining structural features; positive identification of 'tail tube' specifically (vs. other phage structural roles like head or baseplate) relies on general phage protein composition patterns rather than a unique sequence motif.",
    "The protein's identity as a phage tail tube protein is established by its UniProt name and organism context, which were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally distinct compartments. B requires actin-binding capability, C and D require membrane integration, and A requires virion structural assembly. The sequence clearly lacks features for B, C, and D, leaving A as the only consistent choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAE9G628) names this protein 'Tail tube protein' from Bacillus phage SPR (Caudoviricetes, Spbetavirus). The GO annotation GO:0098026 'virus tail, tube' is present (evidence IEA:UniProtKB-KW), and the subcellular location is annotated as 'Virion' (ECO:0000305, curator inference). The protein name directly corresponds to the GO term. The GO annotation is keyword-derived rather than experimentally validated, but the protein's identity as a phage tail tube structural protein is well-established by its naming and organism context.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (264 AA) can be evaluated against the defining structural requirements of each option. Options C (host cell plasma membrane) and D (microvillus membrane) require transmembrane domains or lipid-anchor motifs; the sequence lacks any hydrophobic stretch of ~20+ residues characteristic of a transmembrane helix, and lacks signal peptides or GPI-anchor signals. Option B (actin cytoskeleton) requires actin-binding motifs (WH2, profilin-like, or similar); none are present. Option A (virus tail, tube) is a small, beta-sheet-rich structural protein forming the virion tube; the sequence's compact size, absence of membrane/secretion signals, and alternating hydrophobic-polar composition consistent with beta-strand packing align with phage tail tube proteins (e.g., gp19 of T4, gp7 of lambda). By elimination of B, C, D and positive match to small viral structural protein features, A is distinguished.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B (no actin-binding motifs), C and D (no transmembrane domains or membrane-association signals) based on well-established structural requirements for those compartments. The remaining option A is the only one consistent with a small, non-membrane, non-cytoskeletal protein. The beta-sheet-like composition and absence of eukaryotic targeting signals further support a viral structural protein assignment. This is a legitimate elimination-plus-positive-feature argument using transferable knowledge of membrane protein architecture, actin-binding domains, and phage structural biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally distinct compartments. B requires actin-binding capability, C and D require membrane integration, and A requires virion structural assembly. The sequence clearly lacks features for B, C, and D, leaving A as the only consistent choice."
  },
  "important_caveats": [
    "The GO annotation is IEA:UniProtKB-KW (keyword-based electronic inference) rather than direct experimental evidence; the subcellular location 'Virion' uses ECO:0000305 (curator inference).",
    "The primary discriminating argument is elimination of B, C, D by absence of their defining structural features; positive identification of 'tail tube' specifically (vs. other phage structural roles like head or baseplate) relies on general phage protein composition patterns rather than a unique sequence motif.",
    "The protein's identity as a phage tail tube protein is established by its UniProt name and organism context, which were not provided to the evaluated model."
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
  "benchmark_sequence_length": 264,
  "benchmark_sequence_sha256": "e2a1e44bf404d80667d2a67af1489abb62e09d7756b230d2f8882b178d00d944",
  "current_entry_audit": {
    "entryVersion": 9,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 264,
  "current_source_sequence_sha256": "e2a1e44bf404d80667d2a67af1489abb62e09d7756b230d2f8882b178d00d944",
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
  "requested_accession": "A0AAE9G628",
  "selected_historical_entry_version": 7,
  "selected_historical_record_sha256": "26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650",
  "selected_historical_source_sequence_length": 264,
  "selected_historical_source_sequence_sha256": "e2a1e44bf404d80667d2a67af1489abb62e09d7756b230d2f8882b178d00d944",
  "selected_historical_version": {
    "accession": "A0AAE9G628",
    "database": "Swiss-Prot",
    "entryVersion": 7,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TUBE_BPSPR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAE9G628\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:26.141304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAE9G628.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":9,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:26.141304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAE9G628.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteriophage SPR\",\"lineage\":[\"Viruses\",\"Duplodnaviria\",\"Heunggongvirae\",\"Uroviricota\",\"Caudoviricetes\",\"Caudoviricetes incertae sedis\",\"Spbetavirus\"],\"scientificName\":\"Bacillus phage SPR\",\"taxonId\":10725}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:26.141304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAE9G628.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"Tail tube protein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:26.141304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAE9G628.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0274\",\"value\":\"Virion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:26.141304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAE9G628.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0098026\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:virus tail, tube\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "retrieved_utc": "2026-11-02T04:26:26.141304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAE9G628.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H1",
  "excerpt": "ID   TUBE_BPSPR              Reviewed;         264 AA.\nAC   A0AAE9G628;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2024, sequence version 1.\nDT   28-JAN-2026, entry version 7.\nDE   RecName: Full=Tail tube protein;\nGN   ORFNames=spr_64 {ECO:0000312|EMBL:UNY48585.1};\nOS   Bacillus phage SPR (Bacteriophage SPR).\nOC   Viruses; Duplodnaviria; Heunggongvirae; Uroviricota; Caudoviricetes;\nOC   Spbetavirus.\nOX   NCBI_TaxID=10725 {ECO:0000312|EMBL:UNY48585.1, ECO:0000312|Proteomes:UP000831086};\nOH   NCBI_TaxID=1423; Bacillus subtilis.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:28.241173+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650",
  "url": "https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000305}.\nCC   ---------------------------------------------------------------------------\nCC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms\nCC   Distributed under the Creative Commons Attribution (CC BY 4.0) License\nCC   ---------------------------------------------------------------------------\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:28.241173+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650",
  "url": "https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7)

```json
{
  "entry_version": 7,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0098026; C:virus tail, tube; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:28.241173+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650",
  "url": "https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0015629\nname: actin cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of actin and associated proteins. Includes actin cytoskeleton-associated complexes.\" [GOC:jl, ISBN:0395825172, ISBN:0815316194]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015629",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119402-119408",
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
  "excerpt": "[Term]\nid: GO:0020002\nname: host cell plasma membrane\nnamespace: cellular_component\ndef: \"The plasma membrane surrounding a host cell.\" [GOC:mb]\nsubset: goslim_virus\nis_a: GO:0033644 ! host cell membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020002",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155120-155127",
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
  "excerpt": "[Term]\nid: GO:0031528\nname: microvillus membrane\nnamespace: cellular_component\ndef: \"The portion of the plasma membrane surrounding a microvillus.\" [GOC:mah]\nis_a: GO:0031253 ! cell projection membrane\nrelationship: part_of GO:0005902 ! microvillus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031528",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 177423-177430",
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
  "excerpt": "[Term]\nid: GO:0098026\nname: virus tail, tube\nnamespace: cellular_component\ndef: \"The internal tube of the tail of some viruses. The virus tail tube is the channel for DNA ejection into the host cytoplasm.\" [PMID:33188213, VZ:3960]\ncomment: Applies in particular the Myoviridae bacteriophages. Many bacteriophages with dsDNA genomes, or Caudovirales, have a tail. The viral tail can be short (Podoviridae), long and non-contractile (Siphoviridae) or long and contractile (Myoviridae). The tail is the channel through which the phage genome is injected into the host bacterial cell.\nsynonym: \"bacteriophage tail tube\" NARROW [GOC:bm]\nxref: VZ:3960 \"Viral tail tube protein\"\nis_a: GO:0044423 ! virion component\nrelationship: part_of GO:0098015 ! virus tail\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098026",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 408367-408377",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
