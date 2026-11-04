# active_site_0062

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0062.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 275 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. Position 197 (For decarboxylation activity of LM)
B. Position 113 (Nucleophile)
C. Position 213 (Proton donor)
D. Position 275 (Nucleophile)
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

> The matched sequence has a UniProt active-site annotation identifying position 275 as the nucleophile. This annotation is transferred from a homolog rather than presented as direct experimental evidence for this exact protein, so it supports the key by homology-based inference.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an NAD-dependent UDP-sugar dehydrogenase, and it contains a conserved catalytic-cysteine region around position 275. In this enzyme family, the cysteine acts as the nucleophile; that family-level pattern distinguishes position 275 from the other proposed roles and positions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could infer the enzyme family from sequence features and transfer the conserved catalytic-cysteine role from related enzymes. This is a meaningful basis for selecting D, even though it does not independently prove the exact residue’s role experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice has an equally credible family-level basis for the nucleophile role.


### Important caveats

- The supplied source annotation is homology-transferred, not direct experimental evidence for this exact protein.
- The annotation’s applicability is supported by an exact sequence match, but the author’s source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an NAD-dependent UDP-sugar dehydrogenase, and it contains a conserved catalytic-cysteine region around position 275. In this enzyme family, the cysteine acts as the nucleophile; that family-level pattern distinguishes position 275 from the other proposed roles and positions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could infer the enzyme family from sequence features and transfer the conserved catalytic-cysteine role from related enzymes. This is a meaningful basis for selecting D, even though it does not independently prove the exact residue’s role experimentally."
  },
  "case_id": "active_site_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt active-site annotation identifying position 275 as the nucleophile. This annotation is transferred from a homolog rather than presented as direct experimental evidence for this exact protein, so it supports the key by homology-based inference."
  },
  "important_caveats": [
    "The supplied source annotation is homology-transferred, not direct experimental evidence for this exact protein.",
    "The annotation’s applicability is supported by an exact sequence match, but the author’s source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has an equally credible family-level basis for the nucleophile role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt active-site annotation identifying position 275 as the nucleophile. This annotation is transferred from a homolog rather than presented as direct experimental evidence for this exact protein, so it supports the key by homology-based inference.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an NAD-dependent UDP-sugar dehydrogenase, and it contains a conserved catalytic-cysteine region around position 275. In this enzyme family, the cysteine acts as the nucleophile; that family-level pattern distinguishes position 275 from the other proposed roles and positions.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could infer the enzyme family from sequence features and transfer the conserved catalytic-cysteine role from related enzymes. This is a meaningful basis for selecting D, even though it does not independently prove the exact residue’s role experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has an equally credible family-level basis for the nucleophile role."
  },
  "important_caveats": [
    "The supplied source annotation is homology-transferred, not direct experimental evidence for this exact protein.",
    "The annotation’s applicability is supported by an exact sequence match, but the author’s source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A7GKX6 annotates position 275 as an active site 'Nucleophile' (evidence code ECO:0000250, inferred by similarity to Q0P8H3). The residue at position 275 in the provided sequence is Cysteine (C), which is chemically consistent with a nucleophilic role. The sequence matches the source record (SHA256 confirmed). While the annotation is computational (similarity-based) rather than experimentally determined, it is a reasonable and consistent assignment for an NAD-dependent oxidoreductase.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains a Rossmann-fold-like NAD-binding motif (LGYVGLPLAI at positions 21-30), identifying it as an NAD-dependent oxidoreductase. Reading the amino acid at each listed position directly from the sequence: position 113 = Leucine (cannot be a nucleophile), position 213 = Proline (cannot be a proton donor), position 197 = Glutamine with a nonsensical 'decarboxylation activity of LM' label (inconsistent with dehydrogenase function), and position 275 = Cysteine (a well-established nucleophile in enzymatic catalysis, e.g., cysteine proteases, certain dehydrogenases). Options B and C are eliminated on pure chemical grounds (Leu and Pro cannot perform the stated catalytic roles). Option A is eliminated by functional inconsistency (decarboxylation is not a dehydrogenase mechanism). Only option D presents a residue (Cys) chemically capable of acting as a nucleophile in an oxidoreductase context, making it the sole defensible choice without needing the specific UniProt annotation for this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can distinguish the answer by (1) recognizing the NAD-binding Rossmann fold to confirm oxidoreductase context, (2) reading the amino acid identity at each proposed position from the sequence, and (3) applying basic chemical reasoning about which residues can serve as nucleophiles or proton donors. Three of four options are eliminated by straightforward chemical incompatibility (Leu as nucleophile, Pro as proton donor) or functional mismatch (decarboxylation for a dehydrogenase). Cys as a nucleophile is a well-known general biochemical principle transferable across many enzyme families.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D presents a chemically and functionally consistent residue-role pairing. The other three options are clearly eliminable: Leu cannot be a nucleophile, Pro cannot be a proton donor, and 'decarboxylation' is inconsistent with the dehydrogenase function evident from the sequence.


### Important caveats

- The UniProt annotation for position 275 is based on similarity (ECO:0000250 to Q0P8H3), not direct experimental evidence for this specific protein.
- The question tests whether the model can identify the correct residue among options that include chemically impossible pairings, making it largely a sequence-reading and basic chemistry task rather than requiring deep family-specific knowledge.
- Option A's reference to 'LM' (likely lipoyl moiety or similar) and 'decarboxylation' appears to be a distractor drawn from a different enzyme class entirely.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains a Rossmann-fold-like NAD-binding motif (LGYVGLPLAI at positions 21-30), identifying it as an NAD-dependent oxidoreductase. Reading the amino acid at each listed position directly from the sequence: position 113 = Leucine (cannot be a nucleophile), position 213 = Proline (cannot be a proton donor), position 197 = Glutamine with a nonsensical 'decarboxylation activity of LM' label (inconsistent with dehydrogenase function), and position 275 = Cysteine (a well-established nucleophile in enzymatic catalysis, e.g., cysteine proteases, certain dehydrogenases). Options B and C are eliminated on pure chemical grounds (Leu and Pro cannot perform the stated catalytic roles). Option A is eliminated by functional inconsistency (decarboxylation is not a dehydrogenase mechanism). Only option D presents a residue (Cys) chemically capable of acting as a nucleophile in an oxidoreductase context, making it the sole defensible choice without needing the specific UniProt annotation for this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the answer by (1) recognizing the NAD-binding Rossmann fold to confirm oxidoreductase context, (2) reading the amino acid identity at each proposed position from the sequence, and (3) applying basic chemical reasoning about which residues can serve as nucleophiles or proton donors. Three of four options are eliminated by straightforward chemical incompatibility (Leu as nucleophile, Pro as proton donor) or functional mismatch (decarboxylation for a dehydrogenase). Cys as a nucleophile is a well-known general biochemical principle transferable across many enzyme families."
  },
  "case_id": "active_site_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A7GKX6 annotates position 275 as an active site 'Nucleophile' (evidence code ECO:0000250, inferred by similarity to Q0P8H3). The residue at position 275 in the provided sequence is Cysteine (C), which is chemically consistent with a nucleophilic role. The sequence matches the source record (SHA256 confirmed). While the annotation is computational (similarity-based) rather than experimentally determined, it is a reasonable and consistent assignment for an NAD-dependent oxidoreductase."
  },
  "important_caveats": [
    "The UniProt annotation for position 275 is based on similarity (ECO:0000250 to Q0P8H3), not direct experimental evidence for this specific protein.",
    "The question tests whether the model can identify the correct residue among options that include chemically impossible pairings, making it largely a sequence-reading and basic chemistry task rather than requiring deep family-specific knowledge.",
    "Option A's reference to 'LM' (likely lipoyl moiety or similar) and 'decarboxylation' appears to be a distractor drawn from a different enzyme class entirely."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D presents a chemically and functionally consistent residue-role pairing. The other three options are clearly eliminable: Leu cannot be a nucleophile, Pro cannot be a proton donor, and 'decarboxylation' is inconsistent with the dehydrogenase function evident from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A7GKX6 annotates position 275 as an active site 'Nucleophile' (evidence code ECO:0000250, inferred by similarity to Q0P8H3). The residue at position 275 in the provided sequence is Cysteine (C), which is chemically consistent with a nucleophilic role. The sequence matches the source record (SHA256 confirmed). While the annotation is computational (similarity-based) rather than experimentally determined, it is a reasonable and consistent assignment for an NAD-dependent oxidoreductase.",
    "evidence_ids": ["C5", "H3", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains a Rossmann-fold-like NAD-binding motif (LGYVGLPLAI at positions 21-30), identifying it as an NAD-dependent oxidoreductase. Reading the amino acid at each listed position directly from the sequence: position 113 = Leucine (cannot be a nucleophile), position 213 = Proline (cannot be a proton donor), position 197 = Glutamine with a nonsensical 'decarboxylation activity of LM' label (inconsistent with dehydrogenase function), and position 275 = Cysteine (a well-established nucleophile in enzymatic catalysis, e.g., cysteine proteases, certain dehydrogenases). Options B and C are eliminated on pure chemical grounds (Leu and Pro cannot perform the stated catalytic roles). Option A is eliminated by functional inconsistency (decarboxylation is not a dehydrogenase mechanism). Only option D presents a residue (Cys) chemically capable of acting as a nucleophile in an oxidoreductase context, making it the sole defensible choice without needing the specific UniProt annotation for this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the answer by (1) recognizing the NAD-binding Rossmann fold to confirm oxidoreductase context, (2) reading the amino acid identity at each proposed position from the sequence, and (3) applying basic chemical reasoning about which residues can serve as nucleophiles or proton donors. Three of four options are eliminated by straightforward chemical incompatibility (Leu as nucleophile, Pro as proton donor) or functional mismatch (decarboxylation for a dehydrogenase). Cys as a nucleophile is a well-known general biochemical principle transferable across many enzyme families."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D presents a chemically and functionally consistent residue-role pairing. The other three options are clearly eliminable: Leu cannot be a nucleophile, Pro cannot be a proton donor, and 'decarboxylation' is inconsistent with the dehydrogenase function evident from the sequence."
  },
  "important_caveats": [
    "The UniProt annotation for position 275 is based on similarity (ECO:0000250 to Q0P8H3), not direct experimental evidence for this specific protein.",
    "The question tests whether the model can identify the correct residue among options that include chemically impossible pairings, making it largely a sequence-reading and basic chemistry task rather than requiring deep family-specific knowledge.",
    "Option A's reference to 'LM' (likely lipoyl moiety or similar) and 'decarboxylation' appears to be a distractor drawn from a different enzyme class entirely."
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
  "benchmark_sequence_length": 423,
  "benchmark_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_entry_audit": {
    "entryVersion": 98,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 423,
  "current_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 96,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7GKX6",
  "selected_historical_entry_version": 96,
  "selected_historical_record_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "selected_historical_source_sequence_length": 423,
  "selected_historical_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "selected_historical_version": {
    "accession": "A7GKX6",
    "database": "Swiss-Prot",
    "entryVersion": 96,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UGNAD_BACCN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7GKX6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":98,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":275}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":24},\"start\":{\"modifier\":\"EXACT\",\"value\":24}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":43},\"start\":{\"modifier\":\"EXACT\",\"value\":43}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":48},\"start\":{\"modifier\":\"EXACT\",\"value\":48}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":100},\"start\":{\"modifier\":\"EXACT\",\"value\":100}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":135},\"start\":{\"modifier\":\"EXACT\",\"value\":135}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":340},\"start\":{\"modifier\":\"EXACT\",\"value\":340}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43879.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H1",
  "excerpt": "ID   UGNAD_BACCN             Reviewed;         423 AA.\nAC   A7GKX6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 96.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};\nGN   Name=UGlcNAcDH {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0429 {ECO:0000312|EMBL:ABS20784.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43879.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        275\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         24\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         43\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         48\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         100\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         135\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         340\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
