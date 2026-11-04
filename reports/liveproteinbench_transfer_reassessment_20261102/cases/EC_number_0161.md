# EC_number_0161

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0161.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.5.1.15

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKIFGIVNITTDSFSDGGLYLDTDKAIEHALHLVEDGADVIDLGAASSNPDTTEVGVVEEIKRLKPVIKALKEKGISISVDTFKPEVQSFCIEQKVDFINDIQGFPYPEIYSGLAKSDCKLVLMHSVQRIGAATKVETNPEEVFTSMMEFFKERIAALVEAGVKRERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG

[Multiple Choices]
A. 2.5.1.56
B. 3.1.26.3
C. 5.3.1.8
D. 2.5.1.15
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

> The sequence-matched UniProt record reports EC 2.5.1.15 and a catalytic reaction consistent with dihydropteroate synthase. The reaction annotation cites experimental evidence, supporting choice D; the record also includes a computational annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 263-aa sequence is credibly recognizable by family-level sequence patterns and homology as a bacterial dihydropteroate synthase. That family catalyzes formation of dihydropteroate, corresponding to EC 2.5.1.15 (D). This distinguishes D from the nuclease and isomerase choices, and family-level homolog recognition distinguishes it from the other transferase option, A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can use transferable knowledge of dihydropteroate synthase homologs and their reaction classification to make a meaningful choice from the offered alternatives. This does not require access to the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a dihydropteroate synthase family assignment, and among these alternatives only D matches that enzyme's EC number.


### Important caveats

