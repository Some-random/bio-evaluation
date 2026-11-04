# active_site_0073

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0073.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 93 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSEPVRAEGETMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSTSASLHFIDRAAMPKDVILYTDDNEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTFMWNNPFTERHLISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGNGDI

[Multiple Choices]
A. Position 959 (Proton acceptor; for dehydratase activity)
B. Position 170 (Proton donor)
C. Position 93 (Proton donor)
D. Position 4848 (Proton donor; for dehydratase activity 2)
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

> The sequence-matched UniProt record annotates position 93 as a proton donor. That annotation is transferred by similarity from Q9SWE5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the phosphopantothenoylcysteine decarboxylase family, for which conserved catalytic residues can be inferred by homology. Among the plausible-length choices, residue 93 is His, a credible proton donor and a conserved catalytic feature in this family; residue 170 is Pro, which lacks a side-chain proton-donating group and has no backbone amide proton. Choices at 959 and 4848 are outside the 211-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level catalytic knowledge, together with the residues actually present at the offered positions, meaningfully favors C without needing the target's database record. This is a credible inference, though not an independent experimental demonstration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the offered options identifies a plausible proton-donating residue at a valid position. The record also annotates another proton donor at position 178, but that position is not an offered option.


### Important caveats

- The supporting annotation is similarity-based rather than direct experimental evidence for this sequence.
- The options ask for a single residue even though the source record annotates more than one proton donor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the phosphopantothenoylcysteine decarboxylase family, for which conserved catalytic residues can be inferred by homology. Among the plausible-length choices, residue 93 is His, a credible proton donor and a conserved catalytic feature in this family; residue 170 is Pro, which lacks a side-chain proton-donating group and has no backbone amide proton. Choices at 959 and 4848 are outside the 211-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic knowledge, together with the residues actually present at the offered positions, meaningfully favors C without needing the target's database record. This is a credible inference, though not an independent experimental demonstration."
  },
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 93 as a proton donor. That annotation is transferred by similarity from Q9SWE5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based rather than direct experimental evidence for this sequence.",
    "The options ask for a single residue even though the source record annotates more than one proton donor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered options identifies a plausible proton-donating residue at a valid position. The record also annotates another proton donor at position 178, but that position is not an offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 93 as a proton donor. That annotation is transferred by similarity from Q9SWE5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the phosphopantothenoylcysteine decarboxylase family, for which conserved catalytic residues can be inferred by homology. Among the plausible-length choices, residue 93 is His, a credible proton donor and a conserved catalytic feature in this family; residue 170 is Pro, which lacks a side-chain proton-donating group and has no backbone amide proton. Choices at 959 and 4848 are outside the 211-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic knowledge, together with the residues actually present at the offered positions, meaningfully favors C without needing the target's database record. This is a credible inference, though not an independent experimental demonstration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered options identifies a plausible proton-donating residue at a valid position. The record also annotates another proton donor at position 178, but that position is not an offered option."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based rather than direct experimental evidence for this sequence.",
    "The options ask for a single residue even though the source record annotates more than one proton donor."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6SZ50 annotates position 93 as an Active Site with description 'Proton donor' (evidence code ECO:0000250, transferred from Q9SWE5). Position 93 in the 211-residue sequence corresponds to Histidine (H), consistent with a proton donor role in an FMN-dependent decarboxylase. The annotation is a similarity-transfer annotation rather than direct experimental evidence, but it is a valid database annotation supporting the expected answer.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence is 211 amino acids long. Options A (position 959) and D (position 4848) refer to positions that do not exist in this sequence and can be eliminated immediately by counting residues. This leaves B (position 170) and C (position 93). Position 170 is Proline (P), which lacks any ionizable side chain and is structurally rigid—proline is essentially never a catalytic proton donor. Position 93 is Histidine (H), whose imidazole side chain (pKa ~6-7) is the canonical proton donor/acceptor in enzyme catalysis. Furthermore, the sequence contains FMN-binding Rossmann-fold motifs (e.g., GxGxxG patterns around residues 31-33, 56-58), identifying this as an FMN-dependent decarboxylase. In the PPCDC (phosphopantothenoylcysteine decarboxylase) family, a conserved histidine serves as the proton donor in the decarboxylation mechanism. Thus, family-level knowledge of FMN-dependent decarboxylases combined with basic amino-acid chemistry (His vs. Pro as catalytic residues) meaningfully distinguishes C from B without needing the specific UniProt annotation for this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through: (1) sequence-length elimination of A and D, (2) chemical reasoning that proline cannot be a proton donor while histidine commonly is, and (3) family-level knowledge of FMN-dependent decarboxylase mechanisms where a conserved His acts as proton donor. No fact specific to this exact protein beyond what is inferable from the sequence and general biochemistry is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are eliminated by sequence length (211 residues). Option B (position 170 = Proline) is chemically implausible as a proton donor. Option C (position 93 = Histidine) is the only chemically sensible proton donor among the viable choices. No ambiguity remains.


### Important caveats

