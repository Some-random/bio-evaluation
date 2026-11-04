# GO_molecular_function_0181

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0181.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — metal ion binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTNKELQAIRKLLMLDVSEAAEHIGRVSARSWQYWESGRSAVPDDVEQEMLDLASVRIEMMSAIDKRLADGERPKLRFYNKLDEYLADNPDHNVIGWRLSQSVAALYYTEGHADLI

[Multiple Choices]
A. ADP binding
B. metal ion binding
C. sodium channel inhibitor activity
D. carboxylesterase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns metal ion binding, but the assignment is IEA (computational annotation). A cited crystal structure is also described as being in complex with Mg2+, supporting metal association. The record's experimentally supported functional description emphasizes DNA/RNA binding and repression, so the evidence does not establish metal binding as the protein's primary biological activity.

Citations as saved: [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this exact protein is annotated for metal ion binding or binds Mg2+ in the reported structure; neither is evident from a clear metal-binding sequence motif.


**Reason**

> The small, helix-rich sequence and lack of an obvious nucleotide-binding motif or enzyme catalytic motif make ADP binding and carboxylesterase activity poor fits; there is also no clear basis for sodium-channel inhibition. But those exclusions do not positively distinguish metal ion binding. The sequence does not supply a recognizable metal-binding feature, and the more likely regulatory/nucleic-acid-binding activity is not offered. Choosing B therefore depends on the item-specific annotation or structural fact, not a meaningful transferable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the other listed choices is comparably supported by the sequence. However, the choices omit the nucleic-acid-binding function described in the source evidence, and the source does not establish metal binding as the primary activity.


### Important caveats

- The GO metal-ion-binding assignment is computational (IEA), not direct experimental evidence of a primary function.
- The Mg2+ structural description supports metal association but alone does not show that metal binding is the protein's central biological activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this exact protein is annotated for metal ion binding or binds Mg2+ in the reported structure; neither is evident from a clear metal-binding sequence motif.",
    "reason": "The small, helix-rich sequence and lack of an obvious nucleotide-binding motif or enzyme catalytic motif make ADP binding and carboxylesterase activity poor fits; there is also no clear basis for sodium-channel inhibition. But those exclusions do not positively distinguish metal ion binding. The sequence does not supply a recognizable metal-binding feature, and the more likely regulatory/nucleic-acid-binding activity is not offered. Choosing B therefore depends on the item-specific annotation or structural fact, not a meaningful transferable inference."
  },
  "case_id": "GO_molecular_function_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns metal ion binding, but the assignment is IEA (computational annotation). A cited crystal structure is also described as being in complex with Mg2+, supporting metal association. The record's experimentally supported functional description emphasizes DNA/RNA binding and repression, so the evidence does not establish metal binding as the protein's primary biological activity."
  },
  "important_caveats": [
    "The GO metal-ion-binding assignment is computational (IEA), not direct experimental evidence of a primary function.",
    "The Mg2+ structural description supports metal association but alone does not show that metal binding is the protein's central biological activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the other listed choices is comparably supported by the sequence. However, the choices omit the nucleic-acid-binding function described in the source evidence, and the source does not establish metal binding as the primary activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns metal ion binding, but the assignment is IEA (computational annotation). A cited crystal structure is also described as being in complex with Mg2+, supporting metal association. The record's experimentally supported functional description emphasizes DNA/RNA binding and repression, so the evidence does not establish metal binding as the protein's primary biological activity.",
    "evidence_ids": ["C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this exact protein is annotated for metal ion binding or binds Mg2+ in the reported structure; neither is evident from a clear metal-binding sequence motif.",
    "reason": "The small, helix-rich sequence and lack of an obvious nucleotide-binding motif or enzyme catalytic motif make ADP binding and carboxylesterase activity poor fits; there is also no clear basis for sodium-channel inhibition. But those exclusions do not positively distinguish metal ion binding. The sequence does not supply a recognizable metal-binding feature, and the more likely regulatory/nucleic-acid-binding activity is not offered. Choosing B therefore depends on the item-specific annotation or structural fact, not a meaningful transferable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the other listed choices is comparably supported by the sequence. However, the choices omit the nucleic-acid-binding function described in the source evidence, and the source does not establish metal binding as the primary activity."
  },
  "important_caveats": [
    "The GO metal-ion-binding assignment is computational (IEA), not direct experimental evidence of a primary function.",
    "The Mg2+ structural description supports metal association but alone does not show that metal binding is the protein's central biological activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (H9C180, Aca2 repressor) carries GO:0046872 (metal ion binding) with IEA:UniProtKB-KW evidence. More importantly, the crystal structures PDB 7VJO and 7VJP were solved at 1.31 Å in complex with Mg(2+), providing direct experimental evidence that this protein coordinates a metal ion. Although the protein's primary molecular function is DNA/RNA binding (as a transcriptional repressor), neither DNA binding nor RNA binding appears among the answer choices. Among the four offered options, metal ion binding is the only one actually annotated and experimentally supported for this protein. The annotation evidence code is IEA (inferred from keyword), but the co-crystal structure with Mg2+ elevates the support beyond mere annotation.

Citations as saved: [C7](#evidence-c7), [C10](#evidence-c10), [H3](#evidence-h3), [H7](#evidence-h7), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply elimination and positive inference from sequence features. (1) ADP binding (A) requires motifs such as Walker A (GxxxxGK&#91;T/S&#93;) or a Rossmann-fold β-sheet; none are present in this 116-aa sequence. (2) Sodium channel inhibitor activity (C) is characteristic of small disulfide-knottin peptides (scorpion toxins, conotoxins) with a rigid Cys-rich scaffold; this sequence lacks the dense cysteine spacing and knottin topology. (3) Carboxylesterase activity (D) requires the GXSXG serine-hydrolase catalytic motif and typically a much larger fold (400–600 aa); this 116-aa protein has no GXSXG and is far too small. (4) The central region (~residues 25–70) displays a helix-turn-helix (HTH) pattern recognizable from hydrophobic/charged periodicity, a motif well known from many transcriptional regulators (e.g., lambda Cro, T4 Rep, and numerous bacterial HTH repressors) that frequently coordinate a structural metal ion (Zn2+ or Mg2+) to stabilize the fold. Thus, by eliminating A, C, and D on motif grounds and recognizing HTH-associated metal coordination as a common feature of this protein family, B is the most defensible choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of three options relies on well-established, transferable knowledge about the structural motifs required for ADP binding, sodium channel inhibition, and carboxylesterase catalysis—none of which are present in the sequence. The positive inference toward metal ion binding draws on the widely recognized association between HTH domains and metal coordination, a pattern learned from many other HTH proteins. This constitutes a concrete, transferable argument that meaningfully distinguishes B from the other three choices without requiring knowledge of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D each require specific structural motifs or fold features (Walker A/Rossmann, knottin disulfide scaffold, GXSXG catalytic triad in a large esterase fold) that are clearly absent from this 116-aa sequence. Option B is the only choice consistent with the protein's size, composition, and recognizable HTH-like architecture. No other option is defensible given the sequence.


### Important caveats

- The GO metal ion binding annotation carries IEA:UniProtKB-KW evidence (inferred from keyword), not a direct experimental GO assignment; however, the co-crystal structures with Mg2+ (PDB 7VJO, 7VJP) provide independent experimental support for metal coordination.
- The protein's primary molecular function is DNA binding and RNA binding (as a repressor of the acrIF8-aca2 operon); metal ion binding is a secondary structural role. The question's framing as 'primary molecular function' is slightly imprecise, but since DNA/RNA binding are not among the choices, B is the best available answer.
- The HTH motif recognition from a raw 116-aa sequence without structural context is a moderate-confidence inference; it is supported by the crystal structures but is not trivially obvious from sequence alone for every model.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt H9C180 across both current and archived (v36) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply elimination and positive inference from sequence features. (1) ADP binding (A) requires motifs such as Walker A (GxxxxGK[T/S]) or a Rossmann-fold β-sheet; none are present in this 116-aa sequence. (2) Sodium channel inhibitor activity (C) is characteristic of small disulfide-knottin peptides (scorpion toxins, conotoxins) with a rigid Cys-rich scaffold; this sequence lacks the dense cysteine spacing and knottin topology. (3) Carboxylesterase activity (D) requires the GXSXG serine-hydrolase catalytic motif and typically a much larger fold (400–600 aa); this 116-aa protein has no GXSXG and is far too small. (4) The central region (~residues 25–70) displays a helix-turn-helix (HTH) pattern recognizable from hydrophobic/charged periodicity, a motif well known from many transcriptional regulators (e.g., lambda Cro, T4 Rep, and numerous bacterial HTH repressors) that frequently coordinate a structural metal ion (Zn2+ or Mg2+) to stabilize the fold. Thus, by eliminating A, C, and D on motif grounds and recognizing HTH-associated metal coordination as a common feature of this protein family, B is the most defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of three options relies on well-established, transferable knowledge about the structural motifs required for ADP binding, sodium channel inhibition, and carboxylesterase catalysis—none of which are present in the sequence. The positive inference toward metal ion binding draws on the widely recognized association between HTH domains and metal coordination, a pattern learned from many other HTH proteins. This constitutes a concrete, transferable argument that meaningfully distinguishes B from the other three choices without requiring knowledge of this specific protein's database annotation."
  },
  "case_id": "GO_molecular_function_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C10",
      "H3",
      "H7",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (H9C180, Aca2 repressor) carries GO:0046872 (metal ion binding) with IEA:UniProtKB-KW evidence. More importantly, the crystal structures PDB 7VJO and 7VJP were solved at 1.31 Å in complex with Mg(2+), providing direct experimental evidence that this protein coordinates a metal ion. Although the protein's primary molecular function is DNA/RNA binding (as a transcriptional repressor), neither DNA binding nor RNA binding appears among the answer choices. Among the four offered options, metal ion binding is the only one actually annotated and experimentally supported for this protein. The annotation evidence code is IEA (inferred from keyword), but the co-crystal structure with Mg2+ elevates the support beyond mere annotation."
  },
  "important_caveats": [
    "The GO metal ion binding annotation carries IEA:UniProtKB-KW evidence (inferred from keyword), not a direct experimental GO assignment; however, the co-crystal structures with Mg2+ (PDB 7VJO, 7VJP) provide independent experimental support for metal coordination.",
    "The protein's primary molecular function is DNA binding and RNA binding (as a repressor of the acrIF8-aca2 operon); metal ion binding is a secondary structural role. The question's framing as 'primary molecular function' is slightly imprecise, but since DNA/RNA binding are not among the choices, B is the best available answer.",
    "The HTH motif recognition from a raw 116-aa sequence without structural context is a moderate-confidence inference; it is supported by the crystal structures but is not trivially obvious from sequence alone for every model.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt H9C180 across both current and archived (v36) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D each require specific structural motifs or fold features (Walker A/Rossmann, knottin disulfide scaffold, GXSXG catalytic triad in a large esterase fold) that are clearly absent from this 116-aa sequence. Option B is the only choice consistent with the protein's size, composition, and recognizable HTH-like architecture. No other option is defensible given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (H9C180, Aca2 repressor) carries GO:0046872 (metal ion binding) with IEA:UniProtKB-KW evidence. More importantly, the crystal structures PDB 7VJO and 7VJP were solved at 1.31 Å in complex with Mg(2+), providing direct experimental evidence that this protein coordinates a metal ion. Although the protein's primary molecular function is DNA/RNA binding (as a transcriptional repressor), neither DNA binding nor RNA binding appears among the answer choices. Among the four offered options, metal ion binding is the only one actually annotated and experimentally supported for this protein. The annotation evidence code is IEA (inferred from keyword), but the co-crystal structure with Mg2+ elevates the support beyond mere annotation.",
    "evidence_ids": ["C7", "C10", "H3", "H7", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply elimination and positive inference from sequence features. (1) ADP binding (A) requires motifs such as Walker A (GxxxxGK[T/S]) or a Rossmann-fold β-sheet; none are present in this 116-aa sequence. (2) Sodium channel inhibitor activity (C) is characteristic of small disulfide-knottin peptides (scorpion toxins, conotoxins) with a rigid Cys-rich scaffold; this sequence lacks the dense cysteine spacing and knottin topology. (3) Carboxylesterase activity (D) requires the GXSXG serine-hydrolase catalytic motif and typically a much larger fold (400–600 aa); this 116-aa protein has no GXSXG and is far too small. (4) The central region (~residues 25–70) displays a helix-turn-helix (HTH) pattern recognizable from hydrophobic/charged periodicity, a motif well known from many transcriptional regulators (e.g., lambda Cro, T4 Rep, and numerous bacterial HTH repressors) that frequently coordinate a structural metal ion (Zn2+ or Mg2+) to stabilize the fold. Thus, by eliminating A, C, and D on motif grounds and recognizing HTH-associated metal coordination as a common feature of this protein family, B is the most defensible choice.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of three options relies on well-established, transferable knowledge about the structural motifs required for ADP binding, sodium channel inhibition, and carboxylesterase catalysis—none of which are present in the sequence. The positive inference toward metal ion binding draws on the widely recognized association between HTH domains and metal coordination, a pattern learned from many other HTH proteins. This constitutes a concrete, transferable argument that meaningfully distinguishes B from the other three choices without requiring knowledge of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D each require specific structural motifs or fold features (Walker A/Rossmann, knottin disulfide scaffold, GXSXG catalytic triad in a large esterase fold) that are clearly absent from this 116-aa sequence. Option B is the only choice consistent with the protein's size, composition, and recognizable HTH-like architecture. No other option is defensible given the sequence."
  },
  "important_caveats": [
    "The GO metal ion binding annotation carries IEA:UniProtKB-KW evidence (inferred from keyword), not a direct experimental GO assignment; however, the co-crystal structures with Mg2+ (PDB 7VJO, 7VJP) provide independent experimental support for metal coordination.",
    "The protein's primary molecular function is DNA binding and RNA binding (as a repressor of the acrIF8-aca2 operon); metal ion binding is a secondary structural role. The question's framing as 'primary molecular function' is slightly imprecise, but since DNA/RNA binding are not among the choices, B is the best available answer.",
    "The HTH motif recognition from a raw 116-aa sequence without structural context is a moderate-confidence inference; it is supported by the crystal structures but is not trivially obvious from sequence alone for every model.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt H9C180 across both current and archived (v36) records."
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
  "benchmark_sequence_length": 116,
  "benchmark_sequence_sha256": "54d3ff73ff0c3b715a73ad8e414a47da4eccaddeb034918f99f730cb16a8aa1b",
  "current_entry_audit": {
    "entryVersion": 38,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-05-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 116,
  "current_source_sequence_sha256": "54d3ff73ff0c3b715a73ad8e414a47da4eccaddeb034918f99f730cb16a8aa1b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "H9C180",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "selected_historical_source_sequence_length": 116,
  "selected_historical_source_sequence_sha256": "54d3ff73ff0c3b715a73ad8e414a47da4eccaddeb034918f99f730cb16a8aa1b",
  "selected_historical_version": {
    "accession": "H9C180",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ACA2_BPZF4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"H9C180\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":38,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-05-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteriophage ZF40\",\"lineage\":[\"Viruses\",\"Duplodnaviria\",\"Heunggongvirae\",\"Uroviricota\",\"Caudoviricetes\",\"Marchandvirus\",\"Marchandvirus ZF40\"],\"scientificName\":\"Pectobacterium phage ZF40\",\"taxonId\":1127516}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Aca2 regulator\"}},{\"fullName\":{\"value\":\"Gene product 30\"},\"shortNames\":[{\"value\":\"Gp30\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Aca2 repressor\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31428783\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34756887\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38987591\",\"source\":\"PubMed\"}],\"value\":\"Represses the expression of the acrIF8-aca2 operon (PubMed:31428783, PubMed:34756887, PubMed:38987591). Regulates the transcription and translation of phage anti-CRISPR acrIF8 gene (AC H9C181), which is necessary because the expression of this gene rises rapidely upon infection to enable evasion from host CRISPR-Cas defense but is probably toxic to the host cell (PubMed:38987591). Aca2 repressor can inhibit acrIF8 transcriptionally through DNA binding to 2 inverted repeats in the promoter region and translationally by binding conserved RNA stem-loops on mRNAs thereby blocking ribosome access (PubMed:31428783, PubMed:38987591). Both modes of regulation together are essential for complete tight repression (PubMed:38987591)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003677\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:DNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0046872\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:metal ion binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003723\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:RNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Birkholz N.\",\"Fagerlund R.D.\",\"Smith L.M.\",\"Jackson S.A.\",\"Fineran P.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31428783\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkz721\"}],\"citationType\":\"journal article\",\"firstPage\":\"9658\",\"id\":\"31428783\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"9665\",\"publicationDate\":\"2019\",\"title\":\"The autoregulator Aca2 mediates anti-CRISPR repression.\",\"volume\":\"47\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"DNA-BINDING\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Zhang L.\",\"Guo M.\",\"Chen L.\",\"Wu B.\",\"Huang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34756887\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2021.101357\"}],\"citationType\":\"journal article\",\"firstPage\":\"101357\",\"id\":\"34756887\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"101357\",\"publicationDate\":\"2021\",\"title\":\"Structural basis for anti-CRISPR repression mediated by bacterial operon proteins Aca1 and Aca2.\",\"volume\":\"297\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VJO\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VJP\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.31 ANGSTROMS) IN COMPLEX WITH MG(2+)\",\"FUNCTION\",\"SUBUNIT\",\"MUTAGENESIS OF ARG-30; GLN-33; TYR-34 AND ARG-39\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/H9C180.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Birkholz N.\",\"Kamata K.\",\"Feussner M.\",\"Wilkinson M.E.\",\"Cuba Samaniego C.\",\"Migur A.\",\"Kimanius D.\",\"Ceelen M.\",\"Went S.C.\",\"Usher B.\",\"Blower T.R.\",\"Brown C.M.\",\"Beisel C.L.\",\"Weinberg Z.\",\"Fagerlund R.D.\",\"Jackson S.A.\",\"Fineran P.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38987591\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-024-07644-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"670\",\"id\":\"38987591\",\"journal\":\"Nature\",\"lastPage\":\"677\",\"publicationDate\":\"2024\",\"title\":\"Phage anti-CRISPR control by an RNA- and DNA-binding helix-turn-helix protein.\",\"volume\":\"631\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VJQ\",\"source\":\"PDB\"}],\"referenceNumber\":5,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (2.79 ANGSTROMS) OF 1-116\",\"FUNCTION\",\"DOMAIN\",\"MUTAGENESIS OF ARG-30 AND ASP-45\",\"DNA-BINDING\",\"RNA-BINDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:28:50.058954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "285227c3a72acb25f4c60860431676b8190e077de793bd8c3a516e23ad33855e",
  "url": "https://rest.uniprot.org/uniprotkb/H9C180.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   ACA2_BPZF4              Reviewed;         116 AA.\nAC   H9C180;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAY-2012, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Aca2 repressor;\nDE   AltName: Full=Aca2 regulator;\nDE   AltName: Full=Gene product 30;\nDE            Short=Gp30;\nGN   ORFNames=ZF40_0030;\nOS   Pectobacterium phage ZF40 (Bacteriophage ZF40).\nOC   Viruses; Duplodnaviria; Heunggongvirae; Uroviricota; Caudoviricetes.\nOX   NCBI_TaxID=1127516;\nOH   NCBI_TaxID=554; Pectobacterium carotovorum (Erwinia carotovora).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, SUBUNIT, DNA-BINDING, AND DOMAIN.\nRX   PubMed=31428783; DOI=10.1093/nar/gkz721;\nRA   Birkholz N., Fagerlund R.D., Smith L.M., Jackson S.A., Fineran P.C.;\nRT   \"The autoregulator Aca2 mediates anti-CRISPR repression.\";\nRL   Nucleic Acids Res. 47:9658-9665(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:7VJO, ECO:0007744|PDB:7VJP}\nRP   X-RAY CRYSTALLOGRAPHY (1.31 ANGSTROMS) IN COMPLEX WITH MG(2+), FUNCTION,\nRP   SUBUNIT, AND MUTAGENESIS OF ARG-30; GLN-33; TYR-34 AND ARG-39.\nRX   PubMed=34756887; DOI=10.1016/j.jbc.2021.101357;\nRA   Liu Y., Zhang L., Guo M., Chen L., Wu B., Huang H.;\nRT   \"Structural basis for anti-CRISPR repression mediated by bacterial operon\nRT   proteins Aca1 and Aca2.\";\nRL   J. Biol. Chem. 297:101357-101357(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0007744|PDB:7VJQ}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.79 ANGSTROMS) OF 1-116, FUNCTION,\nRP   DOMAIN, MUTAGENESIS OF ARG-30 AND ASP-45, DNA-BINDING, AND RNA-BINDING.\nRX   PubMed=38987591; DOI=10.1038/s41586-024-07644-1;\nRA   Birkholz N., Kamata K., Feussner M., Wilkinson M.E., Cuba Samaniego C.,\nRA   Migur A., Kimanius D., Ceelen M., Went S.C., Usher B., Blower T.R.,\nRA   Brown C.M., Beisel C.L., Weinberg Z., Fagerlund R.D., Jackson S.A.,\nRA   Fineran P.C.;\nRT   \"Phage anti-CRISPR control by an RNA- and DNA-binding helix-turn-helix\nRT   protein.\";\nRL   Nature 631:670-677(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Represses the expression of the acrIF8-aca2 operon\nCC       (PubMed:31428783, PubMed:34756887, PubMed:38987591). Regulates the\nCC       transcription and translation of phage anti-CRISPR acrIF8 gene (AC\nCC       H9C181), which is necessary because the expression of this gene rises\nCC       rapidely upon infection to enable evasion from host CRISPR-Cas defense\nCC       but is probably toxic to the host cell (PubMed:38987591). Aca2\nCC       repressor can inhibit acrIF8 transcriptionally through DNA binding to 2\nCC       inverted repeats in the promoter region and translationally by binding\nCC       conserved RNA stem-loops on mRNAs thereby blocking ribosome access\nCC       (PubMed:31428783, PubMed:38987591). Both modes of regulation together\nCC       are essential for complete tight repression (PubMed:38987591).\nCC       {ECO:0000269|PubMed:31428783, ECO:0000269|PubMed:34756887,\nCC       ECO:0000269|PubMed:38987591}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0003677; F:DNA binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0003723; F:RNA binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.730440+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "478ec54da69150ad62dd5be94639444619dfc5ecf0d351b6812f572b1da1d146",
  "url": "https://rest.uniprot.org/unisave/H9C180?format=txt&versions=36"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0019871\nname: sodium channel inhibitor activity\nnamespace: molecular_function\nalt_id: GO:0019868\ndef: \"Binds to and stops, prevents, or reduces the activity of a sodium channel.\" [GOC:mah]\nis_a: GO:0008200 ! ion channel inhibitor activity\nis_a: GO:0017080 ! sodium channel regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019871",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 154099-154107",
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
  "excerpt": "[Term]\nid: GO:0043531\nname: ADP binding\nnamespace: molecular_function\ndef: \"Binding to ADP, adenosine 5'-diphosphate.\" [GOC:jl]\nsynonym: \"adenosine 5'-diphosphate binding\" EXACT []\nsynonym: \"adenosine diphosphate binding\" EXACT []\nis_a: GO:0032559 ! adenyl ribonucleotide binding\nis_a: GO:0043168 ! anion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043531",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 248248-248257",
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
  "excerpt": "[Term]\nid: GO:0046872\nname: metal ion binding\nnamespace: molecular_function\ndef: \"Binding to a metal ion.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsynonym: \"heavy metal binding\" NARROW []\nsynonym: \"metal binding\" EXACT []\nis_a: GO:0043169 ! cation binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046872",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281280-281292",
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
  "excerpt": "[Term]\nid: GO:0106435\nname: carboxylesterase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a carboxylic ester + H2O = a carboxylate + an alcohol + H+.\" [RHEA:21164]\ncomment: Note: This covers a broad range of specificity; also hydrolyzes vitamin A esters.\nsynonym: \"ali-esterase activity\" RELATED [EC:3.1.1.1]\nsynonym: \"alpha-carboxylesterase activity\" NARROW []\nsynonym: \"B-esterase activity\" NARROW [EC:3.1.1.1]\nsynonym: \"cocaine esterase\" NARROW [EC:3.1.1.1]\nsynonym: \"nonspecific carboxylesterase activity\" RELATED []\nsynonym: \"procaine esterase\" NARROW [] {comment=\"EC:3.1.1.1\"}\nsynonym: \"serine esterase activity\" NARROW []\nsynonym: \"triacetin esterase\" NARROW []\nsynonym: \"vitamin A esterase\" NARROW []\nxref: EC:3.1.1.1\nxref: MetaCyc:CARBOXYLESTERASE-RXN\nxref: Reactome:R-HSA-9619024 \"CES1 trimer hydrolyses ACEI pro-drugs to ACEIs\"\nxref: Reactome:R-HSA-9727567 \"CES1 hydrolyses sacubitril to sacubitrilat\"\nxref: Reactome:R-HSA-9749647 \"CES2 hydrolyzes ASA-\"\nxref: RHEA:21164\nxref: RHEA:31779\nxref: RHEA:38555\nxref: RHEA:47348\nxref: RHEA:47352\nxref: RHEA:47356\nxref: RHEA:47360\nxref: RHEA:47364\nxref: RHEA:47388\nxref: RHEA:47392\nxref: RHEA:50136\nxref: RHEA:50144\nxref: RHEA:50148\nxref: RHEA:59388\nxref: RHEA:63052\nis_a: GO:0052689 ! carboxylic ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.1.1\nproperty_value: skos:exactMatch RHEA:21164\nproperty_value: skos:narrowMatch RHEA:31779\nproperty_value: skos:narrowMatch RHEA:38555\nproperty_value: skos:narrowMatch RHEA:47348\nproperty_value: skos:narrowMatch RHEA:47352\nproperty_value: skos:narrowMatch RHEA:47356\nproperty_value: skos:narrowMatch RHEA:47360\nproperty_value: skos:narrowMatch RHEA:47364\nproperty_value: skos:narrowMatch RHEA:47388\nproperty_value: skos:narrowMatch RHEA:47392\nproperty_value: skos:narrowMatch RHEA:50136\nproperty_value: skos:narrowMatch RHEA:50144\nproperty_value: skos:narrowMatch RHEA:50148\nproperty_value: skos:narrowMatch RHEA:59388\nproperty_value: skos:narrowMatch RHEA:63052\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106435",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 430643-430695",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 181. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
