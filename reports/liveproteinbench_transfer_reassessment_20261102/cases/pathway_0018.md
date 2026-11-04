# pathway_0018

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0018.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. glycosylphosphatidylinositol-anchor biosynthesis. .
B. Pigment biosynthesis. .
C. Amino-acid biosynthesis
D. deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1. .
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

> The exact sequence matches a UniProt entry annotated as aspartokinase (EC 2.7.2.4), with pathway annotations placing it in amino-acid biosynthesis. These annotations cite evidence by similarity to another UniProt protein, so they support the key but are not direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme in the aspartokinase family; family-level recognition from homologous sequences and conserved enzyme architecture provides a credible distinction. Aspartokinases catalyze an early step in aspartate-family amino-acid synthesis, supporting C over the offered GPI-anchor, pigment, and nicotinate-derived NAD pathway choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-based sequence inference meaningfully favors amino-acid biosynthesis without requiring the exact protein's database annotation. The sequence alone may not establish every functional detail, but the alternatives are sufficiently distinct for this qualitative pathway choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered broad pathway choices, amino-acid biosynthesis is the defensible choice for an aspartokinase-like protein.


### Important caveats

- The supporting pathway annotations are transferred by similarity, not shown here to be experimentally established for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme in the aspartokinase family; family-level recognition from homologous sequences and conserved enzyme architecture provides a credible distinction. Aspartokinases catalyze an early step in aspartate-family amino-acid synthesis, supporting C over the offered GPI-anchor, pigment, and nicotinate-derived NAD pathway choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-based sequence inference meaningfully favors amino-acid biosynthesis without requiring the exact protein's database annotation. The sequence alone may not establish every functional detail, but the alternatives are sufficiently distinct for this qualitative pathway choice."
  },
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartokinase (EC 2.7.2.4), with pathway annotations placing it in amino-acid biosynthesis. These annotations cite evidence by similarity to another UniProt protein, so they support the key but are not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The supporting pathway annotations are transferred by similarity, not shown here to be experimentally established for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered broad pathway choices, amino-acid biosynthesis is the defensible choice for an aspartokinase-like protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartokinase (EC 2.7.2.4), with pathway annotations placing it in amino-acid biosynthesis. These annotations cite evidence by similarity to another UniProt protein, so they support the key but are not direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme in the aspartokinase family; family-level recognition from homologous sequences and conserved enzyme architecture provides a credible distinction. Aspartokinases catalyze an early step in aspartate-family amino-acid synthesis, supporting C over the offered GPI-anchor, pigment, and nicotinate-derived NAD pathway choices.",
    "missing_item_specific_fact": "",
    "reason": "A family-based sequence inference meaningfully favors amino-acid biosynthesis without requiring the exact protein's database annotation. The sequence alone may not establish every functional detail, but the alternatives are sufficiently distinct for this qualitative pathway choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered broad pathway choices, amino-acid biosynthesis is the defensible choice for an aspartokinase-like protein."
  },
  "important_caveats": [
    "The supporting pathway annotations are transferred by similarity, not shown here to be experimentally established for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (A0A1D8PMB8) identifies this protein as Aspartokinase (EC 2.7.2.4) and assigns it to two pathways both under the heading 'Amino-acid biosynthesis': L-methionine biosynthesis (step 1/3) and L-threonine biosynthesis (step 1/5). The expected answer 'Amino-acid biosynthesis' directly matches the pathway category. The evidence code is ECO:0000250 (inferred by similarity to P10869, yeast aspartokinase), which is a computational inference but a well-supported one given strong homology. The sequence is confirmed as a match to the canonical entry.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear P-loop / Walker A motif (GGTSVGK at positions ~35-41) characteristic of the amino acid kinase superfamily. The overall domain architecture — an N-terminal kinase domain with the P-loop followed by a C-terminal regulatory domain — matches the well-known fold of aspartokinases (EC 2.7.2.4), which are the first committed enzymes in the aspartate-family amino acid biosynthesis pathway (producing lysine, methionine, and threonine). A knowledgeable model can recognize: (1) the GxGxxG phosphate-binding motif indicating a kinase; (2) the ~544 aa length and two-domain architecture typical of fungal aspartokinases; (3) the absence of transmembrane segments or glycosyltransferase motifs that would suggest GPI-anchor biosynthesis (option A); (4) the absence of polyketide synthase, tyrosinase, or other pigment-pathway motifs (option B); (5) the absence of quinolinate phosphoribosyltransferase or NAD synthetase (EC 6.3.1.5) domain features expected for the NAD biosynthesis step in option D. The amino acid kinase fold and its well-documented role as the gateway enzyme for amino acid biosynthesis provide a concrete, transferable inference that distinguishes option C from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop motif, two-domain kinase architecture, and the well-established biochemistry of the amino acid kinase superfamily (aspartokinase as the first step in aspartate-family amino acid biosynthesis) constitute transferable knowledge from other proteins in the family. This allows a knowledgeable model to identify the kinase fold, recognize it as an amino acid kinase, and select the amino-acid biosynthesis pathway over GPI-anchor, pigment, or NAD biosynthesis options without needing to recall the specific UniProt record for this Candida albicans protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct metabolic pathways. The P-loop kinase architecture and amino acid kinase fold strongly and unambiguously point to amino-acid biosynthesis (C). GPI-anchor biosynthesis (A) involves ER membrane glycosyltransferases with transmembrane domains absent here. Pigment biosynthesis (B) involves entirely different enzyme classes. The specific NAD biosynthesis step (D) involves NAD synthetase, which has a different domain organization. No two options are genuinely confusable given the sequence features.


### Important caveats

- The UniProt pathway annotation is based on similarity (ECO:0000250) to P10869 (S. cerevisiae aspartokinase), not on direct experimental validation of this Candida albicans protein.
- The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable biochemical knowledge.
- The P-loop motif is shared across many kinase families, but the specific combination of the amino acid kinase fold, domain architecture, and sequence length provides sufficient discrimination among the four offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear P-loop / Walker A motif (GGTSVGK at positions ~35-41) characteristic of the amino acid kinase superfamily. The overall domain architecture — an N-terminal kinase domain with the P-loop followed by a C-terminal regulatory domain — matches the well-known fold of aspartokinases (EC 2.7.2.4), which are the first committed enzymes in the aspartate-family amino acid biosynthesis pathway (producing lysine, methionine, and threonine). A knowledgeable model can recognize: (1) the GxGxxG phosphate-binding motif indicating a kinase; (2) the ~544 aa length and two-domain architecture typical of fungal aspartokinases; (3) the absence of transmembrane segments or glycosyltransferase motifs that would suggest GPI-anchor biosynthesis (option A); (4) the absence of polyketide synthase, tyrosinase, or other pigment-pathway motifs (option B); (5) the absence of quinolinate phosphoribosyltransferase or NAD synthetase (EC 6.3.1.5) domain features expected for the NAD biosynthesis step in option D. The amino acid kinase fold and its well-documented role as the gateway enzyme for amino acid biosynthesis provide a concrete, transferable inference that distinguishes option C from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif, two-domain kinase architecture, and the well-established biochemistry of the amino acid kinase superfamily (aspartokinase as the first step in aspartate-family amino acid biosynthesis) constitute transferable knowledge from other proteins in the family. This allows a knowledgeable model to identify the kinase fold, recognize it as an amino acid kinase, and select the amino-acid biosynthesis pathway over GPI-anchor, pigment, or NAD biosynthesis options without needing to recall the specific UniProt record for this Candida albicans protein."
  },
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (A0A1D8PMB8) identifies this protein as Aspartokinase (EC 2.7.2.4) and assigns it to two pathways both under the heading 'Amino-acid biosynthesis': L-methionine biosynthesis (step 1/3) and L-threonine biosynthesis (step 1/5). The expected answer 'Amino-acid biosynthesis' directly matches the pathway category. The evidence code is ECO:0000250 (inferred by similarity to P10869, yeast aspartokinase), which is a computational inference but a well-supported one given strong homology. The sequence is confirmed as a match to the canonical entry."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on similarity (ECO:0000250) to P10869 (S. cerevisiae aspartokinase), not on direct experimental validation of this Candida albicans protein.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable biochemical knowledge.",
    "The P-loop motif is shared across many kinase families, but the specific combination of the amino acid kinase fold, domain architecture, and sequence length provides sufficient discrimination among the four offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct metabolic pathways. The P-loop kinase architecture and amino acid kinase fold strongly and unambiguously point to amino-acid biosynthesis (C). GPI-anchor biosynthesis (A) involves ER membrane glycosyltransferases with transmembrane domains absent here. Pigment biosynthesis (B) involves entirely different enzyme classes. The specific NAD biosynthesis step (D) involves NAD synthetase, which has a different domain organization. No two options are genuinely confusable given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (A0A1D8PMB8) identifies this protein as Aspartokinase (EC 2.7.2.4) and assigns it to two pathways both under the heading 'Amino-acid biosynthesis': L-methionine biosynthesis (step 1/3) and L-threonine biosynthesis (step 1/5). The expected answer 'Amino-acid biosynthesis' directly matches the pathway category. The evidence code is ECO:0000250 (inferred by similarity to P10869, yeast aspartokinase), which is a computational inference but a well-supported one given strong homology. The sequence is confirmed as a match to the canonical entry.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear P-loop / Walker A motif (GGTSVGK at positions ~35-41) characteristic of the amino acid kinase superfamily. The overall domain architecture — an N-terminal kinase domain with the P-loop followed by a C-terminal regulatory domain — matches the well-known fold of aspartokinases (EC 2.7.2.4), which are the first committed enzymes in the aspartate-family amino acid biosynthesis pathway (producing lysine, methionine, and threonine). A knowledgeable model can recognize: (1) the GxGxxG phosphate-binding motif indicating a kinase; (2) the ~544 aa length and two-domain architecture typical of fungal aspartokinases; (3) the absence of transmembrane segments or glycosyltransferase motifs that would suggest GPI-anchor biosynthesis (option A); (4) the absence of polyketide synthase, tyrosinase, or other pigment-pathway motifs (option B); (5) the absence of quinolinate phosphoribosyltransferase or NAD synthetase (EC 6.3.1.5) domain features expected for the NAD biosynthesis step in option D. The amino acid kinase fold and its well-documented role as the gateway enzyme for amino acid biosynthesis provide a concrete, transferable inference that distinguishes option C from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif, two-domain kinase architecture, and the well-established biochemistry of the amino acid kinase superfamily (aspartokinase as the first step in aspartate-family amino acid biosynthesis) constitute transferable knowledge from other proteins in the family. This allows a knowledgeable model to identify the kinase fold, recognize it as an amino acid kinase, and select the amino-acid biosynthesis pathway over GPI-anchor, pigment, or NAD biosynthesis options without needing to recall the specific UniProt record for this Candida albicans protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct metabolic pathways. The P-loop kinase architecture and amino acid kinase fold strongly and unambiguously point to amino-acid biosynthesis (C). GPI-anchor biosynthesis (A) involves ER membrane glycosyltransferases with transmembrane domains absent here. Pigment biosynthesis (B) involves entirely different enzyme classes. The specific NAD biosynthesis step (D) involves NAD synthetase, which has a different domain organization. No two options are genuinely confusable given the sequence features."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on similarity (ECO:0000250) to P10869 (S. cerevisiae aspartokinase), not on direct experimental validation of this Candida albicans protein.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable biochemical knowledge.",
    "The P-loop motif is shared across many kinase families, but the specific combination of the amino acid kinase fold, domain architecture, and sequence length provides sufficient discrimination among the four offered choices."
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
  "benchmark_sequence_length": 544,
  "benchmark_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 544,
  "current_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 39,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1D8PMB8",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "selected_historical_source_sequence_length": 544,
  "selected_historical_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "selected_historical_version": {
    "accession": "A0A1D8PMB8",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1D8PMB8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CANAL                Reviewed;         544 AA.\nAC   A0A1D8PMB8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   18-JUN-2025, entry version 39.\nDE   RecName: Full=Aspartokinase;\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};\nGN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},\nGN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 1/3.\nCC       {ECO:0000250|UniProtKB:P10869}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 1/5. {ECO:0000250|UniProtKB:P10869}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
