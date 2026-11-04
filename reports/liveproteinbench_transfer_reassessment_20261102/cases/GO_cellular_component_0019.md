# GO_cellular_component_0019

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0019.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — mitochondrial membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MALSRAKPDELPRDAVVITEDQALKYQWKIITSWDKIGEVWSLRYTPGILSALAAGTGAYINNHYRTKLRLGGHGRLSTYLPIVAVPAIFTMLAHKFFIQRPILLNPLGECPVCIQMRSAAFQTSLGIVYPTILAPFAAFLFATRCYTYRIPSITENPREVFLLWRKFTRPIVPALGTLIGLQALLTMFLTGQEDKQNFKLMLRMREIEHQVEEEHLPQRMDF

[Multiple Choices]
A. host cell mitochondrion
B. trans-Golgi network membrane
C. spindle
D. mitochondrial membrane
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

> The sequence-matched record annotates mitochondrial membrane, with the subcellular-location annotation transferred by similarity (C5) and a GO annotation also present (C7). The record additionally associates the protein with the mitochondrial complex I intermediate assembly complex and mitochondrion (C6, C8), supporting the mitochondrial context. The support is not all direct experimental localization evidence, but it is consistent with choice D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a small, strongly multipass membrane protein, which favors a membrane option over the spindle and argues for a membrane rather than merely an unspecified mitochondrial compartment. A TMEM126-like family interpretation, if recognized from transferable sequence-family patterns, further favors mitochondrial membrane proteins involved in respiratory-complex assembly. This makes D a meaningful choice over the specialized host-cell mitochondrion option A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence’s hydrophobic segments establish membrane-protein character, while transferable family-level knowledge can support mitochondrial membrane localization. This is a probabilistic inference, not a guarantee from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are not equally well supported: the sequence favors a multipass membrane protein, and A specifies a host-cell context not indicated by the input. D is the more specific and biologically apt offered choice.


### Important caveats

