# EC_number_0021

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0021.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 5.4.99.14

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIRLLYLLVKPAGMSDETFRAECLRHYEMSHDVPGLHKYEVRLVAEQPTDTHVPFFDIGHVDAIGECWFKDDAAYATYMASDIRKAWFEHGKTFIGQLKPFRTAPVAGDEPAS

[Multiple Choices]
A. 5.4.99.39
B. 3.1.1.80
C. 4.2.1.183
D. 5.4.99.14
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns EC 5.4.99.14 and describes the reaction as 4-methylmuconolactone = 3-methylmuconolactone, citing experimental evidence from published studies.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's specific catalytic reaction, or a reliable match to a characterized homolog that establishes that reaction, is not supplied.


**Reason**

> The 113-aa sequence has no evident catalytic motif or context that distinguishes these particular EC assignments. In particular, A and D are both EC 5.4.99 mutases; choosing between them requires identifying the specific reaction rather than inferring only a broad enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied source evidence supports D; it does not support another listed option.


### Important caveats

- The source records match the supplied sequence, but the author's exact source snapshot is unknown.
- The source annotation cites experimental evidence; this assessment relies on the cited evidence as represented in the record, not independent review of the primary studies.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific catalytic reaction, or a reliable match to a characterized homolog that establishes that reaction, is not supplied.",
    "reason": "The 113-aa sequence has no evident catalytic motif or context that distinguishes these particular EC assignments. In particular, A and D are both EC 5.4.99 mutases; choosing between them requires identifying the specific reaction rather than inferring only a broad enzyme class."
  },
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 5.4.99.14 and describes the reaction as 4-methylmuconolactone = 3-methylmuconolactone, citing experimental evidence from published studies."
  },
  "important_caveats": [
    "The source records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The source annotation cites experimental evidence; this assessment relies on the cited evidence as represented in the record, not independent review of the primary studies."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied source evidence supports D; it does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 5.4.99.14 and describes the reaction as 4-methylmuconolactone = 3-methylmuconolactone, citing experimental evidence from published studies.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's specific catalytic reaction, or a reliable match to a characterized homolog that establishes that reaction, is not supplied.",
    "reason": "The 113-aa sequence has no evident catalytic motif or context that distinguishes these particular EC assignments. In particular, A and D are both EC 5.4.99 mutases; choosing between them requires identifying the specific reaction rather than inferring only a broad enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied source evidence supports D; it does not support another listed option."
  },
  "important_caveats": [
    "The source records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The source annotation cites experimental evidence; this assessment relies on the cited evidence as represented in the record, not independent review of the primary studies."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O51799 (MMLI_CUPPJ) is annotated with EC 5.4.99.14 supported by experimental evidence (ECO:0000269) from two independent PubMed references (9461415 and 2241929). The sequence in the benchmark matches the UniProt sequence exactly (SHA256 verified). The catalytic reaction (4-methylmuconolactone = 3-methylmuconolactone) is confirmed with Rhea cross-references. The annotation has been stable since the entry's creation in 1998.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence (113 aa) lacks typical serine-hydrolase motifs (GxSxG, catalytic triad) making B (3.1.1.80, a carboxylesterase) somewhat unlikely, and lacks obvious lyase catalytic architecture making C (4.2.1.183) less likely. However, the critical distinction is between A (5.4.99.39) and D (5.4.99.14), both of which are intramolecular transferases (mutases) in the 5.4.99.- class. The EC 5.4.99.- subclass contains numerous very specific mutases distinguished solely by their exact substrate. Without recognizing this sequence as MLMI or a close homolog from the modified 3-oxoadipate pathway, there is no generalizable sequence motif or family-level feature that distinguishes a methyl-migration mutase acting on methylmuconolactone (5.4.99.14) from another specific 5.4.99.- mutase (5.4.99.39). The 113-residue sequence provides no cofactor-binding domain, no PLP motif, and no large structural signature that would transfer across the 5.4.99.- family to narrow the specific 4-digit number.


**Missing item-specific fact**

> The specific substrate identity (4-methylmuconolactone) and the particular methyl-group migration chemistry that defines EC 5.4.99.14 versus EC 5.4.99.39. This is a property of this exact enzyme's active-site architecture and substrate pocket, not a feature inferable from general mutase-family knowledge or from the short sequence alone.


**Reason**

> While the broader EC class (mutase vs. hydrolase vs. lyase) can be partially narrowed by the absence of hydrolase/lyase motifs, the decisive discrimination between the two 5.4.99.- options (A and D) requires knowing the specific substrate and reaction of this enzyme. No conserved family-level sequence feature shared broadly with other 5.4.99.- enzymes distinguishes 5.4.99.14 from 5.4.99.39 without recognizing this particular protein or its immediate homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (5.4.99.39) and D (5.4.99.14) belong to the same EC subclass (5.4.99.-, other intramolecular transferases). Without specific substrate knowledge or recognition of the MLMI protein family, a model cannot reliably distinguish which specific 5.4.99.- mutase this 113-aa sequence encodes. The sequence provides no obvious feature that separates one 5.4.99.- enzyme from another.


### Important caveats

- The protein is only 113 amino acids, limiting the amount of sequence information available for family-level inference.
- The EC 5.4.99.- subclass contains many highly specific mutases; general 'mutase' knowledge does not narrow to a 4-digit number.
- The reviewer evidence confirms the annotation experimentally (ECO:0000269), but this experimental knowledge was not available to the evaluated model.
- If well-characterized MLMI homologs exist in other organisms (e.g., Pseudomonas, Rhodococcus) with shared sequence motifs, family recognition could theoretically help, but this borders on recognizing the specific protein rather than a broadly transferable family pattern.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (113 aa) lacks typical serine-hydrolase motifs (GxSxG, catalytic triad) making B (3.1.1.80, a carboxylesterase) somewhat unlikely, and lacks obvious lyase catalytic architecture making C (4.2.1.183) less likely. However, the critical distinction is between A (5.4.99.39) and D (5.4.99.14), both of which are intramolecular transferases (mutases) in the 5.4.99.- class. The EC 5.4.99.- subclass contains numerous very specific mutases distinguished solely by their exact substrate. Without recognizing this sequence as MLMI or a close homolog from the modified 3-oxoadipate pathway, there is no generalizable sequence motif or family-level feature that distinguishes a methyl-migration mutase acting on methylmuconolactone (5.4.99.14) from another specific 5.4.99.- mutase (5.4.99.39). The 113-residue sequence provides no cofactor-binding domain, no PLP motif, and no large structural signature that would transfer across the 5.4.99.- family to narrow the specific 4-digit number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (4-methylmuconolactone) and the particular methyl-group migration chemistry that defines EC 5.4.99.14 versus EC 5.4.99.39. This is a property of this exact enzyme's active-site architecture and substrate pocket, not a feature inferable from general mutase-family knowledge or from the short sequence alone.",
    "reason": "While the broader EC class (mutase vs. hydrolase vs. lyase) can be partially narrowed by the absence of hydrolase/lyase motifs, the decisive discrimination between the two 5.4.99.- options (A and D) requires knowing the specific substrate and reaction of this enzyme. No conserved family-level sequence feature shared broadly with other 5.4.99.- enzymes distinguishes 5.4.99.14 from 5.4.99.39 without recognizing this particular protein or its immediate homologs."
  },
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O51799 (MMLI_CUPPJ) is annotated with EC 5.4.99.14 supported by experimental evidence (ECO:0000269) from two independent PubMed references (9461415 and 2241929). The sequence in the benchmark matches the UniProt sequence exactly (SHA256 verified). The catalytic reaction (4-methylmuconolactone = 3-methylmuconolactone) is confirmed with Rhea cross-references. The annotation has been stable since the entry's creation in 1998."
  },
  "important_caveats": [
    "The protein is only 113 amino acids, limiting the amount of sequence information available for family-level inference.",
    "The EC 5.4.99.- subclass contains many highly specific mutases; general 'mutase' knowledge does not narrow to a 4-digit number.",
    "The reviewer evidence confirms the annotation experimentally (ECO:0000269), but this experimental knowledge was not available to the evaluated model.",
    "If well-characterized MLMI homologs exist in other organisms (e.g., Pseudomonas, Rhodococcus) with shared sequence motifs, family recognition could theoretically help, but this borders on recognizing the specific protein rather than a broadly transferable family pattern."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (5.4.99.39) and D (5.4.99.14) belong to the same EC subclass (5.4.99.-, other intramolecular transferases). Without specific substrate knowledge or recognition of the MLMI protein family, a model cannot reliably distinguish which specific 5.4.99.- mutase this 113-aa sequence encodes. The sequence provides no obvious feature that separates one 5.4.99.- enzyme from another."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O51799 (MMLI_CUPPJ) is annotated with EC 5.4.99.14 supported by experimental evidence (ECO:0000269) from two independent PubMed references (9461415 and 2241929). The sequence in the benchmark matches the UniProt sequence exactly (SHA256 verified). The catalytic reaction (4-methylmuconolactone = 3-methylmuconolactone) is confirmed with Rhea cross-references. The annotation has been stable since the entry's creation in 1998.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence (113 aa) lacks typical serine-hydrolase motifs (GxSxG, catalytic triad) making B (3.1.1.80, a carboxylesterase) somewhat unlikely, and lacks obvious lyase catalytic architecture making C (4.2.1.183) less likely. However, the critical distinction is between A (5.4.99.39) and D (5.4.99.14), both of which are intramolecular transferases (mutases) in the 5.4.99.- class. The EC 5.4.99.- subclass contains numerous very specific mutases distinguished solely by their exact substrate. Without recognizing this sequence as MLMI or a close homolog from the modified 3-oxoadipate pathway, there is no generalizable sequence motif or family-level feature that distinguishes a methyl-migration mutase acting on methylmuconolactone (5.4.99.14) from another specific 5.4.99.- mutase (5.4.99.39). The 113-residue sequence provides no cofactor-binding domain, no PLP motif, and no large structural signature that would transfer across the 5.4.99.- family to narrow the specific 4-digit number.",
    "missing_item_specific_fact": "The specific substrate identity (4-methylmuconolactone) and the particular methyl-group migration chemistry that defines EC 5.4.99.14 versus EC 5.4.99.39. This is a property of this exact enzyme's active-site architecture and substrate pocket, not a feature inferable from general mutase-family knowledge or from the short sequence alone.",
    "reason": "While the broader EC class (mutase vs. hydrolase vs. lyase) can be partially narrowed by the absence of hydrolase/lyase motifs, the decisive discrimination between the two 5.4.99.- options (A and D) requires knowing the specific substrate and reaction of this enzyme. No conserved family-level sequence feature shared broadly with other 5.4.99.- enzymes distinguishes 5.4.99.14 from 5.4.99.39 without recognizing this particular protein or its immediate homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (5.4.99.39) and D (5.4.99.14) belong to the same EC subclass (5.4.99.-, other intramolecular transferases). Without specific substrate knowledge or recognition of the MLMI protein family, a model cannot reliably distinguish which specific 5.4.99.- mutase this 113-aa sequence encodes. The sequence provides no obvious feature that separates one 5.4.99.- enzyme from another."
  },
  "important_caveats": [
    "The protein is only 113 amino acids, limiting the amount of sequence information available for family-level inference.",
    "The EC 5.4.99.- subclass contains many highly specific mutases; general 'mutase' knowledge does not narrow to a 4-digit number.",
    "The reviewer evidence confirms the annotation experimentally (ECO:0000269), but this experimental knowledge was not available to the evaluated model.",
    "If well-characterized MLMI homologs exist in other organisms (e.g., Pseudomonas, Rhodococcus) with shared sequence motifs, family recognition could theoretically help, but this borders on recognizing the specific protein rather than a broadly transferable family pattern."
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
  "benchmark_sequence_length": 113,
  "benchmark_sequence_sha256": "5cff0d57cd7ece41c777ddb6189bfa6b989a549198f8086c53758f07f892f181",
  "current_entry_audit": {
    "entryVersion": 67,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 113,
  "current_source_sequence_sha256": "5cff0d57cd7ece41c777ddb6189bfa6b989a549198f8086c53758f07f892f181",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 65,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O51799",
  "selected_historical_entry_version": 65,
  "selected_historical_record_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "selected_historical_source_sequence_length": 113,
  "selected_historical_source_sequence_sha256": "5cff0d57cd7ece41c777ddb6189bfa6b989a549198f8086c53758f07f892f181",
  "selected_historical_version": {
    "accession": "O51799",
    "database": "Swiss-Prot",
    "entryVersion": 65,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MMLI_CUPPJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O51799\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":67,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cupriavidus necator (strain JMP 134)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Cupriavidus\"],\"scientificName\":\"Cupriavidus pinatubonensis (strain JMP 134 / LMG 1197)\",\"taxonId\":264198}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"2241929\",\"source\":\"PubMed\"}],\"value\":\"4-carboxymethyl-4-methylbut-2-en-4-olide isomerase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"2241929\",\"source\":\"PubMed\"}],\"value\":\"4-methyl-2-enelactone isomerase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"4-methylmuconolactone methylisomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"MLMI\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4-carboxymethyl-4-methylbutenolide mutase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:19238\"}}],\"reaction\":{\"ecNumber\":\"5.4.99.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"name\":\"4-methylmuconolactone = 3-methylmuconolactone\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19237\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57883\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57888\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Erb R.W.\",\"Timmis K.N.\",\"Pieper D.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9461415\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0378-1119(97)00565-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"53\",\"id\":\"9461415\",\"journal\":\"Gene\",\"lastPage\":\"62\",\"publicationDate\":\"1998\",\"title\":\"Characterization of a gene cluster from Ralstonia eutropha JMP134 encoding metabolism of 4-methylmuconolactone.\",\"volume\":\"206\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAA67958.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"JMP134 / LMG 1197\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Pieper D.H.\",\"Stadler-Fritzsche K.\",\"Knackmuss H.J.\",\"Engesser K.H.\",\"Bruce N.C.\",\"Cain R.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"2241929\"},{\"database\":\"DOI\",\"id\":\"10.1042/bj2710529\"}],\"citationType\":\"journal article\",\"firstPage\":\"529\",\"id\":\"2241929\",\"journal\":\"Biochem. J.\",\"lastPage\":\"534\",\"publicationDate\":\"1990\",\"title\":\"Purification and characterization of 4-methylmuconolactone methylisomerase, a novel enzyme of the modified 3-oxoadipate pathway in the gram-negative bacterium Alcaligenes eutrophus JMP 134.\",\"volume\":\"271\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"JMP134 / LMG 1197\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H1",
  "excerpt": "ID   MMLI_CUPPJ              Reviewed;         113 AA.\nAC   O51799; Q471R3;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-1998, sequence version 1.\nDT   28-JAN-2026, entry version 65.\nDE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};\nDE            EC=5.4.99.14 {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};\nDE   AltName: Full=4-carboxymethyl-4-methylbut-2-en-4-olide isomerase {ECO:0000303|PubMed:2241929};\nDE   AltName: Full=4-methyl-2-enelactone isomerase {ECO:0000303|PubMed:2241929};\nDE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:2241929, ECO:0000303|PubMed:9461415};\nDE            Short=MLMI {ECO:0000303|PubMed:9461415};\nGN   Name=mmlI {ECO:0000303|PubMed:9461415};\nGN   OrderedLocusNames=Reut_A1503 {ECO:0000312|EMBL:AAZ60870.1};\nOS   Cupriavidus pinatubonensis (strain JMP 134 / LMG 1197) (Cupriavidus necator\nOS   (strain JMP 134)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Cupriavidus.\nOX   NCBI_TaxID=264198;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};\nDE            EC=5.4.99.14 {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};\nDE   AltName: Full=4-carboxymethyl-4-methylbut-2-en-4-olide isomerase {ECO:0000303|PubMed:2241929};\nDE   AltName: Full=4-methyl-2-enelactone isomerase {ECO:0000303|PubMed:2241929};\nDE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:2241929, ECO:0000303|PubMed:9461415};\nDE            Short=MLMI {ECO:0000303|PubMed:9461415};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAA67958.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   SUBUNIT.\nRC   STRAIN=JMP134 / LMG 1197;\nRX   PubMed=9461415; DOI=10.1016/s0378-1119(97)00565-9;\nRA   Erb R.W., Timmis K.N., Pieper D.H.;\nRT   \"Characterization of a gene cluster from Ralstonia eutropha JMP134 encoding\nRT   metabolism of 4-methylmuconolactone.\";\nRL   Gene 206:53-62(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, AND BIOPHYSICOCHEMICAL\nRP   PROPERTIES.\nRC   STRAIN=JMP134 / LMG 1197;\nRX   PubMed=2241929; DOI=10.1042/bj2710529;\nRA   Pieper D.H., Stadler-Fritzsche K., Knackmuss H.J., Engesser K.H.,\nRA   Bruce N.C., Cain R.B.;\nRT   \"Purification and characterization of 4-methylmuconolactone\nRT   methylisomerase, a novel enzyme of the modified 3-oxoadipate pathway in the\nRT   gram-negative bacterium Alcaligenes eutrophus JMP 134.\";\nRL   Biochem. J. 271:529-534(1990).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;\nCC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;\nCC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:2241929,\nCC         ECO:0000269|PubMed:9461415};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;\nCC         Evidence={ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
