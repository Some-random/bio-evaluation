# cofactor_0078

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0078.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mg(2+)

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
A. Mn(2+)
B. Fe(2+)
C. heme b
D. Mg(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates Mg(2+) as the cofactor, based on a computational RuleBase annotation (C5). The record also cites crystal structures of the protein in complexes with Mg(2+) and substrates (C6), supporting Mg binding. The excerpts do not independently establish that Mg is essential for catalysis, so the direct experimental support for necessity is limited.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a bacterial dihydropteroate synthase family enzyme. Transferable knowledge of this enzyme family supports Mg(2+) use in catalysis, including coordination of substrate phosphate groups. That family-level inference meaningfully favors Mg(2+) over Mn(2+), Fe(2+), or heme b among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choice can be supported through family recognition and conserved biochemical patterns rather than recall of this exact protein's database annotation. The sequence alone may not make family identification certain, but the inference is meaningful for these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the family-level catalytic pattern.


### Important caveats

- The cofactor annotation in the matched record is computational; the cited structures support Mg(2+) binding but do not, in the supplied excerpts, directly demonstrate its necessity for catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a bacterial dihydropteroate synthase family enzyme. Transferable knowledge of this enzyme family supports Mg(2+) use in catalysis, including coordination of substrate phosphate groups. That family-level inference meaningfully favors Mg(2+) over Mn(2+), Fe(2+), or heme b among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choice can be supported through family recognition and conserved biochemical patterns rather than recall of this exact protein's database annotation. The sequence alone may not make family identification certain, but the inference is meaningful for these alternatives."
  },
  "case_id": "cofactor_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mg(2+) as the cofactor, based on a computational RuleBase annotation (C5). The record also cites crystal structures of the protein in complexes with Mg(2+) and substrates (C6), supporting Mg binding. The excerpts do not independently establish that Mg is essential for catalysis, so the direct experimental support for necessity is limited."
  },
  "important_caveats": [
    "The cofactor annotation in the matched record is computational; the cited structures support Mg(2+) binding but do not, in the supplied excerpts, directly demonstrate its necessity for catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the family-level catalytic pattern."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mg(2+) as the cofactor, based on a computational RuleBase annotation (C5). The record also cites crystal structures of the protein in complexes with Mg(2+) and substrates (C6), supporting Mg binding. The excerpts do not independently establish that Mg is essential for catalysis, so the direct experimental support for necessity is limited.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a bacterial dihydropteroate synthase family enzyme. Transferable knowledge of this enzyme family supports Mg(2+) use in catalysis, including coordination of substrate phosphate groups. That family-level inference meaningfully favors Mg(2+) over Mn(2+), Fe(2+), or heme b among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The choice can be supported through family recognition and conserved biochemical patterns rather than recall of this exact protein's database annotation. The sequence alone may not make family identification certain, but the inference is meaningful for these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the family-level catalytic pattern."
  },
  "important_caveats": [
    "The cofactor annotation in the matched record is computational; the cited structures support Mg(2+) binding but do not, in the supplied excerpts, directly demonstrate its necessity for catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C0HMD9 (Dihydropteroate synthase type-3, EC 2.5.1.15) annotates Mg(2+) as the cofactor (evidence_id C5, H5). While the RuleBase annotation (ECO:0000255) is computational, the X-ray crystallography reference (C6, H4; PDB 7S2L, 7S2M, 8SCD) explicitly describes 'complexes with Mg(2+) and with substrates,' providing experimental structural evidence that Mg(2+) binds this protein. The expected answer D (Mg(2+)) is well-supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved DHPS family motif 'DPGMGFF' (around residues ~170-176) and overall length (~263 aa) consistent with dihydropteroate synthase (EC 2.5.1.15). DHPS is a well-characterized enzyme family in folate biosynthesis; every structurally characterized DHPS (E. coli FolP, S. aureus, M. tuberculosis, etc.) requires Mg(2+) as an essential catalytic cofactor to coordinate the pyrophosphate of DHPP substrate. The 'sul' gene family (sul1/sul2/sul3) encoding sulfonamide-resistance DHPS variants are also known to use Mg(2+). A model trained on multiple DHPS homologs would recognize the family from the DPGMGFF motif, conserved acidic residues (D/E in the active site region), and overall fold, then apply the family-level rule that DHPS universally requires Mg(2+). The other options (Mn(2+), Fe(2+), heme b) are not associated with any known DHPS variant and are typical cofactors for entirely different enzyme classes (phosphatases, oxygenases, cytochromes respectively), making them easy to eliminate once DHPS identity is recognized.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DHPS family is extensively characterized across many organisms, and Mg(2+) is its universal cofactor. The sequence provides recognizable family-level signatures (DPGMGFF motif, conserved active-site acidic residues, appropriate length) that allow a knowledgeable model to identify the protein as DHPS and apply the well-established family-level cofactor requirement. This is legitimate transfer from other DHPS proteins, not lookup of this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is recognized as DHPS (via the DPGMGFF motif and conserved fold features), Mg(2+) is the only cofactor consistent with the DHPS enzyme family. The distractors (Mn(2+), Fe(2+), heme b) belong to entirely different enzyme classes and have no association with DHPS. No ambiguity exists among the offered choices for a model that identifies the family.


### Important caveats

- The RuleBase annotation for Mg(2+) is computational (pattern-based), but is corroborated by experimental crystallographic evidence showing Mg(2+) bound in PDB structures 7S2L, 7S2M, 8SCD.
- The sul3 gene product (type-3 DHPS) is a plasmid-borne sulfonamide resistance variant; its Mg(2+) dependence is consistent with all other DHPS enzymes.
- The sequence-to-DHPS identification relies on family motif recognition (DPGMGFF) which is a well-established transferable feature across the DHPS superfamily.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved DHPS family motif 'DPGMGFF' (around residues ~170-176) and overall length (~263 aa) consistent with dihydropteroate synthase (EC 2.5.1.15). DHPS is a well-characterized enzyme family in folate biosynthesis; every structurally characterized DHPS (E. coli FolP, S. aureus, M. tuberculosis, etc.) requires Mg(2+) as an essential catalytic cofactor to coordinate the pyrophosphate of DHPP substrate. The 'sul' gene family (sul1/sul2/sul3) encoding sulfonamide-resistance DHPS variants are also known to use Mg(2+). A model trained on multiple DHPS homologs would recognize the family from the DPGMGFF motif, conserved acidic residues (D/E in the active site region), and overall fold, then apply the family-level rule that DHPS universally requires Mg(2+). The other options (Mn(2+), Fe(2+), heme b) are not associated with any known DHPS variant and are typical cofactors for entirely different enzyme classes (phosphatases, oxygenases, cytochromes respectively), making them easy to eliminate once DHPS identity is recognized.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DHPS family is extensively characterized across many organisms, and Mg(2+) is its universal cofactor. The sequence provides recognizable family-level signatures (DPGMGFF motif, conserved active-site acidic residues, appropriate length) that allow a knowledgeable model to identify the protein as DHPS and apply the well-established family-level cofactor requirement. This is legitimate transfer from other DHPS proteins, not lookup of this specific entry."
  },
  "case_id": "cofactor_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 (Dihydropteroate synthase type-3, EC 2.5.1.15) annotates Mg(2+) as the cofactor (evidence_id C5, H5). While the RuleBase annotation (ECO:0000255) is computational, the X-ray crystallography reference (C6, H4; PDB 7S2L, 7S2M, 8SCD) explicitly describes 'complexes with Mg(2+) and with substrates,' providing experimental structural evidence that Mg(2+) binds this protein. The expected answer D (Mg(2+)) is well-supported."
  },
  "important_caveats": [
    "The RuleBase annotation for Mg(2+) is computational (pattern-based), but is corroborated by experimental crystallographic evidence showing Mg(2+) bound in PDB structures 7S2L, 7S2M, 8SCD.",
    "The sul3 gene product (type-3 DHPS) is a plasmid-borne sulfonamide resistance variant; its Mg(2+) dependence is consistent with all other DHPS enzymes.",
    "The sequence-to-DHPS identification relies on family motif recognition (DPGMGFF) which is a well-established transferable feature across the DHPS superfamily."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is recognized as DHPS (via the DPGMGFF motif and conserved fold features), Mg(2+) is the only cofactor consistent with the DHPS enzyme family. The distractors (Mn(2+), Fe(2+), heme b) belong to entirely different enzyme classes and have no association with DHPS. No ambiguity exists among the offered choices for a model that identifies the family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 (Dihydropteroate synthase type-3, EC 2.5.1.15) annotates Mg(2+) as the cofactor (evidence_id C5, H5). While the RuleBase annotation (ECO:0000255) is computational, the X-ray crystallography reference (C6, H4; PDB 7S2L, 7S2M, 8SCD) explicitly describes 'complexes with Mg(2+) and with substrates,' providing experimental structural evidence that Mg(2+) binds this protein. The expected answer D (Mg(2+)) is well-supported.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved DHPS family motif 'DPGMGFF' (around residues ~170-176) and overall length (~263 aa) consistent with dihydropteroate synthase (EC 2.5.1.15). DHPS is a well-characterized enzyme family in folate biosynthesis; every structurally characterized DHPS (E. coli FolP, S. aureus, M. tuberculosis, etc.) requires Mg(2+) as an essential catalytic cofactor to coordinate the pyrophosphate of DHPP substrate. The 'sul' gene family (sul1/sul2/sul3) encoding sulfonamide-resistance DHPS variants are also known to use Mg(2+). A model trained on multiple DHPS homologs would recognize the family from the DPGMGFF motif, conserved acidic residues (D/E in the active site region), and overall fold, then apply the family-level rule that DHPS universally requires Mg(2+). The other options (Mn(2+), Fe(2+), heme b) are not associated with any known DHPS variant and are typical cofactors for entirely different enzyme classes (phosphatases, oxygenases, cytochromes respectively), making them easy to eliminate once DHPS identity is recognized.",
    "missing_item_specific_fact": "",
    "reason": "The DHPS family is extensively characterized across many organisms, and Mg(2+) is its universal cofactor. The sequence provides recognizable family-level signatures (DPGMGFF motif, conserved active-site acidic residues, appropriate length) that allow a knowledgeable model to identify the protein as DHPS and apply the well-established family-level cofactor requirement. This is legitimate transfer from other DHPS proteins, not lookup of this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is recognized as DHPS (via the DPGMGFF motif and conserved fold features), Mg(2+) is the only cofactor consistent with the DHPS enzyme family. The distractors (Mn(2+), Fe(2+), heme b) belong to entirely different enzyme classes and have no association with DHPS. No ambiguity exists among the offered choices for a model that identifies the family."
  },
  "important_caveats": [
    "The RuleBase annotation for Mg(2+) is computational (pattern-based), but is corroborated by experimental crystallographic evidence showing Mg(2+) bound in PDB structures 7S2L, 7S2M, 8SCD.",
    "The sul3 gene product (type-3 DHPS) is a plasmid-borne sulfonamide resistance variant; its Mg(2+) dependence is consistent with all other DHPS enzymes.",
    "The sequence-to-DHPS identification relies on family motif recognition (DPGMGFF) which is a well-established transferable feature across the DHPS superfamily."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000255|RuleBase:RU361205};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
