# catalytic_activity_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0087.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSTAPEDVARPLLALPAIEAFDAIVRGRRSVRSYADVQVPRRTVRDVLELAARAPSNSNVQPWHTYVLTGRHKRALTDSVLRYYDTIGRTVREFDYQPGPDGWEEPYKERRESFGEGLYGRALGLSLADVDDREFYHRRNYDFFAAPVGLIVTVARNPRLSALIDAGAYIQTILLSARSRGLSTCAQASFLDFHPAVRECLAIPTHRTIVCGISLGYEDAQHPIASNATTREPVDRHVTFLWDDDD

[Multiple Choices]
A. 3alpha(S)-strictosidine + H2O = strictosidine aglycone + D-glucose
B. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
C. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
D. 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O
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

> The sequence-matched UniProt record annotates the exact 4-nitrobenzoate-to-4-hydroxylaminobenzoate reaction and cites ECO:0000269 evidence from a PubMed source. This supports D, although the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 247-residue bacterial sequence is consistent with a compact reductase, and its family-level sequence/profile recognition can favor a bacterial nitroreductase over the glycoside-processing enzymes in A and C. The sequence also lacks an obvious canonical N-terminal Rossmann fingerprint expected for many NAD-dependent dehydrogenases such as B. Among these choices, D is the nitroaromatic reduction. These are transferable family-level clues, not proof of the precise substrate or product.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use sequence-family patterns and the sharply different reaction classes in the options to favor D without knowing this protein's recorded annotation. The exact substrate specificity and reaction stoichiometry are not established by the sequence argument alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options describe distinct reaction classes, and the available evidence supports D; no other option is comparably supported.


### Important caveats

