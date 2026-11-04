# EC_number_0173

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0173.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 6.3.2.35

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKIAIIFGGNSPEYTVSLASATSAIEALQSSPYDYDLSLIGIAPDAMDWYLYTGELENIRQDTWLLDTKHKQKIQPLFEGNGFWLSEEQQTLVPDVLFPIMHGKYGEDGSIQGLFELMKLPYVGCGVAGSALCMNKWLLHQAAAAIGVQSAPTILLTNQANQQEQIEAFIQTHGFPVFFKPNEAGSSKGITKVTCVEEIASALKEAFTYCSAVLLQKNIAGVEIGCGILGNDSLTVGACDAISLVDGFFDFEEKYQLISAKITVPAPLPETIETKVKEQAQLLYRSLGLKGLARIDFFVTERGELYLNEINTMPGFTSHSRYPAMMAAVGLSYQELLQKLLVLAKEEVK

[Multiple Choices]
A. 6.3.5.1
B. 1.1.1.1
C. 6.3.2.35
D. 3.2.1.31
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

> The sequence matches the referenced protein, whose annotation assigns EC 6.3.2.35 and gives the D-serine + D-alanine ligase reaction with experimental evidence codes. The cited study describes characterization of VanC2 as a D-Ala-D-Ser ligase.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 350-residue bacterial sequence is consistent with the D-Ala-D-X ligase family, ATP-dependent enzymes that join amino acids. That family-level inference distinguishes the offered ligase choice, C, from the unrelated oxidoreductase, glycosidase, and carbamoyl-phosphate synthetase choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of the ligase family meaningfully selects C among these alternatives. The exact D-serine substrate preference may be harder to infer from sequence alone, but the other offered choices do not require distinguishing that finer specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C is a plausible choice among the listed EC numbers for a bacterial D-Ala-D-X ligase.


### Important caveats

- The sequence supports a family-level inference; it does not by itself establish the precise substrate preference with experimental certainty.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 350-residue bacterial sequence is consistent with the D-Ala-D-X ligase family, ATP-dependent enzymes that join amino acids. That family-level inference distinguishes the offered ligase choice, C, from the unrelated oxidoreductase, glycosidase, and carbamoyl-phosphate synthetase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the ligase family meaningfully selects C among these alternatives. The exact D-serine substrate preference may be harder to infer from sequence alone, but the other offered choices do not require distinguishing that finer specificity."
  },
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the referenced protein, whose annotation assigns EC 6.3.2.35 and gives the D-serine + D-alanine ligase reaction with experimental evidence codes. The cited study describes characterization of VanC2 as a D-Ala-D-Ser ligase."
  },
  "important_caveats": [
    "The sequence supports a family-level inference; it does not by itself establish the precise substrate preference with experimental certainty."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C is a plausible choice among the listed EC numbers for a bacterial D-Ala-D-X ligase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the referenced protein, whose annotation assigns EC 6.3.2.35 and gives the D-serine + D-alanine ligase reaction with experimental evidence codes. The cited study describes characterization of VanC2 as a D-Ala-D-Ser ligase.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 350-residue bacterial sequence is consistent with the D-Ala-D-X ligase family, ATP-dependent enzymes that join amino acids. That family-level inference distinguishes the offered ligase choice, C, from the unrelated oxidoreductase, glycosidase, and carbamoyl-phosphate synthetase choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the ligase family meaningfully selects C among these alternatives. The exact D-serine substrate preference may be harder to infer from sequence alone, but the other offered choices do not require distinguishing that finer specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C is a plausible choice among the listed EC numbers for a bacterial D-Ala-D-X ligase."
  },
  "important_caveats": [
    "The sequence supports a family-level inference; it does not by itself establish the precise substrate preference with experimental certainty."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q47720 (VanC2 from Enterococcus casseliflavus) is annotated with EC 6.3.2.35 (D-alanine--D-serine ligase) supported by experimental evidence (ECO:0000269) from two primary publications (PubMed 9294159 and 9545431). The catalytic activity is D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate + H(+). The sequence matches exactly (350 AA, identical SHA256). The annotation is based on purification and biochemical characterization, not mere computational transfer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~350 aa) contains hallmark motifs of the D-alanine:D-alanine ligase (Ddl)/Van family of vancomycin-resistance ligases, notably the conserved 'GCGILGND' region and the overall architecture shared with Ddl homologs across many bacteria. This family is one of the most extensively characterized enzyme families in antibiotic resistance literature. Recognition of the Ddl/Van family immediately places the enzyme in EC class 6 (ligase) and subclass 6.3.2 (forming carbon-nitrogen bonds, specifically peptide bonds). Glutamine synthetase (6.3.5.1) is a completely different fold and sequence family (~370 aa, distinct catalytic mechanism involving a gamma-glutamyl intermediate), easily excluded by sequence comparison. Alcohol dehydrogenase (1.1.1.1) requires a Rossmann NAD-binding fold absent here, and beta-glucuronidase (3.2.1.31) is a glycosidase with a TIM-barrel fold, also absent. Since the only 6.3.2.x option provided is 6.3.2.35 (D-Ala-D-Ser ligase, the VanC/VanB-type activity), family-level recognition of the Ddl/Van clade suffices to select C over the other three choices. The Van-type ligases are well-documented across dozens of bacterial species (Enterococcus, Staphylococcus, Lactobacillus, etc.) as D-Ala-D-Ser or D-Ala-D-Lac ligases, making this a transferable family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the Ddl/Van protein family can recognize the sequence motifs, assign the enzyme to EC 6.3.2.x (peptide-bond-forming ligase), and eliminate the glutamine synthetase, oxidoreductase, and hydrolase options. The Van/Ddl family is extensively characterized across many homologs, making this a legitimate family-level transfer rather than a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (1, 3, 6) and two different EC subclasses within class 6 (6.3.2 vs 6.3.5). Family-level recognition of the Ddl/Van clade cleanly separates option C from all others. No ambiguity among the offered choices.


