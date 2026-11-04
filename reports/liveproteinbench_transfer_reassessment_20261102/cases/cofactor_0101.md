# cofactor_0101

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0101.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Na(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQCSVQFRPCIDIHKGKVKQIVGSTLKDLKDDDGSDPITNFESDKSAAEYATLYKQDGLKGGHVIMLGADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Fe(2+)
C. Na(+)
D. cob(II)alamin
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

> The matched-sequence UniProt record annotates Na(+) as a cofactor, with experimental evidence, and states that two sodium ions optimize substrate binding. The cited structural study also reports a sodium-containing complex. This supports choice C, although optimization of binding does not by itself establish that sodium is absolutely required under all conditions.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> That this particular enzyme binds sodium ions that optimize substrate binding, as established by protein-specific structural and biochemical evidence.


**Reason**

> The sequence may permit family recognition, but ordinary family or mechanism knowledge does not meaningfully predict this unusual sodium-binding property. Isomerase function does not imply Na(+), and the sequence provides no clear signature distinguishing sodium binding from the listed alternatives. Identifying the keyed choice therefore depends on the protein-specific finding rather than a credible transferable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence specifically annotates sodium for the matched sequence; no alternative is similarly supported.


### Important caveats

- The reviewer-only evidence was not part of the original model input and is used only to assess key support.
- The evidence describes sodium as optimizing substrate binding; that wording is weaker than demonstrating absolute necessity for catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular enzyme binds sodium ions that optimize substrate binding, as established by protein-specific structural and biochemical evidence.",
    "reason": "The sequence may permit family recognition, but ordinary family or mechanism knowledge does not meaningfully predict this unusual sodium-binding property. Isomerase function does not imply Na(+), and the sequence provides no clear signature distinguishing sodium binding from the listed alternatives. Identifying the keyed choice therefore depends on the protein-specific finding rather than a credible transferable inference."
  },
  "case_id": "cofactor_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates Na(+) as a cofactor, with experimental evidence, and states that two sodium ions optimize substrate binding. The cited structural study also reports a sodium-containing complex. This supports choice C, although optimization of binding does not by itself establish that sodium is absolutely required under all conditions."
  },
  "important_caveats": [
    "The reviewer-only evidence was not part of the original model input and is used only to assess key support.",
    "The evidence describes sodium as optimizing substrate binding; that wording is weaker than demonstrating absolute necessity for catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence specifically annotates sodium for the matched sequence; no alternative is similarly supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates Na(+) as a cofactor, with experimental evidence, and states that two sodium ions optimize substrate binding. The cited structural study also reports a sodium-containing complex. This supports choice C, although optimization of binding does not by itself establish that sodium is absolutely required under all conditions.",
    "evidence_ids": ["C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "That this particular enzyme binds sodium ions that optimize substrate binding, as established by protein-specific structural and biochemical evidence.",
    "reason": "The sequence may permit family recognition, but ordinary family or mechanism knowledge does not meaningfully predict this unusual sodium-binding property. Isomerase function does not imply Na(+), and the sequence provides no clear signature distinguishing sodium binding from the listed alternatives. Identifying the keyed choice therefore depends on the protein-specific finding rather than a credible transferable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence specifically annotates sodium for the matched sequence; no alternative is similarly supported."
  },
  "important_caveats": [
    "The reviewer-only evidence was not part of the original model input and is used only to assess key support.",
    "The evidence describes sodium as optimizing substrate binding; that wording is weaker than demonstrating absolute necessity for catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G7IFI7 (HISN3_MEDTR, 5'-proFAR isomerase, EC 5.3.1.16) annotates Na(+) as the cofactor with experimental evidence (ECO:0000269, PubMed:39186852). X-ray crystallography at 1.54 Å confirmed binding of 2 sodium ions that optimize substrate binding. The annotation is backed by direct structural and biochemical data, not merely computational inference.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows a chloroplast transit peptide (N-terminal Ser/Pro-rich basic region) followed by a ~270-residue core with TIM-barrel-like 'GGG' loop motifs, consistent with the HisA/ProFAR-isomerase (EC 5.3.1.16) family. Among the four cofactor choices, three can be excluded by the absence of their required structural signatures: (A) pantetheine 4'-phosphate is covalently attached to ACP (~80 aa) or fatty-acid-synthase domains, neither of which matches this sequence; (D) cob(II)alamin requires a dedicated ~100-residue B12-binding domain with a conserved His-Asp-Asp motif, entirely absent here; (B) Fe(2+) in non-heme enzymes typically requires a 2-His-1-carboxylate facial triad or heme pocket, neither of which is evident. The remaining choice, Na(+), is consistent with the cluster of acidic residues (DDDGSDP, FSDVSLDA, MDDLER) that can coordinate a simple monovalent cation via carboxylate and backbone-carbonyl ligands. While the specific Na(+) requirement for plant HISN3 was only demonstrated experimentally in 2024, the elimination of the other three options by well-established structural biology of their cofactor-binding domains provides a credible transferable inference favoring C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A (no ACP/FAS fold), D (no B12-binding domain), and B (no canonical iron-coordination motifs) using general structural biology knowledge of those cofactor classes. The remaining option C is the most consistent with the observed acidic-residue clusters and the TIM-barrel isomerase fold. The argument is probabilistic rather than certain—Fe(2+) could theoretically be coordinated by Asp/Glu in non-canonical arrangements—but the elimination of three options with well-defined structural prerequisites meaningfully distinguishes C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the Na(+) vs Fe(2+) distinction is not absolute from sequence alone (both can be coordinated by carboxylates), the absence of any canonical iron-binding motif (2-His-1-carboxylate triad, heme pocket, or Rieske cluster) combined with the presence of clustered Asp residues typical of Na+ sites makes C the clearly preferred answer. The other two options (A, D) are decisively excluded by the absence of their required structural domains.


### Important caveats

- The Na(+) cofactor annotation for plant HISN3 is a 2024 finding (PubMed:39186852). Models trained before mid-2024 may not know this specific fact, though the elimination argument for C remains valid.
- The bacterial homolog HisA (e.g., E. coli) does not require a metal cofactor, so family identification alone would not predict Na(+); the plant-specific context (chloroplast transit peptide) is necessary to shift expectation away from 'no cofactor'.
- The argument against Fe(2+) relies on absence of canonical motifs; non-canonical Fe(2+) coordination by Asp clusters is theoretically possible but uncommon in TIM-barrel isomerases.
- The reviewer-only evidence confirms the key with X-ray crystallographic data, but this evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows a chloroplast transit peptide (N-terminal Ser/Pro-rich basic region) followed by a ~270-residue core with TIM-barrel-like 'GGG' loop motifs, consistent with the HisA/ProFAR-isomerase (EC 5.3.1.16) family. Among the four cofactor choices, three can be excluded by the absence of their required structural signatures: (A) pantetheine 4'-phosphate is covalently attached to ACP (~80 aa) or fatty-acid-synthase domains, neither of which matches this sequence; (D) cob(II)alamin requires a dedicated ~100-residue B12-binding domain with a conserved His-Asp-Asp motif, entirely absent here; (B) Fe(2+) in non-heme enzymes typically requires a 2-His-1-carboxylate facial triad or heme pocket, neither of which is evident. The remaining choice, Na(+), is consistent with the cluster of acidic residues (DDDGSDP, FSDVSLDA, MDDLER) that can coordinate a simple monovalent cation via carboxylate and backbone-carbonyl ligands. While the specific Na(+) requirement for plant HISN3 was only demonstrated experimentally in 2024, the elimination of the other three options by well-established structural biology of their cofactor-binding domains provides a credible transferable inference favoring C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A (no ACP/FAS fold), D (no B12-binding domain), and B (no canonical iron-coordination motifs) using general structural biology knowledge of those cofactor classes. The remaining option C is the most consistent with the observed acidic-residue clusters and the TIM-barrel isomerase fold. The argument is probabilistic rather than certain—Fe(2+) could theoretically be coordinated by Asp/Glu in non-canonical arrangements—but the elimination of three options with well-defined structural prerequisites meaningfully distinguishes C."
  },
  "case_id": "cofactor_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G7IFI7 (HISN3_MEDTR, 5'-proFAR isomerase, EC 5.3.1.16) annotates Na(+) as the cofactor with experimental evidence (ECO:0000269, PubMed:39186852). X-ray crystallography at 1.54 Å confirmed binding of 2 sodium ions that optimize substrate binding. The annotation is backed by direct structural and biochemical data, not merely computational inference."
  },
  "important_caveats": [
    "The Na(+) cofactor annotation for plant HISN3 is a 2024 finding (PubMed:39186852). Models trained before mid-2024 may not know this specific fact, though the elimination argument for C remains valid.",
    "The bacterial homolog HisA (e.g., E. coli) does not require a metal cofactor, so family identification alone would not predict Na(+); the plant-specific context (chloroplast transit peptide) is necessary to shift expectation away from 'no cofactor'.",
    "The argument against Fe(2+) relies on absence of canonical motifs; non-canonical Fe(2+) coordination by Asp clusters is theoretically possible but uncommon in TIM-barrel isomerases.",
    "The reviewer-only evidence confirms the key with X-ray crystallographic data, but this evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the Na(+) vs Fe(2+) distinction is not absolute from sequence alone (both can be coordinated by carboxylates), the absence of any canonical iron-binding motif (2-His-1-carboxylate triad, heme pocket, or Rieske cluster) combined with the presence of clustered Asp residues typical of Na+ sites makes C the clearly preferred answer. The other two options (A, D) are decisively excluded by the absence of their required structural domains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G7IFI7 (HISN3_MEDTR, 5'-proFAR isomerase, EC 5.3.1.16) annotates Na(+) as the cofactor with experimental evidence (ECO:0000269, PubMed:39186852). X-ray crystallography at 1.54 Å confirmed binding of 2 sodium ions that optimize substrate binding. The annotation is backed by direct structural and biochemical data, not merely computational inference.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows a chloroplast transit peptide (N-terminal Ser/Pro-rich basic region) followed by a ~270-residue core with TIM-barrel-like 'GGG' loop motifs, consistent with the HisA/ProFAR-isomerase (EC 5.3.1.16) family. Among the four cofactor choices, three can be excluded by the absence of their required structural signatures: (A) pantetheine 4'-phosphate is covalently attached to ACP (~80 aa) or fatty-acid-synthase domains, neither of which matches this sequence; (D) cob(II)alamin requires a dedicated ~100-residue B12-binding domain with a conserved His-Asp-Asp motif, entirely absent here; (B) Fe(2+) in non-heme enzymes typically requires a 2-His-1-carboxylate facial triad or heme pocket, neither of which is evident. The remaining choice, Na(+), is consistent with the cluster of acidic residues (DDDGSDP, FSDVSLDA, MDDLER) that can coordinate a simple monovalent cation via carboxylate and backbone-carbonyl ligands. While the specific Na(+) requirement for plant HISN3 was only demonstrated experimentally in 2024, the elimination of the other three options by well-established structural biology of their cofactor-binding domains provides a credible transferable inference favoring C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A (no ACP/FAS fold), D (no B12-binding domain), and B (no canonical iron-coordination motifs) using general structural biology knowledge of those cofactor classes. The remaining option C is the most consistent with the observed acidic-residue clusters and the TIM-barrel isomerase fold. The argument is probabilistic rather than certain—Fe(2+) could theoretically be coordinated by Asp/Glu in non-canonical arrangements—but the elimination of three options with well-defined structural prerequisites meaningfully distinguishes C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the Na(+) vs Fe(2+) distinction is not absolute from sequence alone (both can be coordinated by carboxylates), the absence of any canonical iron-binding motif (2-His-1-carboxylate triad, heme pocket, or Rieske cluster) combined with the presence of clustered Asp residues typical of Na+ sites makes C the clearly preferred answer. The other two options (A, D) are decisively excluded by the absence of their required structural domains."
  },
  "important_caveats": [
    "The Na(+) cofactor annotation for plant HISN3 is a 2024 finding (PubMed:39186852). Models trained before mid-2024 may not know this specific fact, though the elimination argument for C remains valid.",
    "The bacterial homolog HisA (e.g., E. coli) does not require a metal cofactor, so family identification alone would not predict Na(+); the plant-specific context (chloroplast transit peptide) is necessary to shift expectation away from 'no cofactor'.",
    "The argument against Fe(2+) relies on absence of canonical motifs; non-canonical Fe(2+) coordination by Asp clusters is theoretically possible but uncommon in TIM-barrel isomerases.",
    "The reviewer-only evidence confirms the key with X-ray crystallographic data, but this evidence was not available to the evaluated model."
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
  "benchmark_sequence_length": 312,
  "benchmark_sequence_sha256": "5cc38259edb8e6a0c05d63b5b309a07322d6beb3042fe4fc48cb46b256ebf155",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-01-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 312,
  "current_source_sequence_sha256": "5cc38259edb8e6a0c05d63b5b309a07322d6beb3042fe4fc48cb46b256ebf155",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 82,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G7IFI7",
  "selected_historical_entry_version": 82,
  "selected_historical_record_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "selected_historical_source_sequence_length": 312,
  "selected_historical_source_sequence_sha256": "5cc38259edb8e6a0c05d63b5b309a07322d6beb3042fe4fc48cb46b256ebf155",
  "selected_historical_version": {
    "accession": "G7IFI7",
    "database": "Swiss-Prot",
    "entryVersion": 82,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISN3_MEDTR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G7IFI7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-01-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Barrel medic\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"Hologalegina\",\"IRL clade\",\"Trifolieae\",\"Medicago\"],\"scientificName\":\"Medicago truncatula\",\"synonyms\":[\"Medicago tribuloides\"],\"taxonId\":3880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"5'-proFAR isomerase 3\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Protein HISTIDINE BIOSYNTHESIS 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"MtHISN3\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29101\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"name\":\"Na(+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Binds 2 sodium ions to optimize substrate binding.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Witek W.\",\"Imiolczyk B.\",\"Ruszkowski M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39186852\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.plaphy.2024.109065\"}],\"citationType\":\"journal article\",\"firstPage\":\"109065\",\"id\":\"39186852\",\"journal\":\"Plant Physiol. Biochem.\",\"lastPage\":\"109065\",\"publicationDate\":\"2024\",\"title\":\"Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-ProFAR isomerase.\",\"volume\":\"215\"},\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM ION; 5'-PROFAR AND PRFAR\",\"FUNCTION\",\"MUTAGENESIS OF ASP-57 AND 74-LEU--SER-80\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"COFACTOR\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H1",
  "excerpt": "ID   HISN3_MEDTR             Reviewed;         312 AA.\nAC   G7IFI7; A0A396J617; B7FHU9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-JAN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 82.\nDE   RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic {ECO:0000303|PubMed:39186852};\nDE            EC=5.3.1.16 {ECO:0000269|PubMed:39186852};\nDE   AltName: Full=5'-proFAR isomerase 3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Protein HISTIDINE BIOSYNTHESIS 3 {ECO:0000303|PubMed:39186852};\nDE            Short=MtHISN3 {ECO:0000303|PubMed:39186852};\nDE   Flags: Precursor;\nGN   Name=HISN3 {ECO:0000303|PubMed:39186852};\nGN   OrderedLocusNames=MTR_2g015010 {ECO:0000312|EMBL:AES63938.1},\nGN   MtrunA17_Chr2g0283151 {ECO:0000312|EMBL:RHN72021.1};\nOS   Medicago truncatula (Barrel medic) (Medicago tribuloides).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; Hologalegina; IRL clade; Trifolieae; Medicago.\nOX   NCBI_TaxID=3880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic {ECO:0000303|PubMed:39186852};\nDE            EC=5.3.1.16 {ECO:0000269|PubMed:39186852};\nDE   AltName: Full=5'-proFAR isomerase 3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Protein HISTIDINE BIOSYNTHESIS 3 {ECO:0000303|PubMed:39186852};\nDE            Short=MtHISN3 {ECO:0000303|PubMed:39186852};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H3",
  "excerpt": "RN   [5]\nRP   X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM\nRP   ION; 5'-PROFAR AND PRFAR, FUNCTION, MUTAGENESIS OF ASP-57 AND\nRP   74-LEU--SER-80, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES,\nRP   COFACTOR, AND PATHWAY.\nRX   PubMed=39186852; DOI=10.1016/j.plaphy.2024.109065;\nRA   Witek W., Imiolczyk B., Ruszkowski M.;\nRT   \"Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-\nRT   ProFAR isomerase.\";\nRL   Plant Physiol. Biochem. 215:109065-109065(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Na(+); Xref=ChEBI:CHEBI:29101;\nCC         Evidence={ECO:0000269|PubMed:39186852};\nCC       Note=Binds 2 sodium ions to optimize substrate binding.\nCC       {ECO:0000269|PubMed:39186852};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
