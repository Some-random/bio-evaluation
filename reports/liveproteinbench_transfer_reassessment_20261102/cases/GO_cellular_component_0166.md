# GO_cellular_component_0166

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0166.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — ATP-binding cassette (ABC) transporter complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTLDLTARSDRGRVYWLLADCWNIVRRGLTHYQRQPVNIAWQLGFPILSVLLYGYVFGSAMKVPGGGDYKDFLMPGMFVMTMAFGFINTATLVVYDSTKGVIDRFRSMPMASSAVVAGRGVTDLITACAELAIMMLTAFAMGWRPDGGLGFLGAFGLLLWLRFALIWIGVWLGLLVPNPEAAGGLFAVAFPLTMISSIMVAPQLMPDWLGWVAMWNPISSTAAATRELFGTPVGGDTWVEQHALLMAGVWPVILTLVFLPLAVRRFKKLSR

[Multiple Choices]
A. nuclear periphery
B. cell surface
C. IRE1-TRAF2-ASK1 complex
D. ATP-binding cassette (ABC) transporter complex
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

> The matched sequence has a UniProt GO annotation to the ABC transporter complex (GO:0043190), inferred by InterPro, and is annotated as a daunorubicin-resistance ABC transporter permease. This supports D, though the GO annotation is computational rather than direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 272-aa sequence is strongly multipass and membrane-protein-like, with no evident soluble ATPase domain. Bacterial ABC transporters commonly have separate multipass permease subunits and ATP-binding subunits, so this architecture supports a transporter-complex component (D) over the nuclear or eukaryotic signaling-complex alternatives. This is a family-level, probabilistic inference; multipass architecture alone does not uniquely identify ABC transporters.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from the sequence architecture and general organization of bacterial ABC transporters meaningfully favors D among these choices. Exact target annotation is not necessary for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> D describes the protein's likely complex membership, while B can describe an integral protein at the cell surface. These cellular-component descriptions need not be mutually exclusive, and the prompt does not specify whether it seeks complex membership or membrane/surface location.


### Important caveats

