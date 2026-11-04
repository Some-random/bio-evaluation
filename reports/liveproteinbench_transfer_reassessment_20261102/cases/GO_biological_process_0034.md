# GO_biological_process_0034

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0034.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — virion assembly

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSQIKIPLPKPPDSDSQRLNAFPIIMAQEGKGRLLRQIRLRKILSGDPSDQQITFVNTYGFIRATPETSEFISESSPQKVTPVVTACMLSFGAGPVLEDPQHMLKALDQTDIRVRKTASDKEQILFEINRIPNLFRHHQISADHLIQASSDKYVKSPAKLIAGVNYIYCVTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEVLLRVTCKKDSQMAKSMLNDPEGEGCIASVWFHLCNLCKGRNKLRSYDENYFASKCRKMNLTVSIGDMWGPTILVHAGGHIPTTAKPFFNSRGWVCHPIHQSSPSLAKTLWSSGCEIKAASAILQGSDYASLAKTDDIIYSKIKVDKDAANYKGVSWSPFRKSASMSNL

[Multiple Choices]
A. virion assembly
B. protein urmylation
C. regulation of monoatomic ion transmembrane transport
D. [2Fe-2S] cluster assembly
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the reviewed UniProt sequence annotated as a mumps-virus matrix protein. Its role in virus assembly is supported by a function annotation transferred from a related UniProt entry and by a GO virion-assembly annotation assigned by InterPro; these are not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 375-residue sequence is compatible with a soluble viral structural protein: it has no long hydrophobic segment suggestive of a membrane transporter and no obvious iron-sulfur-cluster-binding motif or conjugation-enzyme signature. Transferable knowledge that viral matrix proteins associate viral components during particle formation makes virion assembly the credible choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence does not provide an unmistakable motif establishing a viral matrix-protein identity, so the inference is probabilistic. But family-level recognition and the strong contrast with the offered transport, urmylation, and Fe-S assembly options provide a meaningful basis without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, virion assembly is the only one consistent with the sequence's plausible viral structural-protein role.


### Important caveats