- The UniProt annotation for position 93 is based on similarity transfer (ECO:0000250 from Q9SWE5), not direct experimental mutagenesis or structural determination for this specific soybean protein.
- The UniProt entry also annotates position 178 (Cysteine) as a second proton donor active site, but this position is not offered as a choice, so it does not create ambiguity among the provided options.
- The question format lists only a single residue per option, whereas active sites typically involve multiple residues; however, the task asks for the key catalytic residue and the options are structured accordingly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence is 211 amino acids long. Options A (position 959) and D (position 4848) refer to positions that do not exist in this sequence and can be eliminated immediately by counting residues. This leaves B (position 170) and C (position 93). Position 170 is Proline (P), which lacks any ionizable side chain and is structurally rigid—proline is essentially never a catalytic proton donor. Position 93 is Histidine (H), whose imidazole side chain (pKa ~6-7) is the canonical proton donor/acceptor in enzyme catalysis. Furthermore, the sequence contains FMN-binding Rossmann-fold motifs (e.g., GxGxxG patterns around residues 31-33, 56-58), identifying this as an FMN-dependent decarboxylase. In the PPCDC (phosphopantothenoylcysteine decarboxylase) family, a conserved histidine serves as the proton donor in the decarboxylation mechanism. Thus, family-level knowledge of FMN-dependent decarboxylases combined with basic amino-acid chemistry (His vs. Pro as catalytic residues) meaningfully distinguishes C from B without needing the specific UniProt annotation for this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through: (1) sequence-length elimination of A and D, (2) chemical reasoning that proline cannot be a proton donor while histidine commonly is, and (3) family-level knowledge of FMN-dependent decarboxylase mechanisms where a conserved His acts as proton donor. No fact specific to this exact protein beyond what is inferable from the sequence and general biochemistry is required."
  },
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 annotates position 93 as an Active Site with description 'Proton donor' (evidence code ECO:0000250, transferred from Q9SWE5). Position 93 in the 211-residue sequence corresponds to Histidine (H), consistent with a proton donor role in an FMN-dependent decarboxylase. The annotation is a similarity-transfer annotation rather than direct experimental evidence, but it is a valid database annotation supporting the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation for position 93 is based on similarity transfer (ECO:0000250 from Q9SWE5), not direct experimental mutagenesis or structural determination for this specific soybean protein.",
    "The UniProt entry also annotates position 178 (Cysteine) as a second proton donor active site, but this position is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The question format lists only a single residue per option, whereas active sites typically involve multiple residues; however, the task asks for the key catalytic residue and the options are structured accordingly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by sequence length (211 residues). Option B (position 170 = Proline) is chemically implausible as a proton donor. Option C (position 93 = Histidine) is the only chemically sensible proton donor among the viable choices. No ambiguity remains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 annotates position 93 as an Active Site with description 'Proton donor' (evidence code ECO:0000250, transferred from Q9SWE5). Position 93 in the 211-residue sequence corresponds to Histidine (H), consistent with a proton donor role in an FMN-dependent decarboxylase. The annotation is a similarity-transfer annotation rather than direct experimental evidence, but it is a valid database annotation supporting the expected answer.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence is 211 amino acids long. Options A (position 959) and D (position 4848) refer to positions that do not exist in this sequence and can be eliminated immediately by counting residues. This leaves B (position 170) and C (position 93). Position 170 is Proline (P), which lacks any ionizable side chain and is structurally rigid—proline is essentially never a catalytic proton donor. Position 93 is Histidine (H), whose imidazole side chain (pKa ~6-7) is the canonical proton donor/acceptor in enzyme catalysis. Furthermore, the sequence contains FMN-binding Rossmann-fold motifs (e.g., GxGxxG patterns around residues 31-33, 56-58), identifying this as an FMN-dependent decarboxylase. In the PPCDC (phosphopantothenoylcysteine decarboxylase) family, a conserved histidine serves as the proton donor in the decarboxylation mechanism. Thus, family-level knowledge of FMN-dependent decarboxylases combined with basic amino-acid chemistry (His vs. Pro as catalytic residues) meaningfully distinguishes C from B without needing the specific UniProt annotation for this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through: (1) sequence-length elimination of A and D, (2) chemical reasoning that proline cannot be a proton donor while histidine commonly is, and (3) family-level knowledge of FMN-dependent decarboxylase mechanisms where a conserved His acts as proton donor. No fact specific to this exact protein beyond what is inferable from the sequence and general biochemistry is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by sequence length (211 residues). Option B (position 170 = Proline) is chemically implausible as a proton donor. Option C (position 93 = Histidine) is the only chemically sensible proton donor among the viable choices. No ambiguity remains."
  },
  "important_caveats": [
    "The UniProt annotation for position 93 is based on similarity transfer (ECO:0000250 from Q9SWE5), not direct experimental mutagenesis or structural determination for this specific soybean protein.",
    "The UniProt entry also annotates position 178 (Cysteine) as a second proton donor active site, but this position is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The question format lists only a single residue per option, whereas active sites typically involve multiple residues; however, the task asks for the key catalytic residue and the options are structured accordingly."
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
  "benchmark_sequence_length": 211,
  "benchmark_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 211,
  "current_source_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6SZ50",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "selected_historical_source_sequence_length": 211,
  "selected_historical_source_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "selected_historical_version": {
    "accession": "C6SZ50",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HAL3A_SOYBN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6SZ50\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"Halotolerance protein 3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"GmHAL3a\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":93}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":33},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":112},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":145},\"start\":{\"modifier\":\"EXACT\",\"value\":145}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":177},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Important for catalytic activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3A_SOYBN             Reviewed;         211 AA.\nAC   C6SZ50;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3a {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   Name=HAL3A {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   OrderedLocusNames=Glyma03g020900 {ECO:0000312|EMBL:KRH65212.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "FT   ACT_SITE        93\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 150-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        178\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         31..33\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         56..58\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         109..112\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         143\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         145\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-175",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         175\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 176-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         177\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H12",
  "excerpt": "FT   SITE            178\nFT                   /note=\"Important for catalytic activity\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-190",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
