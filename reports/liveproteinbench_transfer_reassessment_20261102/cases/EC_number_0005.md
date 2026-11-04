# EC_number_0005

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0005.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.1.1.440

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKQVQMPEVELNSDHKMPLVGFGTCIPDPIPPLEELATIFLEVIKVGYRHFDTASCYGTEEALGKAVAQAIESGLVNGREEFFITSKLWVEDADQDLILPALKKTLGNLGLDYLDLYLIHMPLRLRQGAEMFKYTKEDFLPFDIKGTWKAMEECSKLGLCKSIGVSNYSCEKLSKLLENATILPAVNQVEMNVVWKQSKLLPFCKEKNIHVSAWSPLLSYGSIWSQNAVMENTVLVDIAASKSKTVAQVALRWIYEQGASFIMRTFNKERMYQNVQIFDWELTQEELDQIQQIPQRRSNLAEAFVHPEGPIKSVEELWDGDL

[Multiple Choices]
A. 1.1.1.440
B. 1.1.1.195
C. 2.7.11.24
D. 1.14.15.9
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

> The sequence-matched UniProt record assigns EC 1.1.1.440 and reports the corresponding rhazimol/rhazimal reaction with ECO:0000269 evidence linked to a publication. This supports choice A, though the evidence here is a database report of experimental evidence rather than an independent review of the paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an oxidoreductase, which makes the EC 1.1.1 options more plausible than the kinase or monooxygenase alternatives. But A and B differ in reaction specificity within that broad class; no substrate, reaction context, or distinctive family-level clue in the input meaningfully separates them.


**Missing item-specific fact**

> The protein's substrate and reaction specificity, or a target-specific functional annotation establishing it.


**Reason**

> Transferable sequence and enzyme-class knowledge can narrow the choices, but does not identify which of the two oxidoreductase EC numbers applies. The exact reaction assignment is supplied by evidence about this protein, not by a sufficiently discriminating feature in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the sequence alone, both offered EC 1.1.1 choices remain plausible at the broad oxidoreductase-class level; the input does not specify the substrate-dependent reaction that distinguishes them.


### Important caveats

- The reviewer-only evidence identifies the exact sequence and supports A, but that target-specific annotation was not part of the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an oxidoreductase, which makes the EC 1.1.1 options more plausible than the kinase or monooxygenase alternatives. But A and B differ in reaction specificity within that broad class; no substrate, reaction context, or distinctive family-level clue in the input meaningfully separates them.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate and reaction specificity, or a target-specific functional annotation establishing it.",
    "reason": "Transferable sequence and enzyme-class knowledge can narrow the choices, but does not identify which of the two oxidoreductase EC numbers applies. The exact reaction assignment is supplied by evidence about this protein, not by a sufficiently discriminating feature in the original input."
  },
  "case_id": "EC_number_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.1.1.440 and reports the corresponding rhazimol/rhazimal reaction with ECO:0000269 evidence linked to a publication. This supports choice A, though the evidence here is a database report of experimental evidence rather than an independent review of the paper."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the exact sequence and supports A, but that target-specific annotation was not part of the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the sequence alone, both offered EC 1.1.1 choices remain plausible at the broad oxidoreductase-class level; the input does not specify the substrate-dependent reaction that distinguishes them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.1.1.440 and reports the corresponding rhazimol/rhazimal reaction with ECO:0000269 evidence linked to a publication. This supports choice A, though the evidence here is a database report of experimental evidence rather than an independent review of the paper.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an oxidoreductase, which makes the EC 1.1.1 options more plausible than the kinase or monooxygenase alternatives. But A and B differ in reaction specificity within that broad class; no substrate, reaction context, or distinctive family-level clue in the input meaningfully separates them.",
    "missing_item_specific_fact": "The protein's substrate and reaction specificity, or a target-specific functional annotation establishing it.",
    "reason": "Transferable sequence and enzyme-class knowledge can narrow the choices, but does not identify which of the two oxidoreductase EC numbers applies. The exact reaction assignment is supplied by evidence about this protein, not by a sufficiently discriminating feature in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the sequence alone, both offered EC 1.1.1 choices remain plausible at the broad oxidoreductase-class level; the input does not specify the substrate-dependent reaction that distinguishes them."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the exact sequence and supports A, but that target-specific annotation was not part of the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S5B9 (Rhazimal reductase 2, AsRHR2) from Alstonia scholaris is annotated with EC 1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci. 13:12389-12395). The catalytic reaction is rhazimol + NADP(+) = rhazimal + NADPH + 2H(+). The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed). The expected answer A (1.1.1.440) is directly supported by experimental characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model can reasonably rule out C (2.7.11.24, protein kinase) because the sequence lacks canonical kinase motifs (VAIK, HRD, DFG) and has an oxidoreductase-like architecture. D (1.14.15.9, dopamine beta-monooxygenase) can be ruled out because DBM is a much larger (~550 aa) copper-dependent enzyme with specific Cu-binding motifs absent here. However, distinguishing A (1.1.1.440, rhazimal reductase) from B (1.1.1.195, dihydroxy-acid oxidoreductase) requires knowing the specific substrate. Both are oxidoreductases acting on CH-OH with NAD(P)+. The sequence lacks a canonical SDR TGxxxGG + YxxxK catalytic tetrad, which might weakly argue against a typical SDR-type dihydroxy-acid oxidoreductase, but EC 1.1.1.195 is not restricted to SDRs. The 4th EC digit encodes substrate specificity (rhazimal vs. 2-hydroxy acids), which cannot be reliably inferred from sequence alone for this recently characterized (2022) plant alkaloid biosynthesis enzyme without knowing the exact protein or its close pathway homologs.


