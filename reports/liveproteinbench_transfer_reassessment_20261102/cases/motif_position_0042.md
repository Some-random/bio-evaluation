# motif_position_0042

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0042.txt)

**Task:** `motif_position`  
**Expected answer:** **D** — 9..19

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKGQVSVEFIVLFLALLVAVVVSTMTPGIFGLNKSVELSSASLAHAALSKVKSNIEILSVSGEGSYKLVYVKSPPANWTFENRTIRVYGNGFNISTNTSVDLNTYNYLASSLKILSVNLTRNDKNVTVAIQ

[Multiple Choices]
A. 134..139
B. 9..17
C. 316..323
D. 9..19
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif.. The inputs provided by the user for this task include:

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

### Expected-answer support: uncertain

> The sequence-matched UniProt record annotates the motif at 9..19, supporting the key as a database annotation (C5, H4). But that annotation describes the motif as QXSXEXXXL, which matches the supplied sequence at 5..13, not 9..19. The annotation and the sequence pattern therefore conflict for the motif-position question; the excerpt does not resolve which is scientifically correct.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The exact target-specific motif annotation assigning coordinates 9..19; transferable sequence-pattern recognition instead locates QXSXEXXXL at 5..13, which is not offered.


**Reason**

> The recognizable sequence pattern does not distinguish B from D: both begin at 9, and neither gives the pattern's sequence-matched location. The other choices are outside the 132-residue sequence. Selecting D requires the target-specific annotation, although that annotation conflicts with the pattern in the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No offered choice matches the literal QXSXEXXXL pattern in the supplied sequence. D is the database-annotated choice, but the annotation's coordinates conflict with that pattern, so the evidence does not establish multiple scientifically defensible options.


### Important caveats

