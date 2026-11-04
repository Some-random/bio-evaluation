# GO_cellular_component_0151

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0151.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — mitochondrion

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQLRSKVISLYKHLQYLGREYPGLNGPQKFRKQIHDAFMNHKDEQDPKKIVALLAQGRYLAKEVEALYSLKKYRSVKQRYSYND

[Multiple Choices]
A. mitochondrial inner membrane
B. incipient cellular bud site
C. mitochondrion
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

> The supplied sequence exactly matches the historical and current UniProt record, which assigns the protein to the mitochondrion. The localization annotation is transferred by similarity, and the GO annotation is supported by sequence similarity, so this supports the key but is not direct experimental localization evidence.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short sequence has an N-terminal region rich in basic and hydrophobic residues, consistent with a mitochondrial targeting peptide. It lacks a long hydrophobic transmembrane segment and the characteristic large domain architecture of an ABC transporter, making mitochondrial inner membrane or ABC-complex localization less likely than the broader mitochondrion option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A plausible transferable targeting-signal inference favors the mitochondrion among these choices. It is probabilistic: sequence alone does not establish localization experimentally or completely rule out membrane association.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based mitochondrial targeting inference favors C; the more specific inner-membrane choice is not supported by an evident transmembrane segment.


### Important caveats

- The reviewer-only localization annotation is based on similarity, not direct experimental evidence in the supplied excerpts.
- A targeting-signal prediction is not definitive proof of the protein's cellular location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence has an N-terminal region rich in basic and hydrophobic residues, consistent with a mitochondrial targeting peptide. It lacks a long hydrophobic transmembrane segment and the characteristic large domain architecture of an ABC transporter, making mitochondrial inner membrane or ABC-complex localization less likely than the broader mitochondrion option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A plausible transferable targeting-signal inference favors the mitochondrion among these choices. It is probabilistic: sequence alone does not establish localization experimentally or completely rule out membrane association."
  },
  "case_id": "GO_cellular_component_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt record, which assigns the protein to the mitochondrion. The localization annotation is transferred by similarity, and the GO annotation is supported by sequence similarity, so this supports the key but is not direct experimental localization evidence."
  },
  "important_caveats": [
    "The reviewer-only localization annotation is based on similarity, not direct experimental evidence in the supplied excerpts.",
    "A targeting-signal prediction is not definitive proof of the protein's cellular location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based mitochondrial targeting inference favors C; the more specific inner-membrane choice is not supported by an evident transmembrane segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt record, which assigns the protein to the mitochondrion. The localization annotation is transferred by similarity, and the GO annotation is supported by sequence similarity, so this supports the key but is not direct experimental localization evidence.",
    "evidence_ids": ["H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence has an N-terminal region rich in basic and hydrophobic residues, consistent with a mitochondrial targeting peptide. It lacks a long hydrophobic transmembrane segment and the characteristic large domain architecture of an ABC transporter, making mitochondrial inner membrane or ABC-complex localization less likely than the broader mitochondrion option.",
    "missing_item_specific_fact": "",
    "reason": "A plausible transferable targeting-signal inference favors the mitochondrion among these choices. It is probabilistic: sequence alone does not establish localization experimentally or completely rule out membrane association."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based mitochondrial targeting inference favors C; the more specific inner-membrane choice is not supported by an evident transmembrane segment."
  },
  "important_caveats": [
    "The reviewer-only localization annotation is based on similarity, not direct experimental evidence in the supplied excerpts.",
    "A targeting-signal prediction is not definitive proof of the protein's cellular location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9VJG4) annotates subcellular location as 'Mitochondrion' (GO:0005739) with evidence code ECO:0000250 (ISS, inferred from sequence similarity to human ETFRF1/Q6IPR1). The GO cross-reference confirms C:mitochondrion. While the evidence is computational (sequence-similarity transfer) rather than direct experimental localization, it does support the expected answer C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish C from the alternatives. (1) The N-terminal ~30 residues (MSQLRSKVISLYKHLQYLGREYPGLNGPQKFRKQ) show enrichment in basic residues (R,K) and hydroxylated residues (S) with very few acidic residues — a pattern consistent with a mitochondrial targeting sequence (MTS) recognized across eukaryotic mitochondrial proteins. (2) The sequence is only 85 amino acids and contains no long hydrophobic stretches characteristic of transmembrane domains, arguing against 'mitochondrial inner membrane' (A), which requires integral membrane anchoring. (3) 'Incipient cellular bud site' (B) is a yeast-specific term (GO:0000131, defined for budding yeast plasma membrane); a knowledgeable model recognizes this as inapplicable to a general eukaryotic protein. (4) 'ABC transporter complex' (D) requires large multi-domain proteins with nucleotide-binding and transmembrane domains; an 85-residue protein is far too small and lacks any ABC-like motifs. (5) If the model recognizes the ETFRF1 family (electron transfer flavoprotein regulatory factors), these are known to be small soluble or loosely-associated mitochondrial matrix proteins in multiple organisms, further supporting 'mitochondrion' over 'inner membrane.'


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The N-terminal basic/hydroxylated residue pattern provides a recognizable MTS signal transferable from knowledge of many mitochondrial proteins. The absence of transmembrane helices distinguishes 'mitochondrion' (soluble) from 'mitochondrial inner membrane' (integral). Options B and D are eliminated by general biological knowledge (yeast-specific term; size/domain requirements for ABC transporters). Together these provide a concrete, credible inference chain from sequence features and family-level knowledge to answer C, without requiring recall of this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly eliminable (yeast-specific term; far too small for an ABC transporter). The C-vs-A distinction is the most challenging, but the absence of transmembrane domains and the small soluble-protein character of ETFRF1 homologs provide a reasonable basis to prefer 'mitochondrion' over 'mitochondrial inner membrane.' No two options are equally defensible given the sequence features.


### Important caveats

- The UniProt annotation for mitochondrial localization is ISS (inferred from sequence similarity), not direct experimental evidence. The human homolog ETFRF1 (Q6IPR1) serves as the transfer source.
- The N-terminal MTS signal in this sequence is present but relatively weak compared to canonical mitochondrial targeting sequences; the inference relies partly on family-level knowledge of ETFRF1 homologs.
- The original model input does not include organism identity; elimination of option B relies on recognizing 'incipient cellular bud site' as a yeast-specific term, which is transferable knowledge.
- The reviewer-only evidence confirms sequence match to Q9VJG4 (Drosophila melanogaster, 85 aa), but this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish C from the alternatives. (1) The N-terminal ~30 residues (MSQLRSKVISLYKHLQYLGREYPGLNGPQKFRKQ) show enrichment in basic residues (R,K) and hydroxylated residues (S) with very few acidic residues — a pattern consistent with a mitochondrial targeting sequence (MTS) recognized across eukaryotic mitochondrial proteins. (2) The sequence is only 85 amino acids and contains no long hydrophobic stretches characteristic of transmembrane domains, arguing against 'mitochondrial inner membrane' (A), which requires integral membrane anchoring. (3) 'Incipient cellular bud site' (B) is a yeast-specific term (GO:0000131, defined for budding yeast plasma membrane); a knowledgeable model recognizes this as inapplicable to a general eukaryotic protein. (4) 'ABC transporter complex' (D) requires large multi-domain proteins with nucleotide-binding and transmembrane domains; an 85-residue protein is far too small and lacks any ABC-like motifs. (5) If the model recognizes the ETFRF1 family (electron transfer flavoprotein regulatory factors), these are known to be small soluble or loosely-associated mitochondrial matrix proteins in multiple organisms, further supporting 'mitochondrion' over 'inner membrane.'",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal basic/hydroxylated residue pattern provides a recognizable MTS signal transferable from knowledge of many mitochondrial proteins. The absence of transmembrane helices distinguishes 'mitochondrion' (soluble) from 'mitochondrial inner membrane' (integral). Options B and D are eliminated by general biological knowledge (yeast-specific term; size/domain requirements for ABC transporters). Together these provide a concrete, credible inference chain from sequence features and family-level knowledge to answer C, without requiring recall of this exact protein's database annotation."
  },
  "case_id": "GO_cellular_component_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9VJG4) annotates subcellular location as 'Mitochondrion' (GO:0005739) with evidence code ECO:0000250 (ISS, inferred from sequence similarity to human ETFRF1/Q6IPR1). The GO cross-reference confirms C:mitochondrion. While the evidence is computational (sequence-similarity transfer) rather than direct experimental localization, it does support the expected answer C."
  },
  "important_caveats": [
    "The UniProt annotation for mitochondrial localization is ISS (inferred from sequence similarity), not direct experimental evidence. The human homolog ETFRF1 (Q6IPR1) serves as the transfer source.",
    "The N-terminal MTS signal in this sequence is present but relatively weak compared to canonical mitochondrial targeting sequences; the inference relies partly on family-level knowledge of ETFRF1 homologs.",
    "The original model input does not include organism identity; elimination of option B relies on recognizing 'incipient cellular bud site' as a yeast-specific term, which is transferable knowledge.",
    "The reviewer-only evidence confirms sequence match to Q9VJG4 (Drosophila melanogaster, 85 aa), but this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly eliminable (yeast-specific term; far too small for an ABC transporter). The C-vs-A distinction is the most challenging, but the absence of transmembrane domains and the small soluble-protein character of ETFRF1 homologs provide a reasonable basis to prefer 'mitochondrion' over 'mitochondrial inner membrane.' No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9VJG4) annotates subcellular location as 'Mitochondrion' (GO:0005739) with evidence code ECO:0000250 (ISS, inferred from sequence similarity to human ETFRF1/Q6IPR1). The GO cross-reference confirms C:mitochondrion. While the evidence is computational (sequence-similarity transfer) rather than direct experimental localization, it does support the expected answer C.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish C from the alternatives. (1) The N-terminal ~30 residues (MSQLRSKVISLYKHLQYLGREYPGLNGPQKFRKQ) show enrichment in basic residues (R,K) and hydroxylated residues (S) with very few acidic residues — a pattern consistent with a mitochondrial targeting sequence (MTS) recognized across eukaryotic mitochondrial proteins. (2) The sequence is only 85 amino acids and contains no long hydrophobic stretches characteristic of transmembrane domains, arguing against 'mitochondrial inner membrane' (A), which requires integral membrane anchoring. (3) 'Incipient cellular bud site' (B) is a yeast-specific term (GO:0000131, defined for budding yeast plasma membrane); a knowledgeable model recognizes this as inapplicable to a general eukaryotic protein. (4) 'ABC transporter complex' (D) requires large multi-domain proteins with nucleotide-binding and transmembrane domains; an 85-residue protein is far too small and lacks any ABC-like motifs. (5) If the model recognizes the ETFRF1 family (electron transfer flavoprotein regulatory factors), these are known to be small soluble or loosely-associated mitochondrial matrix proteins in multiple organisms, further supporting 'mitochondrion' over 'inner membrane.'",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal basic/hydroxylated residue pattern provides a recognizable MTS signal transferable from knowledge of many mitochondrial proteins. The absence of transmembrane helices distinguishes 'mitochondrion' (soluble) from 'mitochondrial inner membrane' (integral). Options B and D are eliminated by general biological knowledge (yeast-specific term; size/domain requirements for ABC transporters). Together these provide a concrete, credible inference chain from sequence features and family-level knowledge to answer C, without requiring recall of this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly eliminable (yeast-specific term; far too small for an ABC transporter). The C-vs-A distinction is the most challenging, but the absence of transmembrane domains and the small soluble-protein character of ETFRF1 homologs provide a reasonable basis to prefer 'mitochondrion' over 'mitochondrial inner membrane.' No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation for mitochondrial localization is ISS (inferred from sequence similarity), not direct experimental evidence. The human homolog ETFRF1 (Q6IPR1) serves as the transfer source.",
    "The N-terminal MTS signal in this sequence is present but relatively weak compared to canonical mitochondrial targeting sequences; the inference relies partly on family-level knowledge of ETFRF1 homologs.",
    "The original model input does not include organism identity; elimination of option B relies on recognizing 'incipient cellular bud site' as a yeast-specific term, which is transferable knowledge.",
    "The reviewer-only evidence confirms sequence match to Q9VJG4 (Drosophila melanogaster, 85 aa), but this accession was not provided to the evaluated model."
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
  "benchmark_sequence_length": 85,
  "benchmark_sequence_sha256": "1645a0a62f1211cc106090fa5945a364fd15e8e74f73247dd11c9ebd4f70b58a",
  "current_entry_audit": {
    "entryVersion": 164,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 85,
  "current_source_sequence_sha256": "1645a0a62f1211cc106090fa5945a364fd15e8e74f73247dd11c9ebd4f70b58a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 162,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VJG4",
  "selected_historical_entry_version": 162,
  "selected_historical_record_sha256": "53096b2cc0cdd502971cca842ec36d0b3923386eee99f28ec2d15bb1fcf2170a",
  "selected_historical_source_sequence_length": 85,
  "selected_historical_source_sequence_sha256": "1645a0a62f1211cc106090fa5945a364fd15e8e74f73247dd11c9ebd4f70b58a",
  "selected_historical_version": {
    "accession": "Q9VJG4",
    "database": "Swiss-Prot",
    "entryVersion": 162,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ETFR1_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VJG4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":164,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36266680\",\"source\":\"PubMed\"}],\"value\":\"Protein orsai\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Electron transfer flavoprotein regulatory factor 1 homolog\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q6IPR1\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0173\",\"value\":\"Mitochondrion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005739\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrion\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/31",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJG4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Fernandez-Acosta M.\",\"Romero J.I.\",\"Bernabo G.\",\"Velazquez-Campos G.M.\",\"Gonzalez N.\",\"Mares M.L.\",\"Werbajh S.\",\"Avendano-Vazquez L.A.\",\"Rechberger G.N.\",\"Kuehnlein R.P.\",\"Marino-Buslje C.\",\"Cantera R.\",\"Rezaval C.\",\"Ceriani M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36266680\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12915-022-01417-w\"}],\"citationType\":\"journal article\",\"firstPage\":\"233\",\"id\":\"36266680\",\"journal\":\"BMC Biol.\",\"lastPage\":\"233\",\"publicationDate\":\"2022\",\"title\":\"orsai, the Drosophila homolog of human ETFRF1, links lipid catabolism to growth control.\",\"volume\":\"20\"},\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:25.548922+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3430179ea3593ebb0189732146e49a9d0f3e62dbafa01159d32b97a3ab4c6c72",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJG4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H1",
  "excerpt": "ID   ETFR1_DROME             Reviewed;          85 AA.\nAC   Q9VJG4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 162.\nDE   RecName: Full=Electron transfer flavoprotein regulatory factor 1 homolog {ECO:0000305};\nDE   AltName: Full=Protein orsai {ECO:0000303|PubMed:36266680};\nGN   Name=osi {ECO:0000303|PubMed:36266680, ECO:0000312|FlyBase:FBgn0040985};\nGN   ORFNames=CG6115 {ECO:0000312|FlyBase:FBgn0040985};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:34.217162+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "53096b2cc0cdd502971cca842ec36d0b3923386eee99f28ec2d15bb1fcf2170a",
  "url": "https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H2",
  "excerpt": "RN   [5]\nRP   FUNCTION, TISSUE SPECIFICITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=36266680; DOI=10.1186/s12915-022-01417-w;\nRA   Fernandez-Acosta M., Romero J.I., Bernabo G., Velazquez-Campos G.M.,\nRA   Gonzalez N., Mares M.L., Werbajh S., Avendano-Vazquez L.A.,\nRA   Rechberger G.N., Kuehnlein R.P., Marino-Buslje C., Cantera R., Rezaval C.,\nRA   Ceriani M.F.;\nRT   \"orsai, the Drosophila homolog of human ETFRF1, links lipid catabolism to\nRT   growth control.\";\nRL   BMC Biol. 20:233-233(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:34.217162+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "53096b2cc0cdd502971cca842ec36d0b3923386eee99f28ec2d15bb1fcf2170a",
  "url": "https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000250|UniProtKB:Q6IPR1}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:34.217162+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "53096b2cc0cdd502971cca842ec36d0b3923386eee99f28ec2d15bb1fcf2170a",
  "url": "https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005739; C:mitochondrion; ISS:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:34.217162+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "53096b2cc0cdd502971cca842ec36d0b3923386eee99f28ec2d15bb1fcf2170a",
  "url": "https://rest.uniprot.org/unisave/Q9VJG4?format=txt&versions=162"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000131\nname: incipient cellular bud site\nnamespace: cellular_component\ndef: \"The portion of the budding yeast plasma membrane where a daughter cell will emerge. The yeast marks this spot with bud-site selection proteins before bud emergence occurs. Actin is polarized to this spot just prior to and during bud emergence.\" [GOC:clt]\nis_a: GO:0030427 ! site of polarized growth\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000131",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1308-1314",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