- The reviewer-only accession and annotations were not original inputs and are not used as target-specific evidence for answerability.
- The supplied localization evidence includes transfer by similarity; the evidence does not establish that this exact protein’s membrane localization was directly measured.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a small, strongly multipass membrane protein, which favors a membrane option over the spindle and argues for a membrane rather than merely an unspecified mitochondrial compartment. A TMEM126-like family interpretation, if recognized from transferable sequence-family patterns, further favors mitochondrial membrane proteins involved in respiratory-complex assembly. This makes D a meaningful choice over the specialized host-cell mitochondrion option A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence’s hydrophobic segments establish membrane-protein character, while transferable family-level knowledge can support mitochondrial membrane localization. This is a probabilistic inference, not a guarantee from the sequence alone."
  },
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates mitochondrial membrane, with the subcellular-location annotation transferred by similarity (C5) and a GO annotation also present (C7). The record additionally associates the protein with the mitochondrial complex I intermediate assembly complex and mitochondrion (C6, C8), supporting the mitochondrial context. The support is not all direct experimental localization evidence, but it is consistent with choice D."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not original inputs and are not used as target-specific evidence for answerability.",
    "The supplied localization evidence includes transfer by similarity; the evidence does not establish that this exact protein’s membrane localization was directly measured."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are not equally well supported: the sequence favors a multipass membrane protein, and A specifies a host-cell context not indicated by the input. D is the more specific and biologically apt offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates mitochondrial membrane, with the subcellular-location annotation transferred by similarity (C5) and a GO annotation also present (C7). The record additionally associates the protein with the mitochondrial complex I intermediate assembly complex and mitochondrion (C6, C8), supporting the mitochondrial context. The support is not all direct experimental localization evidence, but it is consistent with choice D.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a small, strongly multipass membrane protein, which favors a membrane option over the spindle and argues for a membrane rather than merely an unspecified mitochondrial compartment. A TMEM126-like family interpretation, if recognized from transferable sequence-family patterns, further favors mitochondrial membrane proteins involved in respiratory-complex assembly. This makes D a meaningful choice over the specialized host-cell mitochondrion option A.",
    "missing_item_specific_fact": "",
    "reason": "The sequence’s hydrophobic segments establish membrane-protein character, while transferable family-level knowledge can support mitochondrial membrane localization. This is a probabilistic inference, not a guarantee from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are not equally well supported: the sequence favors a multipass membrane protein, and A specifies a host-cell context not indicated by the input. D is the more specific and biologically apt offered choice."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not original inputs and are not used as target-specific evidence for answerability.",
    "The supplied localization evidence includes transfer by similarity; the evidence does not establish that this exact protein’s membrane localization was directly measured."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9VLM7) annotates this protein as 'Mitochondrion membrane; Multi-pass membrane protein' with evidence ECO:0000250 (similarity to human TMEM126B, Q8IUX1). The GO annotation GO:0031966 (mitochondrial membrane) is assigned via ISS:UniProtKB. Experimental evidence (IDA:FlyBase, PMID 34386730) confirms the protein is in the mitochondrion (GO:0005739) and part of the MCIA complex (GO:0160295), which is defined as part_of the inner mitochondrial membrane (GO:0005743), which is_a mitochondrial membrane (GO:0031966). The specific 'membrane' qualifier is inferred from homology but is consistent with experimental data showing it is a multi-pass membrane protein in the mitochondrial inner membrane.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C6](#evidence-c6), [GO3](#evidence-go3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 223-aa sequence contains multiple hydrophobic stretches in the middle and C-terminal regions (e.g., 'GILSALAAGTGAYINNHYRTKLRLGGHGRLSTYLPIVAVPAIFTMLAHKFFIQRPILLNPLGECPVCIQMRSAAFQTSLGIVYPTILAPFAAFLFATRCYTYRIPSITENPREVFLLWRKFTRPIVPALGTLIGLQALLTMFLTG'), indicating a multi-pass transmembrane topology. This eliminates option C (spindle), which is a microtubule-based structure with no membrane association. The absence of a classic N-terminal ER signal peptide (a short hydrophobic core followed by a polar cleavage site) and the overall architecture of a small multi-pass membrane protein without lumenal Golgi-type domains argue against option B (trans-Golgi network membrane), which typically features single-pass or multi-pass proteins with distinct signal peptides and often larger lumenal regions. Option A ('host cell mitochondrion', GO:0033650) is a specialized GO term defined for pathogen-host interaction contexts ('the host is defined as the larger of the organisms involved in a symbiotic interaction'), making it inappropriate for an endogenous cellular protein. Option D (mitochondrial membrane) is the most precise and appropriate annotation for a multi-pass membrane protein with the observed hydrophobic pattern, consistent with known inner mitochondrial membrane multi-pass proteins (e.g., TMEM family members involved in Complex I assembly).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence's multi-pass hydrophobic architecture, small size, and lack of ER/Golgi-type signal peptides provide a credible basis for mitochondrial membrane assignment. The specialized nature of the 'host cell mitochondrion' GO term (pathogen context) and the spindle option (non-membrane) can be eliminated using general GO knowledge and protein topology principles. The distinction between mitochondrial membrane and trans-Golgi membrane relies on the multi-pass TM pattern in a small protein without a signal peptide, which is a recognized architectural signature of mitochondrial inner membrane proteins learned from many homologous families.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A and D both reference mitochondria, the GO term definitions are distinct: A (host cell mitochondrion) is restricted to pathogen-host contexts and refers to the whole organelle, while D (mitochondrial membrane) is the standard term for membrane-localized mitochondrial proteins. The protein's multi-pass membrane topology specifically supports D over A. No other options are defensible given the sequence features.


### Important caveats

- The 'mitochondrial membrane' annotation (GO:0031966) is assigned via ISS (inferred from similarity to human TMEM126B), not directly from experimental data for this Drosophila protein. The experimental IDA evidence supports 'mitochondrion' and 'MCIA complex' rather than the membrane qualifier directly.
- The N-terminal region lacks a classic cleavable mitochondrial targeting sequence (it contains acidic residues D, E), which is consistent with many inner membrane multi-pass proteins that use internal targeting signals, but makes the mitochondrial assignment less obvious from the N-terminus alone.
- The reviewer-only evidence confirms the sequence matches Q9VLM7 (T126_DROME), but this identification was not available to the evaluated model.
- The GO term 'host cell mitochondrion' (GO:0033650) could theoretically be considered by a model unfamiliar with its pathogen-specific context, though its definition clearly restricts it to symbiotic/host-pathogen settings.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 223-aa sequence contains multiple hydrophobic stretches in the middle and C-terminal regions (e.g., 'GILSALAAGTGAYINNHYRTKLRLGGHGRLSTYLPIVAVPAIFTMLAHKFFIQRPILLNPLGECPVCIQMRSAAFQTSLGIVYPTILAPFAAFLFATRCYTYRIPSITENPREVFLLWRKFTRPIVPALGTLIGLQALLTMFLTG'), indicating a multi-pass transmembrane topology. This eliminates option C (spindle), which is a microtubule-based structure with no membrane association. The absence of a classic N-terminal ER signal peptide (a short hydrophobic core followed by a polar cleavage site) and the overall architecture of a small multi-pass membrane protein without lumenal Golgi-type domains argue against option B (trans-Golgi network membrane), which typically features single-pass or multi-pass proteins with distinct signal peptides and often larger lumenal regions. Option A ('host cell mitochondrion', GO:0033650) is a specialized GO term defined for pathogen-host interaction contexts ('the host is defined as the larger of the organisms involved in a symbiotic interaction'), making it inappropriate for an endogenous cellular protein. Option D (mitochondrial membrane) is the most precise and appropriate annotation for a multi-pass membrane protein with the observed hydrophobic pattern, consistent with known inner mitochondrial membrane multi-pass proteins (e.g., TMEM family members involved in Complex I assembly).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence's multi-pass hydrophobic architecture, small size, and lack of ER/Golgi-type signal peptides provide a credible basis for mitochondrial membrane assignment. The specialized nature of the 'host cell mitochondrion' GO term (pathogen context) and the spindle option (non-membrane) can be eliminated using general GO knowledge and protein topology principles. The distinction between mitochondrial membrane and trans-Golgi membrane relies on the multi-pass TM pattern in a small protein without a signal peptide, which is a recognized architectural signature of mitochondrial inner membrane proteins learned from many homologous families."
  },
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "C6",
      "GO3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9VLM7) annotates this protein as 'Mitochondrion membrane; Multi-pass membrane protein' with evidence ECO:0000250 (similarity to human TMEM126B, Q8IUX1). The GO annotation GO:0031966 (mitochondrial membrane) is assigned via ISS:UniProtKB. Experimental evidence (IDA:FlyBase, PMID 34386730) confirms the protein is in the mitochondrion (GO:0005739) and part of the MCIA complex (GO:0160295), which is defined as part_of the inner mitochondrial membrane (GO:0005743), which is_a mitochondrial membrane (GO:0031966). The specific 'membrane' qualifier is inferred from homology but is consistent with experimental data showing it is a multi-pass membrane protein in the mitochondrial inner membrane."
  },
  "important_caveats": [
    "The 'mitochondrial membrane' annotation (GO:0031966) is assigned via ISS (inferred from similarity to human TMEM126B), not directly from experimental data for this Drosophila protein. The experimental IDA evidence supports 'mitochondrion' and 'MCIA complex' rather than the membrane qualifier directly.",
    "The N-terminal region lacks a classic cleavable mitochondrial targeting sequence (it contains acidic residues D, E), which is consistent with many inner membrane multi-pass proteins that use internal targeting signals, but makes the mitochondrial assignment less obvious from the N-terminus alone.",
    "The reviewer-only evidence confirms the sequence matches Q9VLM7 (T126_DROME), but this identification was not available to the evaluated model.",
    "The GO term 'host cell mitochondrion' (GO:0033650) could theoretically be considered by a model unfamiliar with its pathogen-specific context, though its definition clearly restricts it to symbiotic/host-pathogen settings."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and D both reference mitochondria, the GO term definitions are distinct: A (host cell mitochondrion) is restricted to pathogen-host contexts and refers to the whole organelle, while D (mitochondrial membrane) is the standard term for membrane-localized mitochondrial proteins. The protein's multi-pass membrane topology specifically supports D over A. No other options are defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9VLM7) annotates this protein as 'Mitochondrion membrane; Multi-pass membrane protein' with evidence ECO:0000250 (similarity to human TMEM126B, Q8IUX1). The GO annotation GO:0031966 (mitochondrial membrane) is assigned via ISS:UniProtKB. Experimental evidence (IDA:FlyBase, PMID 34386730) confirms the protein is in the mitochondrion (GO:0005739) and part of the MCIA complex (GO:0160295), which is defined as part_of the inner mitochondrial membrane (GO:0005743), which is_a mitochondrial membrane (GO:0031966). The specific 'membrane' qualifier is inferred from homology but is consistent with experimental data showing it is a multi-pass membrane protein in the mitochondrial inner membrane.",
    "evidence_ids": ["C5", "C7", "C8", "C6", "GO3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 223-aa sequence contains multiple hydrophobic stretches in the middle and C-terminal regions (e.g., 'GILSALAAGTGAYINNHYRTKLRLGGHGRLSTYLPIVAVPAIFTMLAHKFFIQRPILLNPLGECPVCIQMRSAAFQTSLGIVYPTILAPFAAFLFATRCYTYRIPSITENPREVFLLWRKFTRPIVPALGTLIGLQALLTMFLTG'), indicating a multi-pass transmembrane topology. This eliminates option C (spindle), which is a microtubule-based structure with no membrane association. The absence of a classic N-terminal ER signal peptide (a short hydrophobic core followed by a polar cleavage site) and the overall architecture of a small multi-pass membrane protein without lumenal Golgi-type domains argue against option B (trans-Golgi network membrane), which typically features single-pass or multi-pass proteins with distinct signal peptides and often larger lumenal regions. Option A ('host cell mitochondrion', GO:0033650) is a specialized GO term defined for pathogen-host interaction contexts ('the host is defined as the larger of the organisms involved in a symbiotic interaction'), making it inappropriate for an endogenous cellular protein. Option D (mitochondrial membrane) is the most precise and appropriate annotation for a multi-pass membrane protein with the observed hydrophobic pattern, consistent with known inner mitochondrial membrane multi-pass proteins (e.g., TMEM family members involved in Complex I assembly).",
    "missing_item_specific_fact": "",
    "reason": "The sequence's multi-pass hydrophobic architecture, small size, and lack of ER/Golgi-type signal peptides provide a credible basis for mitochondrial membrane assignment. The specialized nature of the 'host cell mitochondrion' GO term (pathogen context) and the spindle option (non-membrane) can be eliminated using general GO knowledge and protein topology principles. The distinction between mitochondrial membrane and trans-Golgi membrane relies on the multi-pass TM pattern in a small protein without a signal peptide, which is a recognized architectural signature of mitochondrial inner membrane proteins learned from many homologous families."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and D both reference mitochondria, the GO term definitions are distinct: A (host cell mitochondrion) is restricted to pathogen-host contexts and refers to the whole organelle, while D (mitochondrial membrane) is the standard term for membrane-localized mitochondrial proteins. The protein's multi-pass membrane topology specifically supports D over A. No other options are defensible given the sequence features."
  },
  "important_caveats": [
    "The 'mitochondrial membrane' annotation (GO:0031966) is assigned via ISS (inferred from similarity to human TMEM126B), not directly from experimental data for this Drosophila protein. The experimental IDA evidence supports 'mitochondrion' and 'MCIA complex' rather than the membrane qualifier directly.",
    "The N-terminal region lacks a classic cleavable mitochondrial targeting sequence (it contains acidic residues D, E), which is consistent with many inner membrane multi-pass proteins that use internal targeting signals, but makes the mitochondrial assignment less obvious from the N-terminus alone.",
    "The reviewer-only evidence confirms the sequence matches Q9VLM7 (T126_DROME), but this identification was not available to the evaluated model.",
    "The GO term 'host cell mitochondrion' (GO:0033650) could theoretically be considered by a model unfamiliar with its pathogen-specific context, though its definition clearly restricts it to symbiotic/host-pathogen settings."
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
  "benchmark_sequence_length": 223,
  "benchmark_sequence_sha256": "348e261d0e928244343eb91071c92f465eb86fcf296f8991e3baaa5305428ff0",
  "current_entry_audit": {
    "entryVersion": 170,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 223,
  "current_source_sequence_sha256": "348e261d0e928244343eb91071c92f465eb86fcf296f8991e3baaa5305428ff0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 168,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VLM7",
  "selected_historical_entry_version": 168,
  "selected_historical_record_sha256": "aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a",
  "selected_historical_source_sequence_length": 223,
  "selected_historical_source_sequence_sha256": "348e261d0e928244343eb91071c92f465eb86fcf296f8991e3baaa5305428ff0",
  "selected_historical_version": {
    "accession": "Q9VLM7",
    "database": "Swiss-Prot",
    "entryVersion": 168,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "T126_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VLM7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":170,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0032033\",\"source\":\"FlyBase\"}],\"value\":\"Transmembrane protein 126\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"value\":\"dTMEM126B\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IUX1\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0171\",\"value\":\"Mitochondrion membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"id\":\"GO:0160295\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial complex I intermediate assembly complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/32",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031966\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/33",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"id\":\"GO:0005739\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrion\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/34",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Murari A.\",\"Rhooms S.K.\",\"Garcia C.\",\"Liu T.\",\"Li H.\",\"Mishra B.\",\"Deshong C.\",\"Owusu-Ansah E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34386730\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.isci.2021.102869\"}],\"citationType\":\"journal article\",\"firstPage\":\"102869\",\"id\":\"34386730\",\"journal\":\"IScience\",\"lastPage\":\"102869\",\"publicationDate\":\"2021\",\"title\":\"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.\",\"volume\":\"24\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH COMPLEX 1\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:25.958156+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VLM7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)

```json
{
  "entry_version": 168,
  "evidence_id": "H1",
  "excerpt": "ID   T126_DROME              Reviewed;         223 AA.\nAC   Q9VLM7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 168.\nDE   RecName: Full=Transmembrane protein 126 {ECO:0000312|FlyBase:FBgn0032033};\nDE            Short=dTMEM126B {ECO:0000303|PubMed:34386730};\nGN   Name=Tmem126 {ECO:0000312|FlyBase:FBgn0032033};\nGN   ORFNames=CG13392 {ECO:0000312|FlyBase:FBgn0032033};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:30.846128+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a",
  "url": "https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)

```json
{
  "entry_version": 168,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH COMPLEX 1.\nRX   PubMed=34386730; DOI=10.1016/j.isci.2021.102869;\nRA   Murari A., Rhooms S.K., Garcia C., Liu T., Li H., Mishra B., Deshong C.,\nRA   Owusu-Ansah E.;\nRT   \"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in\nRT   mitochondrial complex I biogenesis.\";\nRL   IScience 24:102869-102869(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:30.846128+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a",
  "url": "https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)

```json
{
  "entry_version": 168,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane\nCC       {ECO:0000250|UniProtKB:Q8IUX1}; Multi-pass membrane protein\nCC       {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:30.846128+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a",
  "url": "https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)

```json
{
  "entry_version": 168,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0031966; C:mitochondrial membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:30.846128+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a",
  "url": "https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)

```json
{
  "entry_version": 168,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005739; C:mitochondrion; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:30.846128+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a",
  "url": "https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005743\nname: mitochondrial inner membrane\nnamespace: cellular_component\ndef: \"The inner, i.e. lumen-facing, lipid bilayer of the mitochondrial envelope. It is highly folded to form cristae.\" [GOC:ai]\nsynonym: \"inner mitochondrial membrane\" EXACT []\nsynonym: \"inner mitochondrion membrane\" EXACT []\nsynonym: \"mitochondrion inner membrane\" EXACT []\nxref: NIF_Subcellular:sao1371347282\nxref: Wikipedia:Inner_mitochondrial_membrane\nis_a: GO:0019866 ! organelle inner membrane\nis_a: GO:0031966 ! mitochondrial membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005743",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59031-59043",
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
  "excerpt": "[Term]\nid: GO:0005819\nname: spindle\nnamespace: cellular_component\ndef: \"The array of microtubules and associated molecules that forms between opposite poles of a eukaryotic cell during mitosis or meiosis and serves to move the duplicated chromosomes apart.\" [ISBN:0198547684]\nxref: Wikipedia:Spindle_apparatus\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0015630 ! microtubule cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005819",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59855-59863",
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
  "excerpt": "[Term]\nid: GO:0031966\nname: mitochondrial membrane\nnamespace: cellular_component\ndef: \"Either of the lipid bilayers that surround the mitochondrion and form the mitochondrial envelope.\" [GOC:mah, NIF_Subcellular:sao1045389829]\nxref: NIF_Subcellular:sao1045389829\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005740 ! mitochondrial envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031966",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 181484-181492",
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
  "excerpt": "[Term]\nid: GO:0032588\nname: trans-Golgi network membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding any of the compartments that make up the trans-Golgi network.\" [GOC:mah]\nsynonym: \"Golgi trans face membrane\" RELATED []\nsynonym: \"trans Golgi network membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005802 ! trans-Golgi network\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032588",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 187565-187574",
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
  "excerpt": "[Term]\nid: GO:0033650\nname: host cell mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle as found in host cells that occurs in varying numbers, shapes, and sizes in the cell cytoplasm. The host is defined as the larger of the organisms involved in a symbiotic interaction.\" [GOC:pamgo_curators]\nsynonym: \"host mitochondria\" EXACT []\nis_a: GO:0033648 ! host intracellular membrane-bounded organelle\nis_a: GO:0033655 ! host cell cytoplasm part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0033650",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 199319-199327",
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
  "excerpt": "[Term]\nid: GO:0098800\nname: inner mitochondrial membrane protein complex\nnamespace: cellular_component\ndef: \"Any protein complex that is part of the inner mitochondrial membrane.\" [GOC:dos]\nis_a: GO:0098796 ! membrane protein complex\nis_a: GO:0098798 ! mitochondrial protein-containing complex\nrelationship: part_of GO:0005743 ! mitochondrial inner membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098800",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 411064-411072",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:0160295\nname: mitochondrial complex I intermediate assembly complex\nnamespace: cellular_component\ndef: \"A protein complex involved in mitochondrial respiratory chain complex I (MCI) assembly. The mitochondrial complex I intermediate assembly (MCIA) complex is an inner mitochondrial membrane complex required for the aggregation, arrangement and bonding together of the subunits of the ND2-module of MCI. In humans, the MCIA complex is formed from NDUFAF1, ACAD9, ECSIT, TMEM126B, TMEM186 and COA1.\" [PMID:32320651]\nsynonym: \"MCIA complex\" EXACT []\nsynonym: \"mitochondrial CI assembly complex\" EXACT []\nis_a: GO:0098800 ! inner mitochondrial membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0160295",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 451477-451485",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
