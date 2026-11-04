# EC_number_0076

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0076.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 5.4.99.14

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIRILYLLVKPESMSHEQFRKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV

[Multiple Choices]
A. 5.3.1.16
B. 1.14.14.187
C. 5.4.99.14
D. 2.5.1.56
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

> The sequence matches the UniProt entry whose experimentally supported catalytic activity is EC 5.4.99.14, the conversion of 4-methylmuconolactone to 3-methylmuconolactone. The annotation cites experimental evidence, though the exact author source snapshot is unknown.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The catalytic activity or a reliable family assignment for this exact sequence; the input provides no reaction, organism, homolog, or diagnostic motif that establishes which isomerase activity it has.


**Reason**

> Sequence length and the absence of an obvious P450 hallmark make some choices less plausible, but do not distinguish the offered isomerase alternatives reliably. The specific substrate rearrangement defining EC 5.4.99.14 is not established by a general sequence feature visible here; identifying it would require target-specific functional annotation or a sufficiently informative homology/family match.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports choice C; no competing option is supported as a defensible EC assignment for this sequence.


### Important caveats

- The experimental annotation is for a sequence-matched database entry; the actual author source snapshot is unknown.
- Reviewer-only accession, organism, and functional annotation were not original model inputs and are not used as transferable evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The catalytic activity or a reliable family assignment for this exact sequence; the input provides no reaction, organism, homolog, or diagnostic motif that establishes which isomerase activity it has.",
    "reason": "Sequence length and the absence of an obvious P450 hallmark make some choices less plausible, but do not distinguish the offered isomerase alternatives reliably. The specific substrate rearrangement defining EC 5.4.99.14 is not established by a general sequence feature visible here; identifying it would require target-specific functional annotation or a sufficiently informative homology/family match."
  },
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry whose experimentally supported catalytic activity is EC 5.4.99.14, the conversion of 4-methylmuconolactone to 3-methylmuconolactone. The annotation cites experimental evidence, though the exact author source snapshot is unknown."
  },
  "important_caveats": [
    "The experimental annotation is for a sequence-matched database entry; the actual author source snapshot is unknown.",
    "Reviewer-only accession, organism, and functional annotation were not original model inputs and are not used as transferable evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice C; no competing option is supported as a defensible EC assignment for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry whose experimentally supported catalytic activity is EC 5.4.99.14, the conversion of 4-methylmuconolactone to 3-methylmuconolactone. The annotation cites experimental evidence, though the exact author source snapshot is unknown.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The catalytic activity or a reliable family assignment for this exact sequence; the input provides no reaction, organism, homolog, or diagnostic motif that establishes which isomerase activity it has.",
    "reason": "Sequence length and the absence of an obvious P450 hallmark make some choices less plausible, but do not distinguish the offered isomerase alternatives reliably. The specific substrate rearrangement defining EC 5.4.99.14 is not established by a general sequence feature visible here; identifying it would require target-specific functional annotation or a sufficiently informative homology/family match."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice C; no competing option is supported as a defensible EC assignment for this sequence."
  },
  "important_caveats": [
    "The experimental annotation is for a sequence-matched database entry; the actual author source snapshot is unknown.",
    "Reviewer-only accession, organism, and functional annotation were not original model inputs and are not used as transferable evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C5MR76 (MMLI_PSERE) from Pseudomonas reinekei is annotated with EC 5.4.99.14 (4-carboxymethyl-4-methylbutenolide mutase / 4-methylmuconolactone methylisomerase). The evidence code ECO:0000269 indicates direct experimental evidence from PubMed:19801657 (Marin et al., J. Biol. Chem. 2009), which includes X-ray crystallography (PDB 3HDS, 3HF5, 3HFK), mutagenesis of active-site residues (His-26, Tyr-39, His-52, Cys-67), and catalytic activity assays. The reaction is 4-methylmuconolactone = 3-methylmuconolactone (Rhea:RHEA:19237). The sequence in the benchmark matches the UniProt sequence exactly (107 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can reliably eliminate B (EC 1.14.14.187, a cytochrome P450-type oxidoreductase requiring ~400-500+ residues and a conserved heme-binding FxxGxxxCxG motif) and D (EC 2.5.1.56, a methyltransferase requiring a SAM-binding Rossmann-like fold with motifs like VIGXG) based on the 107-residue length and absence of these structural motifs. However, the remaining choices A (5.3.1.16, muconolactone isomerase) and C (5.4.99.14, 4-methylmuconolactone methylisomerase) share the MLI (muconolactone isomerase) fold, are nearly identical in length (~100 vs 107 residues), and share an essentially identical C-terminal catalytic domain (the sequence from approximately 'RKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV' is conserved between canonical CatB and this MLMI). The only visible sequence difference is a ~16-residue N-terminal extension (MIRILYLLVKPESMSHEQ) absent in canonical CatB. While this extension is a recognizable subfamily marker, it does not by itself reveal whether the enzyme catalyzes an intramolecular oxidation-reduction (EC 5.3) or an intramolecular methyl-group transfer (EC 5.4). Distinguishing the mechanistic class (oxidoreductase vs mutase) requires knowing that this particular protein acts on a methylated substrate (4-methylmuconolactone) via a methyl-shift mechanism rather than the ring-opening oxidation-reduction used by canonical muconolactone isomerase — a fact specific to this enzyme's experimental characterization.


**Missing item-specific fact**

> The specific substrate preference (methylated vs unmethylated muconolactone) and the mechanistic distinction (intramolecular methyl transfer = mutase EC 5.4 vs intramolecular oxidation-reduction = oxidoreductase EC 5.3) for this exact protein, which cannot be inferred from the sequence alone given the near-identical catalytic domain shared with EC 5.3.1.16.


**Reason**

> Options B and D are eliminable by general structural/biochemical knowledge (size, fold, motifs). Options A and C are both MLI-fold isomerases of similar size with essentially identical catalytic-domain sequences. The N-terminal extension is a visible feature but does not mechanistically predict mutase vs oxidoreductase activity. Distinguishing 5.3.1.16 from 5.4.99.14 requires knowing this protein's specific substrate and mechanism, which is a fact about this exact protein established by experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both EC 5.3.1.16 (muconolactone isomerase) and EC 5.4.99.14 (4-methylmuconolactone methylisomerase) belong to the MLI fold family, have similar sizes (~100-107 residues), and share a highly conserved catalytic domain. From the sequence alone, without specific knowledge of the MLMI subfamily annotation, a model could reasonably assign either EC 5.3.1.16 or 5.4.99.14. The N-terminal extension is suggestive but not mechanistically diagnostic.


### Important caveats

- The EC 5.4.99.14 annotation carries evidence code ECO:0000269 (direct experimental evidence), making it a high-confidence annotation.
- The sequence identity between this MLMI and canonical CatB (EC 5.3.1.16) in the catalytic domain is extremely high, making sequence-based discrimination between A and C inherently difficult.
- The UniProt entry was first publicly released in April 2025; the author's data-construction date and source snapshot are unknown, so the annotation availability at question-creation time is uncertain.
- The reviewer-only accession (C5MR76) was inferred from dataset metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can reliably eliminate B (EC 1.14.14.187, a cytochrome P450-type oxidoreductase requiring ~400-500+ residues and a conserved heme-binding FxxGxxxCxG motif) and D (EC 2.5.1.56, a methyltransferase requiring a SAM-binding Rossmann-like fold with motifs like VIGXG) based on the 107-residue length and absence of these structural motifs. However, the remaining choices A (5.3.1.16, muconolactone isomerase) and C (5.4.99.14, 4-methylmuconolactone methylisomerase) share the MLI (muconolactone isomerase) fold, are nearly identical in length (~100 vs 107 residues), and share an essentially identical C-terminal catalytic domain (the sequence from approximately 'RKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV' is conserved between canonical CatB and this MLMI). The only visible sequence difference is a ~16-residue N-terminal extension (MIRILYLLVKPESMSHEQ) absent in canonical CatB. While this extension is a recognizable subfamily marker, it does not by itself reveal whether the enzyme catalyzes an intramolecular oxidation-reduction (EC 5.3) or an intramolecular methyl-group transfer (EC 5.4). Distinguishing the mechanistic class (oxidoreductase vs mutase) requires knowing that this particular protein acts on a methylated substrate (4-methylmuconolactone) via a methyl-shift mechanism rather than the ring-opening oxidation-reduction used by canonical muconolactone isomerase — a fact specific to this enzyme's experimental characterization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate preference (methylated vs unmethylated muconolactone) and the mechanistic distinction (intramolecular methyl transfer = mutase EC 5.4 vs intramolecular oxidation-reduction = oxidoreductase EC 5.3) for this exact protein, which cannot be inferred from the sequence alone given the near-identical catalytic domain shared with EC 5.3.1.16.",
    "reason": "Options B and D are eliminable by general structural/biochemical knowledge (size, fold, motifs). Options A and C are both MLI-fold isomerases of similar size with essentially identical catalytic-domain sequences. The N-terminal extension is a visible feature but does not mechanistically predict mutase vs oxidoreductase activity. Distinguishing 5.3.1.16 from 5.4.99.14 requires knowing this protein's specific substrate and mechanism, which is a fact about this exact protein established by experimental characterization."
  },
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C5MR76 (MMLI_PSERE) from Pseudomonas reinekei is annotated with EC 5.4.99.14 (4-carboxymethyl-4-methylbutenolide mutase / 4-methylmuconolactone methylisomerase). The evidence code ECO:0000269 indicates direct experimental evidence from PubMed:19801657 (Marin et al., J. Biol. Chem. 2009), which includes X-ray crystallography (PDB 3HDS, 3HF5, 3HFK), mutagenesis of active-site residues (His-26, Tyr-39, His-52, Cys-67), and catalytic activity assays. The reaction is 4-methylmuconolactone = 3-methylmuconolactone (Rhea:RHEA:19237). The sequence in the benchmark matches the UniProt sequence exactly (107 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The EC 5.4.99.14 annotation carries evidence code ECO:0000269 (direct experimental evidence), making it a high-confidence annotation.",
    "The sequence identity between this MLMI and canonical CatB (EC 5.3.1.16) in the catalytic domain is extremely high, making sequence-based discrimination between A and C inherently difficult.",
    "The UniProt entry was first publicly released in April 2025; the author's data-construction date and source snapshot are unknown, so the annotation availability at question-creation time is uncertain.",
    "The reviewer-only accession (C5MR76) was inferred from dataset metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both EC 5.3.1.16 (muconolactone isomerase) and EC 5.4.99.14 (4-methylmuconolactone methylisomerase) belong to the MLI fold family, have similar sizes (~100-107 residues), and share a highly conserved catalytic domain. From the sequence alone, without specific knowledge of the MLMI subfamily annotation, a model could reasonably assign either EC 5.3.1.16 or 5.4.99.14. The N-terminal extension is suggestive but not mechanistically diagnostic."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C5MR76 (MMLI_PSERE) from Pseudomonas reinekei is annotated with EC 5.4.99.14 (4-carboxymethyl-4-methylbutenolide mutase / 4-methylmuconolactone methylisomerase). The evidence code ECO:0000269 indicates direct experimental evidence from PubMed:19801657 (Marin et al., J. Biol. Chem. 2009), which includes X-ray crystallography (PDB 3HDS, 3HF5, 3HFK), mutagenesis of active-site residues (His-26, Tyr-39, His-52, Cys-67), and catalytic activity assays. The reaction is 4-methylmuconolactone = 3-methylmuconolactone (Rhea:RHEA:19237). The sequence in the benchmark matches the UniProt sequence exactly (107 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can reliably eliminate B (EC 1.14.14.187, a cytochrome P450-type oxidoreductase requiring ~400-500+ residues and a conserved heme-binding FxxGxxxCxG motif) and D (EC 2.5.1.56, a methyltransferase requiring a SAM-binding Rossmann-like fold with motifs like VIGXG) based on the 107-residue length and absence of these structural motifs. However, the remaining choices A (5.3.1.16, muconolactone isomerase) and C (5.4.99.14, 4-methylmuconolactone methylisomerase) share the MLI (muconolactone isomerase) fold, are nearly identical in length (~100 vs 107 residues), and share an essentially identical C-terminal catalytic domain (the sequence from approximately 'RKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV' is conserved between canonical CatB and this MLMI). The only visible sequence difference is a ~16-residue N-terminal extension (MIRILYLLVKPESMSHEQ) absent in canonical CatB. While this extension is a recognizable subfamily marker, it does not by itself reveal whether the enzyme catalyzes an intramolecular oxidation-reduction (EC 5.3) or an intramolecular methyl-group transfer (EC 5.4). Distinguishing the mechanistic class (oxidoreductase vs mutase) requires knowing that this particular protein acts on a methylated substrate (4-methylmuconolactone) via a methyl-shift mechanism rather than the ring-opening oxidation-reduction used by canonical muconolactone isomerase — a fact specific to this enzyme's experimental characterization.",
    "missing_item_specific_fact": "The specific substrate preference (methylated vs unmethylated muconolactone) and the mechanistic distinction (intramolecular methyl transfer = mutase EC 5.4 vs intramolecular oxidation-reduction = oxidoreductase EC 5.3) for this exact protein, which cannot be inferred from the sequence alone given the near-identical catalytic domain shared with EC 5.3.1.16.",
    "reason": "Options B and D are eliminable by general structural/biochemical knowledge (size, fold, motifs). Options A and C are both MLI-fold isomerases of similar size with essentially identical catalytic-domain sequences. The N-terminal extension is a visible feature but does not mechanistically predict mutase vs oxidoreductase activity. Distinguishing 5.3.1.16 from 5.4.99.14 requires knowing this protein's specific substrate and mechanism, which is a fact about this exact protein established by experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both EC 5.3.1.16 (muconolactone isomerase) and EC 5.4.99.14 (4-methylmuconolactone methylisomerase) belong to the MLI fold family, have similar sizes (~100-107 residues), and share a highly conserved catalytic domain. From the sequence alone, without specific knowledge of the MLMI subfamily annotation, a model could reasonably assign either EC 5.3.1.16 or 5.4.99.14. The N-terminal extension is suggestive but not mechanistically diagnostic."
  },
  "important_caveats": [
    "The EC 5.4.99.14 annotation carries evidence code ECO:0000269 (direct experimental evidence), making it a high-confidence annotation.",
    "The sequence identity between this MLMI and canonical CatB (EC 5.3.1.16) in the catalytic domain is extremely high, making sequence-based discrimination between A and C inherently difficult.",
    "The UniProt entry was first publicly released in April 2025; the author's data-construction date and source snapshot are unknown, so the annotation availability at question-creation time is uncertain.",
    "The reviewer-only accession (C5MR76) was inferred from dataset metadata and was not available to the evaluated model."
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
  "benchmark_sequence_length": 107,
  "benchmark_sequence_sha256": "9b6ceb842a92c4daf2e9899c4fc70734536969d2e135a330b0230d9b3d196226",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-07-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 107,
  "current_source_sequence_sha256": "9b6ceb842a92c4daf2e9899c4fc70734536969d2e135a330b0230d9b3d196226",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C5MR76",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa",
  "selected_historical_source_sequence_length": 107,
  "selected_historical_source_sequence_sha256": "9b6ceb842a92c4daf2e9899c4fc70734536969d2e135a330b0230d9b3d196226",
  "selected_historical_version": {
    "accession": "C5MR76",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MMLI_PSERE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C5MR76\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:31.044476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "url": "https://rest.uniprot.org/uniprotkb/C5MR76.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-07-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:31.044476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "url": "https://rest.uniprot.org/uniprotkb/C5MR76.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas reinekei\",\"taxonId\":395598}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:31.044476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "url": "https://rest.uniprot.org/uniprotkb/C5MR76.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19801657\",\"source\":\"PubMed\"}],\"value\":\"4-methylmuconolactone methylisomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19801657\",\"source\":\"PubMed\"}],\"value\":\"MLMI\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19801657\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4-carboxymethyl-4-methylbutenolide mutase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:31.044476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "url": "https://rest.uniprot.org/uniprotkb/C5MR76.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19801657\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:19238\"}}],\"reaction\":{\"ecNumber\":\"5.4.99.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19801657\",\"source\":\"PubMed\"}],\"name\":\"4-methylmuconolactone = 3-methylmuconolactone\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19237\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57883\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57888\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:31.044476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "url": "https://rest.uniprot.org/uniprotkb/C5MR76.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Marin M.\",\"Heinz D.W.\",\"Pieper D.H.\",\"Klink B.U.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19801657\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.024604\"}],\"citationType\":\"journal article\",\"firstPage\":\"32709\",\"id\":\"19801657\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"32716\",\"publicationDate\":\"2009\",\"title\":\"Crystal structure and catalytic mechanism of 4-methylmuconolactone methylisomerase.\",\"volume\":\"284\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACR82080.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HDS\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HF5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HFK\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 18361 / CCUG 53116 / MT1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS) IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH 4-METHYLMUCONOLACTONE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROPOSED REACTION MECHANISM\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\",\"ACTIVE SITE\",\"MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:27:31.044476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32",
  "url": "https://rest.uniprot.org/uniprotkb/C5MR76.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   MMLI_PSERE              Reviewed;         107 AA.\nAC   C5MR76;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-JUL-2009, sequence version 1.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};\nDE            EC=5.4.99.14 {ECO:0000269|PubMed:19801657};\nDE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:19801657};\nDE            Short=MLMI {ECO:0000303|PubMed:19801657};\nGN   Name=mmlI {ECO:0000303|PubMed:19801657, ECO:0000303|PubMed:20061479};\nGN   ORFNames=BVK86_00405 {ECO:0000312|EMBL:OLU05856.1},\nGN   F7R15_00410 {ECO:0000312|EMBL:KAB0488369.1},\nGN   SAMN04490202_5523 {ECO:0000312|EMBL:SDP67526.1};\nOS   Pseudomonas reinekei.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=395598;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.227817+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa",
  "url": "https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};\nDE            EC=5.4.99.14 {ECO:0000269|PubMed:19801657};\nDE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:19801657};\nDE            Short=MLMI {ECO:0000303|PubMed:19801657};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.227817+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa",
  "url": "https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ACR82080.1, ECO:0007744|PDB:3HDS, ECO:0007744|PDB:3HF5, ECO:0007744|PDB:3HFK}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS)\nRP   IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH\nRP   4-METHYLMUCONOLACTONE, FUNCTION, CATALYTIC ACTIVITY, PROPOSED REACTION\nRP   MECHANISM, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,\nRP   DOMAIN, ACTIVE SITE, AND MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67.\nRC   STRAIN=DSM 18361 / CCUG 53116 / MT1;\nRX   PubMed=19801657; DOI=10.1074/jbc.m109.024604;\nRA   Marin M., Heinz D.W., Pieper D.H., Klink B.U.;\nRT   \"Crystal structure and catalytic mechanism of 4-methylmuconolactone\nRT   methylisomerase.\";\nRL   J. Biol. Chem. 284:32709-32716(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.227817+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa",
  "url": "https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ACR82080.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=DSM 18361 / CCUG 53116 / MT1;\nRX   PubMed=20061479; DOI=10.1128/jb.01208-09;\nRA   Marin M., Perez-Pantoja D., Donoso R., Wray V., Gonzalez B., Pieper D.H.;\nRT   \"Modified 3-oxoadipate pathway for the biodegradation of methylaromatics in\nRT   Pseudomonas reinekei MT1.\";\nRL   J. Bacteriol. 192:1543-1552(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.227817+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa",
  "url": "https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;\nCC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;\nCC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:19801657};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;\nCC         Evidence={ECO:0000305|PubMed:19801657};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.227817+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa",
  "url": "https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
