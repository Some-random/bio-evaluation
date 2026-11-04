# EC_number_0052

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0052.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 4.2.1.9

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. 4.2.1.18
B. 2.1.1.392
C. 3.2.1.20
D. 4.2.1.9
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

> The matched-sequence UniProt annotation assigns EC 4.2.1.9 and names the protein dihydroxy-acid dehydratase (C4). Its listed catalytic reactions also carry EC 4.2.1.9 (C5, C6). The reaction annotations are supported by similarity evidence, so they are not direct experimental confirmation for this protein, but they support the keyed answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence, with an N-terminal region consistent with a mitochondrial targeting peptide followed by a conserved enzyme domain, is compatible with the IlvD/dihydroxy-acid dehydratase family. Family-level sequence recognition provides a credible route to EC 4.2.1.9; the other options describe methyltransferase, glycosidase, or a different lyase activity and are not comparably supported by this family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family from sequence features and transferring its characteristic reaction assignment from related proteins meaningfully distinguishes D among these choices, without needing this exact protein's database record. The sequence alone may not establish every substrate detail experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level inference supports D, and none of the other offered EC numbers is an equally defensible assignment from the sequence.


### Important caveats

- The source reaction annotations cite similarity evidence, so they should not be represented as direct experimental measurements of this protein's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence, with an N-terminal region consistent with a mitochondrial targeting peptide followed by a conserved enzyme domain, is compatible with the IlvD/dihydroxy-acid dehydratase family. Family-level sequence recognition provides a credible route to EC 4.2.1.9; the other options describe methyltransferase, glycosidase, or a different lyase activity and are not comparably supported by this family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from sequence features and transferring its characteristic reaction assignment from related proteins meaningfully distinguishes D among these choices, without needing this exact protein's database record. The sequence alone may not establish every substrate detail experimentally."
  },
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 4.2.1.9 and names the protein dihydroxy-acid dehydratase (C4). Its listed catalytic reactions also carry EC 4.2.1.9 (C5, C6). The reaction annotations are supported by similarity evidence, so they are not direct experimental confirmation for this protein, but they support the keyed answer."
  },
  "important_caveats": [
    "The source reaction annotations cite similarity evidence, so they should not be represented as direct experimental measurements of this protein's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference supports D, and none of the other offered EC numbers is an equally defensible assignment from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 4.2.1.9 and names the protein dihydroxy-acid dehydratase (C4). Its listed catalytic reactions also carry EC 4.2.1.9 (C5, C6). The reaction annotations are supported by similarity evidence, so they are not direct experimental confirmation for this protein, but they support the keyed answer.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence, with an N-terminal region consistent with a mitochondrial targeting peptide followed by a conserved enzyme domain, is compatible with the IlvD/dihydroxy-acid dehydratase family. Family-level sequence recognition provides a credible route to EC 4.2.1.9; the other options describe methyltransferase, glycosidase, or a different lyase activity and are not comparably supported by this family inference.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from sequence features and transferring its characteristic reaction assignment from related proteins meaningfully distinguishes D among these choices, without needing this exact protein's database record. The sequence alone may not establish every substrate detail experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference supports D, and none of the other offered EC numbers is an equally defensible assignment from the sequence."
  },
  "important_caveats": [
    "The source reaction annotations cite similarity evidence, so they should not be represented as direct experimental measurements of this protein's activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0F7TWW9, PBRD_PENBI) assigns EC 4.2.1.9 (dihydroxy-acid dehydratase) with evidence code ECO:0000305 (inferred from direct assay) citing PubMed:39511739. The catalytic activity comments confirm dehydration of 2,3-dihydroxy acids to 2-oxo acids, consistent with EC 4.2.1.9. The sequence matches the benchmark sequence exactly (SHA-256 confirmed). The EC assignment is supported by the referenced publication characterizing pbrD in the aspterric acid biosynthesis pathway.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'NPCNMHLNDL' motif (residues ~70-80), which is a hallmark signature of the dihydroxy-acid dehydratase (DHAD/IlvD) family. In the canonical E. coli IlvD (P06999), the corresponding region is essentially identical ('NPCNMHLNDL'). This motif houses a cysteine that coordinates the &#91;2Fe-2S&#93; cluster essential for DHAD catalysis. Additional cysteine-rich motifs support this: 'GCSAKG' (~residue 140), 'ACPGKGACGG' (~residue 190, containing two cysteines for Fe-S coordination), 'SCPADDPKKL' (~residue 230), and 'GCVTDGPI' at the C-terminus (~residue 590). Together these provide the four cysteine ligands for the &#91;2Fe-2S&#93; cluster characteristic of DHAD. The ~596-aa length and overall domain architecture (N-terminal Fe-S binding region, central catalytic domain, C-terminal regulatory region) match the DHAD family. None of the other options fit: 2.1.1.392 (transferase) lacks any methyltransferase or acyltransferase motifs; 3.2.1.20 (glycosidase) lacks any glycosidase catalytic residues or TIM-barrel architecture; 4.2.1.18 is not associated with this sequence signature. The NPC motif alone is a strong family-level discriminator for DHAD.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NPCNMHLNDL motif and the constellation of cysteine residues in positions consistent with &#91;2Fe-2S&#93; coordination are well-established, transferable DHAD family signatures. A model trained on general protein biology would recognize these features as diagnostic of dihydroxy-acid dehydratase (EC 4.2.1.9) without needing to know this specific Penicillium protein's annotation. The other three options (a transferase, a glycosidase, and an unrelated lyase) can be excluded by the absence of their characteristic motifs and by the presence of the DHAD-specific sequence architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The NPC motif and cysteine architecture uniquely identify the DHAD family among the four choices. The transferase (B) and glycosidase (C) options are clearly incompatible with the sequence features. Option A (4.2.1.18) does not correspond to any known enzyme with this signature. Only D (4.2.1.9) matches.


### Important caveats

- The EC assignment in UniProt carries evidence code ECO:0000305 (inferred from direct assay) from PubMed:39511739, but the specific catalytic reaction annotations carry ECO:0000250 (inferred by similarity) from known DHADs (Q0CPG9, P05791). The protein was characterized as part of the aspterric acid biosynthesis cluster in Penicillium brasilianum.
- The NPCNMHLNDL motif is shared across the DHAD/IlvD superfamily and is not unique to this particular protein, making the inference genuinely family-level rather than target-specific lookup.
- The reviewer-only evidence confirms sequence match and annotation, but the evaluated model had access only to the raw sequence and four EC number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'NPCNMHLNDL' motif (residues ~70-80), which is a hallmark signature of the dihydroxy-acid dehydratase (DHAD/IlvD) family. In the canonical E. coli IlvD (P06999), the corresponding region is essentially identical ('NPCNMHLNDL'). This motif houses a cysteine that coordinates the [2Fe-2S] cluster essential for DHAD catalysis. Additional cysteine-rich motifs support this: 'GCSAKG' (~residue 140), 'ACPGKGACGG' (~residue 190, containing two cysteines for Fe-S coordination), 'SCPADDPKKL' (~residue 230), and 'GCVTDGPI' at the C-terminus (~residue 590). Together these provide the four cysteine ligands for the [2Fe-2S] cluster characteristic of DHAD. The ~596-aa length and overall domain architecture (N-terminal Fe-S binding region, central catalytic domain, C-terminal regulatory region) match the DHAD family. None of the other options fit: 2.1.1.392 (transferase) lacks any methyltransferase or acyltransferase motifs; 3.2.1.20 (glycosidase) lacks any glycosidase catalytic residues or TIM-barrel architecture; 4.2.1.18 is not associated with this sequence signature. The NPC motif alone is a strong family-level discriminator for DHAD.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NPCNMHLNDL motif and the constellation of cysteine residues in positions consistent with [2Fe-2S] coordination are well-established, transferable DHAD family signatures. A model trained on general protein biology would recognize these features as diagnostic of dihydroxy-acid dehydratase (EC 4.2.1.9) without needing to know this specific Penicillium protein's annotation. The other three options (a transferase, a glycosidase, and an unrelated lyase) can be excluded by the absence of their characteristic motifs and by the presence of the DHAD-specific sequence architecture."
  },
  "case_id": "EC_number_0052",
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
    "reason": "The UniProt entry (A0A0F7TWW9, PBRD_PENBI) assigns EC 4.2.1.9 (dihydroxy-acid dehydratase) with evidence code ECO:0000305 (inferred from direct assay) citing PubMed:39511739. The catalytic activity comments confirm dehydration of 2,3-dihydroxy acids to 2-oxo acids, consistent with EC 4.2.1.9. The sequence matches the benchmark sequence exactly (SHA-256 confirmed). The EC assignment is supported by the referenced publication characterizing pbrD in the aspterric acid biosynthesis pathway."
  },
  "important_caveats": [
    "The EC assignment in UniProt carries evidence code ECO:0000305 (inferred from direct assay) from PubMed:39511739, but the specific catalytic reaction annotations carry ECO:0000250 (inferred by similarity) from known DHADs (Q0CPG9, P05791). The protein was characterized as part of the aspterric acid biosynthesis cluster in Penicillium brasilianum.",
    "The NPCNMHLNDL motif is shared across the DHAD/IlvD superfamily and is not unique to this particular protein, making the inference genuinely family-level rather than target-specific lookup.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model had access only to the raw sequence and four EC number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NPC motif and cysteine architecture uniquely identify the DHAD family among the four choices. The transferase (B) and glycosidase (C) options are clearly incompatible with the sequence features. Option A (4.2.1.18) does not correspond to any known enzyme with this signature. Only D (4.2.1.9) matches."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0F7TWW9, PBRD_PENBI) assigns EC 4.2.1.9 (dihydroxy-acid dehydratase) with evidence code ECO:0000305 (inferred from direct assay) citing PubMed:39511739. The catalytic activity comments confirm dehydration of 2,3-dihydroxy acids to 2-oxo acids, consistent with EC 4.2.1.9. The sequence matches the benchmark sequence exactly (SHA-256 confirmed). The EC assignment is supported by the referenced publication characterizing pbrD in the aspterric acid biosynthesis pathway.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'NPCNMHLNDL' motif (residues ~70-80), which is a hallmark signature of the dihydroxy-acid dehydratase (DHAD/IlvD) family. In the canonical E. coli IlvD (P06999), the corresponding region is essentially identical ('NPCNMHLNDL'). This motif houses a cysteine that coordinates the [2Fe-2S] cluster essential for DHAD catalysis. Additional cysteine-rich motifs support this: 'GCSAKG' (~residue 140), 'ACPGKGACGG' (~residue 190, containing two cysteines for Fe-S coordination), 'SCPADDPKKL' (~residue 230), and 'GCVTDGPI' at the C-terminus (~residue 590). Together these provide the four cysteine ligands for the [2Fe-2S] cluster characteristic of DHAD. The ~596-aa length and overall domain architecture (N-terminal Fe-S binding region, central catalytic domain, C-terminal regulatory region) match the DHAD family. None of the other options fit: 2.1.1.392 (transferase) lacks any methyltransferase or acyltransferase motifs; 3.2.1.20 (glycosidase) lacks any glycosidase catalytic residues or TIM-barrel architecture; 4.2.1.18 is not associated with this sequence signature. The NPC motif alone is a strong family-level discriminator for DHAD.",
    "missing_item_specific_fact": "",
    "reason": "The NPCNMHLNDL motif and the constellation of cysteine residues in positions consistent with [2Fe-2S] coordination are well-established, transferable DHAD family signatures. A model trained on general protein biology would recognize these features as diagnostic of dihydroxy-acid dehydratase (EC 4.2.1.9) without needing to know this specific Penicillium protein's annotation. The other three options (a transferase, a glycosidase, and an unrelated lyase) can be excluded by the absence of their characteristic motifs and by the presence of the DHAD-specific sequence architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NPC motif and cysteine architecture uniquely identify the DHAD family among the four choices. The transferase (B) and glycosidase (C) options are clearly incompatible with the sequence features. Option A (4.2.1.18) does not correspond to any known enzyme with this signature. Only D (4.2.1.9) matches."
  },
  "important_caveats": [
    "The EC assignment in UniProt carries evidence code ECO:0000305 (inferred from direct assay) from PubMed:39511739, but the specific catalytic reaction annotations carry ECO:0000250 (inferred by similarity) from known DHADs (Q0CPG9, P05791). The protein was characterized as part of the aspterric acid biosynthesis cluster in Penicillium brasilianum.",
    "The NPCNMHLNDL motif is shared across the DHAD/IlvD superfamily and is not unique to this particular protein, making the inference genuinely family-level rather than target-specific lookup.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model had access only to the raw sequence and four EC number choices."
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
  "benchmark_sequence_length": 596,
  "benchmark_sequence_sha256": "c113b75f8644468658289da5480b81ecf252c20df4f27a6efbd96538aea1668e",
  "current_entry_audit": {
    "entryVersion": 31,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 2
  },
  "current_record_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 596,
  "current_source_sequence_sha256": "c113b75f8644468658289da5480b81ecf252c20df4f27a6efbd96538aea1668e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0F7TWW9",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "selected_historical_source_sequence_length": 596,
  "selected_historical_source_sequence_sha256": "c113b75f8644468658289da5480b81ecf252c20df4f27a6efbd96538aea1668e",
  "selected_historical_version": {
    "accession": "A0A0F7TWW9",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PBRD_PENBI",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0F7TWW9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":31,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium brasilianum\",\"taxonId\":104259}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase pbrD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhou Z.\",\"Zhang Y.\",\"Wu Q.\",\"Hou X.\",\"Zhang B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39511739\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c08468\"}],\"citationType\":\"journal article\",\"firstPage\":\"25755\",\"id\":\"39511739\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"25766\",\"publicationDate\":\"2024\",\"title\":\"Yeast synthesis and herbicidal activity evaluation of aspterric acid.\",\"volume\":\"72\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   PBRD_PENBI              Reviewed;         596 AA.\nAC   A0A0F7TWW9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 2.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};\nDE            Short=DHAD astD {ECO:0000303|PubMed:39511739};\nDE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};\nDE   Flags: Precursor;\nGN   Name=pbrD {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09713;\nOS   Penicillium brasilianum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=104259;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};\nDE            Short=DHAD astD {ECO:0000303|PubMed:39511739};\nDE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=39511739; DOI=10.1021/acs.jafc.4c08468;\nRA   Zhou Z., Zhang Y., Wu Q., Hou X., Zhang B.;\nRT   \"Yeast synthesis and herbicidal activity evaluation of aspterric acid.\";\nRL   J. Agric. Food Chem. 72:25755-25766(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