- The cited database record supports the key for the sequence-matched protein, but its EC annotation includes both computational and experimental evidence.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 263-aa sequence is credibly recognizable by family-level sequence patterns and homology as a bacterial dihydropteroate synthase. That family catalyzes formation of dihydropteroate, corresponding to EC 2.5.1.15 (D). This distinguishes D from the nuclease and isomerase choices, and family-level homolog recognition distinguishes it from the other transferase option, A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can use transferable knowledge of dihydropteroate synthase homologs and their reaction classification to make a meaningful choice from the offered alternatives. This does not require access to the exact protein's database record."
  },
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports EC 2.5.1.15 and a catalytic reaction consistent with dihydropteroate synthase. The reaction annotation cites experimental evidence, supporting choice D; the record also includes a computational annotation."
  },
  "important_caveats": [
    "The cited database record supports the key for the sequence-matched protein, but its EC annotation includes both computational and experimental evidence.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a dihydropteroate synthase family assignment, and among these alternatives only D matches that enzyme's EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports EC 2.5.1.15 and a catalytic reaction consistent with dihydropteroate synthase. The reaction annotation cites experimental evidence, supporting choice D; the record also includes a computational annotation.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 263-aa sequence is credibly recognizable by family-level sequence patterns and homology as a bacterial dihydropteroate synthase. That family catalyzes formation of dihydropteroate, corresponding to EC 2.5.1.15 (D). This distinguishes D from the nuclease and isomerase choices, and family-level homolog recognition distinguishes it from the other transferase option, A.",
    "missing_item_specific_fact": "",
    "reason": "A model can use transferable knowledge of dihydropteroate synthase homologs and their reaction classification to make a meaningful choice from the offered alternatives. This does not require access to the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a dihydropteroate synthase family assignment, and among these alternatives only D matches that enzyme's EC number."
  },
  "important_caveats": [
    "The cited database record supports the key for the sequence-matched protein, but its EC annotation includes both computational and experimental evidence.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C0HMD9 (sul3, DHP3_ECOLX) is annotated with EC 2.5.1.15 (dihydropteroate synthase type-3) supported by both RuleBase (ECO:0000255) and experimental evidence (ECO:0000269, PubMed 37419898, X-ray crystallography of PDB 7S2L/7S2M/8SCD). The catalytic activity reaction matches EC 2.5.1.15: (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate → 7,8-dihydropteroate + diphosphate. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 263-aa protein contains the 'DPGMGFF' motif (~position 200), a well-known conserved active-site signature of the dihydropteroate synthase (DHPS/folP/sul) family, which catalyzes pABA + DHPP → dihydropteroate (EC 2.5.1.15). The overall length (~263 aa) and alternating hydrophobic/polar TIM-barrel-like sequence pattern are consistent with DHPS family members. This eliminates EC 3.1.26.3 (RNase H, ~150 aa, acidic metal-binding residues, hydrolase class) and EC 5.3.1.8 (glucose-6-phosphate isomerase, ~440–550 aa, isomerase class) by both size and EC-class logic. Between the two remaining transferase options (2.5.1.56 vs 2.5.1.15), the DPGMG motif and TIM-barrel architecture are hallmark features of DHPS specifically, not of the obscure transferase assigned 2.5.1.56 (which lacks this motif and has a different fold/size). The sul-type sulfonamide-resistance DHPS variants (sul1/sul2/sul3) are a well-studied family sharing this motif with chromosomal folP.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the DPGMG active-site motif, the ~263-aa TIM-barrel length, and the transferase (EC 2) class to select DHPS (2.5.1.15) over the other options. The DHPS/sul family is extensively characterized in the literature and databases, making this a legitimate family-level inference rather than a lookup of this exact protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (2, 3, 5) and the two EC 2.5.1.x options differ in family-specific motifs and size. The DPGMG motif and TIM-barrel architecture uniquely point to DHPS among the given choices.


### Important caveats

- The sul3 gene product is a plasmid-borne DHPS variant; its annotation as EC 2.5.1.15 is supported by both computational (RuleBase) and experimental (X-ray crystallography, 2023 Nat. Commun.) evidence.
- EC 2.5.1.56 is a relatively obscure EC number; a model unfamiliar with its specific reaction might find it harder to exclude, but the DPGMG motif and size constraints still favor DHPS.
- The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical), but the model was not given the accession or organism name.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 263-aa protein contains the 'DPGMGFF' motif (~position 200), a well-known conserved active-site signature of the dihydropteroate synthase (DHPS/folP/sul) family, which catalyzes pABA + DHPP → dihydropteroate (EC 2.5.1.15). The overall length (~263 aa) and alternating hydrophobic/polar TIM-barrel-like sequence pattern are consistent with DHPS family members. This eliminates EC 3.1.26.3 (RNase H, ~150 aa, acidic metal-binding residues, hydrolase class) and EC 5.3.1.8 (glucose-6-phosphate isomerase, ~440–550 aa, isomerase class) by both size and EC-class logic. Between the two remaining transferase options (2.5.1.56 vs 2.5.1.15), the DPGMG motif and TIM-barrel architecture are hallmark features of DHPS specifically, not of the obscure transferase assigned 2.5.1.56 (which lacks this motif and has a different fold/size). The sul-type sulfonamide-resistance DHPS variants (sul1/sul2/sul3) are a well-studied family sharing this motif with chromosomal folP.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the DPGMG active-site motif, the ~263-aa TIM-barrel length, and the transferase (EC 2) class to select DHPS (2.5.1.15) over the other options. The DHPS/sul family is extensively characterized in the literature and databases, making this a legitimate family-level inference rather than a lookup of this exact protein's record."
  },
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 (sul3, DHP3_ECOLX) is annotated with EC 2.5.1.15 (dihydropteroate synthase type-3) supported by both RuleBase (ECO:0000255) and experimental evidence (ECO:0000269, PubMed 37419898, X-ray crystallography of PDB 7S2L/7S2M/8SCD). The catalytic activity reaction matches EC 2.5.1.15: (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate → 7,8-dihydropteroate + diphosphate. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The sul3 gene product is a plasmid-borne DHPS variant; its annotation as EC 2.5.1.15 is supported by both computational (RuleBase) and experimental (X-ray crystallography, 2023 Nat. Commun.) evidence.",
    "EC 2.5.1.56 is a relatively obscure EC number; a model unfamiliar with its specific reaction might find it harder to exclude, but the DPGMG motif and size constraints still favor DHPS.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical), but the model was not given the accession or organism name."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (2, 3, 5) and the two EC 2.5.1.x options differ in family-specific motifs and size. The DPGMG motif and TIM-barrel architecture uniquely point to DHPS among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 (sul3, DHP3_ECOLX) is annotated with EC 2.5.1.15 (dihydropteroate synthase type-3) supported by both RuleBase (ECO:0000255) and experimental evidence (ECO:0000269, PubMed 37419898, X-ray crystallography of PDB 7S2L/7S2M/8SCD). The catalytic activity reaction matches EC 2.5.1.15: (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate → 7,8-dihydropteroate + diphosphate. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 263-aa protein contains the 'DPGMGFF' motif (~position 200), a well-known conserved active-site signature of the dihydropteroate synthase (DHPS/folP/sul) family, which catalyzes pABA + DHPP → dihydropteroate (EC 2.5.1.15). The overall length (~263 aa) and alternating hydrophobic/polar TIM-barrel-like sequence pattern are consistent with DHPS family members. This eliminates EC 3.1.26.3 (RNase H, ~150 aa, acidic metal-binding residues, hydrolase class) and EC 5.3.1.8 (glucose-6-phosphate isomerase, ~440–550 aa, isomerase class) by both size and EC-class logic. Between the two remaining transferase options (2.5.1.56 vs 2.5.1.15), the DPGMG motif and TIM-barrel architecture are hallmark features of DHPS specifically, not of the obscure transferase assigned 2.5.1.56 (which lacks this motif and has a different fold/size). The sul-type sulfonamide-resistance DHPS variants (sul1/sul2/sul3) are a well-studied family sharing this motif with chromosomal folP.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the DPGMG active-site motif, the ~263-aa TIM-barrel length, and the transferase (EC 2) class to select DHPS (2.5.1.15) over the other options. The DHPS/sul family is extensively characterized in the literature and databases, making this a legitimate family-level inference rather than a lookup of this exact protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (2, 3, 5) and the two EC 2.5.1.x options differ in family-specific motifs and size. The DPGMG motif and TIM-barrel architecture uniquely point to DHPS among the given choices."
  },
  "important_caveats": [
    "The sul3 gene product is a plasmid-borne DHPS variant; its annotation as EC 2.5.1.15 is supported by both computational (RuleBase) and experimental (X-ray crystallography, 2023 Nat. Commun.) evidence.",
    "EC 2.5.1.56 is a relatively obscure EC number; a model unfamiliar with its specific reaction might find it harder to exclude, but the DPGMG motif and size constraints still favor DHPS.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical), but the model was not given the accession or organism name."
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
  "benchmark_sequence_length": 263,
  "benchmark_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 263,
  "current_source_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C0HMD9",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "selected_historical_source_sequence_length": 263,
  "selected_historical_source_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "selected_historical_version": {
    "accession": "C0HMD9",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHP3_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C0HMD9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAD30683.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C002\",\"source\":\"UniProtKB\"}],\"value\":\"Dihydropteroate pyrophosphorylase type III\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C002\",\"source\":\"UniProtKB\"}],\"value\":\"Dihydropteroate synthase type III\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.15\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"Dihydropteroate synthase type-3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"DHPS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.5.1.15\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"name\":\"(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19949\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17836\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17839\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:72950\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Venkatesan M.\",\"Fruci M.\",\"Verellen L.A.\",\"Skarina T.\",\"Mesa N.\",\"Flick R.\",\"Pham C.\",\"Mahadevan R.\",\"Stogios P.J.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37419898\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-023-39778-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"4031\",\"id\":\"37419898\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"4031\",\"publicationDate\":\"2023\",\"title\":\"Molecular mechanism of plasmid-borne resistance to sulfonamide antibiotics.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7S2L\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7S2M\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8SCD\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH MG(2+) AND WITH SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF PHE-177 AND LEU-179\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   DHP3_ECOLX              Reviewed;         263 AA.\nAC   C0HMD9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};\nDE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};\nDE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};\nGN   Name=sul3 {ECO:0000303|PubMed:12604565, ECO:0000312|EMBL:CAD30683.1};\nOS   Escherichia coli.\nOG   Plasmid pVP440 {ECO:0000312|EMBL:CAD30683.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:CAD30683.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};\nDE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};\nDE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAD30683.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=Rl0044 {ECO:0000312|EMBL:CAD30683.1};\nRC   PLASMID=pVP440 {ECO:0000312|EMBL:CAD30683.1};\nRX   PubMed=12604565; DOI=10.1128/aac.47.3.1169-1172.2003;\nRA   Perreten V., Boerlin P.;\nRT   \"A new sulfonamide resistance gene (sul3) in Escherichia coli is widespread\nRT   in the pig population of Switzerland.\";\nRL   Antimicrob. Agents Chemother. 47:1169-1172(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7S2L, ECO:0007744|PDB:7S2M, ECO:0007744|PDB:8SCD}\nRP   X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH\nRP   MG(2+) AND WITH SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND MUTAGENESIS OF PHE-177 AND LEU-179.\nRX   PubMed=37419898; DOI=10.1038/s41467-023-39778-7;\nRA   Venkatesan M., Fruci M., Verellen L.A., Skarina T., Mesa N., Flick R.,\nRA   Pham C., Mahadevan R., Stogios P.J., Savchenko A.;\nRT   \"Molecular mechanism of plasmid-borne resistance to sulfonamide\nRT   antibiotics.\";\nRL   Nat. Commun. 14:4031-4031(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate =\nCC         7,8-dihydropteroate + diphosphate; Xref=Rhea:RHEA:19949,\nCC         ChEBI:CHEBI:17836, ChEBI:CHEBI:17839, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:72950; EC=2.5.1.15;\nCC         Evidence={ECO:0000269|PubMed:37419898};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
