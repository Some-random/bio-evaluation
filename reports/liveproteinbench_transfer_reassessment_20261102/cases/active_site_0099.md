# active_site_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0099.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 26 (Proton donor/acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIRLLYLLVKPAGMSDETFRAECLRHYEMSHDVPGLHKYEVRLVAEQPTDTHVPFFDIGHVDAIGECWFKDDAAYATYMASDIRKAWFEHGKTFIGQLKPFRTAPVAGDEPAS

[Multiple Choices]
A. Position 38 (Nucleophile)
B. Position 26 (Proton donor/acceptor)
C. Position 170 (Nucleophile)
D. Position 4681 (Proton acceptor; for dehydratase activity 2)
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

> The sequence-matched UniProt entry annotates position 26 as an active-site proton donor/acceptor. That annotation is transferred by similarity from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental validation for this exact protein.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 113 residues long, ruling out positions 170 and 4681. Position 26 is histidine, a common general acid/base residue, whereas position 38 is lysine; among the remaining offered choices, the histidine/proton-donor-acceptor pairing is a credible biochemical distinction favoring B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and option labels provide a meaningful transferable chemical basis for choosing B without needing the exact protein's database annotation. This is a plausible inference, not proof that the residue's role has been experimentally established.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B combines an in-range position with the especially plausible histidine acid/base role; the other in-range alternative assigns a nucleophile role to position 38.


### Important caveats

- The supporting database annotation is similarity-transferred, not shown here to be direct experimental evidence for this protein.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 113 residues long, ruling out positions 170 and 4681. Position 26 is histidine, a common general acid/base residue, whereas position 38 is lysine; among the remaining offered choices, the histidine/proton-donor-acceptor pairing is a credible biochemical distinction favoring B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and option labels provide a meaningful transferable chemical basis for choosing B without needing the exact protein's database annotation. This is a plausible inference, not proof that the residue's role has been experimentally established."
  },
  "case_id": "active_site_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 26 as an active-site proton donor/acceptor. That annotation is transferred by similarity from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental validation for this exact protein."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-transferred, not shown here to be direct experimental evidence for this protein.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B combines an in-range position with the especially plausible histidine acid/base role; the other in-range alternative assigns a nucleophile role to position 38."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 26 as an active-site proton donor/acceptor. That annotation is transferred by similarity from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental validation for this exact protein.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 113 residues long, ruling out positions 170 and 4681. Position 26 is histidine, a common general acid/base residue, whereas position 38 is lysine; among the remaining offered choices, the histidine/proton-donor-acceptor pairing is a credible biochemical distinction favoring B.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and option labels provide a meaningful transferable chemical basis for choosing B without needing the exact protein's database annotation. This is a plausible inference, not proof that the residue's role has been experimentally established."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B combines an in-range position with the especially plausible histidine acid/base role; the other in-range alternative assigns a nucleophile role to position 38."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-transferred, not shown here to be direct experimental evidence for this protein.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt evidence (C5, H4) directly annotates position 26 as 'Active site' with description 'Proton donor/acceptor' for this exact 113-AA sequence (SHA256 matched). The evidence code is ECO:0000250 (similarity to C5MR76), indicating computational inference by homology rather than direct experimental determination, but it is the recorded annotation. The residue at position 26 is Histidine, consistent with the proton donor/acceptor role.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options C (position 170) and D (position 4681) are immediately eliminated because the protein is only 113 amino acids long; a model can count the sequence. Between A and B: counting to position 26 yields Histidine, and counting to position 38 yields Lysine. Histidine's imidazole side chain (pKa ~6.0) is the canonical and most universal proton donor/acceptor in enzymatic catalysis — this is one of the most fundamental principles in biochemistry learned from thousands of enzymes (serine proteases, phosphatases, kinases, etc.). Lysine can serve as a nucleophile in some enzymes (e.g., Schiff-base aldolases), but the pairing 'Histidine + proton donor/acceptor' is far more universally and strongly associated than 'Lysine + nucleophile' for a small isomerase. A model recognizing the His at position 26 and matching it to the proton-transfer function described in option B can make a confident, transferable inference without knowing this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence length eliminates C and D trivially. The His–proton-donor/acceptor association is universal enzymology transferable from many other proteins. Identifying the residue type at a given position requires only counting the provided sequence. No fact specific to this exact protein beyond what is derivable from the sequence itself is needed to distinguish B from A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are impossible (positions exceed sequence length). Option A pairs Lysine with 'nucleophile,' which is biochemically possible but far less canonical than the His–proton-donor/acceptor pairing in B. The strength of the universal His–proton-shuttle association makes B clearly preferred over A without ambiguity.


### Important caveats