- The sequence-matched GO annotation for D is IEA:InterPro, not direct experimental localization or complex-membership evidence.
- The source also describes the protein as a multipass cell-membrane protein; its subcellular-location annotation is transferred by similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 272-aa sequence is strongly multipass and membrane-protein-like, with no evident soluble ATPase domain. Bacterial ABC transporters commonly have separate multipass permease subunits and ATP-binding subunits, so this architecture supports a transporter-complex component (D) over the nuclear or eukaryotic signaling-complex alternatives. This is a family-level, probabilistic inference; multipass architecture alone does not uniquely identify ABC transporters.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the sequence architecture and general organization of bacterial ABC transporters meaningfully favors D among these choices. Exact target annotation is not necessary for that inference."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation to the ABC transporter complex (GO:0043190), inferred by InterPro, and is annotated as a daunorubicin-resistance ABC transporter permease. This supports D, though the GO annotation is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The sequence-matched GO annotation for D is IEA:InterPro, not direct experimental localization or complex-membership evidence.",
    "The source also describes the protein as a multipass cell-membrane protein; its subcellular-location annotation is transferred by similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "D describes the protein's likely complex membership, while B can describe an integral protein at the cell surface. These cellular-component descriptions need not be mutually exclusive, and the prompt does not specify whether it seeks complex membership or membrane/surface location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation to the ABC transporter complex (GO:0043190), inferred by InterPro, and is annotated as a daunorubicin-resistance ABC transporter permease. This supports D, though the GO annotation is computational rather than direct experimental evidence.",
    "evidence_ids": ["C4", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 272-aa sequence is strongly multipass and membrane-protein-like, with no evident soluble ATPase domain. Bacterial ABC transporters commonly have separate multipass permease subunits and ATP-binding subunits, so this architecture supports a transporter-complex component (D) over the nuclear or eukaryotic signaling-complex alternatives. This is a family-level, probabilistic inference; multipass architecture alone does not uniquely identify ABC transporters.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the sequence architecture and general organization of bacterial ABC transporters meaningfully favors D among these choices. Exact target annotation is not necessary for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "D describes the protein's likely complex membership, while B can describe an integral protein at the cell surface. These cellular-component descriptions need not be mutually exclusive, and the prompt does not specify whether it seeks complex membership or membrane/surface location."
  },
  "important_caveats": [
    "The sequence-matched GO annotation for D is IEA:InterPro, not direct experimental localization or complex-membership evidence.",
    "The source also describes the protein as a multipass cell-membrane protein; its subcellular-location annotation is transferred by similarity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU6 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' from Streptomyces coeruleorubidus. The GO term GO:0043190 (ABC transporter complex) is assigned with IEA:InterPro evidence, and the subcellular location is 'Cell membrane; Multi-pass membrane protein' (ECO:0000250 by similarity to P32011). A 2024 publication (PubMed:39375957) confirms function in daunorubicin efflux via ABC transporters. The annotation is computational/similarity-based rather than direct experimental localization, but the protein's identity as an ABC permease is well-supported by literature.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 272 aa, highly hydrophobic, with approximately 6-8 long hydrophobic stretches consistent with multi-pass transmembrane helices, and lacks any Walker A/B or nucleotide-binding motifs. This architecture is the hallmark of the transmembrane permease component of ABC transporters (e.g., MsbA, DrrB, MacB permeases), which are typically 200-400 aa multi-TM proteins that partner with separate NBD subunits. Bacterial origin (inferred from the sequence lacking eukaryotic features and the overall composition) immediately eliminates A (nuclear periphery — no nucleus in bacteria) and C (IRE1-TRAF2-ASK1 complex — an ER-specific eukaryotic signaling complex). Between B (cell surface) and D (ABC transporter complex): 'cell surface' (GO:0009986) is defined for gene products 'attached to the plasma membrane or cell wall,' typically surface-exposed or single-pass proteins. The multi-pass TM topology with characteristic ABC-permease helix spacing and the specific size (~270 aa) are far more consistent with an integral transporter permease than a generic surface-attached protein. Knowledge of other ABC permeases (Pfam PF01061, ABC transporter permease family) provides a transferable signature that distinguishes this from a generic membrane protein, making D the most specific and appropriate choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of ABC transporter permease architecture (multi-TM, ~250-350 aa, no NBD motifs, characteristic helix spacing) can recognize this sequence as an ABC permease component. Bacterial context eliminates eukaryotic-specific options. The multi-pass integral membrane topology distinguishes D from the more generic 'cell surface' option B. This is a family-level inference from other ABC transporters, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B"
]
```

> Option B (cell surface) is technically applicable since the protein is integrated in the plasma membrane of a bacterium, and GO:0009986 covers membrane-integrated proteins. However, GO annotation practice favors the most specific applicable term, and the multi-pass transporter architecture makes D clearly more appropriate. B is a defensible but less specific choice; a well-informed model should prefer D.


### Important caveats

- The GO:0043190 annotation is IEA:InterPro (automated computational assignment based on domain match), not direct experimental evidence of complex membership.
- The subcellular location annotation uses similarity-based evidence (ECO:0000250|UniProtKB:P32011), transferring from a related ABC transporter.
- The protein was only integrated into Swiss-Prot in February 2025; the benchmark may have used TrEMBL or pre-publication data.
- The GO term 'cell surface' (GO:0009986) is broad enough to technically encompass membrane-integrated proteins, creating mild overlap with D, though GO specificity conventions resolve this.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 272 aa, highly hydrophobic, with approximately 6-8 long hydrophobic stretches consistent with multi-pass transmembrane helices, and lacks any Walker A/B or nucleotide-binding motifs. This architecture is the hallmark of the transmembrane permease component of ABC transporters (e.g., MsbA, DrrB, MacB permeases), which are typically 200-400 aa multi-TM proteins that partner with separate NBD subunits. Bacterial origin (inferred from the sequence lacking eukaryotic features and the overall composition) immediately eliminates A (nuclear periphery — no nucleus in bacteria) and C (IRE1-TRAF2-ASK1 complex — an ER-specific eukaryotic signaling complex). Between B (cell surface) and D (ABC transporter complex): 'cell surface' (GO:0009986) is defined for gene products 'attached to the plasma membrane or cell wall,' typically surface-exposed or single-pass proteins. The multi-pass TM topology with characteristic ABC-permease helix spacing and the specific size (~270 aa) are far more consistent with an integral transporter permease than a generic surface-attached protein. Knowledge of other ABC permeases (Pfam PF01061, ABC transporter permease family) provides a transferable signature that distinguishes this from a generic membrane protein, making D the most specific and appropriate choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of ABC transporter permease architecture (multi-TM, ~250-350 aa, no NBD motifs, characteristic helix spacing) can recognize this sequence as an ABC permease component. Bacterial context eliminates eukaryotic-specific options. The multi-pass integral membrane topology distinguishes D from the more generic 'cell surface' option B. This is a family-level inference from other ABC transporters, not a lookup of this specific protein's record."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU6 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' from Streptomyces coeruleorubidus. The GO term GO:0043190 (ABC transporter complex) is assigned with IEA:InterPro evidence, and the subcellular location is 'Cell membrane; Multi-pass membrane protein' (ECO:0000250 by similarity to P32011). A 2024 publication (PubMed:39375957) confirms function in daunorubicin efflux via ABC transporters. The annotation is computational/similarity-based rather than direct experimental localization, but the protein's identity as an ABC permease is well-supported by literature."
  },
  "important_caveats": [
    "The GO:0043190 annotation is IEA:InterPro (automated computational assignment based on domain match), not direct experimental evidence of complex membership.",
    "The subcellular location annotation uses similarity-based evidence (ECO:0000250|UniProtKB:P32011), transferring from a related ABC transporter.",
    "The protein was only integrated into Swiss-Prot in February 2025; the benchmark may have used TrEMBL or pre-publication data.",
    "The GO term 'cell surface' (GO:0009986) is broad enough to technically encompass membrane-integrated proteins, creating mild overlap with D, though GO specificity conventions resolve this."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B"
    ],
    "reason": "Option B (cell surface) is technically applicable since the protein is integrated in the plasma membrane of a bacterium, and GO:0009986 covers membrane-integrated proteins. However, GO annotation practice favors the most specific applicable term, and the multi-pass transporter architecture makes D clearly more appropriate. B is a defensible but less specific choice; a well-informed model should prefer D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU6 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' from Streptomyces coeruleorubidus. The GO term GO:0043190 (ABC transporter complex) is assigned with IEA:InterPro evidence, and the subcellular location is 'Cell membrane; Multi-pass membrane protein' (ECO:0000250 by similarity to P32011). A 2024 publication (PubMed:39375957) confirms function in daunorubicin efflux via ABC transporters. The annotation is computational/similarity-based rather than direct experimental localization, but the protein's identity as an ABC permease is well-supported by literature.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 272 aa, highly hydrophobic, with approximately 6-8 long hydrophobic stretches consistent with multi-pass transmembrane helices, and lacks any Walker A/B or nucleotide-binding motifs. This architecture is the hallmark of the transmembrane permease component of ABC transporters (e.g., MsbA, DrrB, MacB permeases), which are typically 200-400 aa multi-TM proteins that partner with separate NBD subunits. Bacterial origin (inferred from the sequence lacking eukaryotic features and the overall composition) immediately eliminates A (nuclear periphery — no nucleus in bacteria) and C (IRE1-TRAF2-ASK1 complex — an ER-specific eukaryotic signaling complex). Between B (cell surface) and D (ABC transporter complex): 'cell surface' (GO:0009986) is defined for gene products 'attached to the plasma membrane or cell wall,' typically surface-exposed or single-pass proteins. The multi-pass TM topology with characteristic ABC-permease helix spacing and the specific size (~270 aa) are far more consistent with an integral transporter permease than a generic surface-attached protein. Knowledge of other ABC permeases (Pfam PF01061, ABC transporter permease family) provides a transferable signature that distinguishes this from a generic membrane protein, making D the most specific and appropriate choice.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of ABC transporter permease architecture (multi-TM, ~250-350 aa, no NBD motifs, characteristic helix spacing) can recognize this sequence as an ABC permease component. Bacterial context eliminates eukaryotic-specific options. The multi-pass integral membrane topology distinguishes D from the more generic 'cell surface' option B. This is a family-level inference from other ABC transporters, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B"],
    "reason": "Option B (cell surface) is technically applicable since the protein is integrated in the plasma membrane of a bacterium, and GO:0009986 covers membrane-integrated proteins. However, GO annotation practice favors the most specific applicable term, and the multi-pass transporter architecture makes D clearly more appropriate. B is a defensible but less specific choice; a well-informed model should prefer D."
  },
  "important_caveats": [
    "The GO:0043190 annotation is IEA:InterPro (automated computational assignment based on domain match), not direct experimental evidence of complex membership.",
    "The subcellular location annotation uses similarity-based evidence (ECO:0000250|UniProtKB:P32011), transferring from a related ABC transporter.",
    "The protein was only integrated into Swiss-Prot in February 2025; the benchmark may have used TrEMBL or pre-publication data.",
    "The GO term 'cell surface' (GO:0009986) is broad enough to technically encompass membrane-integrated proteins, creating mild overlap with D, though GO specificity conventions resolve this."
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
  "benchmark_sequence_length": 272,
  "benchmark_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 272,
  "current_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU6",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "selected_historical_source_sequence_length": 272,
  "selected_historical_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "selected_historical_version": {
    "accession": "P0DXU6",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB2_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32011\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0043190\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:ATP-binding cassette (ABC) transporter complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRB2_STRC4             Reviewed;         272 AA.\nAC   P0DXU6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB2 {ECO:0000305};\nGN   Name=drrB2 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_15990 {ECO:0000312|EMBL:WOT35540.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32011};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0043190; C:ATP-binding cassette (ABC) transporter complex; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
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

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0034399\nname: nuclear periphery\nnamespace: cellular_component\ndef: \"The portion of the nuclear lumen proximal to the inner nuclear membrane.\" [GOC:krc, GOC:mah]\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0031981 ! nuclear lumen\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034399",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 208650-208657",
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
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244782-244797",
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
  "excerpt": "[Term]\nid: GO:1990604\nname: IRE1-TRAF2-ASK1 complex\nnamespace: cellular_component\ndef: \"A protein complex of the endoplasmic reticulum membrane that consists of IRE1 (Inositol-requiring enzyme-1), TRAF2 (TNF receptor-associated factor 2) and ASK1 (Apoptosis signal-regulating kinase 1, a MAP3K).\" [GOC:bf, GOC:PARL, PMID:12050113, PMID:23000344]\nsynonym: \"ERN1-TRAF2-ASK1 complex\" RELATED [HGNC:3449]\nis_a: GO:0098796 ! membrane protein complex\nis_a: GO:0140534 ! endoplasmic reticulum protein-containing complex\nrelationship: part_of GO:0005789 ! endoplasmic reticulum membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990604",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 553487-553496",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