- The annotation is curator-attributed (ECO:0000305) and cites a paper; the supplied excerpts do not independently establish experimental validation of these coordinates.
- The source record is reported as an exact sequence match, so the discrepancy is not explained by a different sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact target-specific motif annotation assigning coordinates 9..19; transferable sequence-pattern recognition instead locates QXSXEXXXL at 5..13, which is not offered.",
    "reason": "The recognizable sequence pattern does not distinguish B from D: both begin at 9, and neither gives the pattern's sequence-matched location. The other choices are outside the 132-residue sequence. Selecting D requires the target-specific annotation, although that annotation conflicts with the pattern in the sequence."
  },
  "case_id": "motif_position_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "cannot_determine",
    "reason": "The sequence-matched UniProt record annotates the motif at 9..19, supporting the key as a database annotation (C5, H4). But that annotation describes the motif as QXSXEXXXL, which matches the supplied sequence at 5..13, not 9..19. The annotation and the sequence pattern therefore conflict for the motif-position question; the excerpt does not resolve which is scientifically correct."
  },
  "important_caveats": [
    "The annotation is curator-attributed (ECO:0000305) and cites a paper; the supplied excerpts do not independently establish experimental validation of these coordinates.",
    "The source record is reported as an exact sequence match, so the discrepancy is not explained by a different sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No offered choice matches the literal QXSXEXXXL pattern in the supplied sequence. D is the database-annotated choice, but the annotation's coordinates conflict with that pattern, so the evidence does not establish multiple scientifically defensible options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0042",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The sequence-matched UniProt record annotates the motif at 9..19, supporting the key as a database annotation (C5, H4). But that annotation describes the motif as QXSXEXXXL, which matches the supplied sequence at 5..13, not 9..19. The annotation and the sequence pattern therefore conflict for the motif-position question; the excerpt does not resolve which is scientifically correct.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The exact target-specific motif annotation assigning coordinates 9..19; transferable sequence-pattern recognition instead locates QXSXEXXXL at 5..13, which is not offered.",
    "reason": "The recognizable sequence pattern does not distinguish B from D: both begin at 9, and neither gives the pattern's sequence-matched location. The other choices are outside the 132-residue sequence. Selecting D requires the target-specific annotation, although that annotation conflicts with the pattern in the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No offered choice matches the literal QXSXEXXXL pattern in the supplied sequence. D is the database-annotated choice, but the annotation's coordinates conflict with that pattern, so the evidence does not establish multiple scientifically defensible options."
  },
  "important_caveats": [
    "The annotation is curator-attributed (ECO:0000305) and cites a paper; the supplied excerpts do not independently establish experimental validation of these coordinates.",
    "The source record is reported as an exact sequence match, so the discrepancy is not explained by a different sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5 and H4) explicitly annotates a Motif feature at positions 9..19 with the pattern QXSXEXXXL, matching the expected answer D. However, the annotation uses evidence code ECO:0000305 (inferred by curator, not experimental), and the annotation appears internally inconsistent with the sequence: QXSXEXXXL actually matches at positions 5-13 (Q-V-S-V-E-F-I-V-L) in the provided 132-AA sequence, not at 9-19 (E-F-I-V-L-F-L-A-L-L-V, which lacks the required Q and S at positions 9 and 11). The expected answer is supported by the database record but the underlying annotation appears erroneous relative to the sequence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific UniProt annotation assigning the QXSXEXXXL motif to positions 9..19 for this exact protein (Q6M0N4), which is not derivable from the sequence because the motif pattern actually matches at positions 5-13. Additionally, the motif pattern itself is not provided to the model, and the distinction between option B (9..17, 9 residues) and option D (9..19, 11 residues) cannot be resolved by any transferable type IV pilin knowledge since neither interval corresponds to the actual QXSXEXXXL match.


**Reason**

> The model receives only the sequence and four position choices. Options A (134..139) and C (316..323) are trivially eliminated as beyond the 132-AA sequence. Between B (9..17) and D (9..19), no transferable knowledge distinguishes them: the motif pattern QXSXEXXXL is not provided, and even if a model recognized this as a type IV pilin and recalled the QXSXEXXXL motif, it would find the match at positions 5-13, not at either 9-17 or 9-19. The correct answer (per the benchmark) depends entirely on recalling this specific (apparently erroneous) UniProt annotation entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both B (9..17) and D (9..19) start at position 9 and fall within the sequence. Without the motif pattern being specified and given that the annotated motif does not actually match at either interval, there is no sequence-based or family-based argument to prefer 9..19 over 9..17. The distinction requires the specific database annotation.


### Important caveats

- The UniProt annotation (ECO:0000305, curator inference) appears to contain an error: the QXSXEXXXL pattern matches at positions 5-13 in the provided sequence, not 9-19.
- The motif pattern is not provided to the evaluated model in the original question, making the task dependent on knowing which motif to look for.
- The annotation evidence code is ECO:0000305 (inferred by curator), not experimental or mass-spectrometry-derived, despite the cited publication involving mass spectrometry.
- Options A and C are trivially impossible for a 132-AA protein, reducing effective discrimination to B vs D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt annotation assigning the QXSXEXXXL motif to positions 9..19 for this exact protein (Q6M0N4), which is not derivable from the sequence because the motif pattern actually matches at positions 5-13. Additionally, the motif pattern itself is not provided to the model, and the distinction between option B (9..17, 9 residues) and option D (9..19, 11 residues) cannot be resolved by any transferable type IV pilin knowledge since neither interval corresponds to the actual QXSXEXXXL match.",
    "reason": "The model receives only the sequence and four position choices. Options A (134..139) and C (316..323) are trivially eliminated as beyond the 132-AA sequence. Between B (9..17) and D (9..19), no transferable knowledge distinguishes them: the motif pattern QXSXEXXXL is not provided, and even if a model recognized this as a type IV pilin and recalled the QXSXEXXXL motif, it would find the match at positions 5-13, not at either 9-17 or 9-19. The correct answer (per the benchmark) depends entirely on recalling this specific (apparently erroneous) UniProt annotation entry."
  },
  "case_id": "motif_position_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5 and H4) explicitly annotates a Motif feature at positions 9..19 with the pattern QXSXEXXXL, matching the expected answer D. However, the annotation uses evidence code ECO:0000305 (inferred by curator, not experimental), and the annotation appears internally inconsistent with the sequence: QXSXEXXXL actually matches at positions 5-13 (Q-V-S-V-E-F-I-V-L) in the provided 132-AA sequence, not at 9-19 (E-F-I-V-L-F-L-A-L-L-V, which lacks the required Q and S at positions 9 and 11). The expected answer is supported by the database record but the underlying annotation appears erroneous relative to the sequence."
  },
  "important_caveats": [
    "The UniProt annotation (ECO:0000305, curator inference) appears to contain an error: the QXSXEXXXL pattern matches at positions 5-13 in the provided sequence, not 9-19.",
    "The motif pattern is not provided to the evaluated model in the original question, making the task dependent on knowing which motif to look for.",
    "The annotation evidence code is ECO:0000305 (inferred by curator), not experimental or mass-spectrometry-derived, despite the cited publication involving mass spectrometry.",
    "Options A and C are trivially impossible for a 132-AA protein, reducing effective discrimination to B vs D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both B (9..17) and D (9..19) start at position 9 and fall within the sequence. Without the motif pattern being specified and given that the annotated motif does not actually match at either interval, there is no sequence-based or family-based argument to prefer 9..19 over 9..17. The distinction requires the specific database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5 and H4) explicitly annotates a Motif feature at positions 9..19 with the pattern QXSXEXXXL, matching the expected answer D. However, the annotation uses evidence code ECO:0000305 (inferred by curator, not experimental), and the annotation appears internally inconsistent with the sequence: QXSXEXXXL actually matches at positions 5-13 (Q-V-S-V-E-F-I-V-L) in the provided 132-AA sequence, not at 9-19 (E-F-I-V-L-F-L-A-L-L-V, which lacks the required Q and S at positions 9 and 11). The expected answer is supported by the database record but the underlying annotation appears erroneous relative to the sequence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific UniProt annotation assigning the QXSXEXXXL motif to positions 9..19 for this exact protein (Q6M0N4), which is not derivable from the sequence because the motif pattern actually matches at positions 5-13. Additionally, the motif pattern itself is not provided to the model, and the distinction between option B (9..17, 9 residues) and option D (9..19, 11 residues) cannot be resolved by any transferable type IV pilin knowledge since neither interval corresponds to the actual QXSXEXXXL match.",
    "reason": "The model receives only the sequence and four position choices. Options A (134..139) and C (316..323) are trivially eliminated as beyond the 132-AA sequence. Between B (9..17) and D (9..19), no transferable knowledge distinguishes them: the motif pattern QXSXEXXXL is not provided, and even if a model recognized this as a type IV pilin and recalled the QXSXEXXXL motif, it would find the match at positions 5-13, not at either 9-17 or 9-19. The correct answer (per the benchmark) depends entirely on recalling this specific (apparently erroneous) UniProt annotation entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both B (9..17) and D (9..19) start at position 9 and fall within the sequence. Without the motif pattern being specified and given that the annotated motif does not actually match at either interval, there is no sequence-based or family-based argument to prefer 9..19 over 9..17. The distinction requires the specific database annotation."
  },
  "important_caveats": [
    "The UniProt annotation (ECO:0000305, curator inference) appears to contain an error: the QXSXEXXXL pattern matches at positions 5-13 in the provided sequence, not 9-19.",
    "The motif pattern is not provided to the evaluated model in the original question, making the task dependent on knowing which motif to look for.",
    "The annotation evidence code is ECO:0000305 (inferred by curator), not experimental or mass-spectrometry-derived, despite the cited publication involving mass spectrometry.",
    "Options A and C are trivially impossible for a 132-AA protein, reducing effective discrimination to B vs D."
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
  "benchmark_sequence_length": 132,
  "benchmark_sequence_sha256": "8765d660f00798a377e735d315095422bcb044e1bcc416e334a324ebbd785858",
  "current_entry_audit": {
    "entryVersion": 76,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2025-06-18",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 132,
  "current_source_sequence_sha256": "8765d660f00798a377e735d315095422bcb044e1bcc416e334a324ebbd785858",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 76,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6M0N4",
  "selected_historical_entry_version": 76,
  "selected_historical_record_sha256": "da6321a7443875e32e6bbf173da14447e97ad6ff8b2144b4fcda915239520af3",
  "selected_historical_source_sequence_length": 132,
  "selected_historical_source_sequence_sha256": "8765d660f00798a377e735d315095422bcb044e1bcc416e334a324ebbd785858",
  "selected_historical_version": {
    "accession": "Q6M0N4",
    "database": "Swiss-Prot",
    "entryVersion": 76,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "EPDB_METMP",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6M0N4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:41.416988+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":76,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2025-06-18\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:41.416988+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:41.416988+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Minor structural pilin EpdB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:41.416988+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"QXSXEXXXL\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21075925\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":19},\"start\":{\"modifier\":\"EXACT\",\"value\":9}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:41.416988+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ng S.Y.\",\"Wu J.\",\"Nair D.B.\",\"Logan S.M.\",\"Robotham A.\",\"Tessier L.\",\"Kelly J.F.\",\"Uchida K.\",\"Aizawa S.\",\"Jarrell K.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21075925\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.00822-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"804\",\"id\":\"21075925\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"814\",\"publicationDate\":\"2011\",\"title\":\"Genetic and mass spectrometry analyses of the unusual type IV-like pili of the archaeon Methanococcus maripaludis.\",\"volume\":\"193\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DOMAIN\",\"DISRUPTION PHENOTYPE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:41.416988+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e0f4179119f5f58f466c46d7473f346f0a4c12783a89b576e1c82374de82ae23",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H1",
  "excerpt": "ID   EPDB_METMP              Reviewed;         132 AA.\nAC   Q6M0N4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   18-JUN-2025, entry version 76.\nDE   RecName: Full=Minor structural pilin EpdB {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=epdB {ECO:0000303|PubMed:24386316};\nGN   OrderedLocusNames=MMP0236 {ECO:0000312|EMBL:CAF29792.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:43.395652+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da6321a7443875e32e6bbf173da14447e97ad6ff8b2144b4fcda915239520af3",
  "url": "https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DOMAIN, DISRUPTION PHENOTYPE, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=21075925; DOI=10.1128/jb.00822-10;\nRA   Ng S.Y., Wu J., Nair D.B., Logan S.M., Robotham A., Tessier L., Kelly J.F.,\nRA   Uchida K., Aizawa S., Jarrell K.F.;\nRT   \"Genetic and mass spectrometry analyses of the unusual type IV-like pili of\nRT   the archaeon Methanococcus maripaludis.\";\nRL   J. Bacteriol. 193:804-814(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:43.395652+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da6321a7443875e32e6bbf173da14447e97ad6ff8b2144b4fcda915239520af3",
  "url": "https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   NOMENCLATURE.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=24386316; DOI=10.1371/journal.pone.0083961;\nRA   Nair D.B., Chung D.K., Schneider J., Uchida K., Aizawa S., Jarrell K.F.;\nRT   \"Identification of an additional minor pilin essential for piliation in the\nRT   archaeon Methanococcus maripaludis.\";\nRL   PLoS ONE 8:e83961-e83961(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:43.395652+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da6321a7443875e32e6bbf173da14447e97ad6ff8b2144b4fcda915239520af3",
  "url": "https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H4",
  "excerpt": "FT   MOTIF           9..19\nFT                   /note=\"QXSXEXXXL\"\nFT                   /evidence=\"ECO:0000305|PubMed:21075925\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:43.395652+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da6321a7443875e32e6bbf173da14447e97ad6ff8b2144b4fcda915239520af3",
  "url": "https://rest.uniprot.org/unisave/Q6M0N4?format=txt&versions=76"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