- The evidence supports the reaction annotation for the matched sequence, but the cited primary study was not independently assessed.
- The sequence-based argument is probabilistic and does not by itself establish the exact reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 247-residue bacterial sequence is consistent with a compact reductase, and its family-level sequence/profile recognition can favor a bacterial nitroreductase over the glycoside-processing enzymes in A and C. The sequence also lacks an obvious canonical N-terminal Rossmann fingerprint expected for many NAD-dependent dehydrogenases such as B. Among these choices, D is the nitroaromatic reduction. These are transferable family-level clues, not proof of the precise substrate or product.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family patterns and the sharply different reaction classes in the options to favor D without knowing this protein's recorded annotation. The exact substrate specificity and reaction stoichiometry are not established by the sequence argument alone."
  },
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the exact 4-nitrobenzoate-to-4-hydroxylaminobenzoate reaction and cites ECO:0000269 evidence from a PubMed source. This supports D, although the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The evidence supports the reaction annotation for the matched sequence, but the cited primary study was not independently assessed.",
    "The sequence-based argument is probabilistic and does not by itself establish the exact reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options describe distinct reaction classes, and the available evidence supports D; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the exact 4-nitrobenzoate-to-4-hydroxylaminobenzoate reaction and cites ECO:0000269 evidence from a PubMed source. This supports D, although the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 247-residue bacterial sequence is consistent with a compact reductase, and its family-level sequence/profile recognition can favor a bacterial nitroreductase over the glycoside-processing enzymes in A and C. The sequence also lacks an obvious canonical N-terminal Rossmann fingerprint expected for many NAD-dependent dehydrogenases such as B. Among these choices, D is the nitroaromatic reduction. These are transferable family-level clues, not proof of the precise substrate or product.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family patterns and the sharply different reaction classes in the options to favor D without knowing this protein's recorded annotation. The exact substrate specificity and reaction stoichiometry are not established by the sequence argument alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options describe distinct reaction classes, and the available evidence supports D; no other option is comparably supported."
  },
  "important_caveats": [
    "The evidence supports the reaction annotation for the matched sequence, but the cited primary study was not independently assessed.",
    "The sequence-based argument is probabilistic and does not by itself establish the exact reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXG6 (PNBA_NOCS0) from Nocardioides sp. LMS-CY annotates this exact sequence (247 aa, SHA256 matched) as 4-nitrobenzoate reductase / 4-nitrobenzoate nitroreductase (EC 1.7.1.-). The catalytic activity is recorded as '4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O' with experimental evidence (ECO:0000269, PubMed:34554625). This matches choice D exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable sequence and family-level features distinguish D from the alternatives. (1) Size: 247 aa is characteristic of the nitroreductase (NfsA/NfsB/NfsC) family (~200-250 aa), whereas glycosidases (choice A, strictosidine beta-glucosidase) and phosphorylases (choice C) are typically 400-600+ aa with TIM-barrel or beta-propeller folds, making A and C implausible for this small protein. (2) Cofactor preference: The motif 'TGRHKRA' (~residues 55-62) clusters multiple basic residues (Arg, His, Lys, Arg) adjacent to a glycine, a hallmark of NADPH-binding sites where basic residues coordinate the 2'-phosphate of NADPH. This distinguishes D (NADPH-dependent) from B (NAD+-dependent L-galactose dehydrogenase), whose Rossmann fold would typically feature an acidic residue (Asp/Glu) at the C-terminus of the first beta-strand rather than a basic cluster. (3) FMN cofactor: Nitroreductases use FMN as a prosthetic group; the 'ARNPRL' region (~residues 119-124) and the overall fold pattern are consistent with the FMN-binding domain seen in NfsA-type nitroreductases, which is absent in sugar dehydrogenases like B. (4) Substrate context: The small, NADPH-dependent, FMN-containing oxidoreductase architecture is the canonical nitroreductase signature, consistent with reduction of an aromatic nitro group (D) rather than sugar oxidation (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A and C by protein size and fold type, eliminate B by identifying the NADPH-specific basic-residue cluster (vs NAD+ preference), and recognize the overall small-size/NADPH/FMN pattern as consistent with the nitroreductase family learned from NfsA, NfsB, and related proteins. This is a defensible probabilistic inference from transferable family knowledge, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice B (NAD+-dependent dehydrogenase) is the closest distractor, but the prominent basic-residue cluster (TGRHKRA) and small size provide a credible basis to prefer NADPH-dependent nitroreductase (D) over NAD+-dependent sugar dehydrogenase (B). Choices A and C are eliminated by size and fold-type mismatch. No two choices are equally defensible given the sequence features.


### Important caveats

- The NADPH vs NAD+ distinction from the 'TGRHKRA' motif is suggestive but not absolute; some NAD+-dependent enzymes also have basic residues near the binding site. The argument relies on the combined pattern (basic cluster + small size + FMN-binding region) rather than any single motif.
- The UniProt annotation is from a single experimental study (PubMed:34554625, Cheng et al. 2021). The EC number is listed as 1.7.1.- (unspecified subclass), indicating the enzyme's exact EC classification is still open.
- The reviewer-only evidence confirms the sequence match and experimental support, but the evaluated model had access only to the raw sequence and four choices.
- The protein was integrated into Swiss-Prot in February 2025, so it is relatively new; a model trained on earlier data would rely entirely on family-level inference rather than memorized annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable sequence and family-level features distinguish D from the alternatives. (1) Size: 247 aa is characteristic of the nitroreductase (NfsA/NfsB/NfsC) family (~200-250 aa), whereas glycosidases (choice A, strictosidine beta-glucosidase) and phosphorylases (choice C) are typically 400-600+ aa with TIM-barrel or beta-propeller folds, making A and C implausible for this small protein. (2) Cofactor preference: The motif 'TGRHKRA' (~residues 55-62) clusters multiple basic residues (Arg, His, Lys, Arg) adjacent to a glycine, a hallmark of NADPH-binding sites where basic residues coordinate the 2'-phosphate of NADPH. This distinguishes D (NADPH-dependent) from B (NAD+-dependent L-galactose dehydrogenase), whose Rossmann fold would typically feature an acidic residue (Asp/Glu) at the C-terminus of the first beta-strand rather than a basic cluster. (3) FMN cofactor: Nitroreductases use FMN as a prosthetic group; the 'ARNPRL' region (~residues 119-124) and the overall fold pattern are consistent with the FMN-binding domain seen in NfsA-type nitroreductases, which is absent in sugar dehydrogenases like B. (4) Substrate context: The small, NADPH-dependent, FMN-containing oxidoreductase architecture is the canonical nitroreductase signature, consistent with reduction of an aromatic nitro group (D) rather than sugar oxidation (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and C by protein size and fold type, eliminate B by identifying the NADPH-specific basic-residue cluster (vs NAD+ preference), and recognize the overall small-size/NADPH/FMN pattern as consistent with the nitroreductase family learned from NfsA, NfsB, and related proteins. This is a defensible probabilistic inference from transferable family knowledge, not a lookup of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXG6 (PNBA_NOCS0) from Nocardioides sp. LMS-CY annotates this exact sequence (247 aa, SHA256 matched) as 4-nitrobenzoate reductase / 4-nitrobenzoate nitroreductase (EC 1.7.1.-). The catalytic activity is recorded as '4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O' with experimental evidence (ECO:0000269, PubMed:34554625). This matches choice D exactly."
  },
  "important_caveats": [
    "The NADPH vs NAD+ distinction from the 'TGRHKRA' motif is suggestive but not absolute; some NAD+-dependent enzymes also have basic residues near the binding site. The argument relies on the combined pattern (basic cluster + small size + FMN-binding region) rather than any single motif.",
    "The UniProt annotation is from a single experimental study (PubMed:34554625, Cheng et al. 2021). The EC number is listed as 1.7.1.- (unspecified subclass), indicating the enzyme's exact EC classification is still open.",
    "The reviewer-only evidence confirms the sequence match and experimental support, but the evaluated model had access only to the raw sequence and four choices.",
    "The protein was integrated into Swiss-Prot in February 2025, so it is relatively new; a model trained on earlier data would rely entirely on family-level inference rather than memorized annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B (NAD+-dependent dehydrogenase) is the closest distractor, but the prominent basic-residue cluster (TGRHKRA) and small size provide a credible basis to prefer NADPH-dependent nitroreductase (D) over NAD+-dependent sugar dehydrogenase (B). Choices A and C are eliminated by size and fold-type mismatch. No two choices are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXG6 (PNBA_NOCS0) from Nocardioides sp. LMS-CY annotates this exact sequence (247 aa, SHA256 matched) as 4-nitrobenzoate reductase / 4-nitrobenzoate nitroreductase (EC 1.7.1.-). The catalytic activity is recorded as '4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O' with experimental evidence (ECO:0000269, PubMed:34554625). This matches choice D exactly.",
    "evidence_ids": ["C5", "C4", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable sequence and family-level features distinguish D from the alternatives. (1) Size: 247 aa is characteristic of the nitroreductase (NfsA/NfsB/NfsC) family (~200-250 aa), whereas glycosidases (choice A, strictosidine beta-glucosidase) and phosphorylases (choice C) are typically 400-600+ aa with TIM-barrel or beta-propeller folds, making A and C implausible for this small protein. (2) Cofactor preference: The motif 'TGRHKRA' (~residues 55-62) clusters multiple basic residues (Arg, His, Lys, Arg) adjacent to a glycine, a hallmark of NADPH-binding sites where basic residues coordinate the 2'-phosphate of NADPH. This distinguishes D (NADPH-dependent) from B (NAD+-dependent L-galactose dehydrogenase), whose Rossmann fold would typically feature an acidic residue (Asp/Glu) at the C-terminus of the first beta-strand rather than a basic cluster. (3) FMN cofactor: Nitroreductases use FMN as a prosthetic group; the 'ARNPRL' region (~residues 119-124) and the overall fold pattern are consistent with the FMN-binding domain seen in NfsA-type nitroreductases, which is absent in sugar dehydrogenases like B. (4) Substrate context: The small, NADPH-dependent, FMN-containing oxidoreductase architecture is the canonical nitroreductase signature, consistent with reduction of an aromatic nitro group (D) rather than sugar oxidation (B).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and C by protein size and fold type, eliminate B by identifying the NADPH-specific basic-residue cluster (vs NAD+ preference), and recognize the overall small-size/NADPH/FMN pattern as consistent with the nitroreductase family learned from NfsA, NfsB, and related proteins. This is a defensible probabilistic inference from transferable family knowledge, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B (NAD+-dependent dehydrogenase) is the closest distractor, but the prominent basic-residue cluster (TGRHKRA) and small size provide a credible basis to prefer NADPH-dependent nitroreductase (D) over NAD+-dependent sugar dehydrogenase (B). Choices A and C are eliminated by size and fold-type mismatch. No two choices are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The NADPH vs NAD+ distinction from the 'TGRHKRA' motif is suggestive but not absolute; some NAD+-dependent enzymes also have basic residues near the binding site. The argument relies on the combined pattern (basic cluster + small size + FMN-binding region) rather than any single motif.",
    "The UniProt annotation is from a single experimental study (PubMed:34554625, Cheng et al. 2021). The EC number is listed as 1.7.1.- (unspecified subclass), indicating the enzyme's exact EC classification is still open.",
    "The reviewer-only evidence confirms the sequence match and experimental support, but the evaluated model had access only to the raw sequence and four choices.",
    "The protein was integrated into Swiss-Prot in February 2025, so it is relatively new; a model trained on earlier data would rely entirely on family-level inference rather than memorized annotation."
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
  "benchmark_sequence_length": 247,
  "benchmark_sequence_sha256": "221fc9eb61db75050a3de3b4e7de5eeb9eda6e5b7eca6873622ae8201d427a7b",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 247,
  "current_source_sequence_sha256": "221fc9eb61db75050a3de3b4e7de5eeb9eda6e5b7eca6873622ae8201d427a7b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXG6",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36",
  "selected_historical_source_sequence_length": 247,
  "selected_historical_source_sequence_sha256": "221fc9eb61db75050a3de3b4e7de5eeb9eda6e5b7eca6873622ae8201d427a7b",
  "selected_historical_version": {
    "accession": "P0DXG6",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PNBA_NOCS0",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXG6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:26.531539+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:26.531539+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Propionibacteriales\",\"Nocardioidaceae\",\"Nocardioides\"],\"scientificName\":\"Nocardioides sp. (strain LMS-CY)\",\"taxonId\":2840457}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:26.531539+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"4-nitrobenzoate nitroreductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"4-NBA nitroreductase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"1.7.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"4-nitrobenzoate reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"value\":\"4-NBA reductase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:26.531539+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80196\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34554625\",\"source\":\"PubMed\"}],\"name\":\"4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80195\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142863\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:26.531539+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheng M.\",\"Qian Y.\",\"Xing Z.\",\"Zylstra G.J.\",\"Huang X.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34554625\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.15787\"}],\"citationType\":\"journal article\",\"firstPage\":\"7028\",\"id\":\"34554625\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"7041\",\"publicationDate\":\"2021\",\"title\":\"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.\",\"volume\":\"23\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"LMS-CY\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:26.531539+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   PNBA_NOCS0              Reviewed;         247 AA.\nAC   P0DXG6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:34554625};\nDE            Short=4-NBA reductase {ECO:0000303|PubMed:34554625};\nDE            EC=1.7.1.- {ECO:0000269|PubMed:34554625};\nDE   AltName: Full=4-nitrobenzoate nitroreductase {ECO:0000303|PubMed:34554625};\nDE            Short=4-NBA nitroreductase {ECO:0000303|PubMed:34554625};\nGN   Name=pnbA {ECO:0000303|PubMed:34554625};\nGN   ORFNames=KM427_00695 {ECO:0000312|EMBL:QWF22307.1};\nOS   Nocardioides sp. (strain LMS-CY).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Propionibacteriales;\nOC   Nocardioidaceae; Nocardioides.\nOX   NCBI_TaxID=2840457;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:31.939265+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36",
  "url": "https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:34554625};\nDE            Short=4-NBA reductase {ECO:0000303|PubMed:34554625};\nDE            EC=1.7.1.- {ECO:0000269|PubMed:34554625};\nDE   AltName: Full=4-nitrobenzoate nitroreductase {ECO:0000303|PubMed:34554625};\nDE            Short=4-NBA nitroreductase {ECO:0000303|PubMed:34554625};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:31.939265+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36",
  "url": "https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA], FUNCTION, CATALYTIC\nRP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND INDUCTION.\nRC   STRAIN=LMS-CY;\nRX   PubMed=34554625; DOI=10.1111/1462-2920.15787;\nRA   Cheng M., Qian Y., Xing Z., Zylstra G.J., Huang X.;\nRT   \"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively\nRT   regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.\";\nRL   Environ. Microbiol. 23:7028-7041(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:31.939265+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36",
  "url": "https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate +\nCC         2 NADP(+) + H2O; Xref=Rhea:RHEA:80195, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,\nCC         ChEBI:CHEBI:142863, ChEBI:CHEBI:231457;\nCC         Evidence={ECO:0000269|PubMed:34554625};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80196;\nCC         Evidence={ECO:0000269|PubMed:34554625};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:31.939265+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36",
  "url": "https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
