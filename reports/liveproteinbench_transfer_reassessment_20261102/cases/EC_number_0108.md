# EC_number_0108

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0108.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.1.3.112

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSLLDIIYQLRQVPRWDGSFQFEKEDVSQHSFSVIAISHILCELKETLEGKKINKEKLLLYALYHDVTEVVSTHIISPVKKNSILKDPFNAFREQIKNSLFDNLPITLSDTLSTILNNNDLEIQEIVEHADHVDAYCKSCIEVHRGNKDFISIQRSLGDKLDNLTKEYPYLKEFQNLFLKDFPLENKNYRYLN

[Multiple Choices]
A. 3.1.3.2
B. 3.1.3.112
C. 1.3.1.36
D. 4.3.3.9
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

> The sequence-matched UniProt entry assigns EC 3.1.3.112 and gives the corresponding phosphatase reaction, with experimental evidence codes citing two publications. This supports the key, though the evidence is an annotation reporting experimental findings rather than an independent review of those studies.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an H-D motif (in the segment EIVEHADHVD) consistent with an HD-domain metal-dependent phosphohydrolase. That family-level clue favors a phosphatase choice over the oxidoreductase and lyase alternatives, and gives a credible basis to favor the specialized HD-domain phosphatase choice B over the broad acid-phosphatase choice A. This is a probabilistic family-based inference, not a way to establish the exact substrate from the sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of HD-domain phosphohydrolases meaningfully favors B among these choices. The motif does not independently prove the enzyme’s precise substrate specificity, but the alternatives do not require exact experimental reconstruction for a defensible choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The HD-domain clue favors the phosphohydrolase option B; the other offered choices are less consistent with that family-level signal.


### Important caveats

