# pathway_0089

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0089.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLTAVATAVSAVTASPLEALKRGIQPGTGVHDGYFYSFWTDGRGYVDFNNGPRGSYRVSWSNVNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAYGSYNPSSGAARLGTIEDDGGVYDIYRTRRINQPSIIGTASFDQYWSVRRQKRVGGTIDTGKHFDEWRRQGNLQLGAWNYMIMATEGYQSSGSAEIEVRSLD

[Multiple Choices]
A. xylan degradation. .
B. Glycan degradation
C. Antifungal biosynthesis. .
D. Pigment biosynthesis. .
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

> The sequence-matched entry identifies the protein as an endo-1,4-beta-xylanase and annotates its pathway as both glycan degradation and xylan degradation. Thus B is scientifically supported, although it is not the only defensible option.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted fungal enzyme, and the sequence is consistent with a GH11 xylanase. Transferable knowledge that GH11 xylanases hydrolyze xylan supports xylan degradation (A); because xylan is a glycan, it also supports the broader glycan-degradation category (B). These features distinguish both from antifungal and pigment biosynthesis, but do not uniquely select B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A meaningful pathway inference is possible from the sequence and transferable enzyme-family knowledge. The exact target annotation is not needed to distinguish these pathway choices from C and D, but the overlap between A and B prevents a unique choice between them.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Xylan is a glycan, so degradation of xylan is a form of glycan degradation. The sequence-matched annotation explicitly lists both pathways.


### Important caveats

- The reviewer-only source evidence was not part of the original model input.
- The source supports the keyed answer but also directly supports option A; the choices overlap in scope.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal enzyme, and the sequence is consistent with a GH11 xylanase. Transferable knowledge that GH11 xylanases hydrolyze xylan supports xylan degradation (A); because xylan is a glycan, it also supports the broader glycan-degradation category (B). These features distinguish both from antifungal and pigment biosynthesis, but do not uniquely select B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A meaningful pathway inference is possible from the sequence and transferable enzyme-family knowledge. The exact target annotation is not needed to distinguish these pathway choices from C and D, but the overlap between A and B prevents a unique choice between them."
  },
  "case_id": "pathway_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry identifies the protein as an endo-1,4-beta-xylanase and annotates its pathway as both glycan degradation and xylan degradation. Thus B is scientifically supported, although it is not the only defensible option."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original model input.",
    "The source supports the keyed answer but also directly supports option A; the choices overlap in scope."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Xylan is a glycan, so degradation of xylan is a form of glycan degradation. The sequence-matched annotation explicitly lists both pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry identifies the protein as an endo-1,4-beta-xylanase and annotates its pathway as both glycan degradation and xylan degradation. Thus B is scientifically supported, although it is not the only defensible option.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal enzyme, and the sequence is consistent with a GH11 xylanase. Transferable knowledge that GH11 xylanases hydrolyze xylan supports xylan degradation (A); because xylan is a glycan, it also supports the broader glycan-degradation category (B). These features distinguish both from antifungal and pigment biosynthesis, but do not uniquely select B over A.",
    "missing_item_specific_fact": "",
    "reason": "A meaningful pathway inference is possible from the sequence and transferable enzyme-family knowledge. The exact target annotation is not needed to distinguish these pathway choices from C and D, but the overlap between A and B prevents a unique choice between them."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Xylan is a glycan, so degradation of xylan is a form of glycan degradation. The sequence-matched annotation explicitly lists both pathways."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original model input.",
    "The source supports the keyed answer but also directly supports option A; the choices overlap in scope."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt pathway annotation for this sequence (V9TS54, Endo-1,4-beta-xylanase 11A, GH11 family) explicitly states 'Glycan degradation; xylan degradation' (evidence C5/H3). In UniProt's hierarchical pathway format, 'Glycan degradation' is the primary (parent) pathway category with 'xylan degradation' as the specific sub-pathway. The author's choice of B (Glycan degradation) as the 'primary metabolic pathway' is consistent with this hierarchical annotation. The EC 3.2.1.8 designation and experimental characterization (PubMed 24262572) confirm glycoside hydrolase activity within the glycan degradation pathway.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits multiple features diagnostic of a GH11-family glycoside hydrolase: (1) a classic fungal N-terminal secretory signal peptide (MVSFTTLLTAVATAVSAVTASPLEALK) indicating extracellular function; (2) a tryptophan-rich pattern (WNNW, WNNWNVNSY, WNYMIM) characteristic of the GH11 β-jelly-roll fold's substrate-binding cleft; (3) glycine-rich loops and the overall ~221-residue length matching the GH11 domain architecture. From transferable family knowledge, GH11 enzymes are xylanases—glycoside hydrolases that cleave β-1,4-xylosidic bonds in xylan, a plant cell-wall polysaccharide (glycan). Glycoside hydrolases universally function in glycan degradation pathways. This immediately eliminates C (antifungal biosynthesis) and D (pigment biosynthesis), which involve entirely different enzymatic chemistries (e.g., polyketide or non-ribosomal peptide synthetase machinery). Between A and B, the question asks for the 'primary' pathway. In standard pathway database hierarchies (KEGG map00500, UniProt pathway comments), 'Glycan degradation' is the top-level pathway name, while 'xylan degradation' is a sub-process nested within it. Recognizing this convention from general pathway-database knowledge supports selecting B as the 'primary' pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the GH11 xylanase family from sequence composition (signal peptide, Trp/Gly-rich pattern, length), infer glycoside hydrolase function, and apply the standard pathway-hierarchy convention to select 'Glycan degradation' as the primary pathway over the sub-pathway 'xylan degradation.' Options C and D are excluded by the fundamental enzymatic chemistry implied by the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> The UniProt annotation lists both 'Glycan degradation' and 'xylan degradation' in the same pathway line. A model or annotator interpreting 'primary pathway' as 'the most specific pathway this enzyme participates in' could reasonably select A (xylan degradation) rather than B (glycan degradation). However, the hierarchical convention (parent; child) and the word 'primary' favor B. The ambiguity is mild but present because both terms appear in the same annotation and both are factually correct descriptions of the enzyme's pathway role.


