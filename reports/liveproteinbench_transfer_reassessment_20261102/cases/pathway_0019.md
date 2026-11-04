# pathway_0019

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0019.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTIRGTLSELSRAADAFAHEVDEAGYGDYTFLPDNSPFDLSFLTSKGLEARGSLIAAAEKILRLAKGPQGCLASFADTKGIEMGTIQALTQLEVPDKVPLQGSITYEELAGVIRVAPELLQRLVRLAALAGFLIEDESGAVRHTAMSAVFLRDTAAGDTARFLFDVDMRAYSFFADSLRLDPSGQNIGDGPTALAFQHDSDDQGNRPTIWDILERNPIQRARFHSTMQALGSFPSHLLKHILVAHDWHSIGSLVDVGGSLGHASLVIAENFPEIRITVQDLPDVVERGRSSLPTVPHAERVSFQAHDLFQEQAIIADAYFLRQILHDWPDGDAERIVRCLIPAMRPGAKLLIMDIVVPEPGAISPYMEKYLRTYDVSMFSMFSAKERTVQQLRDLVERCSARLQFQGISCPPGSATSLLSWVYSAE

[Multiple Choices]
A. Pyrimidine metabolism
B. Secondary metabolite biosynthesis. .
C. Glycan degradation
D. tetrahydrofolate interconversion. .
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

> The exact sequence matches the archived UniProt record, which annotates the pathway as secondary metabolite biosynthesis and cites a publication with pathway evidence coded experimental. This supports B as a database annotation, though the excerpts do not independently establish the details of the experiments.