- The sequence alone does not establish the specialized substrate reaction or guarantee the complete EC number.
- The cited database annotation and experimental evidence are reviewer-only and were not supplied as original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an H-D motif (in the segment EIVEHADHVD) consistent with an HD-domain metal-dependent phosphohydrolase. That family-level clue favors a phosphatase choice over the oxidoreductase and lyase alternatives, and gives a credible basis to favor the specialized HD-domain phosphatase choice B over the broad acid-phosphatase choice A. This is a probabilistic family-based inference, not a way to establish the exact substrate from the sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of HD-domain phosphohydrolases meaningfully favors B among these choices. The motif does not independently prove the enzyme’s precise substrate specificity, but the alternatives do not require exact experimental reconstruction for a defensible choice."
  },
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.1.3.112 and gives the corresponding phosphatase reaction, with experimental evidence codes citing two publications. This supports the key, though the evidence is an annotation reporting experimental findings rather than an independent review of those studies."
  },
  "important_caveats": [
    "The sequence alone does not establish the specialized substrate reaction or guarantee the complete EC number.",
    "The cited database annotation and experimental evidence are reviewer-only and were not supplied as original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HD-domain clue favors the phosphohydrolase option B; the other offered choices are less consistent with that family-level signal."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.1.3.112 and gives the corresponding phosphatase reaction, with experimental evidence codes citing two publications. This supports the key, though the evidence is an annotation reporting experimental findings rather than an independent review of those studies.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an H-D motif (in the segment EIVEHADHVD) consistent with an HD-domain metal-dependent phosphohydrolase. That family-level clue favors a phosphatase choice over the oxidoreductase and lyase alternatives, and gives a credible basis to favor the specialized HD-domain phosphatase choice B over the broad acid-phosphatase choice A. This is a probabilistic family-based inference, not a way to establish the exact substrate from the sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of HD-domain phosphohydrolases meaningfully favors B among these choices. The motif does not independently prove the enzyme’s precise substrate specificity, but the alternatives do not require exact experimental reconstruction for a defensible choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HD-domain clue favors the phosphohydrolase option B; the other offered choices are less consistent with that family-level signal."
  },
  "important_caveats": [
    "The sequence alone does not establish the specialized substrate reaction or guarantee the complete EC number.",
    "The cited database annotation and experimental evidence are reviewer-only and were not supplied as original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O24769 (OXSA_PRIMG) is annotated with EC 3.1.3.112 (4'-phosphooxetanocin A phosphatase) based on experimental evidence (ECO:0000269) from two primary publications (PubMed:27849620 and PubMed:28346939). The catalytic activity (4'-phosphooxetanocin A + H2O → oxetanocin A + phosphate) was confirmed by X-ray crystallography (PDB 5TK6–5TKA) and biochemical assays. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue sequence contains a recognizable HD-domain motif (e.g., 'HADHVD' around residues 148–153, and 'HD' in 'LYALYHDVTEVVST' around residues 80–81). The HD superfamily is a well-characterized phosphohydrolase family (found in E. coli RppH, various HD-domain phosphodiesterases/phosphatases across bacteria and eukaryotes) that uses a His-Asp dyad for metal-assisted phosphoester hydrolysis. This immediately eliminates C (EC 1.3.1.36, dihydroorotate dehydrogenase — an FMN-dependent oxidoreductase of ~350 aa with a completely different fold) and D (EC 4.3.3.9, selenocysteine lyase — a PLP-dependent lyase of ~250 aa). Between the two remaining phosphatase options, EC 3.1.3.2 (acid phosphatase) belongs to the purple acid phosphatase / alkaline phosphatase structural superfamily with binuclear metal centers and no HD motif, whereas EC 3.1.3.112 is specifically an HD-domain phosphohydrolase. Thus the presence of the HD motif, a transferable family-level feature learned from many other HD-domain proteins, meaningfully distinguishes B from A, C, and D among the four offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the HD-domain phosphohydrolase superfamily can identify the HD motif in the sequence, recognize it as a phosphohydrolase (eliminating the oxidoreductase C and lyase D), and then use the well-established fact that acid phosphatases (EC 3.1.3.2) belong to a structurally distinct superfamily lacking HD motifs to eliminate A. This leaves B as the only consistent option. The specific substrate (4'-phosphooxetanocin A) need not be identified from sequence; the question only requires choosing among four EC numbers, and the family-level inference suffices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The HD-domain signature clearly points to a phosphohydrolase of the HD superfamily, which is structurally and mechanistically distinct from acid phosphatases (EC 3.1.3.2), oxidoreductases (EC 1.3.1.36), and lyases (EC 4.3.3.9). No other option is consistent with the observed HD motif.


### Important caveats

- The specific substrate (4'-phosphooxetanocin A) is unusual and cannot be deduced from sequence alone; however, the question only requires selecting among four EC numbers, and the HD-domain family inference is sufficient to eliminate the three distractors.
- EC 3.1.3.112 was formally established relatively recently (2016–2017 publications); a model trained on older data might not have this EC number in its knowledge, but the HD-domain reasoning still leads to B as the only phosphohydrolase option consistent with the motif.
- The HD motif in this sequence ('HADHVD') is a canonical HD-domain signature, but HD domains are found in a wide variety of phosphohydrolases with different EC numbers; the question's design (only one HD-domain option among four choices) makes the family-level inference sufficient.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue sequence contains a recognizable HD-domain motif (e.g., 'HADHVD' around residues 148–153, and 'HD' in 'LYALYHDVTEVVST' around residues 80–81). The HD superfamily is a well-characterized phosphohydrolase family (found in E. coli RppH, various HD-domain phosphodiesterases/phosphatases across bacteria and eukaryotes) that uses a His-Asp dyad for metal-assisted phosphoester hydrolysis. This immediately eliminates C (EC 1.3.1.36, dihydroorotate dehydrogenase — an FMN-dependent oxidoreductase of ~350 aa with a completely different fold) and D (EC 4.3.3.9, selenocysteine lyase — a PLP-dependent lyase of ~250 aa). Between the two remaining phosphatase options, EC 3.1.3.2 (acid phosphatase) belongs to the purple acid phosphatase / alkaline phosphatase structural superfamily with binuclear metal centers and no HD motif, whereas EC 3.1.3.112 is specifically an HD-domain phosphohydrolase. Thus the presence of the HD motif, a transferable family-level feature learned from many other HD-domain proteins, meaningfully distinguishes B from A, C, and D among the four offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the HD-domain phosphohydrolase superfamily can identify the HD motif in the sequence, recognize it as a phosphohydrolase (eliminating the oxidoreductase C and lyase D), and then use the well-established fact that acid phosphatases (EC 3.1.3.2) belong to a structurally distinct superfamily lacking HD motifs to eliminate A. This leaves B as the only consistent option. The specific substrate (4'-phosphooxetanocin A) need not be identified from sequence; the question only requires choosing among four EC numbers, and the family-level inference suffices."
  },
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O24769 (OXSA_PRIMG) is annotated with EC 3.1.3.112 (4'-phosphooxetanocin A phosphatase) based on experimental evidence (ECO:0000269) from two primary publications (PubMed:27849620 and PubMed:28346939). The catalytic activity (4'-phosphooxetanocin A + H2O → oxetanocin A + phosphate) was confirmed by X-ray crystallography (PDB 5TK6–5TKA) and biochemical assays. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match confirmed)."
  },
  "important_caveats": [
    "The specific substrate (4'-phosphooxetanocin A) is unusual and cannot be deduced from sequence alone; however, the question only requires selecting among four EC numbers, and the HD-domain family inference is sufficient to eliminate the three distractors.",
    "EC 3.1.3.112 was formally established relatively recently (2016–2017 publications); a model trained on older data might not have this EC number in its knowledge, but the HD-domain reasoning still leads to B as the only phosphohydrolase option consistent with the motif.",
    "The HD motif in this sequence ('HADHVD') is a canonical HD-domain signature, but HD domains are found in a wide variety of phosphohydrolases with different EC numbers; the question's design (only one HD-domain option among four choices) makes the family-level inference sufficient."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HD-domain signature clearly points to a phosphohydrolase of the HD superfamily, which is structurally and mechanistically distinct from acid phosphatases (EC 3.1.3.2), oxidoreductases (EC 1.3.1.36), and lyases (EC 4.3.3.9). No other option is consistent with the observed HD motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O24769 (OXSA_PRIMG) is annotated with EC 3.1.3.112 (4'-phosphooxetanocin A phosphatase) based on experimental evidence (ECO:0000269) from two primary publications (PubMed:27849620 and PubMed:28346939). The catalytic activity (4'-phosphooxetanocin A + H2O → oxetanocin A + phosphate) was confirmed by X-ray crystallography (PDB 5TK6–5TKA) and biochemical assays. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue sequence contains a recognizable HD-domain motif (e.g., 'HADHVD' around residues 148–153, and 'HD' in 'LYALYHDVTEVVST' around residues 80–81). The HD superfamily is a well-characterized phosphohydrolase family (found in E. coli RppH, various HD-domain phosphodiesterases/phosphatases across bacteria and eukaryotes) that uses a His-Asp dyad for metal-assisted phosphoester hydrolysis. This immediately eliminates C (EC 1.3.1.36, dihydroorotate dehydrogenase — an FMN-dependent oxidoreductase of ~350 aa with a completely different fold) and D (EC 4.3.3.9, selenocysteine lyase — a PLP-dependent lyase of ~250 aa). Between the two remaining phosphatase options, EC 3.1.3.2 (acid phosphatase) belongs to the purple acid phosphatase / alkaline phosphatase structural superfamily with binuclear metal centers and no HD motif, whereas EC 3.1.3.112 is specifically an HD-domain phosphohydrolase. Thus the presence of the HD motif, a transferable family-level feature learned from many other HD-domain proteins, meaningfully distinguishes B from A, C, and D among the four offered choices.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the HD-domain phosphohydrolase superfamily can identify the HD motif in the sequence, recognize it as a phosphohydrolase (eliminating the oxidoreductase C and lyase D), and then use the well-established fact that acid phosphatases (EC 3.1.3.2) belong to a structurally distinct superfamily lacking HD motifs to eliminate A. This leaves B as the only consistent option. The specific substrate (4'-phosphooxetanocin A) need not be identified from sequence; the question only requires choosing among four EC numbers, and the family-level inference suffices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HD-domain signature clearly points to a phosphohydrolase of the HD superfamily, which is structurally and mechanistically distinct from acid phosphatases (EC 3.1.3.2), oxidoreductases (EC 1.3.1.36), and lyases (EC 4.3.3.9). No other option is consistent with the observed HD motif."
  },
  "important_caveats": [
    "The specific substrate (4'-phosphooxetanocin A) is unusual and cannot be deduced from sequence alone; however, the question only requires selecting among four EC numbers, and the HD-domain family inference is sufficient to eliminate the three distractors.",
    "EC 3.1.3.112 was formally established relatively recently (2016–2017 publications); a model trained on older data might not have this EC number in its knowledge, but the HD-domain reasoning still leads to B as the only phosphohydrolase option consistent with the motif.",
    "The HD motif in this sequence ('HADHVD') is a canonical HD-domain signature, but HD domains are found in a wide variety of phosphohydrolases with different EC numbers; the question's design (only one HD-domain option among four choices) makes the family-level inference sufficient."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "cc417e15ac0354c49fef7a10ef2eaa3595a3619ba1429df8c3467cd7ce1b7a72",
  "current_entry_audit": {
    "entryVersion": 77,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-01-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "cc417e15ac0354c49fef7a10ef2eaa3595a3619ba1429df8c3467cd7ce1b7a72",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 75,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O24769",
  "selected_historical_entry_version": 75,
  "selected_historical_record_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "cc417e15ac0354c49fef7a10ef2eaa3595a3619ba1429df8c3467cd7ce1b7a72",
  "selected_historical_version": {
    "accession": "O24769",
    "database": "Swiss-Prot",
    "entryVersion": 75,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OXSA_PRIMG",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O24769\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":77,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-01-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacillus megaterium\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Priestia\"],\"scientificName\":\"Priestia megaterium\",\"taxonId\":1404}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"HD-domain phosphohydrolase OxsA\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27849620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.112\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4'-phosphooxetanocin A phosphatase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27849620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81368\"}}],\"reaction\":{\"ecNumber\":\"3.1.3.112\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27849620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"name\":\"4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81367\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:85720\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:86012\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bridwell-Rabb J.\",\"Zhong A.\",\"Sun H.G.\",\"Drennan C.L.\",\"Liu H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28346939\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature21689\"}],\"citationType\":\"journal article\",\"firstPage\":\"322\",\"id\":\"28346939\",\"journal\":\"Nature\",\"lastPage\":\"326\",\"publicationDate\":\"2017\",\"title\":\"A B12-dependent radical SAM enzyme involved in oxetanocin A biosynthesis.\",\"volume\":\"544\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Bridwell-Rabb J.\",\"Kang G.\",\"Zhong A.\",\"Liu H.W.\",\"Drennan C.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27849620\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1613610113\"}],\"citationType\":\"journal article\",\"firstPage\":\"13750\",\"id\":\"27849620\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"13755\",\"publicationDate\":\"2016\",\"title\":\"An HD domain phosphohydrolase active site tailored for oxetanocin-A biosynthesis.\",\"volume\":\"113\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK6\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK7\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK8\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK9\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TKA\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM; OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND OXETANOCIN A TRIPHOSPHATE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H1",
  "excerpt": "ID   OXSA_PRIMG              Reviewed;         194 AA.\nAC   O24769;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JAN-1998, sequence version 1.\nDT   18-JUN-2025, entry version 75.\nDE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};\nDE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\nDE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};\nGN   Name=oxsA {ECO:0000312|EMBL:BAA21630.1};\nOS   Priestia megaterium (Bacillus megaterium).\nOG   Plasmid pOXT1 {ECO:0000303|PubMed:10227144}.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Priestia.\nOX   NCBI_TaxID=1404;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};\nDE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\nDE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=NK84-0128; PLASMID=pOXT1;\nRX   PubMed=10227144; DOI=10.1271/bbb.63.563;\nRA   Morita M., Tomita K., Ishizawa M., Takagi K., Kawamura F., Takahashi H.,\nRA   Morino T.;\nRT   \"Cloning of oxetanocin A biosynthetic and resistance genes that reside on a\nRT   plasmid of Bacillus megaterium strain NK84-0128.\";\nRL   Biosci. Biotechnol. Biochem. 63:563-566(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=28346939; DOI=10.1038/nature21689;\nRA   Bridwell-Rabb J., Zhong A., Sun H.G., Drennan C.L., Liu H.W.;\nRT   \"A B12-dependent radical SAM enzyme involved in oxetanocin A\nRT   biosynthesis.\";\nRL   Nature 544:322-326(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H5",
  "excerpt": "RN   [3] {ECO:0007744|PDB:5TK6, ECO:0007744|PDB:5TK7, ECO:0007744|PDB:5TK8, ECO:0007744|PDB:5TK9, ECO:0007744|PDB:5TKA}\nRP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM;\nRP   OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND\nRP   OXETANOCIN A TRIPHOSPHATE, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.\nRX   PubMed=27849620; DOI=10.1073/pnas.1613610113;\nRA   Bridwell-Rabb J., Kang G., Zhong A., Liu H.W., Drennan C.L.;\nRT   \"An HD domain phosphohydrolase active site tailored for oxetanocin-A\nRT   biosynthesis.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 113:13750-13755(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate;\nCC         Xref=Rhea:RHEA:81367, ChEBI:CHEBI:15377, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:85720, ChEBI:CHEBI:86012; EC=3.1.3.112;\nCC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81368;\nCC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
