# EC_number_0171

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0171.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSPRPQIKVGVLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRWKLPSPIPDAVRHMVVHECRPDAPGFAECGVVFSGLDADVAGDIENAFRAADLVVYSNAKNYRRDPLCPLIVPLVNPSHLSIIPYQREQLGLKKGYIVTNANCSTTGIVVPLAALEKAFGPLDTVIVTTLQAISGAGYPGVSSLDIMDNVVPLISGEEDKIEWETNKILGGVTPDNKAFDLHAPKQINVSATCTRVPVIDGHTGCVSVKFARSPPPSVAEVENAFREYTCDAQHLGVPSAPAQAIVVHDAPDRPQPRLDKNLHNGACVSVGRIRECPVFDIKFVCLIDNVRLGAATSSIINAEIAVEKGLIQ

[Multiple Choices]
A. 1.2.1.46
B. 1.2.1.11
C. 1.1.1.336
D. 5.3.1.8
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

> The sequence matches the annotated protein, and the UniProt record assigns EC 1.2.1.11 to its catalytic activity with experimental evidence codes citing two publications. The reported reaction is the aspartate-semialdehyde dehydrogenase reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich dinucleotide-binding motif and features consistent with the conserved aspartate-semialdehyde dehydrogenase family. Family knowledge connects this enzyme to the phosphate-dependent oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 from the other offered EC classes, including the isomerase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family from transferable sequence and family-level knowledge provides a meaningful basis for selecting B; exact-protein annotation is not necessary to distinguish these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices distinguish the aspartate-semialdehyde dehydrogenase activity from different enzyme activities, and no competing option is comparably supported.


### Important caveats