**Missing item-specific fact**

> The specific substrate identity (rhazimal, a monoterpene indole alkaloid intermediate) and the enzyme's membership in the MIA biosynthesis reductase family of Apocynaceae plants. This is a fact about this exact protein's recently experimentally determined catalytic specificity (PubMed:36349266, 2022) that is not derivable from general enzyme family knowledge or sequence motifs alone.


**Reason**

> While C and D can be excluded by general structural knowledge (absence of kinase motifs, absence of DBM copper-binding features), the critical A vs B distinction requires knowledge of the specific substrate (rhazimal) for EC 1.1.1.440. This enzyme was characterized in 2022 and is specific to a narrow plant alkaloid pathway. No well-established transferable family-level pattern reliably predicts the 4th EC digit for this sequence against 1.1.1.195. The weak argument against a typical SDR fold does not positively identify 1.1.1.440 over 1.1.1.195, since the latter is not restricted to SDRs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (1.1.1.440) and B (1.1.1.195) are oxidoreductases acting on CH-OH group with NAD(P)+ as acceptor (same first three EC digits). Without knowledge of the specific substrate or pathway context, a model cannot confidently distinguish the 4th digit. The sequence does not contain a unique motif that unambiguously identifies rhazimal reductase over dihydroxy-acid oxidoreductase.


### Important caveats