### Important caveats

- The sequence was matched to UniProt V9TS54 (Endo-1,4-beta-xylanase 11A, GH11) with experimental EC 3.2.1.8 assignment from PubMed 24262572.
- The pathway annotation combines a RuleBase computational inference (ECO:0000255) with experimental evidence (ECO:0000269, PubMed 24262572).
- The distinction between A and B hinges on interpreting 'primary pathway' as the top-level hierarchical category versus the most specific sub-pathway; the question wording slightly favors B but does not fully exclude A.
- The reviewer-only accession and organism identity were not available to the evaluated model; the sequence-based reasoning relies solely on recognizable GH11 family features and general pathway-hierarchy conventions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits multiple features diagnostic of a GH11-family glycoside hydrolase: (1) a classic fungal N-terminal secretory signal peptide (MVSFTTLLTAVATAVSAVTASPLEALK) indicating extracellular function; (2) a tryptophan-rich pattern (WNNW, WNNWNVNSY, WNYMIM) characteristic of the GH11 β-jelly-roll fold's substrate-binding cleft; (3) glycine-rich loops and the overall ~221-residue length matching the GH11 domain architecture. From transferable family knowledge, GH11 enzymes are xylanases—glycoside hydrolases that cleave β-1,4-xylosidic bonds in xylan, a plant cell-wall polysaccharide (glycan). Glycoside hydrolases universally function in glycan degradation pathways. This immediately eliminates C (antifungal biosynthesis) and D (pigment biosynthesis), which involve entirely different enzymatic chemistries (e.g., polyketide or non-ribosomal peptide synthetase machinery). Between A and B, the question asks for the 'primary' pathway. In standard pathway database hierarchies (KEGG map00500, UniProt pathway comments), 'Glycan degradation' is the top-level pathway name, while 'xylan degradation' is a sub-process nested within it. Recognizing this convention from general pathway-database knowledge supports selecting B as the 'primary' pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GH11 xylanase family from sequence composition (signal peptide, Trp/Gly-rich pattern, length), infer glycoside hydrolase function, and apply the standard pathway-hierarchy convention to select 'Glycan degradation' as the primary pathway over the sub-pathway 'xylan degradation.' Options C and D are excluded by the fundamental enzymatic chemistry implied by the sequence."
  },
  "case_id": "pathway_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for this sequence (V9TS54, Endo-1,4-beta-xylanase 11A, GH11 family) explicitly states 'Glycan degradation; xylan degradation' (evidence C5/H3). In UniProt's hierarchical pathway format, 'Glycan degradation' is the primary (parent) pathway category with 'xylan degradation' as the specific sub-pathway. The author's choice of B (Glycan degradation) as the 'primary metabolic pathway' is consistent with this hierarchical annotation. The EC 3.2.1.8 designation and experimental characterization (PubMed 24262572) confirm glycoside hydrolase activity within the glycan degradation pathway."
  },
  "important_caveats": [
    "The sequence was matched to UniProt V9TS54 (Endo-1,4-beta-xylanase 11A, GH11) with experimental EC 3.2.1.8 assignment from PubMed 24262572.",
    "The pathway annotation combines a RuleBase computational inference (ECO:0000255) with experimental evidence (ECO:0000269, PubMed 24262572).",
    "The distinction between A and B hinges on interpreting 'primary pathway' as the top-level hierarchical category versus the most specific sub-pathway; the question wording slightly favors B but does not fully exclude A.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the sequence-based reasoning relies solely on recognizable GH11 family features and general pathway-hierarchy conventions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "The UniProt annotation lists both 'Glycan degradation' and 'xylan degradation' in the same pathway line. A model or annotator interpreting 'primary pathway' as 'the most specific pathway this enzyme participates in' could reasonably select A (xylan degradation) rather than B (glycan degradation). However, the hierarchical convention (parent; child) and the word 'primary' favor B. The ambiguity is mild but present because both terms appear in the same annotation and both are factually correct descriptions of the enzyme's pathway role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for this sequence (V9TS54, Endo-1,4-beta-xylanase 11A, GH11 family) explicitly states 'Glycan degradation; xylan degradation' (evidence C5/H3). In UniProt's hierarchical pathway format, 'Glycan degradation' is the primary (parent) pathway category with 'xylan degradation' as the specific sub-pathway. The author's choice of B (Glycan degradation) as the 'primary metabolic pathway' is consistent with this hierarchical annotation. The EC 3.2.1.8 designation and experimental characterization (PubMed 24262572) confirm glycoside hydrolase activity within the glycan degradation pathway.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits multiple features diagnostic of a GH11-family glycoside hydrolase: (1) a classic fungal N-terminal secretory signal peptide (MVSFTTLLTAVATAVSAVTASPLEALK) indicating extracellular function; (2) a tryptophan-rich pattern (WNNW, WNNWNVNSY, WNYMIM) characteristic of the GH11 β-jelly-roll fold's substrate-binding cleft; (3) glycine-rich loops and the overall ~221-residue length matching the GH11 domain architecture. From transferable family knowledge, GH11 enzymes are xylanases—glycoside hydrolases that cleave β-1,4-xylosidic bonds in xylan, a plant cell-wall polysaccharide (glycan). Glycoside hydrolases universally function in glycan degradation pathways. This immediately eliminates C (antifungal biosynthesis) and D (pigment biosynthesis), which involve entirely different enzymatic chemistries (e.g., polyketide or non-ribosomal peptide synthetase machinery). Between A and B, the question asks for the 'primary' pathway. In standard pathway database hierarchies (KEGG map00500, UniProt pathway comments), 'Glycan degradation' is the top-level pathway name, while 'xylan degradation' is a sub-process nested within it. Recognizing this convention from general pathway-database knowledge supports selecting B as the 'primary' pathway.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GH11 xylanase family from sequence composition (signal peptide, Trp/Gly-rich pattern, length), infer glycoside hydrolase function, and apply the standard pathway-hierarchy convention to select 'Glycan degradation' as the primary pathway over the sub-pathway 'xylan degradation.' Options C and D are excluded by the fundamental enzymatic chemistry implied by the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "The UniProt annotation lists both 'Glycan degradation' and 'xylan degradation' in the same pathway line. A model or annotator interpreting 'primary pathway' as 'the most specific pathway this enzyme participates in' could reasonably select A (xylan degradation) rather than B (glycan degradation). However, the hierarchical convention (parent; child) and the word 'primary' favor B. The ambiguity is mild but present because both terms appear in the same annotation and both are factually correct descriptions of the enzyme's pathway role."
  },
  "important_caveats": [
    "The sequence was matched to UniProt V9TS54 (Endo-1,4-beta-xylanase 11A, GH11) with experimental EC 3.2.1.8 assignment from PubMed 24262572.",
    "The pathway annotation combines a RuleBase computational inference (ECO:0000255) with experimental evidence (ECO:0000269, PubMed 24262572).",
    "The distinction between A and B hinges on interpreting 'primary pathway' as the top-level hierarchical category versus the most specific sub-pathway; the question wording slightly favors B but does not fully exclude A.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the sequence-based reasoning relies solely on recognizable GH11 family features and general pathway-hierarchy conventions."
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
  "benchmark_sequence_length": 221,
  "benchmark_sequence_sha256": "6e283cc779810dd9174f1b61924b8c74d0bd81ae7161f1184006352195efc500",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 221,
  "current_source_sequence_sha256": "6e283cc779810dd9174f1b61924b8c74d0bd81ae7161f1184006352195efc500",
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
  "requested_accession": "V9TS54",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "selected_historical_source_sequence_length": 221,
  "selected_historical_source_sequence_sha256": "6e283cc779810dd9174f1b61924b8c74d0bd81ae7161f1184006352195efc500",
  "selected_historical_version": {
    "accession": "V9TS54",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XY11A_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"V9TS54\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase 11A\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase 11A\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylanase 11A\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362015\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Shi P.\",\"Huang H.\",\"Luo H.\",\"Wang Y.\",\"Zhang W.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24262572\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.foodchem.2013.10.062\"}],\"citationType\":\"journal article\",\"firstPage\":\"381\",\"id\":\"24262572\",\"journal\":\"Food Chem.\",\"lastPage\":\"387\",\"publicationDate\":\"2014\",\"title\":\"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.\",\"volume\":\"148\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   XY11A_HUMIN             Reviewed;         221 AA.\nAC   V9TS54;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   18-JUN-2025, entry version 39.\nDE   RecName: Full=Endo-1,4-beta-xylanase 11A {ECO:0000303|PubMed:24262572};\nDE            Short=Xylanase 11A {ECO:0000303|PubMed:24262572};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:24262572};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11A {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=Xyn11A {ECO:0000303|PubMed:24262572};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;\nRA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;\nRT   \"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and\nRT   one GH11 xylanase from Humicola insolens and their synergy in the\nRT   degradation of xylan.\";\nRL   Food Chem. 148:381-387(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation.\nCC       {ECO:0000255|RuleBase:RU362015, ECO:0000269|PubMed:24262572}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