- The UniProt active-site annotation uses evidence code ECO:0000250 (similarity to C5MR76), meaning it is a computational inference by homology, not direct experimental characterization of this specific enzyme.
- The protein identity (4-carboxymethyl-4-methylbutenolide mutase / methylmuconolactone isomerase, EC 5.4.99.14) and organism are reviewer-only information not provided to the evaluated model; the model must rely on sequence-based reasoning and general biochemistry.
- The model must count the 113-residue sequence accurately to identify residue types at positions 26 and 38; an off-by-one counting error could misidentify the residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C (position 170) and D (position 4681) are immediately eliminated because the protein is only 113 amino acids long; a model can count the sequence. Between A and B: counting to position 26 yields Histidine, and counting to position 38 yields Lysine. Histidine's imidazole side chain (pKa ~6.0) is the canonical and most universal proton donor/acceptor in enzymatic catalysis — this is one of the most fundamental principles in biochemistry learned from thousands of enzymes (serine proteases, phosphatases, kinases, etc.). Lysine can serve as a nucleophile in some enzymes (e.g., Schiff-base aldolases), but the pairing 'Histidine + proton donor/acceptor' is far more universally and strongly associated than 'Lysine + nucleophile' for a small isomerase. A model recognizing the His at position 26 and matching it to the proton-transfer function described in option B can make a confident, transferable inference without knowing this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence length eliminates C and D trivially. The His–proton-donor/acceptor association is universal enzymology transferable from many other proteins. Identifying the residue type at a given position requires only counting the provided sequence. No fact specific to this exact protein beyond what is derivable from the sequence itself is needed to distinguish B from A."
  },
  "case_id": "active_site_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt evidence (C5, H4) directly annotates position 26 as 'Active site' with description 'Proton donor/acceptor' for this exact 113-AA sequence (SHA256 matched). The evidence code is ECO:0000250 (similarity to C5MR76), indicating computational inference by homology rather than direct experimental determination, but it is the recorded annotation. The residue at position 26 is Histidine, consistent with the proton donor/acceptor role."
  },
  "important_caveats": [
    "The UniProt active-site annotation uses evidence code ECO:0000250 (similarity to C5MR76), meaning it is a computational inference by homology, not direct experimental characterization of this specific enzyme.",
    "The protein identity (4-carboxymethyl-4-methylbutenolide mutase / methylmuconolactone isomerase, EC 5.4.99.14) and organism are reviewer-only information not provided to the evaluated model; the model must rely on sequence-based reasoning and general biochemistry.",
    "The model must count the 113-residue sequence accurately to identify residue types at positions 26 and 38; an off-by-one counting error could misidentify the residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are impossible (positions exceed sequence length). Option A pairs Lysine with 'nucleophile,' which is biochemically possible but far less canonical than the His–proton-donor/acceptor pairing in B. The strength of the universal His–proton-shuttle association makes B clearly preferred over A without ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt evidence (C5, H4) directly annotates position 26 as 'Active site' with description 'Proton donor/acceptor' for this exact 113-AA sequence (SHA256 matched). The evidence code is ECO:0000250 (similarity to C5MR76), indicating computational inference by homology rather than direct experimental determination, but it is the recorded annotation. The residue at position 26 is Histidine, consistent with the proton donor/acceptor role.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options C (position 170) and D (position 4681) are immediately eliminated because the protein is only 113 amino acids long; a model can count the sequence. Between A and B: counting to position 26 yields Histidine, and counting to position 38 yields Lysine. Histidine's imidazole side chain (pKa ~6.0) is the canonical and most universal proton donor/acceptor in enzymatic catalysis — this is one of the most fundamental principles in biochemistry learned from thousands of enzymes (serine proteases, phosphatases, kinases, etc.). Lysine can serve as a nucleophile in some enzymes (e.g., Schiff-base aldolases), but the pairing 'Histidine + proton donor/acceptor' is far more universally and strongly associated than 'Lysine + nucleophile' for a small isomerase. A model recognizing the His at position 26 and matching it to the proton-transfer function described in option B can make a confident, transferable inference without knowing this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The sequence length eliminates C and D trivially. The His–proton-donor/acceptor association is universal enzymology transferable from many other proteins. Identifying the residue type at a given position requires only counting the provided sequence. No fact specific to this exact protein beyond what is derivable from the sequence itself is needed to distinguish B from A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are impossible (positions exceed sequence length). Option A pairs Lysine with 'nucleophile,' which is biochemically possible but far less canonical than the His–proton-donor/acceptor pairing in B. The strength of the universal His–proton-shuttle association makes B clearly preferred over A without ambiguity."
  },
  "important_caveats": [
    "The UniProt active-site annotation uses evidence code ECO:0000250 (similarity to C5MR76), meaning it is a computational inference by homology, not direct experimental characterization of this specific enzyme.",
    "The protein identity (4-carboxymethyl-4-methylbutenolide mutase / methylmuconolactone isomerase, EC 5.4.99.14) and organism are reviewer-only information not provided to the evaluated model; the model must rely on sequence-based reasoning and general biochemistry.",
    "The model must count the 113-residue sequence accurately to identify residue types at positions 26 and 38; an off-by-one counting error could misidentify the residues."
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
  "excerpt": "{\"description\":\"Proton donor/acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"C5MR76\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":26}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"C5MR76\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57883\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57883\",\"name\":\"3-methylmuconolactone\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":26}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"C5MR76\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57888\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57888\",\"name\":\"4-methylmuconolactone\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":26}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"C5MR76\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57883\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57883\",\"name\":\"3-methylmuconolactone\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":39},\"start\":{\"modifier\":\"EXACT\",\"value\":39}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"C5MR76\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57888\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57888\",\"name\":\"4-methylmuconolactone\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":39},\"start\":{\"modifier\":\"EXACT\",\"value\":39}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C10",
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

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C11",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H3",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        26\nFT                   /note=\"Proton donor/acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:C5MR76\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-114",
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
  "excerpt": "FT   BINDING         26\nFT                   /ligand=\"3-methylmuconolactone\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57883\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:C5MR76\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         26\nFT                   /ligand=\"4-methylmuconolactone\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57888\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:C5MR76\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         39\nFT                   /ligand=\"3-methylmuconolactone\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57883\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:C5MR76\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         39\nFT                   /ligand=\"4-methylmuconolactone\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57888\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:C5MR76\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