- Rhazimal reductase 2 was experimentally characterized in 2022 (Wang et al., Chem. Sci.) and is specific to monoterpene indole alkaloid biosynthesis in Apocynaceae. This is a very recent annotation unlikely to be well-represented in training data.
- The organism (Alstonia scholaris) and pathway context (MIA biosynthesis) are not provided to the model, removing the strongest contextual clue.
- The sequence lacks a canonical SDR TGxxxGG + YxxxK + NxxxN catalytic tetrad, which might weakly argue against a typical SDR-type dihydroxy-acid oxidoreductase, but this is not conclusive since EC 1.1.1.195 includes non-SDR members.
- The UniProt annotation carries experimental evidence code ECO:0000269 (assay), confirming the EC assignment is experimentally determined, not merely predicted.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can reasonably rule out C (2.7.11.24, protein kinase) because the sequence lacks canonical kinase motifs (VAIK, HRD, DFG) and has an oxidoreductase-like architecture. D (1.14.15.9, dopamine beta-monooxygenase) can be ruled out because DBM is a much larger (~550 aa) copper-dependent enzyme with specific Cu-binding motifs absent here. However, distinguishing A (1.1.1.440, rhazimal reductase) from B (1.1.1.195, dihydroxy-acid oxidoreductase) requires knowing the specific substrate. Both are oxidoreductases acting on CH-OH with NAD(P)+. The sequence lacks a canonical SDR TGxxxGG + YxxxK catalytic tetrad, which might weakly argue against a typical SDR-type dihydroxy-acid oxidoreductase, but EC 1.1.1.195 is not restricted to SDRs. The 4th EC digit encodes substrate specificity (rhazimal vs. 2-hydroxy acids), which cannot be reliably inferred from sequence alone for this recently characterized (2022) plant alkaloid biosynthesis enzyme without knowing the exact protein or its close pathway homologs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (rhazimal, a monoterpene indole alkaloid intermediate) and the enzyme's membership in the MIA biosynthesis reductase family of Apocynaceae plants. This is a fact about this exact protein's recently experimentally determined catalytic specificity (PubMed:36349266, 2022) that is not derivable from general enzyme family knowledge or sequence motifs alone.",
    "reason": "While C and D can be excluded by general structural knowledge (absence of kinase motifs, absence of DBM copper-binding features), the critical A vs B distinction requires knowledge of the specific substrate (rhazimal) for EC 1.1.1.440. This enzyme was characterized in 2022 and is specific to a narrow plant alkaloid pathway. No well-established transferable family-level pattern reliably predicts the 4th EC digit for this sequence against 1.1.1.195. The weak argument against a typical SDR fold does not positively identify 1.1.1.440 over 1.1.1.195, since the latter is not restricted to SDRs."
  },
  "case_id": "EC_number_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S5B9 (Rhazimal reductase 2, AsRHR2) from Alstonia scholaris is annotated with EC 1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci. 13:12389-12395). The catalytic reaction is rhazimol + NADP(+) = rhazimal + NADPH + 2H(+). The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed). The expected answer A (1.1.1.440) is directly supported by experimental characterization."
  },
  "important_caveats": [
    "Rhazimal reductase 2 was experimentally characterized in 2022 (Wang et al., Chem. Sci.) and is specific to monoterpene indole alkaloid biosynthesis in Apocynaceae. This is a very recent annotation unlikely to be well-represented in training data.",
    "The organism (Alstonia scholaris) and pathway context (MIA biosynthesis) are not provided to the model, removing the strongest contextual clue.",
    "The sequence lacks a canonical SDR TGxxxGG + YxxxK + NxxxN catalytic tetrad, which might weakly argue against a typical SDR-type dihydroxy-acid oxidoreductase, but this is not conclusive since EC 1.1.1.195 includes non-SDR members.",
    "The UniProt annotation carries experimental evidence code ECO:0000269 (assay), confirming the EC assignment is experimentally determined, not merely predicted."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (1.1.1.440) and B (1.1.1.195) are oxidoreductases acting on CH-OH group with NAD(P)+ as acceptor (same first three EC digits). Without knowledge of the specific substrate or pathway context, a model cannot confidently distinguish the 4th digit. The sequence does not contain a unique motif that unambiguously identifies rhazimal reductase over dihydroxy-acid oxidoreductase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S5B9 (Rhazimal reductase 2, AsRHR2) from Alstonia scholaris is annotated with EC 1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci. 13:12389-12395). The catalytic reaction is rhazimol + NADP(+) = rhazimal + NADPH + 2H(+). The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed). The expected answer A (1.1.1.440) is directly supported by experimental characterization.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model can reasonably rule out C (2.7.11.24, protein kinase) because the sequence lacks canonical kinase motifs (VAIK, HRD, DFG) and has an oxidoreductase-like architecture. D (1.14.15.9, dopamine beta-monooxygenase) can be ruled out because DBM is a much larger (~550 aa) copper-dependent enzyme with specific Cu-binding motifs absent here. However, distinguishing A (1.1.1.440, rhazimal reductase) from B (1.1.1.195, dihydroxy-acid oxidoreductase) requires knowing the specific substrate. Both are oxidoreductases acting on CH-OH with NAD(P)+. The sequence lacks a canonical SDR TGxxxGG + YxxxK catalytic tetrad, which might weakly argue against a typical SDR-type dihydroxy-acid oxidoreductase, but EC 1.1.1.195 is not restricted to SDRs. The 4th EC digit encodes substrate specificity (rhazimal vs. 2-hydroxy acids), which cannot be reliably inferred from sequence alone for this recently characterized (2022) plant alkaloid biosynthesis enzyme without knowing the exact protein or its close pathway homologs.",
    "missing_item_specific_fact": "The specific substrate identity (rhazimal, a monoterpene indole alkaloid intermediate) and the enzyme's membership in the MIA biosynthesis reductase family of Apocynaceae plants. This is a fact about this exact protein's recently experimentally determined catalytic specificity (PubMed:36349266, 2022) that is not derivable from general enzyme family knowledge or sequence motifs alone.",
    "reason": "While C and D can be excluded by general structural knowledge (absence of kinase motifs, absence of DBM copper-binding features), the critical A vs B distinction requires knowledge of the specific substrate (rhazimal) for EC 1.1.1.440. This enzyme was characterized in 2022 and is specific to a narrow plant alkaloid pathway. No well-established transferable family-level pattern reliably predicts the 4th EC digit for this sequence against 1.1.1.195. The weak argument against a typical SDR fold does not positively identify 1.1.1.440 over 1.1.1.195, since the latter is not restricted to SDRs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (1.1.1.440) and B (1.1.1.195) are oxidoreductases acting on CH-OH group with NAD(P)+ as acceptor (same first three EC digits). Without knowledge of the specific substrate or pathway context, a model cannot confidently distinguish the 4th digit. The sequence does not contain a unique motif that unambiguously identifies rhazimal reductase over dihydroxy-acid oxidoreductase."
  },
  "important_caveats": [
    "Rhazimal reductase 2 was experimentally characterized in 2022 (Wang et al., Chem. Sci.) and is specific to monoterpene indole alkaloid biosynthesis in Apocynaceae. This is a very recent annotation unlikely to be well-represented in training data.",
    "The organism (Alstonia scholaris) and pathway context (MIA biosynthesis) are not provided to the model, removing the strongest contextual clue.",
    "The sequence lacks a canonical SDR TGxxxGG + YxxxK + NxxxN catalytic tetrad, which might weakly argue against a typical SDR-type dihydroxy-acid oxidoreductase, but this is not conclusive since EC 1.1.1.195 includes non-SDR members.",
    "The UniProt annotation carries experimental evidence code ECO:0000269 (assay), confirming the EC assignment is experimentally determined, not merely predicted."
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
  "benchmark_sequence_length": 323,
  "benchmark_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 323,
  "current_source_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S5B9",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "selected_historical_source_sequence_length": 323,
  "selected_historical_source_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "selected_historical_version": {
    "accession": "A0A9E7S5B9",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RHR2_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S5B9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.440\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Rhazimal reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsRHR2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79617\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.440\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79615\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230473\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230474\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65386.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   RHR2_ALSSC              Reviewed;         323 AA.\nAC   A0A9E7S5B9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Rhazimal reductase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR2 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\nGN   Name=RHR2 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Rhazimal reductase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR2 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65386.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+);\nCC         Xref=Rhea:RHEA:79615, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:230473, ChEBI:CHEBI:230474;\nCC         EC=1.1.1.440; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79617;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
