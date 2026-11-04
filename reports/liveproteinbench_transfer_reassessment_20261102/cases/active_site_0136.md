# active_site_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0136.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 31 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKTDFSHDLLRFSDEVKEALHSGKPVVALESTVIAHGLPYPENVATARKIEAAVRAEGAIPATIGIENGRFLIGMSDADLERFGSTRGIPKASSRDIPVILAQGGMGATTVASSLVAADLAGIPFFASAGIGGVHRGAERSMDISADLIQFTRSRVAVVCAGAKSILDLGLTLEYLETQCVPIISYQSDDFPAFYCRSSGFHSPHRLDDATVIARSIDMHWKLGNQSSVLITHPIHEEDAIGTDEVESIIREAAVQAEHEGIRGPGATPYLMRAVAKATEGKTVKANMSVLISTAALAGKLACAHIDYLRQQNQA

[Multiple Choices]
A. Position 1336 (For beta-ketoacyl synthase 1 activity)
B. Position 141 (Proton acceptor)
C. Position 385 (Glycyl thioester intermediate)
D. Position 31 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies position 31 as the proton donor. This is a HAMAP-rule computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as fitting a bacterial pseudouridine-5'-phosphate glycosidase family profile and use transferable family-level knowledge that a conserved N-terminal acidic residue acts as the proton donor. Position 31 is glutamate in this sequence. The 316-residue sequence also rules out positions 385 and 1336; the family-level role favors position 31 over position 141.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices provide a credible, probabilistic family-based route to the keyed choice; this need not rely on recalling this exact protein's database record. The precise catalytic assignment is not established by generic acid-base chemistry alone, but conserved family patterns meaningfully distinguish the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 31 is supported as the proton donor among the viable coordinates; the other listed positions are either beyond the sequence length or have a different proposed role.


### Important caveats

- The reviewer-only annotation supports the key but is based on a computational HAMAP rule; the excerpts do not establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as fitting a bacterial pseudouridine-5'-phosphate glycosidase family profile and use transferable family-level knowledge that a conserved N-terminal acidic residue acts as the proton donor. Position 31 is glutamate in this sequence. The 316-residue sequence also rules out positions 385 and 1336; the family-level role favors position 31 over position 141.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a credible, probabilistic family-based route to the keyed choice; this need not rely on recalling this exact protein's database record. The precise catalytic assignment is not established by generic acid-base chemistry alone, but conserved family patterns meaningfully distinguish the options."
  },
  "case_id": "active_site_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 31 as the proton donor. This is a HAMAP-rule computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but is based on a computational HAMAP rule; the excerpts do not establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 31 is supported as the proton donor among the viable coordinates; the other listed positions are either beyond the sequence length or have a different proposed role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 31 as the proton donor. This is a HAMAP-rule computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as fitting a bacterial pseudouridine-5'-phosphate glycosidase family profile and use transferable family-level knowledge that a conserved N-terminal acidic residue acts as the proton donor. Position 31 is glutamate in this sequence. The 316-residue sequence also rules out positions 385 and 1336; the family-level role favors position 31 over position 141.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a credible, probabilistic family-based route to the keyed choice; this need not rely on recalling this exact protein's database record. The precise catalytic assignment is not established by generic acid-base chemistry alone, but conserved family patterns meaningfully distinguish the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 31 is supported as the proton donor among the viable coordinates; the other listed positions are either beyond the sequence length or have a different proposed role."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but is based on a computational HAMAP rule; the excerpts do not establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9L393 annotates position 31 as 'Proton donor' (Active site, evidence C5/H3), consistent with the expected answer D. The annotation is from HAMAP-Rule MF_01876 (ECO:0000255), a curated computational annotation rather than direct experimental evidence, but it is the standard database record. The residue at position 31 in the provided sequence is E (Glutamic acid), whose carboxyl side chain is a well-known proton donor, consistent with the annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The provided sequence is 316 residues long. Options A (position 1336) and C (position 385) are immediately eliminated because they exceed the sequence length. Between B and D, the model can read the residue at each position from the provided sequence: position 31 is E (Glutamic acid) and position 141 is R (Arginine). General amino-acid chemistry tells us that Glutamic acid, with its carboxyl side chain (pKa ~4.3), is a classic proton donor in enzyme active sites, while Arginine's guanidinium group is permanently positively charged at physiological pH and is not a proton acceptor. Thus the functional labels paired with the positions allow a chemistry-based discrimination: 'Proton donor' at a Glu is chemically coherent, whereas 'Proton acceptor' at an Arg is not. This reasoning uses only the provided sequence, sequence-length arithmetic, and transferable amino-acid chemistry knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The model can eliminate A and C by noting positions exceed the 316-residue sequence, then distinguish B from D by checking the identity of the residue at each position against the stated chemical role using general amino-acid chemistry. No fact specific to this exact protein beyond the provided sequence is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are eliminated by sequence length. Between B and D, the amino acid at position 141 (Arg) is chemically incompatible with 'proton acceptor,' while the amino acid at position 31 (Glu) is a textbook proton donor. No other option is defensible.