- Reviewer-only annotations support the key but were not part of the original model input.
- The function annotation is transferred by similarity, and the GO annotation is computational; the excerpts do not establish direct experimental evidence for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 375-residue sequence is compatible with a soluble viral structural protein: it has no long hydrophobic segment suggestive of a membrane transporter and no obvious iron-sulfur-cluster-binding motif or conjugation-enzyme signature. Transferable knowledge that viral matrix proteins associate viral components during particle formation makes virion assembly the credible choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence does not provide an unmistakable motif establishing a viral matrix-protein identity, so the inference is probabilistic. But family-level recognition and the strong contrast with the offered transport, urmylation, and Fe-S assembly options provide a meaningful basis without needing the exact protein's database record."
  },
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed UniProt sequence annotated as a mumps-virus matrix protein. Its role in virus assembly is supported by a function annotation transferred from a related UniProt entry and by a GO virion-assembly annotation assigned by InterPro; these are not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "Reviewer-only annotations support the key but were not part of the original model input.",
    "The function annotation is transferred by similarity, and the GO annotation is computational; the excerpts do not establish direct experimental evidence for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, virion assembly is the only one consistent with the sequence's plausible viral structural-protein role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed UniProt sequence annotated as a mumps-virus matrix protein. Its role in virus assembly is supported by a function annotation transferred from a related UniProt entry and by a GO virion-assembly annotation assigned by InterPro; these are not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 375-residue sequence is compatible with a soluble viral structural protein: it has no long hydrophobic segment suggestive of a membrane transporter and no obvious iron-sulfur-cluster-binding motif or conjugation-enzyme signature. Transferable knowledge that viral matrix proteins associate viral components during particle formation makes virion assembly the credible choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence does not provide an unmistakable motif establishing a viral matrix-protein identity, so the inference is probabilistic. But family-level recognition and the strong contrast with the offered transport, urmylation, and Fe-S assembly options provide a meaningful basis without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, virion assembly is the only one consistent with the sequence's plausible viral structural-protein role."
  },
  "important_caveats": [
    "Reviewer-only annotations support the key but were not part of the original model input.",
    "The function annotation is transferred by similarity, and the GO annotation is computational; the excerpts do not establish direct experimental evidence for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q5SC54 (Mumps virus Matrix protein, 375 aa). UniProt annotates GO:0019068 (virion assembly) via IEA:InterPro, and the function comment states 'The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane' (ECO:0000250, inferred from similarity to Q9W850). The annotation is computational/transferred rather than direct experimental evidence for this exact protein, but it is consistent with well-established paramyxovirus biology. The expected answer A is supported by the database record.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 375-aa protein lacks eukaryotic hallmarks (no signal peptide, no multi-pass TM topology, no enzymatic domains such as adenylation/thioesterase/transferase motifs). Its amphipathic helical regions (e.g., 'LAARSRLVRAVQMEVLLRV', 'VTFLSVTVCSASLKFRVARPLLAARS') and small size are characteristic of viral matrix proteins across Paramyxoviridae and related Mononegavirales, whose conserved role is virion assembly (bridging envelope and RNP). This eliminates B (urmylation requires E1/E2/E3 enzymatic machinery with specific domains absent here), D (&#91;2Fe-2S&#93; assembly requires scaffold proteins with canonical Cys-X2-C-X2,4-C-X2,3-C clusters; the scattered Cys residues here do not match), and C (ion transport regulation requires channel/transporter topology or regulatory subunit features absent here). Family-level knowledge of paramyxovirus M proteins (e.g., Sendai, measles, Nipah M proteins) supports selecting A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with viral matrix protein families can recognize the small size, amphipathic helical character, absence of enzymatic or channel features, and infer virion assembly as the biological process. This is legitimate transfer from other paramyxovirus and Mononegavirales matrix proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (urmylation, ion transport regulation, Fe-S cluster assembly) each require specific structural/enzymatic features clearly absent from this small, non-enzymatic, non-channel protein. Only virion assembly is consistent with the sequence's overall character and family-level inference.


### Important caveats

- The UniProt GO annotation is IEA (Inferred from Electronic Annotation via InterPro) and the function comment is transferred from Q9W850 by similarity (ECO:0000250), not direct experimental evidence for this exact Mumps M protein.
- The C-terminal region contains several Cys residues that could superficially resemble Fe-S motifs, but they do not form canonical &#91;2Fe-2S&#93; binding patterns.
- The protein's viral origin is not explicitly stated in the input; a model must infer it from sequence composition and absence of eukaryotic features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 375-aa protein lacks eukaryotic hallmarks (no signal peptide, no multi-pass TM topology, no enzymatic domains such as adenylation/thioesterase/transferase motifs). Its amphipathic helical regions (e.g., 'LAARSRLVRAVQMEVLLRV', 'VTFLSVTVCSASLKFRVARPLLAARS') and small size are characteristic of viral matrix proteins across Paramyxoviridae and related Mononegavirales, whose conserved role is virion assembly (bridging envelope and RNP). This eliminates B (urmylation requires E1/E2/E3 enzymatic machinery with specific domains absent here), D ([2Fe-2S] assembly requires scaffold proteins with canonical Cys-X2-C-X2,4-C-X2,3-C clusters; the scattered Cys residues here do not match), and C (ion transport regulation requires channel/transporter topology or regulatory subunit features absent here). Family-level knowledge of paramyxovirus M proteins (e.g., Sendai, measles, Nipah M proteins) supports selecting A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with viral matrix protein families can recognize the small size, amphipathic helical character, absence of enzymatic or channel features, and infer virion assembly as the biological process. This is legitimate transfer from other paramyxovirus and Mononegavirales matrix proteins."
  },
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC54 (Mumps virus Matrix protein, 375 aa). UniProt annotates GO:0019068 (virion assembly) via IEA:InterPro, and the function comment states 'The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane' (ECO:0000250, inferred from similarity to Q9W850). The annotation is computational/transferred rather than direct experimental evidence for this exact protein, but it is consistent with well-established paramyxovirus biology. The expected answer A is supported by the database record."
  },
  "important_caveats": [
    "The UniProt GO annotation is IEA (Inferred from Electronic Annotation via InterPro) and the function comment is transferred from Q9W850 by similarity (ECO:0000250), not direct experimental evidence for this exact Mumps M protein.",
    "The C-terminal region contains several Cys residues that could superficially resemble Fe-S motifs, but they do not form canonical [2Fe-2S] binding patterns.",
    "The protein's viral origin is not explicitly stated in the input; a model must infer it from sequence composition and absence of eukaryotic features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (urmylation, ion transport regulation, Fe-S cluster assembly) each require specific structural/enzymatic features clearly absent from this small, non-enzymatic, non-channel protein. Only virion assembly is consistent with the sequence's overall character and family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC54 (Mumps virus Matrix protein, 375 aa). UniProt annotates GO:0019068 (virion assembly) via IEA:InterPro, and the function comment states 'The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane' (ECO:0000250, inferred from similarity to Q9W850). The annotation is computational/transferred rather than direct experimental evidence for this exact protein, but it is consistent with well-established paramyxovirus biology. The expected answer A is supported by the database record.",
    "evidence_ids": ["C5", "C6", "H2", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 375-aa protein lacks eukaryotic hallmarks (no signal peptide, no multi-pass TM topology, no enzymatic domains such as adenylation/thioesterase/transferase motifs). Its amphipathic helical regions (e.g., 'LAARSRLVRAVQMEVLLRV', 'VTFLSVTVCSASLKFRVARPLLAARS') and small size are characteristic of viral matrix proteins across Paramyxoviridae and related Mononegavirales, whose conserved role is virion assembly (bridging envelope and RNP). This eliminates B (urmylation requires E1/E2/E3 enzymatic machinery with specific domains absent here), D ([2Fe-2S] assembly requires scaffold proteins with canonical Cys-X2-C-X2,4-C-X2,3-C clusters; the scattered Cys residues here do not match), and C (ion transport regulation requires channel/transporter topology or regulatory subunit features absent here). Family-level knowledge of paramyxovirus M proteins (e.g., Sendai, measles, Nipah M proteins) supports selecting A.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with viral matrix protein families can recognize the small size, amphipathic helical character, absence of enzymatic or channel features, and infer virion assembly as the biological process. This is legitimate transfer from other paramyxovirus and Mononegavirales matrix proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (urmylation, ion transport regulation, Fe-S cluster assembly) each require specific structural/enzymatic features clearly absent from this small, non-enzymatic, non-channel protein. Only virion assembly is consistent with the sequence's overall character and family-level inference."
  },
  "important_caveats": [
    "The UniProt GO annotation is IEA (Inferred from Electronic Annotation via InterPro) and the function comment is transferred from Q9W850 by similarity (ECO:0000250), not direct experimental evidence for this exact Mumps M protein.",
    "The C-terminal region contains several Cys residues that could superficially resemble Fe-S motifs, but they do not form canonical [2Fe-2S] binding patterns.",
    "The protein's viral origin is not explicitly stated in the input; a model must infer it from sequence composition and absence of eukaryotic features."
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
  "benchmark_sequence_length": 375,
  "benchmark_sequence_sha256": "eff2e86924870e96c29559b784ee828ecae7dc89a34eea3f75361d6b1ba12d51",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 375,
  "current_source_sequence_sha256": "eff2e86924870e96c29559b784ee828ecae7dc89a34eea3f75361d6b1ba12d51",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5SC54",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4",
  "selected_historical_source_sequence_length": 375,
  "selected_historical_source_sequence_sha256": "eff2e86924870e96c29559b784ee828ecae7dc89a34eea3f75361d6b1ba12d51",
  "selected_historical_version": {
    "accession": "Q5SC54",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MATRX_MUMPZ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5SC54\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:31.669710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC54.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:31.669710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC54.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:31.669710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC54.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"Matrix protein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:31.669710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC54.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9W850\",\"source\":\"UniProtKB\"}],\"value\":\"The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:31.669710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC54.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0019068\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:virion assembly\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:31:31.669710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC54.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   MATRX_MUMPZ             Reviewed;         375 AA.\nAC   Q5SC54;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Matrix protein;\nGN   Name=M;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:33.730421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4",
  "url": "https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "CC   -!- FUNCTION: The M protein has a crucial role in virus assembly and\nCC       interacts with the RNP complex as well as with the viral membrane.\nCC       {ECO:0000250|UniProtKB:Q9W850}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:33.730421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4",
  "url": "https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0019068; P:virion assembly; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:33.730421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4",
  "url": "https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0019068\nname: virion assembly\nnamespace: biological_process\nalt_id: GO:0042963\ndef: \"A late phase of the viral life cycle during which all the components necessary for the formation of a mature virion collect at a particular site in the cell and the basic structure of the virus particle is formed.\" [ISBN:0121585336]\nsubset: goslim_virus\nsynonym: \"bacteriophage assembly\" NARROW [GOC:bm]\nsynonym: \"phage assembly\" NARROW [GOC:bm]\nsynonym: \"viral assembly\" EXACT []\nsynonym: \"viral particle assembly\" EXACT []\nsynonym: \"virion assembly and maintenance\" EXACT [GOC:bf, GOC:jl]\nsynonym: \"virion organization\" EXACT [GOC:bf, GOC:jl]\nsynonym: \"virus assembly\" EXACT [GOC:dph, GOC:tb]\nsynonym: \"virus particle assembly\" EXACT []\nxref: Reactome:R-HSA-168302 \"Budding\"\nxref: Reactome:R-HSA-168316 \"Assembly of Viral Components at the Budding Site\"\nxref: Reactome:R-HSA-175474 \"Assembly Of The HIV Virion\"\nis_a: GO:0016032 ! viral process\nrelationship: part_of GO:0019058 ! viral life cycle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019068",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 145078-145098",
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
  "excerpt": "[Term]\nid: GO:0032447\nname: protein urmylation\nnamespace: biological_process\ndef: \"Covalent attachment of the ubiquitin-like protein URM1 to another protein.\" [GOC:vw]\nis_a: GO:0032446 ! protein modification by small protein conjugation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032447",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 186263-186269",
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
  "excerpt": "[Term]\nid: GO:0034765\nname: regulation of monoatomic ion transmembrane transport\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of the directed movement of ions from one side of a membrane to the other.\" [GOC:mah]\nsynonym: \"regulation of ion membrane transport\" EXACT []\nsynonym: \"regulation of ion transmembrane transport\" BROAD []\nsynonym: \"regulation of transmembrane ion transport\" EXACT [GOC:dph, GOC:tb]\nis_a: GO:0034762 ! regulation of transmembrane transport\nis_a: GO:0043269 ! regulation of monoatomic ion transport\nrelationship: regulates GO:0034220 ! monoatomic ion transmembrane transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034765",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 212058-212069",
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
  "excerpt": "[Term]\nid: GO:0044571\nname: [2Fe-2S] cluster assembly\nnamespace: biological_process\ndef: \"The incorporation of two iron atoms and two sulfur atoms into an iron-sulfur cluster.\" [GOC:jl, GOC:mengo_curators, GOC:pde, GOC:tt, GOC:vw, PMID:15952888]\nsynonym: \"2Fe-2S cluster assembly\" EXACT []\nsynonym: \"[2Fe-2S] cluster biosynthetic process\" RELATED []\nis_a: GO:0016226 ! iron-sulfur cluster assembly\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044571",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 258499-258507",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
