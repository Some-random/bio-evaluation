# pathway_0068

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0068.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Amino-acid degradation. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIETPYLLFLGDAPDMLAAKVAIGIRDWRPDHAVGQISLPGCGANLGLTEMTLEEAKAAGAKTLVIGVANRGGKISQEWKKVLVQALEEGFDLASGLHNLLRDEPDLAAVAEATGRTLHDVRVPSVQYPIADGVKRRGKRCLAVGTDCSVGKMYTALAMDAEMQARGIKSTFRATGQTGILITGDGVPLDAVIADFMAGSIEYLTPDNDDDHWDLIEGQGSLFHVSYSGVTMALVHGGQPDALILCHEPTRTHMRGLPDYDVPSLEELRDVALPLAQRANKDCKIVGISVNTQHLGEEEAVAYLKEVEGRMGLPAVDPYRHGAGRLVDALAAV

[Multiple Choices]
A. Secondary metabolite biosynthesis. .
B. CoA from (R)-pantothenate: step 3/5. .
C. N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2. .
D. Amino-acid degradation. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns the protein as D-glutamate N-acetyltransferase and lists its pathway as amino-acid degradation. The annotation cites a study on a novel D-glutamate catabolic pathway; this supports choice D, while the source-snapshot caveat remains.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> That this particular enzyme acts on D-glutamate in a catabolic pathway (rather than functioning in one of the listed biosynthetic pathways).


**Reason**

> The input gives a soluble, enzyme-sized sequence, but its generic sequence features do not establish its substrate or pathway. Those facts are what distinguish broad amino-acid degradation from the specific CoA and purine-biosynthesis alternatives. No recognizable family-level feature in the supplied sequence provides a meaningful basis for that distinction without knowing this protein's function or a sufficiently informative homolog.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source evidence supports D; the limitation is that the original sequence does not make the pathway assignment readily distinguishable, not that another offered option is comparably supported.


### Important caveats

- The reviewer-only annotations match the supplied sequence, but the author's exact source snapshot is unknown.
- The pathway field is a database annotation; the cited publication and enzyme-function annotation provide supporting context, but the supplied excerpts are not an independent review of the full experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular enzyme acts on D-glutamate in a catabolic pathway (rather than functioning in one of the listed biosynthetic pathways).",
    "reason": "The input gives a soluble, enzyme-sized sequence, but its generic sequence features do not establish its substrate or pathway. Those facts are what distinguish broad amino-acid degradation from the specific CoA and purine-biosynthesis alternatives. No recognizable family-level feature in the supplied sequence provides a meaningful basis for that distinction without knowing this protein's function or a sufficiently informative homolog."
  },
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the protein as D-glutamate N-acetyltransferase and lists its pathway as amino-acid degradation. The annotation cites a study on a novel D-glutamate catabolic pathway; this supports choice D, while the source-snapshot caveat remains."
  },
  "important_caveats": [
    "The reviewer-only annotations match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway field is a database annotation; the cited publication and enzyme-function annotation provide supporting context, but the supplied excerpts are not an independent review of the full experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports D; the limitation is that the original sequence does not make the pathway assignment readily distinguishable, not that another offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the protein as D-glutamate N-acetyltransferase and lists its pathway as amino-acid degradation. The annotation cites a study on a novel D-glutamate catabolic pathway; this supports choice D, while the source-snapshot caveat remains.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "That this particular enzyme acts on D-glutamate in a catabolic pathway (rather than functioning in one of the listed biosynthetic pathways).",
    "reason": "The input gives a soluble, enzyme-sized sequence, but its generic sequence features do not establish its substrate or pathway. Those facts are what distinguish broad amino-acid degradation from the specific CoA and purine-biosynthesis alternatives. No recognizable family-level feature in the supplied sequence provides a meaningful basis for that distinction without knowing this protein's function or a sufficiently informative homolog."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports D; the limitation is that the original sequence does not make the pathway assignment readily distinguishable, not that another offered option is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotations match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway field is a database annotation; the cited publication and enzyme-function annotation provide supporting context, but the supplied excerpts are not an independent review of the full experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A2T1AE85) annotates this protein as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the pathway explicitly stated as 'Amino-acid degradation' (evidence C5, H3), supported by experimental data including X-ray crystallography (PDB 7XRJ) and a 2023 ISME J. publication (PubMed:36690779) describing a novel D-glutamate catabolic pathway. The EC number 2.3.1.312 is a transferase (acetyltransferase) acting on D-glutamate, which is an amino acid, placing it squarely in amino-acid degradation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly contains the GNAT (GCN5-related N-acetyltransferase) fold signature motifs 'GCGANLGL' and 'VANRGGK', allowing identification as an acetyltransferase. This eliminates options B (pantothenate kinase pathway) and C (GAR synthetase, purine biosynthesis), which involve entirely different enzyme classes. However, the GNAT superfamily is enormous and acetylates an extremely diverse range of substrates: histones, polyamines, amino acids, drugs, and secondary metabolite intermediates. The GNAT fold alone does not reveal whether the acetyl acceptor is an amino acid (→ D, amino-acid degradation) or a secondary-metabolite intermediate (→ A, secondary metabolite biosynthesis). No distinctive amino-acid-binding pocket motif or subfamily-specific signature is apparent in the sequence that would reliably distinguish amino-acid acetylation from secondary-metabolite acetylation using general GNAT family knowledge.


