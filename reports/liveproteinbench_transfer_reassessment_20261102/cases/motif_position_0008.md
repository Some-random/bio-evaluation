# motif_position_0008

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0008.txt)

**Task:** `motif_position`  
**Expected answer:** **C** — 319..322

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIYHRIAVNVPLSDGLLTYSHSEPLPPGTRVLVPFRNKTVVGMVWETDIAPDMDAARILSVQTVFVEEKPLSQSWRDLLAFTSRYYHYPTGQAVFAALPQGLKETRAVEMPQPPLFYALNEAGRAQTPPPARFNKKAALWDALLSGEMTMAALKQANAQAAKLIEDWAEQGWIETTEAAKPVLRPYRGQASHSEFVLNTGQQKASDEIQTALGRFRSFLLYGITGSGKTEVYFDAMAKVLAQGRQVLFLLPEINLTPQLLKRVENRFADVPTAVLHSRMAAGRRTQDYLRAMLGQAKLVIGTRLAVFTPLPDVGLIVVDEEHDGSFKQDNELRYHARDLAVWRAKQGGCPVVLGSATPSLESWHKAQSGAYRLLQLTERAHASAQLPQVDILNIGRLKLDNGFSPQALQLLKQNFEAGGMSLVYLNRRGFAPALFCGDCGHTFGCPNCSAKMVLHQRARQLRCHHCDHREPIPFKCPDCGNQDLTAVGHGTQRVEETLRAFLPKAAVVRVDRDSTAHKNDWADLYRRIANDEIDILVGTQMLAKGHDFARLNLVIVLNADGSLYSADFRAPERLFAELMQVSGRAGRADKPGKVLIQTQLPEHPVFAAVKAQDYAVFAENELNERQMFAMPPFGFQTAVRADAPRVADAMEFLNAAKETLAPLLPESVSRFGAAPMLMVRLAERERAQVFLESTSRQDLHRAVSLWVQVLQQNRDGKIRWSVDVDPQEA

[Multiple Choices]
A. 972..974
B. 14..24
C. 319..322
D. 178..180
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

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the motif at 319..322. This is a computational HAMAP annotation, not direct experimental evidence of the motif boundaries. The sequence at those positions is DEEH, so the annotation supports the location of the helicase motif but the sequence is not a literal canonical DEAH string.

