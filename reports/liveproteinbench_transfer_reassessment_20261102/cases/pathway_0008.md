# pathway_0008

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0008.txt)

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
MSPRPQIKVGVLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRWKLPSPIPDAVRHMVVHECRPDAPGFAECGVVFSGLDADVAGDIENAFRAADLVVYSNAKNYRRDPLCPLIVPLVNPSHLSIIPYQREQLGLKKGYIVTNANCSTTGIVVPLAALEKAFGPLDTVIVTTLQAISGAGYPGVSSLDIMDNVVPLISGEEDKIEWETNKILGGVTPDNKAFDLHAPKQINVSATCTRVPVIDGHTGCVSVKFARSPPPSVAEVENAFREYTCDAQHLGVPSAPAQAIVVHDAPDRPQPRLDKNLHNGACVSVGRIRECPVFDIKFVCLIDNVRLGAATSSIINAEIAVEKGLIQ

[Multiple Choices]
A. Capsule biogenesis
B. iron-sulfur cluster biosynthesis. .
C. Amino-acid biosynthesis
D. L-fucose degradation. .
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

> The supplied sequence matches the source sequence. The source identifies the protein as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) and assigns it to amino-acid biosynthesis, including methionine and threonine biosynthesis. The pathway annotations carry experimental evidence codes, supporting choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the conserved NAD(P)-dependent aspartate-semialdehyde dehydrogenase family, including an N-terminal glycine-rich nucleotide-binding motif. Transferable knowledge of this enzyme family links it to the aspartate-family amino-acid biosynthesis pathway, which meaningfully favors C over capsule biogenesis, iron-sulfur cluster biosynthesis, or L-fucose degradation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family from its sequence and applying its well-established pathway role provides a credible distinction among the offered options without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may participate in multiple branches of amino-acid biosynthesis, but only one offered choice captures that pathway category.


### Important caveats

