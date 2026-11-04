# EC_number_0126

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0126.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAGVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPQPWLTPLVVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTAAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. 3.2.1.8
B. 3.2.1.20
C. 4.1.1.36
D. 4.2.3.1
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

> The sequence-matched UniProt entry assigns EC 3.2.1.8 and specifies endohydrolysis of beta-1,4-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the following aromatic-rich catalytic region is compatible with a fungal glycoside hydrolase, particularly an endo-xylanase. Transferable recognition of fungal xylanase sequence-family patterns supports EC 3.2.1.8 (A) over the other choices, which describe different hydrolase or lyase activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence meaningfully distinguishes the xylanase option without requiring the exact protein's database record. It is a sequence-based prediction, not proof of the precise substrate activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered EC numbers, 3.2.1.8 is the clearly compatible choice; the alternatives represent distinct reaction classes or substrate specificities.


### Important caveats

- The cited EC assignment is computationally supported by a PROSITE-ProRule; the excerpts do not establish direct experimental characterization of this exact protein's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the following aromatic-rich catalytic region is compatible with a fungal glycoside hydrolase, particularly an endo-xylanase. Transferable recognition of fungal xylanase sequence-family patterns supports EC 3.2.1.8 (A) over the other choices, which describe different hydrolase or lyase activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully distinguishes the xylanase option without requiring the exact protein's database record. It is a sequence-based prediction, not proof of the precise substrate activity."
  },
  "case_id": "EC_number_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.8 and specifies endohydrolysis of beta-1,4-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The cited EC assignment is computationally supported by a PROSITE-ProRule; the excerpts do not establish direct experimental characterization of this exact protein's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered EC numbers, 3.2.1.8 is the clearly compatible choice; the alternatives represent distinct reaction classes or substrate specificities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.8 and specifies endohydrolysis of beta-1,4-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the following aromatic-rich catalytic region is compatible with a fungal glycoside hydrolase, particularly an endo-xylanase. Transferable recognition of fungal xylanase sequence-family patterns supports EC 3.2.1.8 (A) over the other choices, which describe different hydrolase or lyase activities.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully distinguishes the xylanase option without requiring the exact protein's database record. It is a sequence-based prediction, not proof of the precise substrate activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered EC numbers, 3.2.1.8 is the clearly compatible choice; the alternatives represent distinct reaction classes or substrate specificities."
  },
  "important_caveats": [
    "The cited EC assignment is computationally supported by a PROSITE-ProRule; the excerpts do not establish direct experimental characterization of this exact protein's catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X8M4 (EIX3_VERDV) is annotated as EC 3.2.1.8 (Endo-1,4-beta-xylanase) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating a computational/pattern-based assignment to the GH10 xylanase family. The protein is named 'Ethylene-inducing xylanase 3' and 'Endo-1,4-beta-xylanase EIX3,' directly consistent with EC 3.2.1.8. The annotation is supported by a PubMed reference (33205907) documenting its function as an EIX-like protein from Verticillium dahliae.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains well-established GH10 (glycoside hydrolase family 10) xylanase motifs. The region 'WTRNPQPWLTPLVVEYYVVENFGTYNP' contains the conserved Trp and Glu residues characteristic of the GH10 acid/base catalytic machinery, and 'GALYRLFESTRTNQ' contains the conserved Glu nucleophile of GH10. These motifs are distinct from GH13 (alpha-amylase, EC 3.2.1.20) catalytic signatures, which use an Asn-Glu acid/base pair and an Asp nucleophile in different structural contexts. The N-terminal signal peptide (MVCFSSLFVAASAIAGVFASPVD...) indicates secretion, consistent with extracellular xylan-degrading enzymes. Options C (pyruvate decarboxylase, TPP-dependent) and D (terpene synthase, DDXXD motif) are lyases with entirely different folds and sequence signatures, easily excluded. The EIX (Ethylene-Inducing Xylanase) protein family in fungal pathogens is well-characterized as GH10 xylanases, a family-level fact transferable from related proteins like Fusarium EIX1/EIX2.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH10 family catalytic motifs (conserved Trp, Glu acid/base, Glu nucleophile in specific sequence contexts) are generalizable knowledge about glycoside hydrolases, not specific to this one protein. The distinction between GH10 xylanase (A) and GH13 alpha-amylase (B) rests on well-characterized family-specific sequence signatures visible in the input. Options C and D are trivially excluded as lyases. The EIX family association with GH10 xylanases is a transferable family-level fact learned from other fungal elicitor proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (4.1.1.36) and D (4.2.3.1) are lyases with completely different catalytic mechanisms and structural folds, easily excluded from a secreted glycoside hydrolase sequence. The distinction between A (3.2.1.8, GH10) and B (3.2.1.20, GH13 alpha-amylase) is resolved by the GH10-specific catalytic motifs present in the sequence. No genuine ambiguity exists among the offered choices.


### Important caveats

- The EC annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental enzymatic assay of xylan hydrolysis. However, the protein name and family assignment are corroborated by the PubMed reference.
- The EIX protein family is specialized (fungal elicitors with xylanase activity); while the GH10 motifs are generalizable, recognizing the EIX family specifically adds confidence but is not strictly necessary for the answer.
- The sequence is a precursor (signal peptide included); the mature GH10 domain begins after the signal peptide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains well-established GH10 (glycoside hydrolase family 10) xylanase motifs. The region 'WTRNPQPWLTPLVVEYYVVENFGTYNP' contains the conserved Trp and Glu residues characteristic of the GH10 acid/base catalytic machinery, and 'GALYRLFESTRTNQ' contains the conserved Glu nucleophile of GH10. These motifs are distinct from GH13 (alpha-amylase, EC 3.2.1.20) catalytic signatures, which use an Asn-Glu acid/base pair and an Asp nucleophile in different structural contexts. The N-terminal signal peptide (MVCFSSLFVAASAIAGVFASPVD...) indicates secretion, consistent with extracellular xylan-degrading enzymes. Options C (pyruvate decarboxylase, TPP-dependent) and D (terpene synthase, DDXXD motif) are lyases with entirely different folds and sequence signatures, easily excluded. The EIX (Ethylene-Inducing Xylanase) protein family in fungal pathogens is well-characterized as GH10 xylanases, a family-level fact transferable from related proteins like Fusarium EIX1/EIX2.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH10 family catalytic motifs (conserved Trp, Glu acid/base, Glu nucleophile in specific sequence contexts) are generalizable knowledge about glycoside hydrolases, not specific to this one protein. The distinction between GH10 xylanase (A) and GH13 alpha-amylase (B) rests on well-characterized family-specific sequence signatures visible in the input. Options C and D are trivially excluded as lyases. The EIX family association with GH10 xylanases is a transferable family-level fact learned from other fungal elicitor proteins."
  },
  "case_id": "EC_number_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X8M4 (EIX3_VERDV) is annotated as EC 3.2.1.8 (Endo-1,4-beta-xylanase) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating a computational/pattern-based assignment to the GH10 xylanase family. The protein is named 'Ethylene-inducing xylanase 3' and 'Endo-1,4-beta-xylanase EIX3,' directly consistent with EC 3.2.1.8. The annotation is supported by a PubMed reference (33205907) documenting its function as an EIX-like protein from Verticillium dahliae."
  },
  "important_caveats": [
    "The EC annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental enzymatic assay of xylan hydrolysis. However, the protein name and family assignment are corroborated by the PubMed reference.",
    "The EIX protein family is specialized (fungal elicitors with xylanase activity); while the GH10 motifs are generalizable, recognizing the EIX family specifically adds confidence but is not strictly necessary for the answer.",
    "The sequence is a precursor (signal peptide included); the mature GH10 domain begins after the signal peptide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (4.1.1.36) and D (4.2.3.1) are lyases with completely different catalytic mechanisms and structural folds, easily excluded from a secreted glycoside hydrolase sequence. The distinction between A (3.2.1.8, GH10) and B (3.2.1.20, GH13 alpha-amylase) is resolved by the GH10-specific catalytic motifs present in the sequence. No genuine ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X8M4 (EIX3_VERDV) is annotated as EC 3.2.1.8 (Endo-1,4-beta-xylanase) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating a computational/pattern-based assignment to the GH10 xylanase family. The protein is named 'Ethylene-inducing xylanase 3' and 'Endo-1,4-beta-xylanase EIX3,' directly consistent with EC 3.2.1.8. The annotation is supported by a PubMed reference (33205907) documenting its function as an EIX-like protein from Verticillium dahliae.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains well-established GH10 (glycoside hydrolase family 10) xylanase motifs. The region 'WTRNPQPWLTPLVVEYYVVENFGTYNP' contains the conserved Trp and Glu residues characteristic of the GH10 acid/base catalytic machinery, and 'GALYRLFESTRTNQ' contains the conserved Glu nucleophile of GH10. These motifs are distinct from GH13 (alpha-amylase, EC 3.2.1.20) catalytic signatures, which use an Asn-Glu acid/base pair and an Asp nucleophile in different structural contexts. The N-terminal signal peptide (MVCFSSLFVAASAIAGVFASPVD...) indicates secretion, consistent with extracellular xylan-degrading enzymes. Options C (pyruvate decarboxylase, TPP-dependent) and D (terpene synthase, DDXXD motif) are lyases with entirely different folds and sequence signatures, easily excluded. The EIX (Ethylene-Inducing Xylanase) protein family in fungal pathogens is well-characterized as GH10 xylanases, a family-level fact transferable from related proteins like Fusarium EIX1/EIX2.",
    "missing_item_specific_fact": "",
    "reason": "The GH10 family catalytic motifs (conserved Trp, Glu acid/base, Glu nucleophile in specific sequence contexts) are generalizable knowledge about glycoside hydrolases, not specific to this one protein. The distinction between GH10 xylanase (A) and GH13 alpha-amylase (B) rests on well-characterized family-specific sequence signatures visible in the input. Options C and D are trivially excluded as lyases. The EIX family association with GH10 xylanases is a transferable family-level fact learned from other fungal elicitor proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (4.1.1.36) and D (4.2.3.1) are lyases with completely different catalytic mechanisms and structural folds, easily excluded from a secreted glycoside hydrolase sequence. The distinction between A (3.2.1.8, GH10) and B (3.2.1.20, GH13 alpha-amylase) is resolved by the GH10-specific catalytic motifs present in the sequence. No genuine ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The EC annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental enzymatic assay of xylan hydrolysis. However, the protein name and family assignment are corroborated by the PubMed reference.",
    "The EIX protein family is specialized (fungal elicitors with xylanase activity); while the GH10 motifs are generalizable, recognizing the EIX family specifically adds confidence but is not strictly necessary for the answer.",
    "The sequence is a precursor (signal peptide included); the mature GH10 domain begins after the signal peptide."
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
  "benchmark_sequence_length": 294,
  "benchmark_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 294,
  "current_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 61,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X8M4",
  "selected_historical_entry_version": 61,
  "selected_historical_record_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "selected_historical_source_sequence_length": 294,
  "selected_historical_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "selected_historical_version": {
    "accession": "G2X8M4",
    "database": "Swiss-Prot",
    "entryVersion": 61,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX3_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X8M4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX3\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H1",
  "excerpt": "ID   EIX3_VERDV              Reviewed;         294 AA.\nAC   G2X8M4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 61.\nDE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_06165;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
