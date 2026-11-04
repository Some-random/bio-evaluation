# active_site_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0028.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 92 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. Position 418 (For beta-ketoacyl synthase activity)
B. Position 21 (Proton acceptor)
C. Position 92 (Proton donor)
D. Position 1160 (Proton donor; for dehydratase activity)
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

> The sequence-matched UniProt annotation identifies position 92 as a proton donor. Its evidence code indicates the annotation was transferred by similarity from another UniProt entry, so this supports the key as a homolog-based annotation, not as direct experimental confirmation for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is consistent with a compact PPCDC-like enzyme family. Transferable family knowledge supports a conserved catalytic histidine acting as a proton donor; position 92 is histidine in the supplied sequence. That makes C meaningfully more plausible than the alternatives, including the positions beyond the sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and conserved active-site patterns provide a credible basis for choosing C without requiring the exact protein's recorded annotation. The residue identity alone would not prove catalytic function, but the family-level inference distinguishes the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C is a plausible offered choice for the proton-donor site. The source also annotates another proton donor at position 177, but that position is not among the choices.


### Important caveats

- The supporting active-site annotation is similarity-based rather than direct experimental evidence for this exact protein.
- The prompt refers to residues in the plural, while each option gives a single position.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is consistent with a compact PPCDC-like enzyme family. Transferable family knowledge supports a conserved catalytic histidine acting as a proton donor; position 92 is histidine in the supplied sequence. That makes C meaningfully more plausible than the alternatives, including the positions beyond the sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and conserved active-site patterns provide a credible basis for choosing C without requiring the exact protein's recorded annotation. The residue identity alone would not prove catalytic function, but the family-level inference distinguishes the offered choices."
  },
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 92 as a proton donor. Its evidence code indicates the annotation was transferred by similarity from another UniProt entry, so this supports the key as a homolog-based annotation, not as direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The supporting active-site annotation is similarity-based rather than direct experimental evidence for this exact protein.",
    "The prompt refers to residues in the plural, while each option gives a single position."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C is a plausible offered choice for the proton-donor site. The source also annotates another proton donor at position 177, but that position is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 92 as a proton donor. Its evidence code indicates the annotation was transferred by similarity from another UniProt entry, so this supports the key as a homolog-based annotation, not as direct experimental confirmation for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is consistent with a compact PPCDC-like enzyme family. Transferable family knowledge supports a conserved catalytic histidine acting as a proton donor; position 92 is histidine in the supplied sequence. That makes C meaningfully more plausible than the alternatives, including the positions beyond the sequence length.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and conserved active-site patterns provide a credible basis for choosing C without requiring the exact protein's recorded annotation. The residue identity alone would not prove catalytic function, but the family-level inference distinguishes the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C is a plausible offered choice for the proton-donor site. The source also annotates another proton donor at position 177, but that position is not among the choices."
  },
  "important_caveats": [
    "The supporting active-site annotation is similarity-based rather than direct experimental evidence for this exact protein.",
    "The prompt refers to residues in the plural, while each option gives a single position."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this entry (A0A498JQK2, HAL3_MALDO) lists position 92 as an 'Active site' with description 'Proton donor' (evidence_id C5, H3). The residue at position 92 in the supplied 214-residue sequence is H (Histidine), consistent with a proton donor role. However, the evidence code is ECO:0000250 (inferred by similarity from Q9SWE5), meaning this is a computational transfer rather than direct experimental determination for this specific protein. The annotation is present and consistent with the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (position 418) and D (position 1160) are immediately eliminated because the supplied sequence is only 214 amino acids long; these positions do not exist in the protein. This is a purely structural constraint from the input. Between the remaining options B (position 21, 'Proton acceptor') and C (position 92, 'Proton donor'), a knowledgeable model can apply general enzyme biochemistry: position 21 is Arginine (R, pKa ~12.5, permanently protonated at physiological pH, not a typical proton acceptor), while position 92 is Histidine (H, pKa ~6.0, the canonical proton donor/acceptor residue in enzyme catalysis). Describing Arginine as a 'proton acceptor' is biochemically atypical, whereas Histidine as a 'proton donor' is the textbook paradigm. Additionally, the sequence contains motifs suggestive of a flavin-dependent (FMN-binding) enzyme (e.g., the GDSV motif near residues 87-90), consistent with the PPCDC/HAL3 family where a conserved histidine serves as the catalytic proton donor. This combination of sequence-length elimination and residue-type biochemistry provides a credible, transferable path to select C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The two distractor options A and D reference positions beyond the protein length, making them trivially eliminable from the input alone. The remaining choice between B and C is resolved by general biochemistry: Histidine (position 92) is the prototypical proton donor in catalysis, while Arginine (position 21) is not a typical proton acceptor due to its high pKa. This reasoning relies on transferable knowledge of amino acid chemistry and enzyme catalysis, not on memorizing this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are eliminated by sequence length (positions 418 and 1160 exceed the 214-residue protein). Option B misidentifies Arginine as a proton acceptor, which is biochemically implausible. Option C correctly identifies Histidine as a proton donor, consistent with both the annotation and general catalytic chemistry. No ambiguity remains among the offered choices.


### Important caveats

- The UniProt annotation for position 92 is by similarity (ECO:0000250 from Q9SWE5), not direct experimental evidence for this specific apple HAL3 protein.
- Position 177 is also annotated as a 'Proton donor' active site in this entry, but it is not among the offered options, so it does not create ambiguity in this multiple-choice context.
- Options A and D appear to be drawn from entirely different proteins (beta-ketoacyl synthase, a dehydratase with 1160+ residues), serving as obvious distractors.
- The protein's identity as PPCDC/HAL3 is not stated in the original input; the model must infer family membership from sequence features or rely on the biochemical reasoning about residue types.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (position 418) and D (position 1160) are immediately eliminated because the supplied sequence is only 214 amino acids long; these positions do not exist in the protein. This is a purely structural constraint from the input. Between the remaining options B (position 21, 'Proton acceptor') and C (position 92, 'Proton donor'), a knowledgeable model can apply general enzyme biochemistry: position 21 is Arginine (R, pKa ~12.5, permanently protonated at physiological pH, not a typical proton acceptor), while position 92 is Histidine (H, pKa ~6.0, the canonical proton donor/acceptor residue in enzyme catalysis). Describing Arginine as a 'proton acceptor' is biochemically atypical, whereas Histidine as a 'proton donor' is the textbook paradigm. Additionally, the sequence contains motifs suggestive of a flavin-dependent (FMN-binding) enzyme (e.g., the GDSV motif near residues 87-90), consistent with the PPCDC/HAL3 family where a conserved histidine serves as the catalytic proton donor. This combination of sequence-length elimination and residue-type biochemistry provides a credible, transferable path to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The two distractor options A and D reference positions beyond the protein length, making them trivially eliminable from the input alone. The remaining choice between B and C is resolved by general biochemistry: Histidine (position 92) is the prototypical proton donor in catalysis, while Arginine (position 21) is not a typical proton acceptor due to its high pKa. This reasoning relies on transferable knowledge of amino acid chemistry and enzyme catalysis, not on memorizing this specific protein's database annotation."
  },
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this entry (A0A498JQK2, HAL3_MALDO) lists position 92 as an 'Active site' with description 'Proton donor' (evidence_id C5, H3). The residue at position 92 in the supplied 214-residue sequence is H (Histidine), consistent with a proton donor role. However, the evidence code is ECO:0000250 (inferred by similarity from Q9SWE5), meaning this is a computational transfer rather than direct experimental determination for this specific protein. The annotation is present and consistent with the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation for position 92 is by similarity (ECO:0000250 from Q9SWE5), not direct experimental evidence for this specific apple HAL3 protein.",
    "Position 177 is also annotated as a 'Proton donor' active site in this entry, but it is not among the offered options, so it does not create ambiguity in this multiple-choice context.",
    "Options A and D appear to be drawn from entirely different proteins (beta-ketoacyl synthase, a dehydratase with 1160+ residues), serving as obvious distractors.",
    "The protein's identity as PPCDC/HAL3 is not stated in the original input; the model must infer family membership from sequence features or rely on the biochemical reasoning about residue types."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by sequence length (positions 418 and 1160 exceed the 214-residue protein). Option B misidentifies Arginine as a proton acceptor, which is biochemically implausible. Option C correctly identifies Histidine as a proton donor, consistent with both the annotation and general catalytic chemistry. No ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this entry (A0A498JQK2, HAL3_MALDO) lists position 92 as an 'Active site' with description 'Proton donor' (evidence_id C5, H3). The residue at position 92 in the supplied 214-residue sequence is H (Histidine), consistent with a proton donor role. However, the evidence code is ECO:0000250 (inferred by similarity from Q9SWE5), meaning this is a computational transfer rather than direct experimental determination for this specific protein. The annotation is present and consistent with the expected answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (position 418) and D (position 1160) are immediately eliminated because the supplied sequence is only 214 amino acids long; these positions do not exist in the protein. This is a purely structural constraint from the input. Between the remaining options B (position 21, 'Proton acceptor') and C (position 92, 'Proton donor'), a knowledgeable model can apply general enzyme biochemistry: position 21 is Arginine (R, pKa ~12.5, permanently protonated at physiological pH, not a typical proton acceptor), while position 92 is Histidine (H, pKa ~6.0, the canonical proton donor/acceptor residue in enzyme catalysis). Describing Arginine as a 'proton acceptor' is biochemically atypical, whereas Histidine as a 'proton donor' is the textbook paradigm. Additionally, the sequence contains motifs suggestive of a flavin-dependent (FMN-binding) enzyme (e.g., the GDSV motif near residues 87-90), consistent with the PPCDC/HAL3 family where a conserved histidine serves as the catalytic proton donor. This combination of sequence-length elimination and residue-type biochemistry provides a credible, transferable path to select C.",
    "missing_item_specific_fact": "",
    "reason": "The two distractor options A and D reference positions beyond the protein length, making them trivially eliminable from the input alone. The remaining choice between B and C is resolved by general biochemistry: Histidine (position 92) is the prototypical proton donor in catalysis, while Arginine (position 21) is not a typical proton acceptor due to its high pKa. This reasoning relies on transferable knowledge of amino acid chemistry and enzyme catalysis, not on memorizing this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by sequence length (positions 418 and 1160 exceed the 214-residue protein). Option B misidentifies Arginine as a proton acceptor, which is biochemically implausible. Option C correctly identifies Histidine as a proton donor, consistent with both the annotation and general catalytic chemistry. No ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 92 is by similarity (ECO:0000250 from Q9SWE5), not direct experimental evidence for this specific apple HAL3 protein.",
    "Position 177 is also annotated as a 'Proton donor' active site in this entry, but it is not among the offered options, so it does not create ambiguity in this multiple-choice context.",
    "Options A and D appear to be drawn from entirely different proteins (beta-ketoacyl synthase, a dehydratase with 1160+ residues), serving as obvious distractors.",
    "The protein's identity as PPCDC/HAL3 is not stated in the original input; the model must infer family membership from sequence features or rely on the biochemical reasoning about residue types."
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
  "benchmark_sequence_length": 214,
  "benchmark_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 214,
  "current_source_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A498JQK2",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "selected_historical_source_sequence_length": 214,
  "selected_historical_source_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "selected_historical_version": {
    "accession": "A0A498JQK2",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "HAL3_MALDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A498JQK2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Apple\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Rosales\",\"Rosaceae\",\"Amygdaloideae\",\"Maleae\",\"Malus\"],\"scientificName\":\"Malus domestica\",\"synonyms\":[\"Pyrus malus\"],\"taxonId\":3750}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"Halotolerance protein 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"MdHAL3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":92}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":177},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":32},\"start\":{\"modifier\":\"EXACT\",\"value\":30}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":57},\"start\":{\"modifier\":\"EXACT\",\"value\":55}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":111},\"start\":{\"modifier\":\"EXACT\",\"value\":108}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":142},\"start\":{\"modifier\":\"EXACT\",\"value\":142}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":144},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":185},\"start\":{\"modifier\":\"EXACT\",\"value\":185}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Important for catalytic activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":177},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang S.\",\"Zhang F.\",\"Wang Y.\",\"Xue H.\",\"Jiang Q.\",\"Shi J.\",\"Dai H.\",\"Zhang Z.\",\"Li L.\",\"He P.\",\"Li Y.\",\"Ma Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32761275\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00299-020-02576-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"1479\",\"id\":\"32761275\",\"journal\":\"Plant Cell Rep.\",\"lastPage\":\"1491\",\"publicationDate\":\"2020\",\"title\":\"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the salt tolerance of autotetraploid apple.\",\"volume\":\"39\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. GL-3\"},{\"type\":\"STRAIN\",\"value\":\"cv. Hanfu\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"INDUCTION BY SALT STRESS\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3_MALDO              Reviewed;         214 AA.\nAC   A0A498JQK2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3 {ECO:0000305};\nDE            Short=PPCDC {ECO:0000303|PubMed:32761275};\nDE            EC=4.1.1.36 {ECO:0000269|PubMed:32761275};\nDE   AltName: Full=Halotolerance protein 3 {ECO:0000303|PubMed:32761275};\nDE            Short=MdHAL3 {ECO:0000303|PubMed:32761275};\nGN   Name=HAL3 {ECO:0000303|PubMed:32761275};\nGN   ORFNames=DVH24_008624 {ECO:0000312|EMBL:RXH96124.1};\nOS   Malus domestica (Apple) (Pyrus malus).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Rosales; Rosaceae; Amygdaloideae; Maleae; Malus.\nOX   NCBI_TaxID=3750;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, TISSUE SPECIFICITY,\nRP   INDUCTION BY SALT STRESS, AND SUBCELLULAR LOCATION.\nRC   STRAIN=cv. GL-3, and cv. Hanfu;\nRX   PubMed=32761275; DOI=10.1007/s00299-020-02576-2;\nRA   Yang S., Zhang F., Wang Y., Xue H., Jiang Q., Shi J., Dai H., Zhang Z.,\nRA   Li L., He P., Li Y., Ma Y.;\nRT   \"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the\nRT   salt tolerance of autotetraploid apple.\";\nRL   Plant Cell Rep. 39:1479-1491(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        92\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        177\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         30..32\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         55..57\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         108..111\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         142\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         144\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         174\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         176\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         185\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H13",
  "excerpt": "FT   SITE            177\nFT                   /note=\"Important for catalytic activity\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
