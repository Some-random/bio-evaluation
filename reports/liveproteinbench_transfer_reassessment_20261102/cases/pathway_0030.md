# pathway_0030

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0030.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Cofactor biosynthesis

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
A. L-threonine from L-aspartate: step 5/5. .
B. fatty acid beta-oxidation. .
C. Cofactor biosynthesis
D. N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as phosphopantothenoylcysteine decarboxylase, an enzyme in coenzyme A biosynthesis, supporting the broader choice of cofactor biosynthesis. The enzyme and pathway assignments cite evidence transferred from another UniProt protein, so this supports the key but is not direct experimental evidence for this soybean protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 211-aa sequence is consistent with the phosphopantothenoylcysteine decarboxylase/Hal3 family. Transferable knowledge of this enzyme family connects the enzyme to coenzyme A biosynthesis, placing it under option C. That meaningfully distinguishes C from the threonine, fatty-acid beta-oxidation, and purine-biosynthesis alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features can distinguish the broad pathway choice without knowing this exact protein's database record. The inference is credible but not an independent experimental confirmation of the soybean protein's function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level pathway inference supports C; none of the other options is an equally defensible match.


### Important caveats

- The supplied pathway annotation is based on evidence transferred by similarity, rather than direct experimental evidence cited for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 211-aa sequence is consistent with the phosphopantothenoylcysteine decarboxylase/Hal3 family. Transferable knowledge of this enzyme family connects the enzyme to coenzyme A biosynthesis, placing it under option C. That meaningfully distinguishes C from the threonine, fatty-acid beta-oxidation, and purine-biosynthesis alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features can distinguish the broad pathway choice without knowing this exact protein's database record. The inference is credible but not an independent experimental confirmation of the soybean protein's function."
  },
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as phosphopantothenoylcysteine decarboxylase, an enzyme in coenzyme A biosynthesis, supporting the broader choice of cofactor biosynthesis. The enzyme and pathway assignments cite evidence transferred from another UniProt protein, so this supports the key but is not direct experimental evidence for this soybean protein."
  },
  "important_caveats": [
    "The supplied pathway annotation is based on evidence transferred by similarity, rather than direct experimental evidence cited for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level pathway inference supports C; none of the other options is an equally defensible match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as phosphopantothenoylcysteine decarboxylase, an enzyme in coenzyme A biosynthesis, supporting the broader choice of cofactor biosynthesis. The enzyme and pathway assignments cite evidence transferred from another UniProt protein, so this supports the key but is not direct experimental evidence for this soybean protein.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 211-aa sequence is consistent with the phosphopantothenoylcysteine decarboxylase/Hal3 family. Transferable knowledge of this enzyme family connects the enzyme to coenzyme A biosynthesis, placing it under option C. That meaningfully distinguishes C from the threonine, fatty-acid beta-oxidation, and purine-biosynthesis alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features can distinguish the broad pathway choice without knowing this exact protein's database record. The inference is credible but not an independent experimental confirmation of the soybean protein's function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level pathway inference supports C; none of the other options is an equally defensible match."
  },
  "important_caveats": [
    "The supplied pathway annotation is based on evidence transferred by similarity, rather than direct experimental evidence cited for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6SZ50 (HAL3A_SOYBN) is annotated as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36) with the pathway 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5.' This directly supports the expected answer C (Cofactor biosynthesis). The annotation is based on similarity transfer (ECO:0000250) from Q9SWE5, but the enzyme identity and pathway assignment are consistent with the well-characterized PPCDC family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GDYGNG' motif (near position ~190: 'RLACGDYGNGAMAEP'), which is a well-known family signature of phosphopantothenoylcysteine decarboxylase (PPCDC) enzymes across bacteria, fungi, and plants (e.g., E. coli CoaB, yeast Ppc1, Arabidopsis PPCDC). PPCDC catalyzes the decarboxylation of 4'-phosphopantothenoyl-L-cysteine in the CoA biosynthesis pathway, which is classified under cofactor biosynthesis. This motif and the overall ~211-residue length with the characteristic fold are transferable features recognized in many PPCDC homologs. Option A (threonine synthase) is a PLP-dependent enzyme with different catalytic motifs (e.g., KXXXK for PLP binding). Option B (fatty acid beta-oxidation) involves acyl-CoA dehydrogenases/enoyl-CoA hydratases with entirely different sequence architecture. Option D (GAR synthase) belongs to a purine biosynthesis family with no resemblance to this sequence. The GDYGNG motif and family-level recognition of PPCDC meaningfully distinguish C from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GDYGNG motif is a conserved family-level signature shared across PPCDC enzymes in many organisms. Recognizing this motif as belonging to the PPCDC family (and thus CoA/cofactor biosynthesis) is legitimate transferable knowledge from homologous proteins, not a lookup of this specific soybean entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme families and pathways. The PPCDC family signature (GDYGNG motif, ~211 aa length, iron-dependent decarboxylase fold) clearly points to cofactor biosynthesis (CoA pathway) and does not overlap with threonine synthase, fatty acid beta-oxidation enzymes, or GAR synthase.


### Important caveats

- The UniProt pathway annotation is based on similarity transfer (ECO:0000250 from Q9SWE5) rather than direct experimental validation for this specific soybean protein.
- The PPCDC family is structurally related to aspartate decarboxylase, but the specific GDYGNG motif and pathway assignment to CoA biosynthesis (not amino acid biosynthesis) are well-established across the family.
- The protein was originally named 'Halotolerance protein 3a' (GmHAL3a) in some literature, reflecting its role in stress tolerance, but its enzymatic function is PPCDC in CoA biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GDYGNG' motif (near position ~190: 'RLACGDYGNGAMAEP'), which is a well-known family signature of phosphopantothenoylcysteine decarboxylase (PPCDC) enzymes across bacteria, fungi, and plants (e.g., E. coli CoaB, yeast Ppc1, Arabidopsis PPCDC). PPCDC catalyzes the decarboxylation of 4'-phosphopantothenoyl-L-cysteine in the CoA biosynthesis pathway, which is classified under cofactor biosynthesis. This motif and the overall ~211-residue length with the characteristic fold are transferable features recognized in many PPCDC homologs. Option A (threonine synthase) is a PLP-dependent enzyme with different catalytic motifs (e.g., KXXXK for PLP binding). Option B (fatty acid beta-oxidation) involves acyl-CoA dehydrogenases/enoyl-CoA hydratases with entirely different sequence architecture. Option D (GAR synthase) belongs to a purine biosynthesis family with no resemblance to this sequence. The GDYGNG motif and family-level recognition of PPCDC meaningfully distinguish C from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GDYGNG motif is a conserved family-level signature shared across PPCDC enzymes in many organisms. Recognizing this motif as belonging to the PPCDC family (and thus CoA/cofactor biosynthesis) is legitimate transferable knowledge from homologous proteins, not a lookup of this specific soybean entry's annotation."
  },
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 (HAL3A_SOYBN) is annotated as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36) with the pathway 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5.' This directly supports the expected answer C (Cofactor biosynthesis). The annotation is based on similarity transfer (ECO:0000250) from Q9SWE5, but the enzyme identity and pathway assignment are consistent with the well-characterized PPCDC family."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on similarity transfer (ECO:0000250 from Q9SWE5) rather than direct experimental validation for this specific soybean protein.",
    "The PPCDC family is structurally related to aspartate decarboxylase, but the specific GDYGNG motif and pathway assignment to CoA biosynthesis (not amino acid biosynthesis) are well-established across the family.",
    "The protein was originally named 'Halotolerance protein 3a' (GmHAL3a) in some literature, reflecting its role in stress tolerance, but its enzymatic function is PPCDC in CoA biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme families and pathways. The PPCDC family signature (GDYGNG motif, ~211 aa length, iron-dependent decarboxylase fold) clearly points to cofactor biosynthesis (CoA pathway) and does not overlap with threonine synthase, fatty acid beta-oxidation enzymes, or GAR synthase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 (HAL3A_SOYBN) is annotated as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36) with the pathway 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5.' This directly supports the expected answer C (Cofactor biosynthesis). The annotation is based on similarity transfer (ECO:0000250) from Q9SWE5, but the enzyme identity and pathway assignment are consistent with the well-characterized PPCDC family.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GDYGNG' motif (near position ~190: 'RLACGDYGNGAMAEP'), which is a well-known family signature of phosphopantothenoylcysteine decarboxylase (PPCDC) enzymes across bacteria, fungi, and plants (e.g., E. coli CoaB, yeast Ppc1, Arabidopsis PPCDC). PPCDC catalyzes the decarboxylation of 4'-phosphopantothenoyl-L-cysteine in the CoA biosynthesis pathway, which is classified under cofactor biosynthesis. This motif and the overall ~211-residue length with the characteristic fold are transferable features recognized in many PPCDC homologs. Option A (threonine synthase) is a PLP-dependent enzyme with different catalytic motifs (e.g., KXXXK for PLP binding). Option B (fatty acid beta-oxidation) involves acyl-CoA dehydrogenases/enoyl-CoA hydratases with entirely different sequence architecture. Option D (GAR synthase) belongs to a purine biosynthesis family with no resemblance to this sequence. The GDYGNG motif and family-level recognition of PPCDC meaningfully distinguish C from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The GDYGNG motif is a conserved family-level signature shared across PPCDC enzymes in many organisms. Recognizing this motif as belonging to the PPCDC family (and thus CoA/cofactor biosynthesis) is legitimate transferable knowledge from homologous proteins, not a lookup of this specific soybean entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme families and pathways. The PPCDC family signature (GDYGNG motif, ~211 aa length, iron-dependent decarboxylase fold) clearly points to cofactor biosynthesis (CoA pathway) and does not overlap with threonine synthase, fatty acid beta-oxidation enzymes, or GAR synthase."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on similarity transfer (ECO:0000250 from Q9SWE5) rather than direct experimental validation for this specific soybean protein.",
    "The PPCDC family is structurally related to aspartate decarboxylase, but the specific GDYGNG motif and pathway assignment to CoA biosynthesis (not amino acid biosynthesis) are well-established across the family.",
    "The protein was originally named 'Halotolerance protein 3a' (GmHAL3a) in some literature, reflecting its role in stress tolerance, but its enzymatic function is PPCDC in CoA biosynthesis."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-\nCC       pantothenate: step 3/5. {ECO:0000250|UniProtKB:Q9SWE5}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