### Important caveats

- The reviewer evidence confirms the annotation is experimentally supported (two primary publications with ECO:0000269), not merely computational.
- The model does not need to distinguish VanC from VanA/VanB at the sub-EC level because no other 6.3.2.x option is offered; recognizing the Ddl/Van family and eliminating the non-ligase and glutamine-synthetase options is sufficient.
- The sequence is from Enterococcus casseliflavus (VanC2), but the family-level argument relies on motifs shared across many Ddl/Van homologs, not on organism-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~350 aa) contains hallmark motifs of the D-alanine:D-alanine ligase (Ddl)/Van family of vancomycin-resistance ligases, notably the conserved 'GCGILGND' region and the overall architecture shared with Ddl homologs across many bacteria. This family is one of the most extensively characterized enzyme families in antibiotic resistance literature. Recognition of the Ddl/Van family immediately places the enzyme in EC class 6 (ligase) and subclass 6.3.2 (forming carbon-nitrogen bonds, specifically peptide bonds). Glutamine synthetase (6.3.5.1) is a completely different fold and sequence family (~370 aa, distinct catalytic mechanism involving a gamma-glutamyl intermediate), easily excluded by sequence comparison. Alcohol dehydrogenase (1.1.1.1) requires a Rossmann NAD-binding fold absent here, and beta-glucuronidase (3.2.1.31) is a glycosidase with a TIM-barrel fold, also absent. Since the only 6.3.2.x option provided is 6.3.2.35 (D-Ala-D-Ser ligase, the VanC/VanB-type activity), family-level recognition of the Ddl/Van clade suffices to select C over the other three choices. The Van-type ligases are well-documented across dozens of bacterial species (Enterococcus, Staphylococcus, Lactobacillus, etc.) as D-Ala-D-Ser or D-Ala-D-Lac ligases, making this a transferable family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the Ddl/Van protein family can recognize the sequence motifs, assign the enzyme to EC 6.3.2.x (peptide-bond-forming ligase), and eliminate the glutamine synthetase, oxidoreductase, and hydrolase options. The Van/Ddl family is extensively characterized across many homologs, making this a legitimate family-level transfer rather than a lookup of this specific protein's record."
  },
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q47720 (VanC2 from Enterococcus casseliflavus) is annotated with EC 6.3.2.35 (D-alanine--D-serine ligase) supported by experimental evidence (ECO:0000269) from two primary publications (PubMed 9294159 and 9545431). The catalytic activity is D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate + H(+). The sequence matches exactly (350 AA, identical SHA256). The annotation is based on purification and biochemical characterization, not mere computational transfer."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (two primary publications with ECO:0000269), not merely computational.",
    "The model does not need to distinguish VanC from VanA/VanB at the sub-EC level because no other 6.3.2.x option is offered; recognizing the Ddl/Van family and eliminating the non-ligase and glutamine-synthetase options is sufficient.",
    "The sequence is from Enterococcus casseliflavus (VanC2), but the family-level argument relies on motifs shared across many Ddl/Van homologs, not on organism-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (1, 3, 6) and two different EC subclasses within class 6 (6.3.2 vs 6.3.5). Family-level recognition of the Ddl/Van clade cleanly separates option C from all others. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q47720 (VanC2 from Enterococcus casseliflavus) is annotated with EC 6.3.2.35 (D-alanine--D-serine ligase) supported by experimental evidence (ECO:0000269) from two primary publications (PubMed 9294159 and 9545431). The catalytic activity is D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate + H(+). The sequence matches exactly (350 AA, identical SHA256). The annotation is based on purification and biochemical characterization, not mere computational transfer.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~350 aa) contains hallmark motifs of the D-alanine:D-alanine ligase (Ddl)/Van family of vancomycin-resistance ligases, notably the conserved 'GCGILGND' region and the overall architecture shared with Ddl homologs across many bacteria. This family is one of the most extensively characterized enzyme families in antibiotic resistance literature. Recognition of the Ddl/Van family immediately places the enzyme in EC class 6 (ligase) and subclass 6.3.2 (forming carbon-nitrogen bonds, specifically peptide bonds). Glutamine synthetase (6.3.5.1) is a completely different fold and sequence family (~370 aa, distinct catalytic mechanism involving a gamma-glutamyl intermediate), easily excluded by sequence comparison. Alcohol dehydrogenase (1.1.1.1) requires a Rossmann NAD-binding fold absent here, and beta-glucuronidase (3.2.1.31) is a glycosidase with a TIM-barrel fold, also absent. Since the only 6.3.2.x option provided is 6.3.2.35 (D-Ala-D-Ser ligase, the VanC/VanB-type activity), family-level recognition of the Ddl/Van clade suffices to select C over the other three choices. The Van-type ligases are well-documented across dozens of bacterial species (Enterococcus, Staphylococcus, Lactobacillus, etc.) as D-Ala-D-Ser or D-Ala-D-Lac ligases, making this a transferable family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the Ddl/Van protein family can recognize the sequence motifs, assign the enzyme to EC 6.3.2.x (peptide-bond-forming ligase), and eliminate the glutamine synthetase, oxidoreductase, and hydrolase options. The Van/Ddl family is extensively characterized across many homologs, making this a legitimate family-level transfer rather than a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (1, 3, 6) and two different EC subclasses within class 6 (6.3.2 vs 6.3.5). Family-level recognition of the Ddl/Van clade cleanly separates option C from all others. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (two primary publications with ECO:0000269), not merely computational.",
    "The model does not need to distinguish VanC from VanA/VanB at the sub-EC level because no other 6.3.2.x option is offered; recognizing the Ddl/Van family and eliminating the non-ligase and glutamine-synthetase options is sufficient.",
    "The sequence is from Enterococcus casseliflavus (VanC2), but the family-level argument relies on motifs shared across many Ddl/Van homologs, not on organism-specific knowledge."
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
  "benchmark_sequence_length": 350,
  "benchmark_sequence_sha256": "b4602f311134ca7446d9c233196a8829e27e15dc29e27680e1d34564cbfdd19c",
  "current_entry_audit": {
    "entryVersion": 149,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1996-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 350,
  "current_source_sequence_sha256": "b4602f311134ca7446d9c233196a8829e27e15dc29e27680e1d34564cbfdd19c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 147,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q47720",
  "selected_historical_entry_version": 147,
  "selected_historical_record_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "selected_historical_source_sequence_length": 350,
  "selected_historical_source_sequence_sha256": "b4602f311134ca7446d9c233196a8829e27e15dc29e27680e1d34564cbfdd19c",
  "selected_historical_version": {
    "accession": "Q47720",
    "database": "Swiss-Prot",
    "entryVersion": 147,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VANC2_ENTCA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q47720\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":149,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1996-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Enterococcus flavescens\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAA60990.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Lactobacillales\",\"Enterococcaceae\",\"Enterococcus\"],\"scientificName\":\"Enterococcus casseliflavus\",\"taxonId\":37734}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00047\",\"source\":\"HAMAP-Rule\"}],\"value\":\"D-alanine--D-serine ligase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"VanC2 ligase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9294159\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9545431\",\"source\":\"PubMed\"}],\"value\":\"6.3.2.35\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9294159\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Vancomycin C-type resistance protein VanC2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"6.3.2.35\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9294159\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9545431\",\"source\":\"PubMed\"}],\"name\":\"D-serine + D-alanine + ATP = D-alanyl-D-serine + ADP + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27706\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35247\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57416\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60390\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Park I.S.\",\"Lin C.H.\",\"Walsh C.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9294159\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.94.19.10040\"}],\"citationType\":\"journal article\",\"firstPage\":\"10040\",\"id\":\"9294159\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"10044\",\"publicationDate\":\"1997\",\"title\":\"Bacterial resistance to vancomycin: overproduction, purification, and characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser ligase.\",\"volume\":\"94\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9294159\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 25788\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Healy V.L.\",\"Park I.S.\",\"Walsh C.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9545431\"},{\"database\":\"DOI\",\"id\":\"10.1016/s1074-5521(98)90633-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"197\",\"id\":\"9545431\",\"journal\":\"Chem. Biol.\",\"lastPage\":\"207\",\"publicationDate\":\"1998\",\"title\":\"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic of one vancomycin-resistant bacterial phenotype, revert towards wild-type D-alanyl-D-alanine ligases.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF PHE-250 AND ARG-322\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H1",
  "excerpt": "ID   VANC2_ENTCA             Reviewed;         350 AA.\nAC   Q47720;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1996, sequence version 1.\nDT   28-JAN-2026, entry version 147.\nDE   RecName: Full=Vancomycin C-type resistance protein VanC2 {ECO:0000303|PubMed:9294159, ECO:0000305};\nDE            EC=6.3.2.35 {ECO:0000269|PubMed:9294159, ECO:0000269|PubMed:9545431};\nDE   AltName: Full=D-alanine--D-serine ligase {ECO:0000255|HAMAP-Rule:MF_00047};\nDE   AltName: Full=VanC2 ligase {ECO:0000305};\nGN   Name=vanC2 {ECO:0000303|PubMed:9294159, ECO:0000303|PubMed:9545431,\nGN   ECO:0000312|EMBL:ABX79432.1};\nGN   Synonyms=ddl {ECO:0000255|HAMAP-Rule:MF_00047},\nGN   vanC-2 {ECO:0000312|EMBL:AAA60990.1};\nGN   ORFNames=P7I34_04740 {ECO:0000312|EMBL:MDT2981959.1};\nOS   Enterococcus casseliflavus (Enterococcus flavescens).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae;\nOC   Enterococcus.\nOX   NCBI_TaxID=37734 {ECO:0000312|EMBL:AAA60990.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Vancomycin C-type resistance protein VanC2 {ECO:0000303|PubMed:9294159, ECO:0000305};\nDE            EC=6.3.2.35 {ECO:0000269|PubMed:9294159, ECO:0000269|PubMed:9545431};\nDE   AltName: Full=D-alanine--D-serine ligase {ECO:0000255|HAMAP-Rule:MF_00047};\nDE   AltName: Full=VanC2 ligase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY\nRP   REGULATION, AND SUBUNIT.\nRC   STRAIN=ATCC 25788 {ECO:0000303|PubMed:9294159};\nRX   PubMed=9294159; DOI=10.1073/pnas.94.19.10040;\nRA   Park I.S., Lin C.H., Walsh C.T.;\nRT   \"Bacterial resistance to vancomycin: overproduction, purification, and\nRT   characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser\nRT   ligase.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 94:10040-10044(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF PHE-250 AND ARG-322.\nRX   PubMed=9545431; DOI=10.1016/s1074-5521(98)90633-0;\nRA   Healy V.L., Park I.S., Walsh C.T.;\nRT   \"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic\nRT   of one vancomycin-resistant bacterial phenotype, revert towards wild-type\nRT   D-alanyl-D-alanine ligases.\";\nRL   Chem. Biol. 5:197-207(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-serine + D-alanine + ATP = D-alanyl-D-serine + ADP +\nCC         phosphate + H(+); Xref=Rhea:RHEA:27706, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:35247, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:57416, ChEBI:CHEBI:60390, ChEBI:CHEBI:456216;\nCC         EC=6.3.2.35; Evidence={ECO:0000269|PubMed:9294159,\nCC         ECO:0000269|PubMed:9545431};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