**Missing item-specific fact**

> The specific substrate identity (D-glutamate) and the experimentally determined catabolic pathway assignment for this exact protein (EC 2.3.1.312, D-glutamate N-acetyltransferase, characterized in 2023). Without knowing the substrate, the GNAT fold is too promiscuous in substrate scope to distinguish 'amino-acid degradation' from 'secondary metabolite biosynthesis.'


**Reason**

> While the GNAT fold is identifiable from sequence motifs, the critical A-vs-D distinction depends on knowing the substrate is D-glutamate. The GNAT superfamily includes acetyltransferases for amino acids, polyamines, histones, antibiotics, and secondary metabolites. General family-level knowledge does not provide a reliable basis to assign this particular GNAT to amino-acid degradation rather than secondary metabolite biosynthesis. The enzyme was characterized experimentally in 2023, and its pathway assignment is a specific annotation fact about this protein rather than a predictable inference from the fold.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 'Secondary metabolite biosynthesis' and 'Amino-acid degradation' are plausible pathway assignments for a GNAT acetyltransferase when only the fold is known. GNAT enzymes participate in both categories. Without substrate-specific information, a model could reasonably argue for either option based on general GNAT family diversity.


### Important caveats

- The GNAT fold is unambiguously identifiable from the sequence, which correctly eliminates options B and C.
- The D-glutamate N-acetyltransferase (EC 2.3.1.312) was experimentally characterized in 2023 (Yu et al., ISME J.), making it a relatively recently annotated enzyme with limited precedent in training corpora.
- The pathway annotation 'Amino-acid degradation' is supported by experimental evidence (PDB 7XRJ, PubMed:36690779), not merely computational inference.
- A model with very broad training coverage might associate specific GNAT sequence patterns with amino-acid acetylation, but this would be a learned pattern from this or closely related proteins rather than a deductive inference from general GNAT biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly contains the GNAT (GCN5-related N-acetyltransferase) fold signature motifs 'GCGANLGL' and 'VANRGGK', allowing identification as an acetyltransferase. This eliminates options B (pantothenate kinase pathway) and C (GAR synthetase, purine biosynthesis), which involve entirely different enzyme classes. However, the GNAT superfamily is enormous and acetylates an extremely diverse range of substrates: histones, polyamines, amino acids, drugs, and secondary metabolite intermediates. The GNAT fold alone does not reveal whether the acetyl acceptor is an amino acid (→ D, amino-acid degradation) or a secondary-metabolite intermediate (→ A, secondary metabolite biosynthesis). No distinctive amino-acid-binding pocket motif or subfamily-specific signature is apparent in the sequence that would reliably distinguish amino-acid acetylation from secondary-metabolite acetylation using general GNAT family knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate) and the experimentally determined catabolic pathway assignment for this exact protein (EC 2.3.1.312, D-glutamate N-acetyltransferase, characterized in 2023). Without knowing the substrate, the GNAT fold is too promiscuous in substrate scope to distinguish 'amino-acid degradation' from 'secondary metabolite biosynthesis.'",
    "reason": "While the GNAT fold is identifiable from sequence motifs, the critical A-vs-D distinction depends on knowing the substrate is D-glutamate. The GNAT superfamily includes acetyltransferases for amino acids, polyamines, histones, antibiotics, and secondary metabolites. General family-level knowledge does not provide a reliable basis to assign this particular GNAT to amino-acid degradation rather than secondary metabolite biosynthesis. The enzyme was characterized experimentally in 2023, and its pathway assignment is a specific annotation fact about this protein rather than a predictable inference from the fold."
  },
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2T1AE85) annotates this protein as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the pathway explicitly stated as 'Amino-acid degradation' (evidence C5, H3), supported by experimental data including X-ray crystallography (PDB 7XRJ) and a 2023 ISME J. publication (PubMed:36690779) describing a novel D-glutamate catabolic pathway. The EC number 2.3.1.312 is a transferase (acetyltransferase) acting on D-glutamate, which is an amino acid, placing it squarely in amino-acid degradation."
  },
  "important_caveats": [
    "The GNAT fold is unambiguously identifiable from the sequence, which correctly eliminates options B and C.",
    "The D-glutamate N-acetyltransferase (EC 2.3.1.312) was experimentally characterized in 2023 (Yu et al., ISME J.), making it a relatively recently annotated enzyme with limited precedent in training corpora.",
    "The pathway annotation 'Amino-acid degradation' is supported by experimental evidence (PDB 7XRJ, PubMed:36690779), not merely computational inference.",
    "A model with very broad training coverage might associate specific GNAT sequence patterns with amino-acid acetylation, but this would be a learned pattern from this or closely related proteins rather than a deductive inference from general GNAT biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 'Secondary metabolite biosynthesis' and 'Amino-acid degradation' are plausible pathway assignments for a GNAT acetyltransferase when only the fold is known. GNAT enzymes participate in both categories. Without substrate-specific information, a model could reasonably argue for either option based on general GNAT family diversity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2T1AE85) annotates this protein as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the pathway explicitly stated as 'Amino-acid degradation' (evidence C5, H3), supported by experimental data including X-ray crystallography (PDB 7XRJ) and a 2023 ISME J. publication (PubMed:36690779) describing a novel D-glutamate catabolic pathway. The EC number 2.3.1.312 is a transferase (acetyltransferase) acting on D-glutamate, which is an amino acid, placing it squarely in amino-acid degradation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly contains the GNAT (GCN5-related N-acetyltransferase) fold signature motifs 'GCGANLGL' and 'VANRGGK', allowing identification as an acetyltransferase. This eliminates options B (pantothenate kinase pathway) and C (GAR synthetase, purine biosynthesis), which involve entirely different enzyme classes. However, the GNAT superfamily is enormous and acetylates an extremely diverse range of substrates: histones, polyamines, amino acids, drugs, and secondary metabolite intermediates. The GNAT fold alone does not reveal whether the acetyl acceptor is an amino acid (→ D, amino-acid degradation) or a secondary-metabolite intermediate (→ A, secondary metabolite biosynthesis). No distinctive amino-acid-binding pocket motif or subfamily-specific signature is apparent in the sequence that would reliably distinguish amino-acid acetylation from secondary-metabolite acetylation using general GNAT family knowledge.",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate) and the experimentally determined catabolic pathway assignment for this exact protein (EC 2.3.1.312, D-glutamate N-acetyltransferase, characterized in 2023). Without knowing the substrate, the GNAT fold is too promiscuous in substrate scope to distinguish 'amino-acid degradation' from 'secondary metabolite biosynthesis.'",
    "reason": "While the GNAT fold is identifiable from sequence motifs, the critical A-vs-D distinction depends on knowing the substrate is D-glutamate. The GNAT superfamily includes acetyltransferases for amino acids, polyamines, histones, antibiotics, and secondary metabolites. General family-level knowledge does not provide a reliable basis to assign this particular GNAT to amino-acid degradation rather than secondary metabolite biosynthesis. The enzyme was characterized experimentally in 2023, and its pathway assignment is a specific annotation fact about this protein rather than a predictable inference from the fold."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 'Secondary metabolite biosynthesis' and 'Amino-acid degradation' are plausible pathway assignments for a GNAT acetyltransferase when only the fold is known. GNAT enzymes participate in both categories. Without substrate-specific information, a model could reasonably argue for either option based on general GNAT family diversity."
  },
  "important_caveats": [
    "The GNAT fold is unambiguously identifiable from the sequence, which correctly eliminates options B and C.",
    "The D-glutamate N-acetyltransferase (EC 2.3.1.312) was experimentally characterized in 2023 (Yu et al., ISME J.), making it a relatively recently annotated enzyme with limited precedent in training corpora.",
    "The pathway annotation 'Amino-acid degradation' is supported by experimental evidence (PDB 7XRJ, PubMed:36690779), not merely computational inference.",
    "A model with very broad training coverage might associate specific GNAT sequence patterns with amino-acid acetylation, but this would be a learned pattern from this or closely related proteins rather than a deductive inference from general GNAT biology."
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
  "benchmark_sequence_length": 333,
  "benchmark_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-07-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 333,
  "current_source_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2T1AE85",
  "selected_historical_entry_version": 17,
  "selected_historical_record_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "selected_historical_source_sequence_length": 333,
  "selected_historical_source_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "selected_historical_version": {
    "accession": "A0A2T1AE85",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCN_TRISK",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2T1AE85\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-07-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Epibacterium scottomollicae\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Rhodobacterales\",\"Paracoccaceae\",\"Tritonibacter\"],\"scientificName\":\"Tritonibacter scottomollicae\",\"taxonId\":483013}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.312\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"D-glutamate N-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7XRJ\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 25328 / CCUG 55858 / LMG 24367 / R-28751\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H1",
  "excerpt": "ID   DGCN_TRISK              Reviewed;         333 AA.\nAC   A0A2T1AE85;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUL-2018, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcN {ECO:0000303|PubMed:36690779};\nGN   ORFNames=CLV89_10851 {ECO:0000312|EMBL:PRZ46905.1};\nOS   Tritonibacter scottomollicae (Epibacterium scottomollicae).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Rhodobacterales; Paracoccaceae; Tritonibacter.\nOX   NCBI_TaxID=483013;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7XRJ}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY, AND\nRP   MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190.\nRC   STRAIN=DSM 25328 / CCUG 55858 / LMG 24367 / R-28751;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid degradation. {ECO:0000305|PubMed:36690779}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