Citations as saved: [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a helicase-like P-loop, GSGKT, around positions 226..230, followed by an acidic motif at 319..322 (DEEH). Conserved helicase ATPase motifs occur in this core, making C a meaningful choice over the unrelated-looking regions in B and D; A is beyond the sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence’s ATPase/helicase motifs meaningfully distinguishes the offered position. The noncanonical DEEH sequence makes the exact motif label less certain, but does not erase the positional evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed positions, only C coincides with the sequence’s acidic helicase-motif region.


### Important caveats

- The supplied sequence has DEEH, not literal DEAH, at positions 319..322.
- The reviewer-only annotation is computational and applies to a sequence-matched record; it is not experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a helicase-like P-loop, GSGKT, around positions 226..230, followed by an acidic motif at 319..322 (DEEH). Conserved helicase ATPase motifs occur in this core, making C a meaningful choice over the unrelated-looking regions in B and D; A is beyond the sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence’s ATPase/helicase motifs meaningfully distinguishes the offered position. The noncanonical DEEH sequence makes the exact motif label less certain, but does not erase the positional evidence."
  },
  "case_id": "motif_position_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the motif at 319..322. This is a computational HAMAP annotation, not direct experimental evidence of the motif boundaries. The sequence at those positions is DEEH, so the annotation supports the location of the helicase motif but the sequence is not a literal canonical DEAH string."
  },
  "important_caveats": [
    "The supplied sequence has DEEH, not literal DEAH, at positions 319..322.",
    "The reviewer-only annotation is computational and applies to a sequence-matched record; it is not experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed positions, only C coincides with the sequence’s acidic helicase-motif region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the motif at 319..322. This is a computational HAMAP annotation, not direct experimental evidence of the motif boundaries. The sequence at those positions is DEEH, so the annotation supports the location of the helicase motif but the sequence is not a literal canonical DEAH string.",
    "evidence_ids": ["C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a helicase-like P-loop, GSGKT, around positions 226..230, followed by an acidic motif at 319..322 (DEEH). Conserved helicase ATPase motifs occur in this core, making C a meaningful choice over the unrelated-looking regions in B and D; A is beyond the sequence length.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence’s ATPase/helicase motifs meaningfully distinguishes the offered position. The noncanonical DEEH sequence makes the exact motif label less certain, but does not erase the positional evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed positions, only C coincides with the sequence’s acidic helicase-motif region."
  },
  "important_caveats": [
    "The supplied sequence has DEEH, not literal DEAH, at positions 319..322.",
    "The reviewer-only annotation is computational and applies to a sequence-matched record; it is not experimental confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5F6V8 annotates a 'DEAH box' motif at positions 319..322 (evidence C7/H7, HAMAP-Rule MF_00983). The sequence residues at 319-322 are D-E-E-H, a recognized variant of the canonical DEAH box found in SF2 helicases. The annotation is computational (ECO:0000255, HAMAP-Rule), but the DEAH box is a well-established superfamily-level motif in RecQ/DNA helicases, and the sequence match is confirmed. The expected answer C (319..322) is consistent with the supplied evidence.

Citations as saved: [C7](#evidence-c7), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Walker A motif (GxxxxGK&#91;ST&#93;) around positions 222-230 ('GITGSGKTE'), identifying the protein as a superfamily 2 (SF2) helicase. In SF2 helicases, the DEAH box (consensus D-E-&#91;AE&#93;-H) is a well-known conserved motif located within the helicase ATP-binding domain, typically ~80-120 residues downstream of the Walker A motif. Scanning the sequence at the offered positions: (A) 972..974 is beyond the 729-residue protein, immediately eliminable; (B) 14..24 ('GLLTYSHSEPL') lies in the N-terminal region far upstream of the helicase core; (D) 178..180 ('AAK') is before the helicase ATP-binding domain and matches no recognized motif; (C) 319..322 ('DEEH') falls squarely within the helicase ATP-binding domain (~90 residues downstream of the Walker A) and matches the DEAH-box pattern. Family-level knowledge of SF2 helicase motif architecture (Walker A → DEAH box ordering) and the ability to recognize the DEEH variant of DEAH from the sequence itself meaningfully distinguish C from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of helicase superfamily motifs can recognize the Walker A motif in the sequence, infer the protein is an SF2 helicase, know that the DEAH box is a conserved SF2 motif positioned downstream of Walker A within the ATP-binding domain, and scan the four candidate ranges for a matching D-E-x-H pattern. Only option C satisfies all these criteria. The other options are eliminable by basic sequence-length check (A), domain-position reasoning (B, D), or absence of any recognizable motif pattern.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The question asks for 'a conserved motif' without naming it, but only option C corresponds to a recognized conserved motif (DEAH box variant DEEH) within the helicase domain. Option A is outside the protein length, B and D do not match any known motif pattern. The choices are effectively unambiguous.


### Important caveats

- The DEAH box annotation is computational (HAMAP-Rule, ECO:0000255), not directly experimentally validated for this specific protein, though the motif is extensively characterized across the SF2 helicase superfamily.
- The residues at 319-322 are DEEH rather than the canonical DEAH; the HAMAP rule accepts this variant, and it is annotated as 'DEAH box'.
- The question does not specify which motif to locate, relying on the examinee to identify the only option matching a recognized conserved motif.
- The protein identity (PriA, Neisseria gonorrhoeae) and accession Q5F6V8 are reviewer-only and were not provided to the evaluated model; the reasoning above relies solely on sequence features and superfamily knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A motif (GxxxxGK[ST]) around positions 222-230 ('GITGSGKTE'), identifying the protein as a superfamily 2 (SF2) helicase. In SF2 helicases, the DEAH box (consensus D-E-[AE]-H) is a well-known conserved motif located within the helicase ATP-binding domain, typically ~80-120 residues downstream of the Walker A motif. Scanning the sequence at the offered positions: (A) 972..974 is beyond the 729-residue protein, immediately eliminable; (B) 14..24 ('GLLTYSHSEPL') lies in the N-terminal region far upstream of the helicase core; (D) 178..180 ('AAK') is before the helicase ATP-binding domain and matches no recognized motif; (C) 319..322 ('DEEH') falls squarely within the helicase ATP-binding domain (~90 residues downstream of the Walker A) and matches the DEAH-box pattern. Family-level knowledge of SF2 helicase motif architecture (Walker A → DEAH box ordering) and the ability to recognize the DEEH variant of DEAH from the sequence itself meaningfully distinguish C from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of helicase superfamily motifs can recognize the Walker A motif in the sequence, infer the protein is an SF2 helicase, know that the DEAH box is a conserved SF2 motif positioned downstream of Walker A within the ATP-binding domain, and scan the four candidate ranges for a matching D-E-x-H pattern. Only option C satisfies all these criteria. The other options are eliminable by basic sequence-length check (A), domain-position reasoning (B, D), or absence of any recognizable motif pattern."
  },
  "case_id": "motif_position_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5F6V8 annotates a 'DEAH box' motif at positions 319..322 (evidence C7/H7, HAMAP-Rule MF_00983). The sequence residues at 319-322 are D-E-E-H, a recognized variant of the canonical DEAH box found in SF2 helicases. The annotation is computational (ECO:0000255, HAMAP-Rule), but the DEAH box is a well-established superfamily-level motif in RecQ/DNA helicases, and the sequence match is confirmed. The expected answer C (319..322) is consistent with the supplied evidence."
  },
  "important_caveats": [
    "The DEAH box annotation is computational (HAMAP-Rule, ECO:0000255), not directly experimentally validated for this specific protein, though the motif is extensively characterized across the SF2 helicase superfamily.",
    "The residues at 319-322 are DEEH rather than the canonical DEAH; the HAMAP rule accepts this variant, and it is annotated as 'DEAH box'.",
    "The question does not specify which motif to locate, relying on the examinee to identify the only option matching a recognized conserved motif.",
    "The protein identity (PriA, Neisseria gonorrhoeae) and accession Q5F6V8 are reviewer-only and were not provided to the evaluated model; the reasoning above relies solely on sequence features and superfamily knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'a conserved motif' without naming it, but only option C corresponds to a recognized conserved motif (DEAH box variant DEEH) within the helicase domain. Option A is outside the protein length, B and D do not match any known motif pattern. The choices are effectively unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5F6V8 annotates a 'DEAH box' motif at positions 319..322 (evidence C7/H7, HAMAP-Rule MF_00983). The sequence residues at 319-322 are D-E-E-H, a recognized variant of the canonical DEAH box found in SF2 helicases. The annotation is computational (ECO:0000255, HAMAP-Rule), but the DEAH box is a well-established superfamily-level motif in RecQ/DNA helicases, and the sequence match is confirmed. The expected answer C (319..322) is consistent with the supplied evidence.",
    "evidence_ids": ["C7", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A motif (GxxxxGK[ST]) around positions 222-230 ('GITGSGKTE'), identifying the protein as a superfamily 2 (SF2) helicase. In SF2 helicases, the DEAH box (consensus D-E-[AE]-H) is a well-known conserved motif located within the helicase ATP-binding domain, typically ~80-120 residues downstream of the Walker A motif. Scanning the sequence at the offered positions: (A) 972..974 is beyond the 729-residue protein, immediately eliminable; (B) 14..24 ('GLLTYSHSEPL') lies in the N-terminal region far upstream of the helicase core; (D) 178..180 ('AAK') is before the helicase ATP-binding domain and matches no recognized motif; (C) 319..322 ('DEEH') falls squarely within the helicase ATP-binding domain (~90 residues downstream of the Walker A) and matches the DEAH-box pattern. Family-level knowledge of SF2 helicase motif architecture (Walker A → DEAH box ordering) and the ability to recognize the DEEH variant of DEAH from the sequence itself meaningfully distinguish C from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of helicase superfamily motifs can recognize the Walker A motif in the sequence, infer the protein is an SF2 helicase, know that the DEAH box is a conserved SF2 motif positioned downstream of Walker A within the ATP-binding domain, and scan the four candidate ranges for a matching D-E-x-H pattern. Only option C satisfies all these criteria. The other options are eliminable by basic sequence-length check (A), domain-position reasoning (B, D), or absence of any recognizable motif pattern."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'a conserved motif' without naming it, but only option C corresponds to a recognized conserved motif (DEAH box variant DEEH) within the helicase domain. Option A is outside the protein length, B and D do not match any known motif pattern. The choices are effectively unambiguous."
  },
  "important_caveats": [
    "The DEAH box annotation is computational (HAMAP-Rule, ECO:0000255), not directly experimentally validated for this specific protein, though the motif is extensively characterized across the SF2 helicase superfamily.",
    "The residues at 319-322 are DEEH rather than the canonical DEAH; the HAMAP rule accepts this variant, and it is annotated as 'DEAH box'.",
    "The question does not specify which motif to locate, relying on the examinee to identify the only option matching a recognized conserved motif.",
    "The protein identity (PriA, Neisseria gonorrhoeae) and accession Q5F6V8 are reviewer-only and were not provided to the evaluated model; the reasoning above relies solely on sequence features and superfamily knowledge."
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
  "benchmark_sequence_length": 729,
  "benchmark_sequence_sha256": "ef6c3ffe7dc37bec3d2529c78a1850288bf6360f53389681bff488df263499ab",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-03-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 729,
  "current_source_sequence_sha256": "ef6c3ffe7dc37bec3d2529c78a1850288bf6360f53389681bff488df263499ab",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 129,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5F6V8",
  "selected_historical_entry_version": 129,
  "selected_historical_record_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "selected_historical_source_sequence_length": 729,
  "selected_historical_source_sequence_sha256": "ef6c3ffe7dc37bec3d2529c78a1850288bf6360f53389681bff488df263499ab",
  "selected_historical_version": {
    "accession": "Q5F6V8",
    "database": "Swiss-Prot",
    "entryVersion": 129,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PRIA_NEIG1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5F6V8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-03-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090)\",\"taxonId\":242231}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21861872\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23193948\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"ATP-dependent DNA helicase PriA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"DNA 3'-5' helicase PriA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16030229\",\"source\":\"PubMed\"}],\"value\":\"Helicase PriA\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Replication restart protein PriA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helicase ATP-binding\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":376},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helicase C-terminal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":623},\"start\":{\"modifier\":\"EXACT\",\"value\":471}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"DEAH box\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":322},\"start\":{\"modifier\":\"EXACT\",\"value\":319}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Kline K.A.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16030229\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.15.5347-5355.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"5347\",\"id\":\"16030229\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"5355\",\"publicationDate\":\"2005\",\"title\":\"Mutation of the priA gene of Neisseria gonorrhoeae affects DNA transformation and DNA repair.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Feng C.\",\"Sunchu B.\",\"Greenwood M.E.\",\"Lopper M.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21861872\"},{\"database\":\"DOI\",\"id\":\"10.1186/1471-2180-11-189\"}],\"citationType\":\"journal article\",\"firstPage\":\"189\",\"id\":\"21861872\",\"journal\":\"BMC Microbiol.\",\"lastPage\":\"189\",\"publicationDate\":\"2011\",\"title\":\"A bacterial PriB with weak single-stranded DNA binding activity can stimulate the DNA unwinding activity of its cognate PriA helicase.\",\"volume\":\"11\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION AS A HELICASE\",\"FUNCTION AS AN ATPASE\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DNA-BINDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Sunchu B.\",\"Berg L.\",\"Ward H.E.\",\"Lopper M.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23193948\"},{\"database\":\"DOI\",\"id\":\"10.1021/bi301100w\"}],\"citationType\":\"journal article\",\"firstPage\":\"10137\",\"id\":\"23193948\",\"journal\":\"Biochemistry\",\"lastPage\":\"10146\",\"publicationDate\":\"2012\",\"title\":\"Identification of a small molecule PriA helicase inhibitor.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:22.112172+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F6V8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H1",
  "excerpt": "ID   PRIA_NEIG1              Reviewed;         729 AA.\nAC   Q5F6V8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-MAR-2005, sequence version 1.\nDT   28-JAN-2026, entry version 129.\nDE   RecName: Full=Replication restart protein PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE   AltName: Full=ATP-dependent DNA helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE            EC=5.6.2.4 {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305|PubMed:21861872, ECO:0000305|PubMed:23193948};\nDE   AltName: Full=DNA 3'-5' helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE   AltName: Full=Helicase PriA {ECO:0000303|PubMed:16030229};\nGN   Name=priA {ECO:0000255|HAMAP-Rule:MF_00983};\nGN   OrderedLocusNames=NGO_1437 {ECO:0000312|EMBL:AAW90079.1};\nOS   Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=242231;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700825 / FA 1090;\nRX   PubMed=16030229; DOI=10.1128/jb.187.15.5347-5355.2005;\nRA   Kline K.A., Seifert H.S.;\nRT   \"Mutation of the priA gene of Neisseria gonorrhoeae affects DNA\nRT   transformation and DNA repair.\";\nRL   J. Bacteriol. 187:5347-5355(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY, ACTIVITY\nRP   REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND DNA-BINDING.\nRC   STRAIN=ATCC 700825 / FA 1090;\nRX   PubMed=21861872; DOI=10.1186/1471-2180-11-189;\nRA   Feng C., Sunchu B., Greenwood M.E., Lopper M.E.;\nRT   \"A bacterial PriB with weak single-stranded DNA binding activity can\nRT   stimulate the DNA unwinding activity of its cognate PriA helicase.\";\nRL   BMC Microbiol. 11:189-189(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H4",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRC   STRAIN=ATCC 700825 / FA 1090;\nRX   PubMed=23193948; DOI=10.1021/bi301100w;\nRA   Sunchu B., Berg L., Ward H.E., Lopper M.E.;\nRT   \"Identification of a small molecule PriA helicase inhibitor.\";\nRL   Biochemistry 51:10137-10146(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H5",
  "excerpt": "FT   DOMAIN          209..376\nFT                   /note=\"Helicase ATP-binding\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00983\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H6",
  "excerpt": "FT   DOMAIN          471..623\nFT                   /note=\"Helicase C-terminal\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00983\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H7",
  "excerpt": "FT   MOTIF           319..322\nFT                   /note=\"DEAH box\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00983\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:37.505271+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-180",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3",
  "url": "https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