### Important caveats

- The UniProt annotation for position 31 is from HAMAP-Rule MF_01876 (ECO:0000255), a computational/curated family-rule annotation, not direct experimental characterization of this specific protein.
- The protein is annotated as Pseudouridine-5'-phosphate glycosidase (EC 4.2.1.70), a glycosylase; the proton-donor role at position 31 is inferred from family rules rather than site-directed mutagenesis on this exact enzyme.
- The question's distractors (positions 1336 and 385) are trivially eliminable by sequence length, making the effective choice a binary B-vs-D discrimination based on amino-acid chemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The provided sequence is 316 residues long. Options A (position 1336) and C (position 385) are immediately eliminated because they exceed the sequence length. Between B and D, the model can read the residue at each position from the provided sequence: position 31 is E (Glutamic acid) and position 141 is R (Arginine). General amino-acid chemistry tells us that Glutamic acid, with its carboxyl side chain (pKa ~4.3), is a classic proton donor in enzyme active sites, while Arginine's guanidinium group is permanently positively charged at physiological pH and is not a proton acceptor. Thus the functional labels paired with the positions allow a chemistry-based discrimination: 'Proton donor' at a Glu is chemically coherent, whereas 'Proton acceptor' at an Arg is not. This reasoning uses only the provided sequence, sequence-length arithmetic, and transferable amino-acid chemistry knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The model can eliminate A and C by noting positions exceed the 316-residue sequence, then distinguish B from D by checking the identity of the residue at each position against the stated chemical role using general amino-acid chemistry. No fact specific to this exact protein beyond the provided sequence is needed."
  },
  "case_id": "active_site_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9L393 annotates position 31 as 'Proton donor' (Active site, evidence C5/H3), consistent with the expected answer D. The annotation is from HAMAP-Rule MF_01876 (ECO:0000255), a curated computational annotation rather than direct experimental evidence, but it is the standard database record. The residue at position 31 in the provided sequence is E (Glutamic acid), whose carboxyl side chain is a well-known proton donor, consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt annotation for position 31 is from HAMAP-Rule MF_01876 (ECO:0000255), a computational/curated family-rule annotation, not direct experimental characterization of this specific protein.",
    "The protein is annotated as Pseudouridine-5'-phosphate glycosidase (EC 4.2.1.70), a glycosylase; the proton-donor role at position 31 is inferred from family rules rather than site-directed mutagenesis on this exact enzyme.",
    "The question's distractors (positions 1336 and 385) are trivially eliminable by sequence length, making the effective choice a binary B-vs-D discrimination based on amino-acid chemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are eliminated by sequence length. Between B and D, the amino acid at position 141 (Arg) is chemically incompatible with 'proton acceptor,' while the amino acid at position 31 (Glu) is a textbook proton donor. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9L393 annotates position 31 as 'Proton donor' (Active site, evidence C5/H3), consistent with the expected answer D. The annotation is from HAMAP-Rule MF_01876 (ECO:0000255), a curated computational annotation rather than direct experimental evidence, but it is the standard database record. The residue at position 31 in the provided sequence is E (Glutamic acid), whose carboxyl side chain is a well-known proton donor, consistent with the annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The provided sequence is 316 residues long. Options A (position 1336) and C (position 385) are immediately eliminated because they exceed the sequence length. Between B and D, the model can read the residue at each position from the provided sequence: position 31 is E (Glutamic acid) and position 141 is R (Arginine). General amino-acid chemistry tells us that Glutamic acid, with its carboxyl side chain (pKa ~4.3), is a classic proton donor in enzyme active sites, while Arginine's guanidinium group is permanently positively charged at physiological pH and is not a proton acceptor. Thus the functional labels paired with the positions allow a chemistry-based discrimination: 'Proton donor' at a Glu is chemically coherent, whereas 'Proton acceptor' at an Arg is not. This reasoning uses only the provided sequence, sequence-length arithmetic, and transferable amino-acid chemistry knowledge.",
    "missing_item_specific_fact": "",
    "reason": "The model can eliminate A and C by noting positions exceed the 316-residue sequence, then distinguish B from D by checking the identity of the residue at each position against the stated chemical role using general amino-acid chemistry. No fact specific to this exact protein beyond the provided sequence is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are eliminated by sequence length. Between B and D, the amino acid at position 141 (Arg) is chemically incompatible with 'proton acceptor,' while the amino acid at position 31 (Glu) is a textbook proton donor. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation for position 31 is from HAMAP-Rule MF_01876 (ECO:0000255), a computational/curated family-rule annotation, not direct experimental characterization of this specific protein.",
    "The protein is annotated as Pseudouridine-5'-phosphate glycosidase (EC 4.2.1.70), a glycosylase; the proton-donor role at position 31 is inferred from family rules rather than site-directed mutagenesis on this exact enzyme.",
    "The question's distractors (positions 1336 and 385) are trivially eliminable by sequence length, making the effective choice a binary B-vs-D discrimination based on amino-acid chemistry."
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
  "benchmark_sequence_length": 316,
  "benchmark_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 316,
  "current_source_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9L393",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "selected_historical_source_sequence_length": 316,
  "selected_historical_source_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "selected_historical_version": {
    "accession": "Q9L393",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PSUG_DICD3",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9L393\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Erwinia chrysanthemi (strain 3937)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Pectobacteriaceae\",\"Dickeya\"],\"scientificName\":\"Dickeya dadantii (strain 3937)\",\"taxonId\":198628}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"4.2.1.70\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pseudouridine-5'-phosphate glycosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"PsiMP glycosidase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":31},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":165},\"start\":{\"modifier\":\"EXACT\",\"value\":165}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"ligand\":{\"name\":\"substrate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":92}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"ligand\":{\"name\":\"substrate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":112},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":144},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"ligand\":{\"name\":\"substrate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":148},\"start\":{\"modifier\":\"EXACT\",\"value\":146}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   PSUG_DICD3              Reviewed;         316 AA.\nAC   Q9L393; E0SMH8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};\nGN   Name=indA {ECO:0000303|PubMed:11790734};\nGN   Synonyms=psuG {ECO:0000255|HAMAP-Rule:MF_01876};\nGN   OrderedLocusNames=Dda3937_00974 {ECO:0000312|EMBL:ADN00617.1};\nOS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Pectobacteriaceae; Dickeya.\nOX   NCBI_TaxID=198628;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB87988.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, INDUCTION, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=3937;\nRX   PubMed=11790734; DOI=10.1128/jb.184.3.654-665.2002;\nRA   Reverchon S., Rouanet C., Expert D., Nasser W.;\nRT   \"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi\nRT   and role of this blue pigment in pathogenicity.\";\nRL   J. Bacteriol. 184:654-665(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        31\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_01876\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        165\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_01876\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         92\nFT                   /ligand=\"substrate\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_01876\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         112\nFT                   /ligand=\"substrate\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_01876\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         144\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_01876\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         146..148\nFT                   /ligand=\"substrate\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_01876\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