- The reviewer-only source evidence supports the key but was not part of the model's original input.
- The sequence-based family identification is a transferable inference, not direct experimental evidence from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the conserved NAD(P)-dependent aspartate-semialdehyde dehydrogenase family, including an N-terminal glycine-rich nucleotide-binding motif. Transferable knowledge of this enzyme family links it to the aspartate-family amino-acid biosynthesis pathway, which meaningfully favors C over capsule biogenesis, iron-sulfur cluster biosynthesis, or L-fucose degradation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from its sequence and applying its well-established pathway role provides a credible distinction among the offered options without needing the exact protein's database record."
  },
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence. The source identifies the protein as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) and assigns it to amino-acid biosynthesis, including methionine and threonine biosynthesis. The pathway annotations carry experimental evidence codes, supporting choice C."
  },
  "important_caveats": [
    "The reviewer-only source evidence supports the key but was not part of the model's original input.",
    "The sequence-based family identification is a transferable inference, not direct experimental evidence from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may participate in multiple branches of amino-acid biosynthesis, but only one offered choice captures that pathway category."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence. The source identifies the protein as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) and assigns it to amino-acid biosynthesis, including methionine and threonine biosynthesis. The pathway annotations carry experimental evidence codes, supporting choice C.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the conserved NAD(P)-dependent aspartate-semialdehyde dehydrogenase family, including an N-terminal glycine-rich nucleotide-binding motif. Transferable knowledge of this enzyme family links it to the aspartate-family amino-acid biosynthesis pathway, which meaningfully favors C over capsule biogenesis, iron-sulfur cluster biosynthesis, or L-fucose degradation.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from its sequence and applying its well-established pathway role provides a credible distinction among the offered options without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may participate in multiple branches of amino-acid biosynthesis, but only one offered choice captures that pathway category."
  },
  "important_caveats": [
    "The reviewer-only source evidence supports the key but was not part of the model's original input.",
    "The sequence-based family identification is a transferable inference, not direct experimental evidence from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only UniProt evidence (C4, C5, C6, H4, H5) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with explicit pathway annotations: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5'. These are supported by experimental evidence (X-ray crystallography, PubMed 26527262 and 29608391). The sequence matches the benchmark sequence exactly. The expected answer C is fully supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a clear Rossmann-fold nucleotide-binding motif 'GVLGATGTVGQ' (GxGxxG pattern) indicating an NAD(P)-dependent dehydrogenase. The mid-sequence contains 'ANCSTTGIVVPLAALE' — the 'ANC' (Ala-Asn-Cys) motif is a hallmark of the semialdehyde dehydrogenase (SSDH) superfamily. The catalytic region 'GHTGCVSVKF' places a catalytic cysteine in the conserved 'GHTGC' context characteristic of semialdehyde dehydrogenases. Transferable knowledge: semialdehyde dehydrogenases (ASADH, GSA-DH, succinic semialdehyde dehydrogenase) are oxidoreductases that convert amino-acid aldehydes to amino acids or intermediates; the aspartate-semialdehyde dehydrogenase specifically sits in the aspartate biosynthetic pathway producing homoserine → threonine/methionine. Among the four options: (A) capsule biogenesis involves glycosyltransferases and polysaccharide synthases, not Rossmann-fold dehydrogenases; (B) Fe-S cluster biosynthesis involves cysteine desulfurases (PLP-dependent), scaffold proteins, and chaperones with entirely different folds; (D) L-fucose degradation involves sugar kinases, isomerases, and aldolases, none of which use the SSDH catalytic architecture. The combination of Rossmann fold + GHTGC catalytic Cys + ANC motif uniquely identifies the semialdehyde dehydrogenase family, whose primary biological role is amino-acid biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the Rossmann fold and the semialdehyde dehydrogenase catalytic motifs (GHTGC, ANC) can infer the enzyme family from sequence alone. Family-level knowledge (learned from many homologous ASADH/GSA-DH proteins across bacteria, archaea, and eukaryotes) places this enzyme in amino-acid biosynthesis. The other three options involve mechanistically and structurally unrelated enzyme classes, making them readily excludable.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct enzyme classes (glycosyltransferases, Fe-S assembly proteins, dehydrogenases in amino-acid pathways, sugar-processing enzymes). The sequence motifs unambiguously point to a dehydrogenase in amino-acid biosynthesis, leaving no realistic ambiguity among the choices.


### Important caveats

- The reviewer-only evidence confirms the annotation experimentally (X-ray crystallography, PubMed 26527262, 29608391), but the evaluated model must rely on sequence-motif recognition and family-level transfer.
- The 'ANC' and 'GHTGC' motifs are well-conserved across the SSDH superfamily but are not absolutely unique to ASADH; however, among the four offered pathway options, only amino-acid biosynthesis is compatible with any SSDH-family member.
- The sequence is from a fungal organism (Cryptococcus deneoformans per reviewer evidence), but the family-level inference does not depend on knowing the organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a clear Rossmann-fold nucleotide-binding motif 'GVLGATGTVGQ' (GxGxxG pattern) indicating an NAD(P)-dependent dehydrogenase. The mid-sequence contains 'ANCSTTGIVVPLAALE' — the 'ANC' (Ala-Asn-Cys) motif is a hallmark of the semialdehyde dehydrogenase (SSDH) superfamily. The catalytic region 'GHTGCVSVKF' places a catalytic cysteine in the conserved 'GHTGC' context characteristic of semialdehyde dehydrogenases. Transferable knowledge: semialdehyde dehydrogenases (ASADH, GSA-DH, succinic semialdehyde dehydrogenase) are oxidoreductases that convert amino-acid aldehydes to amino acids or intermediates; the aspartate-semialdehyde dehydrogenase specifically sits in the aspartate biosynthetic pathway producing homoserine → threonine/methionine. Among the four options: (A) capsule biogenesis involves glycosyltransferases and polysaccharide synthases, not Rossmann-fold dehydrogenases; (B) Fe-S cluster biosynthesis involves cysteine desulfurases (PLP-dependent), scaffold proteins, and chaperones with entirely different folds; (D) L-fucose degradation involves sugar kinases, isomerases, and aldolases, none of which use the SSDH catalytic architecture. The combination of Rossmann fold + GHTGC catalytic Cys + ANC motif uniquely identifies the semialdehyde dehydrogenase family, whose primary biological role is amino-acid biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the Rossmann fold and the semialdehyde dehydrogenase catalytic motifs (GHTGC, ANC) can infer the enzyme family from sequence alone. Family-level knowledge (learned from many homologous ASADH/GSA-DH proteins across bacteria, archaea, and eukaryotes) places this enzyme in amino-acid biosynthesis. The other three options involve mechanistically and structurally unrelated enzyme classes, making them readily excludable."
  },
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, C6, H4, H5) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with explicit pathway annotations: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5'. These are supported by experimental evidence (X-ray crystallography, PubMed 26527262 and 29608391). The sequence matches the benchmark sequence exactly. The expected answer C is fully supported."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation experimentally (X-ray crystallography, PubMed 26527262, 29608391), but the evaluated model must rely on sequence-motif recognition and family-level transfer.",
    "The 'ANC' and 'GHTGC' motifs are well-conserved across the SSDH superfamily but are not absolutely unique to ASADH; however, among the four offered pathway options, only amino-acid biosynthesis is compatible with any SSDH-family member.",
    "The sequence is from a fungal organism (Cryptococcus deneoformans per reviewer evidence), but the family-level inference does not depend on knowing the organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct enzyme classes (glycosyltransferases, Fe-S assembly proteins, dehydrogenases in amino-acid pathways, sugar-processing enzymes). The sequence motifs unambiguously point to a dehydrogenase in amino-acid biosynthesis, leaving no realistic ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, C6, H4, H5) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with explicit pathway annotations: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5'. These are supported by experimental evidence (X-ray crystallography, PubMed 26527262 and 29608391). The sequence matches the benchmark sequence exactly. The expected answer C is fully supported.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a clear Rossmann-fold nucleotide-binding motif 'GVLGATGTVGQ' (GxGxxG pattern) indicating an NAD(P)-dependent dehydrogenase. The mid-sequence contains 'ANCSTTGIVVPLAALE' — the 'ANC' (Ala-Asn-Cys) motif is a hallmark of the semialdehyde dehydrogenase (SSDH) superfamily. The catalytic region 'GHTGCVSVKF' places a catalytic cysteine in the conserved 'GHTGC' context characteristic of semialdehyde dehydrogenases. Transferable knowledge: semialdehyde dehydrogenases (ASADH, GSA-DH, succinic semialdehyde dehydrogenase) are oxidoreductases that convert amino-acid aldehydes to amino acids or intermediates; the aspartate-semialdehyde dehydrogenase specifically sits in the aspartate biosynthetic pathway producing homoserine → threonine/methionine. Among the four options: (A) capsule biogenesis involves glycosyltransferases and polysaccharide synthases, not Rossmann-fold dehydrogenases; (B) Fe-S cluster biosynthesis involves cysteine desulfurases (PLP-dependent), scaffold proteins, and chaperones with entirely different folds; (D) L-fucose degradation involves sugar kinases, isomerases, and aldolases, none of which use the SSDH catalytic architecture. The combination of Rossmann fold + GHTGC catalytic Cys + ANC motif uniquely identifies the semialdehyde dehydrogenase family, whose primary biological role is amino-acid biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the Rossmann fold and the semialdehyde dehydrogenase catalytic motifs (GHTGC, ANC) can infer the enzyme family from sequence alone. Family-level knowledge (learned from many homologous ASADH/GSA-DH proteins across bacteria, archaea, and eukaryotes) places this enzyme in amino-acid biosynthesis. The other three options involve mechanistically and structurally unrelated enzyme classes, making them readily excludable."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct enzyme classes (glycosyltransferases, Fe-S assembly proteins, dehydrogenases in amino-acid pathways, sugar-processing enzymes). The sequence motifs unambiguously point to a dehydrogenase in amino-acid biosynthesis, leaving no realistic ambiguity among the choices."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation experimentally (X-ray crystallography, PubMed 26527262, 29608391), but the evaluated model must rely on sequence-motif recognition and family-level transfer.",
    "The 'ANC' and 'GHTGC' motifs are well-conserved across the SSDH superfamily but are not absolutely unique to ASADH; however, among the four offered pathway options, only amino-acid biosynthesis is compatible with any SSDH-family member.",
    "The sequence is from a fungal organism (Cryptococcus deneoformans per reviewer evidence), but the family-level inference does not depend on knowing the organism."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26527262\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26527262\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)

```json
{
  "evidence_id": "C8",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H3",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:26527262}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-83",
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
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:26527262}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:27.262588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4",
  "url": "https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
