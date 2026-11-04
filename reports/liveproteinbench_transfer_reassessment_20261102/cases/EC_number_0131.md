# EC_number_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0131.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.1.1.128

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. 4.1.1.36
B. 5.6.1.1
C. 4.1.1.128
D. 1.14.14.154
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

> The sequence matches the cited UniProt entry, whose EC 4.1.1.128 annotation and catalytic reaction are supported there by experimental-evidence codes citing PubMed 20529859. This supports the key for the supplied sequence, though the paper itself was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a glycine-rich dinucleotide-binding motif (ITGGAGF...), consistent with an NAD-dependent nucleotide-sugar enzyme. Transferable knowledge of this enzyme family supports a nucleotide-sugar decarboxylase over the isomerase and monooxygenase choices, and makes the offered UDP-sugar decarboxylase EC 4.1.1.128 a credible best match. This is a family-level inference, not a definitive sequence-only proof of substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable cofactor-binding feature and the associated nucleotide-sugar enzyme family provide a meaningful basis for choosing among the offered reaction classes without relying on the target's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference favors C among the supplied options; no second option is comparably supported.


### Important caveats

- The Rossmann-like motif supports an enzyme-family inference but does not alone establish the exact substrate or EC number.
- Reviewer-only source evidence supports the key but was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a glycine-rich dinucleotide-binding motif (ITGGAGF...), consistent with an NAD-dependent nucleotide-sugar enzyme. Transferable knowledge of this enzyme family supports a nucleotide-sugar decarboxylase over the isomerase and monooxygenase choices, and makes the offered UDP-sugar decarboxylase EC 4.1.1.128 a credible best match. This is a family-level inference, not a definitive sequence-only proof of substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable cofactor-binding feature and the associated nucleotide-sugar enzyme family provide a meaningful basis for choosing among the offered reaction classes without relying on the target's recorded annotation."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, whose EC 4.1.1.128 annotation and catalytic reaction are supported there by experimental-evidence codes citing PubMed 20529859. This supports the key for the supplied sequence, though the paper itself was not independently reviewed here."
  },
  "important_caveats": [
    "The Rossmann-like motif supports an enzyme-family inference but does not alone establish the exact substrate or EC number.",
    "Reviewer-only source evidence supports the key but was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors C among the supplied options; no second option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, whose EC 4.1.1.128 annotation and catalytic reaction are supported there by experimental-evidence codes citing PubMed 20529859. This supports the key for the supplied sequence, though the paper itself was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a glycine-rich dinucleotide-binding motif (ITGGAGF...), consistent with an NAD-dependent nucleotide-sugar enzyme. Transferable knowledge of this enzyme family supports a nucleotide-sugar decarboxylase over the isomerase and monooxygenase choices, and makes the offered UDP-sugar decarboxylase EC 4.1.1.128 a credible best match. This is a family-level inference, not a definitive sequence-only proof of substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable cofactor-binding feature and the associated nucleotide-sugar enzyme family provide a meaningful basis for choosing among the offered reaction classes without relying on the target's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors C among the supplied options; no second option is comparably supported."
  },
  "important_caveats": [
    "The Rossmann-like motif supports an enzyme-family inference but does not alone establish the exact substrate or EC number.",
    "Reviewer-only source evidence supports the key but was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms UniProt entry A7GKX7 (UXNAS_BACCN) with sequence match (321 aa, SHA256 matched). The EC number 4.1.1.128 is annotated with experimental evidence (ECO:0000269, PubMed:20529859, Gu et al. 2010 JBC). The catalytic reaction is UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ = UDP-N-acetyl-alpha-D-xylosamine + CO2, confirmed by Rhea cross-reference. The sequence comparison is 'matched' for both current and historical records.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The Rossmann-fold motif 'GGAGFIGS' at the N-terminus indicates a nucleotide-binding fold, which reasonably eliminates option D (1.14.14.154, a cytochrome P450 monooxygenase with a completely different heme-binding fold) and option B (5.6.1.1, an isomerase category not associated with Rossmann folds). This narrows the choice to A (4.1.1.36, UDP-glucuronate decarboxylase) or C (4.1.1.128, UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase). Both are carboxy-lyases (EC 4.1.1.x) acting on UDP-sugar acids, potentially sharing similar overall folds and UDP-binding motifs. The critical distinction—whether the enzyme accommodates an N-acetyl group on C2 of the sugar (4.1.1.128) or acts on unsubstituted UDP-glucuronate (4.1.1.36)—is a subtle active-site specificity difference not discernible from the sequence alone. No obvious sequence motif in the provided 321-aa sequence specifically encodes N-acetyl recognition versus its absence.


**Missing item-specific fact**

> The specific substrate-binding active-site residues that distinguish UDP-glucuronate decarboxylase (4.1.1.36) from UDP-N-acetyl-glucosaminuronate decarboxylase (4.1.1.128), or the taxonomic/family context (Bacillus cytotoxicus, characterized in 2010) that identifies this particular enzyme as the N-acetyl-accepting variant rather than the classical UDP-glucuronate decarboxylase.


**Reason**

> While the Rossmann fold and decarboxylase character allow elimination of B and D, the remaining choice between A and C requires knowledge of the precise substrate specificity of these two closely related UDP-sugar acid decarboxylases. Both catalyze decarboxylation of UDP-linked sugar acids, likely share structural folds, and differ only in the presence/absence of an N-acetyl substituent on the substrate. No transferable family-level sequence feature in the provided input meaningfully distinguishes the N-acetyl-accepting variant (C) from the non-acetylated substrate variant (A) without recalling the specific annotation or experimental characterization of this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (4.1.1.36) and C (4.1.1.128) are UDP-sugar acid decarboxylases (EC 4.1.1.x) that could plausibly share a Rossmann-like nucleotide-binding fold. From the sequence alone, without specific knowledge of the N-acetyl substrate recognition, both remain viable. The distinction is subtle and not resolvable by general family-level inference.


### Important caveats

- The EC 4.1.1.128 annotation is based on experimental evidence (ECO:0000269, PubMed:20529859), not computational prediction.
- EC 4.1.1.128 was established relatively recently (2010 characterization), making it less likely to be encoded in a model's training data compared to the more established 4.1.1.36.
- The Rossmann fold 'GGAGFIGS' in a decarboxylase context is somewhat unusual and could in principle be used to argue against a classical dehydrogenase-like 4.1.1.36 if one knew that plant UGDs lack this specific fold variant, but this is very specific knowledge.
- Option B (5.6.1.1) appears to be an unusual or possibly non-standard EC number, serving as an easy distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Rossmann-fold motif 'GGAGFIGS' at the N-terminus indicates a nucleotide-binding fold, which reasonably eliminates option D (1.14.14.154, a cytochrome P450 monooxygenase with a completely different heme-binding fold) and option B (5.6.1.1, an isomerase category not associated with Rossmann folds). This narrows the choice to A (4.1.1.36, UDP-glucuronate decarboxylase) or C (4.1.1.128, UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase). Both are carboxy-lyases (EC 4.1.1.x) acting on UDP-sugar acids, potentially sharing similar overall folds and UDP-binding motifs. The critical distinction—whether the enzyme accommodates an N-acetyl group on C2 of the sugar (4.1.1.128) or acts on unsubstituted UDP-glucuronate (4.1.1.36)—is a subtle active-site specificity difference not discernible from the sequence alone. No obvious sequence motif in the provided 321-aa sequence specifically encodes N-acetyl recognition versus its absence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding active-site residues that distinguish UDP-glucuronate decarboxylase (4.1.1.36) from UDP-N-acetyl-glucosaminuronate decarboxylase (4.1.1.128), or the taxonomic/family context (Bacillus cytotoxicus, characterized in 2010) that identifies this particular enzyme as the N-acetyl-accepting variant rather than the classical UDP-glucuronate decarboxylase.",
    "reason": "While the Rossmann fold and decarboxylase character allow elimination of B and D, the remaining choice between A and C requires knowledge of the precise substrate specificity of these two closely related UDP-sugar acid decarboxylases. Both catalyze decarboxylation of UDP-linked sugar acids, likely share structural folds, and differ only in the presence/absence of an N-acetyl substituent on the substrate. No transferable family-level sequence feature in the provided input meaningfully distinguishes the N-acetyl-accepting variant (C) from the non-acetylated substrate variant (A) without recalling the specific annotation or experimental characterization of this protein."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms UniProt entry A7GKX7 (UXNAS_BACCN) with sequence match (321 aa, SHA256 matched). The EC number 4.1.1.128 is annotated with experimental evidence (ECO:0000269, PubMed:20529859, Gu et al. 2010 JBC). The catalytic reaction is UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ = UDP-N-acetyl-alpha-D-xylosamine + CO2, confirmed by Rhea cross-reference. The sequence comparison is 'matched' for both current and historical records."
  },
  "important_caveats": [
    "The EC 4.1.1.128 annotation is based on experimental evidence (ECO:0000269, PubMed:20529859), not computational prediction.",
    "EC 4.1.1.128 was established relatively recently (2010 characterization), making it less likely to be encoded in a model's training data compared to the more established 4.1.1.36.",
    "The Rossmann fold 'GGAGFIGS' in a decarboxylase context is somewhat unusual and could in principle be used to argue against a classical dehydrogenase-like 4.1.1.36 if one knew that plant UGDs lack this specific fold variant, but this is very specific knowledge.",
    "Option B (5.6.1.1) appears to be an unusual or possibly non-standard EC number, serving as an easy distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) are UDP-sugar acid decarboxylases (EC 4.1.1.x) that could plausibly share a Rossmann-like nucleotide-binding fold. From the sequence alone, without specific knowledge of the N-acetyl substrate recognition, both remain viable. The distinction is subtle and not resolvable by general family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms UniProt entry A7GKX7 (UXNAS_BACCN) with sequence match (321 aa, SHA256 matched). The EC number 4.1.1.128 is annotated with experimental evidence (ECO:0000269, PubMed:20529859, Gu et al. 2010 JBC). The catalytic reaction is UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ = UDP-N-acetyl-alpha-D-xylosamine + CO2, confirmed by Rhea cross-reference. The sequence comparison is 'matched' for both current and historical records.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The Rossmann-fold motif 'GGAGFIGS' at the N-terminus indicates a nucleotide-binding fold, which reasonably eliminates option D (1.14.14.154, a cytochrome P450 monooxygenase with a completely different heme-binding fold) and option B (5.6.1.1, an isomerase category not associated with Rossmann folds). This narrows the choice to A (4.1.1.36, UDP-glucuronate decarboxylase) or C (4.1.1.128, UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase). Both are carboxy-lyases (EC 4.1.1.x) acting on UDP-sugar acids, potentially sharing similar overall folds and UDP-binding motifs. The critical distinction—whether the enzyme accommodates an N-acetyl group on C2 of the sugar (4.1.1.128) or acts on unsubstituted UDP-glucuronate (4.1.1.36)—is a subtle active-site specificity difference not discernible from the sequence alone. No obvious sequence motif in the provided 321-aa sequence specifically encodes N-acetyl recognition versus its absence.",
    "missing_item_specific_fact": "The specific substrate-binding active-site residues that distinguish UDP-glucuronate decarboxylase (4.1.1.36) from UDP-N-acetyl-glucosaminuronate decarboxylase (4.1.1.128), or the taxonomic/family context (Bacillus cytotoxicus, characterized in 2010) that identifies this particular enzyme as the N-acetyl-accepting variant rather than the classical UDP-glucuronate decarboxylase.",
    "reason": "While the Rossmann fold and decarboxylase character allow elimination of B and D, the remaining choice between A and C requires knowledge of the precise substrate specificity of these two closely related UDP-sugar acid decarboxylases. Both catalyze decarboxylation of UDP-linked sugar acids, likely share structural folds, and differ only in the presence/absence of an N-acetyl substituent on the substrate. No transferable family-level sequence feature in the provided input meaningfully distinguishes the N-acetyl-accepting variant (C) from the non-acetylated substrate variant (A) without recalling the specific annotation or experimental characterization of this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) are UDP-sugar acid decarboxylases (EC 4.1.1.x) that could plausibly share a Rossmann-like nucleotide-binding fold. From the sequence alone, without specific knowledge of the N-acetyl substrate recognition, both remain viable. The distinction is subtle and not resolvable by general family-level inference."
  },
  "important_caveats": [
    "The EC 4.1.1.128 annotation is based on experimental evidence (ECO:0000269, PubMed:20529859), not computational prediction.",
    "EC 4.1.1.128 was established relatively recently (2010 characterization), making it less likely to be encoded in a model's training data compared to the more established 4.1.1.36.",
    "The Rossmann fold 'GGAGFIGS' in a decarboxylase context is somewhat unusual and could in principle be used to argue against a classical dehydrogenase-like 4.1.1.36 if one knew that plant UGDs lack this specific fold variant, but this is very specific knowledge.",
    "Option B (5.6.1.1) appears to be an unusual or possibly non-standard EC number, serving as an easy distractor."
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
  "benchmark_sequence_length": 321,
  "benchmark_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_entry_audit": {
    "entryVersion": 96,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 321,
  "current_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 94,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7GKX7",
  "selected_historical_entry_version": 94,
  "selected_historical_record_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "selected_historical_source_sequence_length": 321,
  "selected_historical_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "selected_historical_version": {
    "accession": "A7GKX7",
    "database": "Swiss-Prot",
    "entryVersion": 94,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UXNAS_BACCN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7GKX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":96,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-XylNAc synthase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.128\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAcA decarboxylase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81488\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.128\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"name\":\"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81487\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231888\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43880.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H1",
  "excerpt": "ID   UXNAS_BACCN             Reviewed;         321 AA.\nAC   A7GKX7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 94.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};\nDE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};\nDE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};\nDE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};\nGN   Name=UXNAcS {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0430 {ECO:0000312|EMBL:ABS20785.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};\nDE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};\nDE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};\nDE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43880.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-\nCC         acetyl-alpha-D-xylosamine + CO2; Xref=Rhea:RHEA:81487,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:65040,\nCC         ChEBI:CHEBI:231888; EC=4.1.1.128;\nCC         Evidence={ECO:0000269|PubMed:20529859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81488;\nCC         Evidence={ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