Citations as saved: [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble O-methyltransferase. Transferable knowledge about this enzyme class makes a tailoring role in secondary-metabolite biosynthesis a plausible choice: such enzymes methylate small-molecule intermediates, whereas pyrimidine and tetrahydrofolate pathways involve more specific nucleotide- or folate-processing enzymes. That makes B meaningfully more plausible among these options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supports a useful enzyme-family inference, and the offered alternatives permit a probabilistic pathway distinction without needing the exact protein's database annotation. The sequence alone does not identify the methyl acceptor or prove its pathway, so the inference is not certain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The pathway is not uniquely established from sequence alone, but the available enzyme-family inference favors B over the listed alternatives; no second option is comparably supported.


### Important caveats

- The pathway evidence is a database annotation linked to a publication, not an independent review of the underlying experiments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble O-methyltransferase. Transferable knowledge about this enzyme class makes a tailoring role in secondary-metabolite biosynthesis a plausible choice: such enzymes methylate small-molecule intermediates, whereas pyrimidine and tetrahydrofolate pathways involve more specific nucleotide- or folate-processing enzymes. That makes B meaningfully more plausible among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a useful enzyme-family inference, and the offered alternatives permit a probabilistic pathway distinction without needing the exact protein's database annotation. The sequence alone does not identify the methyl acceptor or prove its pathway, so the inference is not certain."
  },
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt record, which annotates the pathway as secondary metabolite biosynthesis and cites a publication with pathway evidence coded experimental. This supports B as a database annotation, though the excerpts do not independently establish the details of the experiments."
  },
  "important_caveats": [
    "The pathway evidence is a database annotation linked to a publication, not an independent review of the underlying experiments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The pathway is not uniquely established from sequence alone, but the available enzyme-family inference favors B over the listed alternatives; no second option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt record, which annotates the pathway as secondary metabolite biosynthesis and cites a publication with pathway evidence coded experimental. This supports B as a database annotation, though the excerpts do not independently establish the details of the experiments.",
    "evidence_ids": ["H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble O-methyltransferase. Transferable knowledge about this enzyme class makes a tailoring role in secondary-metabolite biosynthesis a plausible choice: such enzymes methylate small-molecule intermediates, whereas pyrimidine and tetrahydrofolate pathways involve more specific nucleotide- or folate-processing enzymes. That makes B meaningfully more plausible among these options.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a useful enzyme-family inference, and the offered alternatives permit a probabilistic pathway distinction without needing the exact protein's database annotation. The sequence alone does not identify the methyl acceptor or prove its pathway, so the inference is not certain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The pathway is not uniquely established from sequence alone, but the available enzyme-family inference favors B over the listed alternatives; no second option is comparably supported."
  },
  "important_caveats": [
    "The pathway evidence is a database annotation linked to a publication, not an independent review of the underlying experiments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8J1Z8) annotates this protein as O-methyltransferase FrzF, a component of the FR901483 biosynthesis cluster in Cladobotryum sp. The pathway annotation 'Secondary metabolite biosynthesis' carries evidence code ECO:0000269 (experimental evidence) from PubMed:33372776 (Zhang et al., JACS 2021). The sequence matches exactly (427 aa, SHA-256 confirmed). The answer B is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'DVGG' motif (visible in 'VDVGGSLGHASLVIAEN'), a hallmark of the Class I SAM-dependent methyltransferase fold (Rossmann-like). This is a conserved feature shared across hundreds of characterized methyltransferases (e.g., catechol-O-methyltransferase, DNA methyltransferases, many fungal tailoring methyltransferases), so it is transferable family knowledge. This immediately excludes A (pyrimidine metabolism: carbamoyl phosphate synthetase, dihydroorotase, thymidylate synthase, etc. have entirely different folds and motifs such as 'GGD' or carbamoyl-transferase motifs) and C (glycan degradation: glycosidases require catalytic Asp/Glu pairs, often signal peptides, CBMs, and GH-family folds). Between B and D, folate-interconversion enzymes (DHFR, thymidylate synthase, SHMT, MTHFR) are folate- or PLP-dependent and lack the DVGG SAM-binding motif; they have distinct structural architectures. Furthermore, a well-learned pattern in fungal genomics is that SAM-dependent methyltransferases encoded within biosynthetic gene clusters serve as tailoring enzymes for secondary metabolites (polyketides, NRPS products, terpenes), rather than participating in primary folate or pyrimidine metabolism. The ~427 aa size, absence of transmembrane segments, and lack of any primary-metabolism enzyme motif further support the secondary-metabolite tailoring role. Thus, recognizing the methyltransferase fold and applying the fungal secondary-metabolite-cluster context meaningfully distinguishes B from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DVGG SAM-methyltransferase motif is a sequence-visible, family-level feature learned from many characterized methyltransferases. Combined with the exclusion of pyrimidine, glycan-degrading, and folate-pathway enzyme architectures, and the well-established fungal pattern of methyltransferases as secondary-metabolite tailoring enzymes, a knowledgeable model can arrive at B without recalling this specific protein's UniProt record. The inference is probabilistic but concrete and multi-step.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The DVGG methyltransferase motif cleanly separates the protein from pyrimidine enzymes (A) and glycan-degrading enzymes (C). The SAM-dependent methyltransferase fold is structurally and mechanistically distinct from folate-dependent enzymes in tetrahydrofolate interconversion (D). No other option is a credible alternative once the methyltransferase identity is recognized.


### Important caveats

- The specific secondary metabolite (FR901483) is not identifiable from sequence alone; the question only requires the broad pathway category, which is addressable via the methyltransferase/fungal-cluster inference.
- The DVGG motif recognition from a raw 427-aa sequence requires some training in methyltransferase sequence motifs; a model without this background might struggle, but the question is assessed for whether transferable knowledge CAN distinguish the choices, not whether every model will.
- The UniProt annotation is experimental (ECO:0000269), lending strong support to the key, but the model's reasoning path is independent of this annotation.
- The organism (Cladobotryum sp., a fungus) is not provided in the original input; the fungal secondary-metabolite-cluster inference relies on the methyltransferase context and the absence of primary-metabolism enzyme features, which is a reasonable generalization but not a certainty for every methyltransferase.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'DVGG' motif (visible in 'VDVGGSLGHASLVIAEN'), a hallmark of the Class I SAM-dependent methyltransferase fold (Rossmann-like). This is a conserved feature shared across hundreds of characterized methyltransferases (e.g., catechol-O-methyltransferase, DNA methyltransferases, many fungal tailoring methyltransferases), so it is transferable family knowledge. This immediately excludes A (pyrimidine metabolism: carbamoyl phosphate synthetase, dihydroorotase, thymidylate synthase, etc. have entirely different folds and motifs such as 'GGD' or carbamoyl-transferase motifs) and C (glycan degradation: glycosidases require catalytic Asp/Glu pairs, often signal peptides, CBMs, and GH-family folds). Between B and D, folate-interconversion enzymes (DHFR, thymidylate synthase, SHMT, MTHFR) are folate- or PLP-dependent and lack the DVGG SAM-binding motif; they have distinct structural architectures. Furthermore, a well-learned pattern in fungal genomics is that SAM-dependent methyltransferases encoded within biosynthetic gene clusters serve as tailoring enzymes for secondary metabolites (polyketides, NRPS products, terpenes), rather than participating in primary folate or pyrimidine metabolism. The ~427 aa size, absence of transmembrane segments, and lack of any primary-metabolism enzyme motif further support the secondary-metabolite tailoring role. Thus, recognizing the methyltransferase fold and applying the fungal secondary-metabolite-cluster context meaningfully distinguishes B from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DVGG SAM-methyltransferase motif is a sequence-visible, family-level feature learned from many characterized methyltransferases. Combined with the exclusion of pyrimidine, glycan-degrading, and folate-pathway enzyme architectures, and the well-established fungal pattern of methyltransferases as secondary-metabolite tailoring enzymes, a knowledgeable model can arrive at B without recalling this specific protein's UniProt record. The inference is probabilistic but concrete and multi-step."
  },
  "case_id": "pathway_0019",
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
    "reason": "The UniProt entry (A0A7T8J1Z8) annotates this protein as O-methyltransferase FrzF, a component of the FR901483 biosynthesis cluster in Cladobotryum sp. The pathway annotation 'Secondary metabolite biosynthesis' carries evidence code ECO:0000269 (experimental evidence) from PubMed:33372776 (Zhang et al., JACS 2021). The sequence matches exactly (427 aa, SHA-256 confirmed). The answer B is directly and experimentally supported."
  },
  "important_caveats": [
    "The specific secondary metabolite (FR901483) is not identifiable from sequence alone; the question only requires the broad pathway category, which is addressable via the methyltransferase/fungal-cluster inference.",
    "The DVGG motif recognition from a raw 427-aa sequence requires some training in methyltransferase sequence motifs; a model without this background might struggle, but the question is assessed for whether transferable knowledge CAN distinguish the choices, not whether every model will.",
    "The UniProt annotation is experimental (ECO:0000269), lending strong support to the key, but the model's reasoning path is independent of this annotation.",
    "The organism (Cladobotryum sp., a fungus) is not provided in the original input; the fungal secondary-metabolite-cluster inference relies on the methyltransferase context and the absence of primary-metabolism enzyme features, which is a reasonable generalization but not a certainty for every methyltransferase."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The DVGG methyltransferase motif cleanly separates the protein from pyrimidine enzymes (A) and glycan-degrading enzymes (C). The SAM-dependent methyltransferase fold is structurally and mechanistically distinct from folate-dependent enzymes in tetrahydrofolate interconversion (D). No other option is a credible alternative once the methyltransferase identity is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1Z8) annotates this protein as O-methyltransferase FrzF, a component of the FR901483 biosynthesis cluster in Cladobotryum sp. The pathway annotation 'Secondary metabolite biosynthesis' carries evidence code ECO:0000269 (experimental evidence) from PubMed:33372776 (Zhang et al., JACS 2021). The sequence matches exactly (427 aa, SHA-256 confirmed). The answer B is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'DVGG' motif (visible in 'VDVGGSLGHASLVIAEN'), a hallmark of the Class I SAM-dependent methyltransferase fold (Rossmann-like). This is a conserved feature shared across hundreds of characterized methyltransferases (e.g., catechol-O-methyltransferase, DNA methyltransferases, many fungal tailoring methyltransferases), so it is transferable family knowledge. This immediately excludes A (pyrimidine metabolism: carbamoyl phosphate synthetase, dihydroorotase, thymidylate synthase, etc. have entirely different folds and motifs such as 'GGD' or carbamoyl-transferase motifs) and C (glycan degradation: glycosidases require catalytic Asp/Glu pairs, often signal peptides, CBMs, and GH-family folds). Between B and D, folate-interconversion enzymes (DHFR, thymidylate synthase, SHMT, MTHFR) are folate- or PLP-dependent and lack the DVGG SAM-binding motif; they have distinct structural architectures. Furthermore, a well-learned pattern in fungal genomics is that SAM-dependent methyltransferases encoded within biosynthetic gene clusters serve as tailoring enzymes for secondary metabolites (polyketides, NRPS products, terpenes), rather than participating in primary folate or pyrimidine metabolism. The ~427 aa size, absence of transmembrane segments, and lack of any primary-metabolism enzyme motif further support the secondary-metabolite tailoring role. Thus, recognizing the methyltransferase fold and applying the fungal secondary-metabolite-cluster context meaningfully distinguishes B from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The DVGG SAM-methyltransferase motif is a sequence-visible, family-level feature learned from many characterized methyltransferases. Combined with the exclusion of pyrimidine, glycan-degrading, and folate-pathway enzyme architectures, and the well-established fungal pattern of methyltransferases as secondary-metabolite tailoring enzymes, a knowledgeable model can arrive at B without recalling this specific protein's UniProt record. The inference is probabilistic but concrete and multi-step."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The DVGG methyltransferase motif cleanly separates the protein from pyrimidine enzymes (A) and glycan-degrading enzymes (C). The SAM-dependent methyltransferase fold is structurally and mechanistically distinct from folate-dependent enzymes in tetrahydrofolate interconversion (D). No other option is a credible alternative once the methyltransferase identity is recognized."
  },
  "important_caveats": [
    "The specific secondary metabolite (FR901483) is not identifiable from sequence alone; the question only requires the broad pathway category, which is addressable via the methyltransferase/fungal-cluster inference.",
    "The DVGG motif recognition from a raw 427-aa sequence requires some training in methyltransferase sequence motifs; a model without this background might struggle, but the question is assessed for whether transferable knowledge CAN distinguish the choices, not whether every model will.",
    "The UniProt annotation is experimental (ECO:0000269), lending strong support to the key, but the model's reasoning path is independent of this annotation.",
    "The organism (Cladobotryum sp., a fungus) is not provided in the original input; the fungal secondary-metabolite-cluster inference relies on the methyltransferase context and the absence of primary-metabolism enzyme features, which is a reasonable generalization but not a certainty for every methyltransferase."
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
  "benchmark_sequence_length": 427,
  "benchmark_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 427,
  "current_source_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
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
  "requested_accession": "A0A7T8J1Z8",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "selected_historical_source_sequence_length": 427,
  "selected_historical_source_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "selected_historical_version": {
    "accession": "A0A7T8J1Z8",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZF_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8J1Z8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase FrzF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   FRZF_CLASX              Reviewed;         427 AA.\nAC   A0A7T8J1Z8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=O-methyltransferase FrzF {ECO:0000303|PubMed:33372776};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein F {ECO:0000303|PubMed:33372776};\nGN   Name=FrzF {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