- The UniProt EC annotation cites experimental evidence, but the primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding motif and features consistent with the conserved aspartate-semialdehyde dehydrogenase family. Family knowledge connects this enzyme to the phosphate-dependent oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 from the other offered EC classes, including the isomerase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from transferable sequence and family-level knowledge provides a meaningful basis for selecting B; exact-protein annotation is not necessary to distinguish these alternatives."
  },
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the UniProt record assigns EC 1.2.1.11 to its catalytic activity with experimental evidence codes citing two publications. The reported reaction is the aspartate-semialdehyde dehydrogenase reaction."
  },
  "important_caveats": [
    "The UniProt EC annotation cites experimental evidence, but the primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish the aspartate-semialdehyde dehydrogenase activity from different enzyme activities, and no competing option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the UniProt record assigns EC 1.2.1.11 to its catalytic activity with experimental evidence codes citing two publications. The reported reaction is the aspartate-semialdehyde dehydrogenase reaction.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding motif and features consistent with the conserved aspartate-semialdehyde dehydrogenase family. Family knowledge connects this enzyme to the phosphate-dependent oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 from the other offered EC classes, including the isomerase option.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from transferable sequence and family-level knowledge provides a meaningful basis for selecting B; exact-protein annotation is not necessary to distinguish these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish the aspartate-semialdehyde dehydrogenase activity from different enzyme activities, and no competing option is comparably supported."
  },
  "important_caveats": [
    "The UniProt EC annotation cites experimental evidence, but the primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5KPK7 (DHAS_CRYD1) annotates this 365-aa protein as aspartate-semialdehyde dehydrogenase with EC=1.2.1.11, supported by experimental evidence (ECO:0000269) from PubMed 26527262 (X-ray crystallography at 2.60 Å, PDB 5CEF) and PubMed 29608391 (functional/inhibitor-screening assays). The catalytic reaction (L-aspartate 4-semialdehyde + Pi + NADP+ → 4-phospho-L-aspartate + NADPH + H+) is confirmed experimentally. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark features of the aspartate-semialdehyde dehydrogenase (ASD) family that are transferable from well-characterized homologs (E. coli HemL, yeast LYS4, and other fungal ASDs): (1) The N-terminal Rossmann-fold nucleotide-binding motif 'VLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRW' contains the canonical GxGxxG (GATGTVG) signature for NAD(P)-binding, and the specific residues in the βαβ motif are highly conserved across ASD orthologs. (2) The catalytic cysteine in the 'CGVVFSGLD' region (~position 95) sits in the context expected for the nucleophilic Cys of the aldehyde-dehydrogenase catalytic tetrad (Cys-Asp-His-Asn). (3) The overall length (~365 aa) and two-domain architecture (N-terminal NAD(P)-binding Rossmann domain + C-terminal substrate-binding domain) match the ASD fold precisely. (4) Basic residues in the C-terminal region are consistent with the phosphate-binding site that uniquely accommodates the 4-phospho-L-aspartate product of ASD. These features collectively rule out C (1.1.1.336, an alcohol/CH-OH dehydrogenase lacking a catalytic Cys) and D (5.3.1.8, an isomerase with no Rossmann fold or catalytic Cys). Between A (1.2.1.46, N-acetyl-γ-glutamyl-phosphate reductase) and B (1.2.1.11, ASD), the specific 'GATGTVG' Rossmann motif, the catalytic-Cys context, the ~365-aa length, and the phosphate-binding residue pattern are diagnostic of the ASD subfamily rather than the NAGPR subfamily, whose substrate-binding pocket is configured for the bulkier N-acetyl-glutamyl-phosphate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with the ASD protein family (from E. coli, yeast, or other fungal ASDs) can recognize the characteristic Rossmann-fold sequence, catalytic Cys context, length, and phosphate-binding architecture in this sequence, distinguishing it from the other three options. The argument relies on family-level transfer from homologous ASD proteins rather than a memorized annotation of this exact Cryptococcus entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (EC 1.2.1.46) and B (EC 1.2.1.11) are aldehyde dehydrogenases (EC 1.2.1.x) sharing a Rossmann fold and catalytic Cys, so a model lacking detailed family-level knowledge of ASD vs. NAGPR active-site residues could consider both as plausible. However, the specific 'GATGTVG' motif, catalytic-Cys context, and phosphate-binding features shift the balance toward B. The distinction is defensible but not trivially obvious from sequence alone.


### Important caveats

- The UniProt annotation is experimentally supported (X-ray structure PDB 5CEF, functional assays), not merely computational or similarity-based.
- Distinguishing EC 1.2.1.11 from EC 1.2.1.46 purely from sequence is a recognized difficulty in enzyme function prediction; the argument here depends on familiarity with the ASD subfamily's conserved motifs learned from other organisms.
- The reviewer-only evidence identifies the protein as from Cryptococcus deneoformans (strain JEC21), but this organism identity was not provided to the evaluated model and is not needed for the family-level inference.
- EC 1.2.1.46 (N-acetyl-γ-glutamyl-phosphate reductase) is a less commonly encountered enzyme; some models may have limited training exposure to its sequence features, which could bias predictions toward the more prevalent ASD family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark features of the aspartate-semialdehyde dehydrogenase (ASD) family that are transferable from well-characterized homologs (E. coli HemL, yeast LYS4, and other fungal ASDs): (1) The N-terminal Rossmann-fold nucleotide-binding motif 'VLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRW' contains the canonical GxGxxG (GATGTVG) signature for NAD(P)-binding, and the specific residues in the βαβ motif are highly conserved across ASD orthologs. (2) The catalytic cysteine in the 'CGVVFSGLD' region (~position 95) sits in the context expected for the nucleophilic Cys of the aldehyde-dehydrogenase catalytic tetrad (Cys-Asp-His-Asn). (3) The overall length (~365 aa) and two-domain architecture (N-terminal NAD(P)-binding Rossmann domain + C-terminal substrate-binding domain) match the ASD fold precisely. (4) Basic residues in the C-terminal region are consistent with the phosphate-binding site that uniquely accommodates the 4-phospho-L-aspartate product of ASD. These features collectively rule out C (1.1.1.336, an alcohol/CH-OH dehydrogenase lacking a catalytic Cys) and D (5.3.1.8, an isomerase with no Rossmann fold or catalytic Cys). Between A (1.2.1.46, N-acetyl-γ-glutamyl-phosphate reductase) and B (1.2.1.11, ASD), the specific 'GATGTVG' Rossmann motif, the catalytic-Cys context, the ~365-aa length, and the phosphate-binding residue pattern are diagnostic of the ASD subfamily rather than the NAGPR subfamily, whose substrate-binding pocket is configured for the bulkier N-acetyl-glutamyl-phosphate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the ASD protein family (from E. coli, yeast, or other fungal ASDs) can recognize the characteristic Rossmann-fold sequence, catalytic Cys context, length, and phosphate-binding architecture in this sequence, distinguishing it from the other three options. The argument relies on family-level transfer from homologous ASD proteins rather than a memorized annotation of this exact Cryptococcus entry."
  },
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5KPK7 (DHAS_CRYD1) annotates this 365-aa protein as aspartate-semialdehyde dehydrogenase with EC=1.2.1.11, supported by experimental evidence (ECO:0000269) from PubMed 26527262 (X-ray crystallography at 2.60 Å, PDB 5CEF) and PubMed 29608391 (functional/inhibitor-screening assays). The catalytic reaction (L-aspartate 4-semialdehyde + Pi + NADP+ → 4-phospho-L-aspartate + NADPH + H+) is confirmed experimentally. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The UniProt annotation is experimentally supported (X-ray structure PDB 5CEF, functional assays), not merely computational or similarity-based.",
    "Distinguishing EC 1.2.1.11 from EC 1.2.1.46 purely from sequence is a recognized difficulty in enzyme function prediction; the argument here depends on familiarity with the ASD subfamily's conserved motifs learned from other organisms.",
    "The reviewer-only evidence identifies the protein as from Cryptococcus deneoformans (strain JEC21), but this organism identity was not provided to the evaluated model and is not needed for the family-level inference.",
    "EC 1.2.1.46 (N-acetyl-γ-glutamyl-phosphate reductase) is a less commonly encountered enzyme; some models may have limited training exposure to its sequence features, which could bias predictions toward the more prevalent ASD family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (EC 1.2.1.46) and B (EC 1.2.1.11) are aldehyde dehydrogenases (EC 1.2.1.x) sharing a Rossmann fold and catalytic Cys, so a model lacking detailed family-level knowledge of ASD vs. NAGPR active-site residues could consider both as plausible. However, the specific 'GATGTVG' motif, catalytic-Cys context, and phosphate-binding features shift the balance toward B. The distinction is defensible but not trivially obvious from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5KPK7 (DHAS_CRYD1) annotates this 365-aa protein as aspartate-semialdehyde dehydrogenase with EC=1.2.1.11, supported by experimental evidence (ECO:0000269) from PubMed 26527262 (X-ray crystallography at 2.60 Å, PDB 5CEF) and PubMed 29608391 (functional/inhibitor-screening assays). The catalytic reaction (L-aspartate 4-semialdehyde + Pi + NADP+ → 4-phospho-L-aspartate + NADPH + H+) is confirmed experimentally. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark features of the aspartate-semialdehyde dehydrogenase (ASD) family that are transferable from well-characterized homologs (E. coli HemL, yeast LYS4, and other fungal ASDs): (1) The N-terminal Rossmann-fold nucleotide-binding motif 'VLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRW' contains the canonical GxGxxG (GATGTVG) signature for NAD(P)-binding, and the specific residues in the βαβ motif are highly conserved across ASD orthologs. (2) The catalytic cysteine in the 'CGVVFSGLD' region (~position 95) sits in the context expected for the nucleophilic Cys of the aldehyde-dehydrogenase catalytic tetrad (Cys-Asp-His-Asn). (3) The overall length (~365 aa) and two-domain architecture (N-terminal NAD(P)-binding Rossmann domain + C-terminal substrate-binding domain) match the ASD fold precisely. (4) Basic residues in the C-terminal region are consistent with the phosphate-binding site that uniquely accommodates the 4-phospho-L-aspartate product of ASD. These features collectively rule out C (1.1.1.336, an alcohol/CH-OH dehydrogenase lacking a catalytic Cys) and D (5.3.1.8, an isomerase with no Rossmann fold or catalytic Cys). Between A (1.2.1.46, N-acetyl-γ-glutamyl-phosphate reductase) and B (1.2.1.11, ASD), the specific 'GATGTVG' Rossmann motif, the catalytic-Cys context, the ~365-aa length, and the phosphate-binding residue pattern are diagnostic of the ASD subfamily rather than the NAGPR subfamily, whose substrate-binding pocket is configured for the bulkier N-acetyl-glutamyl-phosphate.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the ASD protein family (from E. coli, yeast, or other fungal ASDs) can recognize the characteristic Rossmann-fold sequence, catalytic Cys context, length, and phosphate-binding architecture in this sequence, distinguishing it from the other three options. The argument relies on family-level transfer from homologous ASD proteins rather than a memorized annotation of this exact Cryptococcus entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (EC 1.2.1.46) and B (EC 1.2.1.11) are aldehyde dehydrogenases (EC 1.2.1.x) sharing a Rossmann fold and catalytic Cys, so a model lacking detailed family-level knowledge of ASD vs. NAGPR active-site residues could consider both as plausible. However, the specific 'GATGTVG' motif, catalytic-Cys context, and phosphate-binding features shift the balance toward B. The distinction is defensible but not trivially obvious from sequence alone."
  },
  "important_caveats": [
    "The UniProt annotation is experimentally supported (X-ray structure PDB 5CEF, functional assays), not merely computational or similarity-based.",
    "Distinguishing EC 1.2.1.11 from EC 1.2.1.46 purely from sequence is a recognized difficulty in enzyme function prediction; the argument here depends on familiarity with the ASD subfamily's conserved motifs learned from other organisms.",
    "The reviewer-only evidence identifies the protein as from Cryptococcus deneoformans (strain JEC21), but this organism identity was not provided to the evaluated model and is not needed for the family-level inference.",
    "EC 1.2.1.46 (N-acetyl-γ-glutamyl-phosphate reductase) is a less commonly encountered enzyme; some models may have limited training exposure to its sequence features, which could bias predictions toward the more prevalent ASD family."
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
  "benchmark_sequence_length": 365,
  "benchmark_sequence_sha256": "289af240e9c521aacb1c323e0f199e1285a4f553efd19687f56152d3509323b8",
  "current_entry_audit": {
    "entryVersion": 123,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-02-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 365,
  "current_source_sequence_sha256": "289af240e9c521aacb1c323e0f199e1285a4f553efd19687f56152d3509323b8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 121,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5KPK7",
  "selected_historical_entry_version": 121,
  "selected_historical_record_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "selected_historical_source_sequence_length": 365,
  "selected_historical_source_sequence_sha256": "289af240e9c521aacb1c323e0f199e1285a4f553efd19687f56152d3509323b8",
  "selected_historical_version": {
    "accession": "Q5KPK7",
    "database": "Swiss-Prot",
    "entryVersion": 121,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_CRYD1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5KPK7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":123,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-02-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. neoformans serotype D\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002149\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565)\",\"taxonId\":214684}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26527262\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26527262\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24286\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26527262\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"name\":\"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24284\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:537519\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26527262\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x15017495\"}],\"citationType\":\"journal article\",\"firstPage\":\"1365\",\"id\":\"26527262\",\"journal\":\"Acta Crystallogr. F Struct. Biol. Commun.\",\"lastPage\":\"1371\",\"publicationDate\":\"2015\",\"title\":\"Structure of a fungal form of aspartate semialdehyde dehydrogenase from Cryptococcus neoformans.\",\"volume\":\"71\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5CEF\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:24.745599+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KPK7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_CRYD1              Reviewed;         365 AA.\nAC   Q5KPK7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-FEB-2005, sequence version 1.\nDT   28-JAN-2026, entry version 121.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};\nGN   OrderedLocusNames=CNA02450 {ECO:0000312|EMBL:AAW40826.1};\nOS   Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565) (Cryptococcus\nOS   neoformans var. neoformans serotype D).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=214684 {ECO:0000312|Proteomes:UP000002149};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "url": "https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "url": "https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "url": "https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5CEF}\nRP   X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=26527262; DOI=10.1107/s2053230x15017495;\nRA   Dahal G., Viola R.E.;\nRT   \"Structure of a fungal form of aspartate semialdehyde dehydrogenase from\nRT   Cryptococcus neoformans.\";\nRL   Acta Crystallogr. F Struct. Biol. Commun. 71:1365-1371(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "url": "https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-\nCC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;\nCC         Evidence={ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;\nCC         Evidence={ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "url": "https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
