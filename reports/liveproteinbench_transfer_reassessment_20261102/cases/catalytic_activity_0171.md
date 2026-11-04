# catalytic_activity_0171

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0171.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — N-&#91;(R)-4-phosphopantothenoyl&#93;-L-cysteine + H(+) = (R)-4&#x27;-phosphopantetheine + CO2

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
A. deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)
B. (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)
C. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
D. 4-methylmuconolactone = 3-methylmuconolactone
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as a phosphopantothenoylcysteine decarboxylase, and the annotation gives reaction C. The evidence is transferred by similarity from another protein (ECO:0000250), so it supports the expected answer but is not direct experimental confirmation for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The compact, roughly 211-aa enzyme sequence can be recognized by sequence homology as belonging to the PPCDC/CoaC family. That family catalyzes the decarboxylation in option C; this family-level inference distinguishes it from the unrelated reactions in A, B, and D without requiring the exact protein's recorded annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use transferable homology and family-function knowledge to select C. The sequence does not explain the reaction in plain terms, so family recognition or sequence comparison is needed, but that is legitimate transfer from related proteins rather than dependence on this protein's exact record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe distinct reactions, and the PPCDC-family inference points specifically to C.


### Important caveats

- The supplied reviewer evidence supports a similarity-based database annotation; it does not establish direct experimental measurement of this exact protein's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The compact, roughly 211-aa enzyme sequence can be recognized by sequence homology as belonging to the PPCDC/CoaC family. That family catalyzes the decarboxylation in option C; this family-level inference distinguishes it from the unrelated reactions in A, B, and D without requiring the exact protein's recorded annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use transferable homology and family-function knowledge to select C. The sequence does not explain the reaction in plain terms, so family recognition or sequence comparison is needed, but that is legitimate transfer from related proteins rather than dependence on this protein's exact record."
  },
  "case_id": "catalytic_activity_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a phosphopantothenoylcysteine decarboxylase, and the annotation gives reaction C. The evidence is transferred by similarity from another protein (ECO:0000250), so it supports the expected answer but is not direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The supplied reviewer evidence supports a similarity-based database annotation; it does not establish direct experimental measurement of this exact protein's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct reactions, and the PPCDC-family inference points specifically to C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a phosphopantothenoylcysteine decarboxylase, and the annotation gives reaction C. The evidence is transferred by similarity from another protein (ECO:0000250), so it supports the expected answer but is not direct experimental confirmation for this sequence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The compact, roughly 211-aa enzyme sequence can be recognized by sequence homology as belonging to the PPCDC/CoaC family. That family catalyzes the decarboxylation in option C; this family-level inference distinguishes it from the unrelated reactions in A, B, and D without requiring the exact protein's recorded annotation.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use transferable homology and family-function knowledge to select C. The sequence does not explain the reaction in plain terms, so family recognition or sequence comparison is needed, but that is legitimate transfer from related proteins rather than dependence on this protein's exact record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct reactions, and the PPCDC-family inference points specifically to C."
  },
  "important_caveats": [
    "The supplied reviewer evidence supports a similarity-based database annotation; it does not establish direct experimental measurement of this exact protein's activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6SZ50 (HAL3A_SOYBN) is annotated as Phosphopantothenoylcysteine decarboxylase (EC 4.1.1.36) with the exact catalytic reaction matching option C. The sequence matches the benchmark input (211 aa, SHA-256 confirmed). However, the annotation evidence code is ECO:0000250 (inferred by similarity from Q9SWE5, yeast HAL3), meaning this is a similarity-based computational annotation rather than direct experimental characterization of this specific soybean protein. The database record supports the key, but the evidence is inferential.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 211 amino acids long. This size provides strong discrimination among the four options using general enzyme-family knowledge: (A) NAD synthetase (EC 6.3.5.1) is a large bifunctional enzyme of ~500+ aa with a glutaminase domain, incompatible with 211 aa; (B) Cinnamyl alcohol dehydrogenase (EC 1.1.1.195) is a zinc-dependent dehydrogenase of ~350-400 aa, also incompatible; (D) 4-methylmuconolactone isomerase (EC 5.3.3.10) is a small muconate-lactonizing-enzyme-family protein of ~130-150 aa, too small for 211 aa. (C) PPCDC/HAL3-family proteins are typically 200-250 aa with a TIM-barrel fold, matching the observed size. Additionally, the sequence contains glycine-rich regions (e.g., 'ASGSVAAVKF') and a C-terminal 'DYGNG' motif consistent with the conserved catalytic architecture of the well-characterized HAL3/PPCDC decarboxylase family (e.g., yeast HAL3, Q9SWE5). The absence of zinc-binding motifs (Cys/His clusters typical of alcohol dehydrogenases), absence of glutaminase-domain features, and absence of the muconate-lactonizing-enzyme fold further support PPCDC over the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 211-aa length, combined with well-established size ranges for the four enzyme families represented in the options, provides a concrete and credible inference that eliminates A, B, and D. The sequence composition (glycine-rich loops, TIM-barrel-compatible hydrophobic/polar pattern, C-terminal catalytic-region motifs) is consistent with the HAL3/PPCDC family as characterized in yeast and other organisms. This is legitimate transferable knowledge from related proteins, not a lookup of this specific soybean entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size-based elimination is clear: options A and B are far too large, option D is too small. Only option C matches the observed 211-aa length and the sequence features consistent with a TIM-barrel decarboxylase of the PPCDC/HAL3 family.


### Important caveats

- The UniProt annotation for C6SZ50 carries evidence code ECO:0000250 (similarity to Q9SWE5/yeast HAL3), not direct experimental evidence for this specific soybean protein. The key is database-supported but computationally inferred.
- The size-based argument is strong but not absolute: some enzyme families have variable-length members. However, the magnitude of the size differences here (211 vs. 500, 350-400, or 130-150 aa) makes the discrimination robust.
- The HAL3/PPCDC family annotation was first publicly released in April 2025 (entry firstPublicDate 2025-04-09), so the specific soybean entry is relatively recent, but the family itself (yeast HAL3) has been characterized for decades.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 211 amino acids long. This size provides strong discrimination among the four options using general enzyme-family knowledge: (A) NAD synthetase (EC 6.3.5.1) is a large bifunctional enzyme of ~500+ aa with a glutaminase domain, incompatible with 211 aa; (B) Cinnamyl alcohol dehydrogenase (EC 1.1.1.195) is a zinc-dependent dehydrogenase of ~350-400 aa, also incompatible; (D) 4-methylmuconolactone isomerase (EC 5.3.3.10) is a small muconate-lactonizing-enzyme-family protein of ~130-150 aa, too small for 211 aa. (C) PPCDC/HAL3-family proteins are typically 200-250 aa with a TIM-barrel fold, matching the observed size. Additionally, the sequence contains glycine-rich regions (e.g., 'ASGSVAAVKF') and a C-terminal 'DYGNG' motif consistent with the conserved catalytic architecture of the well-characterized HAL3/PPCDC decarboxylase family (e.g., yeast HAL3, Q9SWE5). The absence of zinc-binding motifs (Cys/His clusters typical of alcohol dehydrogenases), absence of glutaminase-domain features, and absence of the muconate-lactonizing-enzyme fold further support PPCDC over the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 211-aa length, combined with well-established size ranges for the four enzyme families represented in the options, provides a concrete and credible inference that eliminates A, B, and D. The sequence composition (glycine-rich loops, TIM-barrel-compatible hydrophobic/polar pattern, C-terminal catalytic-region motifs) is consistent with the HAL3/PPCDC family as characterized in yeast and other organisms. This is legitimate transferable knowledge from related proteins, not a lookup of this specific soybean entry's annotation."
  },
  "case_id": "catalytic_activity_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 (HAL3A_SOYBN) is annotated as Phosphopantothenoylcysteine decarboxylase (EC 4.1.1.36) with the exact catalytic reaction matching option C. The sequence matches the benchmark input (211 aa, SHA-256 confirmed). However, the annotation evidence code is ECO:0000250 (inferred by similarity from Q9SWE5, yeast HAL3), meaning this is a similarity-based computational annotation rather than direct experimental characterization of this specific soybean protein. The database record supports the key, but the evidence is inferential."
  },
  "important_caveats": [
    "The UniProt annotation for C6SZ50 carries evidence code ECO:0000250 (similarity to Q9SWE5/yeast HAL3), not direct experimental evidence for this specific soybean protein. The key is database-supported but computationally inferred.",
    "The size-based argument is strong but not absolute: some enzyme families have variable-length members. However, the magnitude of the size differences here (211 vs. 500, 350-400, or 130-150 aa) makes the discrimination robust.",
    "The HAL3/PPCDC family annotation was first publicly released in April 2025 (entry firstPublicDate 2025-04-09), so the specific soybean entry is relatively recent, but the family itself (yeast HAL3) has been characterized for decades."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size-based elimination is clear: options A and B are far too large, option D is too small. Only option C matches the observed 211-aa length and the sequence features consistent with a TIM-barrel decarboxylase of the PPCDC/HAL3 family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 (HAL3A_SOYBN) is annotated as Phosphopantothenoylcysteine decarboxylase (EC 4.1.1.36) with the exact catalytic reaction matching option C. The sequence matches the benchmark input (211 aa, SHA-256 confirmed). However, the annotation evidence code is ECO:0000250 (inferred by similarity from Q9SWE5, yeast HAL3), meaning this is a similarity-based computational annotation rather than direct experimental characterization of this specific soybean protein. The database record supports the key, but the evidence is inferential.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 211 amino acids long. This size provides strong discrimination among the four options using general enzyme-family knowledge: (A) NAD synthetase (EC 6.3.5.1) is a large bifunctional enzyme of ~500+ aa with a glutaminase domain, incompatible with 211 aa; (B) Cinnamyl alcohol dehydrogenase (EC 1.1.1.195) is a zinc-dependent dehydrogenase of ~350-400 aa, also incompatible; (D) 4-methylmuconolactone isomerase (EC 5.3.3.10) is a small muconate-lactonizing-enzyme-family protein of ~130-150 aa, too small for 211 aa. (C) PPCDC/HAL3-family proteins are typically 200-250 aa with a TIM-barrel fold, matching the observed size. Additionally, the sequence contains glycine-rich regions (e.g., 'ASGSVAAVKF') and a C-terminal 'DYGNG' motif consistent with the conserved catalytic architecture of the well-characterized HAL3/PPCDC decarboxylase family (e.g., yeast HAL3, Q9SWE5). The absence of zinc-binding motifs (Cys/His clusters typical of alcohol dehydrogenases), absence of glutaminase-domain features, and absence of the muconate-lactonizing-enzyme fold further support PPCDC over the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The 211-aa length, combined with well-established size ranges for the four enzyme families represented in the options, provides a concrete and credible inference that eliminates A, B, and D. The sequence composition (glycine-rich loops, TIM-barrel-compatible hydrophobic/polar pattern, C-terminal catalytic-region motifs) is consistent with the HAL3/PPCDC family as characterized in yeast and other organisms. This is legitimate transferable knowledge from related proteins, not a lookup of this specific soybean entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size-based elimination is clear: options A and B are far too large, option D is too small. Only option C matches the observed 211-aa length and the sequence features consistent with a TIM-barrel decarboxylase of the PPCDC/HAL3 family."
  },
  "important_caveats": [
    "The UniProt annotation for C6SZ50 carries evidence code ECO:0000250 (similarity to Q9SWE5/yeast HAL3), not direct experimental evidence for this specific soybean protein. The key is database-supported but computationally inferred.",
    "The size-based argument is strong but not absolute: some enzyme families have variable-length members. However, the magnitude of the size differences here (211 vs. 500, 350-400, or 130-150 aa) makes the discrimination robust.",
    "The HAL3/PPCDC family annotation was first publicly released in April 2025 (entry firstPublicDate 2025-04-09), so the specific soybean entry is relatively recent, but the family itself (yeast HAL3) has been characterized for decades."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16794\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.36\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16793\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61723\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3a {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
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
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-\nCC         phosphopantetheine + CO2; Xref=Rhea:RHEA:16793, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:59458, ChEBI:CHEBI:61723; EC=4.1.1.36;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16794;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
