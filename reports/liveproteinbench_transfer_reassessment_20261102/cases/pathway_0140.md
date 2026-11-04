# pathway_0140

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0140.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTGFLPEPLRMLVTSPALLDFTSDGPLPYALRQKFTGKPPPVTSNLSLASQTVLVTGATSGVGLEAARQLAQLGPRLLILGVRNASKAEQIKSELERDTPNLTVQVAELDLESLLSVDRFVDELSANSIRLDLALLNAGFFAHDDRITDDGYSPLFQVNFLSTAYLTLKLLPLLHTTAPPHPPGTTTPPGPRLVLVTSEAHAWTTFPDVPRPTENRTQPILSVFQDKNTLGSADDQYARAKLLLALFGKELSRRLTAAENDTTVVITTPGFCASNFFPDGMMTRLIQLTSARSVQQGGALHVFAATAPGPEIHGAYLRDGKPTGLSKFAQGPQGQILQERLWGEMEEFFMQRGGSPLGM

[Multiple Choices]
A. Steroid biosynthesis
B. Membrane lipid metabolism. .
C. Antifungal biosynthesis. .
D. Cell wall degradation
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

> The sequence-matched historical UniProt record assigns this protein to antifungal biosynthesis and cites experimental evidence (ECO:0000269). This supports choice C, though it is not an independent validation of the underlying study.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a glycine-rich motif consistent with a Rossmann-type nucleotide-binding enzyme, and its length and motifs are compatible with a short-chain dehydrogenase/reductase. That broad enzyme-family inference does not distinguish antifungal biosynthesis from steroid or membrane-lipid metabolism, which can also involve dehydrogenases.


**Missing item-specific fact**

> The protein's membership in the specific biosynthetic pathway or cluster, or experimental evidence establishing its pathway role, is absent from the original input.


**Reason**

> The sequence supports a broad enzyme-family inference but provides no clearly pathway-diagnostic feature among the offered choices. Distinguishing choice C requires the protein-specific pathway or cluster association, not merely recognizing a transferable dehydrogenase family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not establish a second specific pathway choice; it leaves the pathway distinction underdetermined rather than positively supporting multiple options.


### Important caveats

- The reviewer-only historical record matches the supplied sequence; its pathway annotation cites experimental evidence, but the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich motif consistent with a Rossmann-type nucleotide-binding enzyme, and its length and motifs are compatible with a short-chain dehydrogenase/reductase. That broad enzyme-family inference does not distinguish antifungal biosynthesis from steroid or membrane-lipid metabolism, which can also involve dehydrogenases.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's membership in the specific biosynthetic pathway or cluster, or experimental evidence establishing its pathway role, is absent from the original input.",
    "reason": "The sequence supports a broad enzyme-family inference but provides no clearly pathway-diagnostic feature among the offered choices. Distinguishing choice C requires the protein-specific pathway or cluster association, not merely recognizing a transferable dehydrogenase family."
  },
  "case_id": "pathway_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns this protein to antifungal biosynthesis and cites experimental evidence (ECO:0000269). This supports choice C, though it is not an independent validation of the underlying study."
  },
  "important_caveats": [
    "The reviewer-only historical record matches the supplied sequence; its pathway annotation cites experimental evidence, but the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not establish a second specific pathway choice; it leaves the pathway distinction underdetermined rather than positively supporting multiple options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns this protein to antifungal biosynthesis and cites experimental evidence (ECO:0000269). This supports choice C, though it is not an independent validation of the underlying study.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a glycine-rich motif consistent with a Rossmann-type nucleotide-binding enzyme, and its length and motifs are compatible with a short-chain dehydrogenase/reductase. That broad enzyme-family inference does not distinguish antifungal biosynthesis from steroid or membrane-lipid metabolism, which can also involve dehydrogenases.",
    "missing_item_specific_fact": "The protein's membership in the specific biosynthetic pathway or cluster, or experimental evidence establishing its pathway role, is absent from the original input.",
    "reason": "The sequence supports a broad enzyme-family inference but provides no clearly pathway-diagnostic feature among the offered choices. Distinguishing choice C requires the protein-specific pathway or cluster association, not merely recognizing a transferable dehydrogenase family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not establish a second specific pathway choice; it leaves the pathway distinction underdetermined rather than positively supporting multiple options."
  },
  "important_caveats": [
    "The reviewer-only historical record matches the supplied sequence; its pathway annotation cites experimental evidence, but the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXW2 (RESG_ASPSL) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental evidence) from PubMed:39105744. The protein is named 'Short chain dehydrogenase resG' and identified as 'Restricticin biosynthesis cluster protein G.' Restricticin is a known antifungal secondary metabolite, so the pathway assignment is consistent with the protein's role in that biosynthetic cluster. The sequence matches the benchmark sequence exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable short-chain dehydrogenase/reductase (SDR) domain (Rossmann-fold NAD-binding motif GATSGVGLEAARQLAQLG) and a fungal signal peptide. SDRs are a very large, functionally diverse superfamily participating in steroid biosynthesis (e.g., 3β-HSD, 17β-HSD), membrane lipid metabolism, and secondary metabolite biosynthesis. Option D (cell wall degradation) can be eliminated because the protein is a dehydrogenase, not a glycosidase/hydrolase. However, among A (steroid biosynthesis), B (membrane lipid metabolism), and C (antifungal biosynthesis), the SDR domain alone does not encode sufficient information to specify the substrate or biosynthetic context. The specific assignment to 'antifungal biosynthesis' depends on knowing that this SDR is part of the restricticin biosynthesis gene cluster in Aspergillus sclerotiorum, a fact about this exact protein's genomic context and the bioactivity of its product, not a property inferable from the primary sequence or general SDR family knowledge.


**Missing item-specific fact**

> The specific biosynthetic gene cluster membership (restricticin cluster) and the antifungal bioactivity of the restricticin product, which together justify the non-standard pathway label 'Antifungal biosynthesis' rather than a generic SDR-associated pathway. This is a fact about this exact protein's role in a specific organism's secondary metabolism, not a transferable family-level feature.


**Reason**

> While the SDR domain and fungal signal peptide are recognizable, these features are shared across hundreds of SDRs involved in steroid, lipid, and various secondary metabolite pathways. No sequence motif or domain architecture uniquely points to antifungal compound biosynthesis over steroid or lipid metabolism. The answer requires knowing the specific biosynthetic cluster and product bioactivity of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the sequence alone, an SDR in a fungal context could plausibly be assigned to steroid biosynthesis (many fungal SDRs participate in ergosterol pathway) or membrane lipid metabolism. Without cluster context or substrate specificity data, these alternatives are not clearly distinguishable from the correct answer by sequence reasoning. Option D is eliminable (wrong enzyme class). Option C is the correct annotation but is not uniquely inferable from sequence features.


### Important caveats

- The pathway label 'Antifungal biosynthesis' is a non-standard, organism-specific annotation tied to the restricticin compound's bioactivity, not a canonical metabolic pathway name.
- The UniProt annotation is based on experimental evidence (ECO:0000269) from a 2024 publication, but the evidence code indicates the pathway was determined from functional studies of the cluster, not from sequence features of the individual protein.
- The protein's domain architecture (SDR plus additional regions) is not distinctive enough to predict the specific secondary metabolite pathway among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable short-chain dehydrogenase/reductase (SDR) domain (Rossmann-fold NAD-binding motif GATSGVGLEAARQLAQLG) and a fungal signal peptide. SDRs are a very large, functionally diverse superfamily participating in steroid biosynthesis (e.g., 3β-HSD, 17β-HSD), membrane lipid metabolism, and secondary metabolite biosynthesis. Option D (cell wall degradation) can be eliminated because the protein is a dehydrogenase, not a glycosidase/hydrolase. However, among A (steroid biosynthesis), B (membrane lipid metabolism), and C (antifungal biosynthesis), the SDR domain alone does not encode sufficient information to specify the substrate or biosynthetic context. The specific assignment to 'antifungal biosynthesis' depends on knowing that this SDR is part of the restricticin biosynthesis gene cluster in Aspergillus sclerotiorum, a fact about this exact protein's genomic context and the bioactivity of its product, not a property inferable from the primary sequence or general SDR family knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific biosynthetic gene cluster membership (restricticin cluster) and the antifungal bioactivity of the restricticin product, which together justify the non-standard pathway label 'Antifungal biosynthesis' rather than a generic SDR-associated pathway. This is a fact about this exact protein's role in a specific organism's secondary metabolism, not a transferable family-level feature.",
    "reason": "While the SDR domain and fungal signal peptide are recognizable, these features are shared across hundreds of SDRs involved in steroid, lipid, and various secondary metabolite pathways. No sequence motif or domain architecture uniquely points to antifungal compound biosynthesis over steroid or lipid metabolism. The answer requires knowing the specific biosynthetic cluster and product bioactivity of this exact protein."
  },
  "case_id": "pathway_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW2 (RESG_ASPSL) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental evidence) from PubMed:39105744. The protein is named 'Short chain dehydrogenase resG' and identified as 'Restricticin biosynthesis cluster protein G.' Restricticin is a known antifungal secondary metabolite, so the pathway assignment is consistent with the protein's role in that biosynthetic cluster. The sequence matches the benchmark sequence exactly."
  },
  "important_caveats": [
    "The pathway label 'Antifungal biosynthesis' is a non-standard, organism-specific annotation tied to the restricticin compound's bioactivity, not a canonical metabolic pathway name.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from a 2024 publication, but the evidence code indicates the pathway was determined from functional studies of the cluster, not from sequence features of the individual protein.",
    "The protein's domain architecture (SDR plus additional regions) is not distinctive enough to predict the specific secondary metabolite pathway among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the sequence alone, an SDR in a fungal context could plausibly be assigned to steroid biosynthesis (many fungal SDRs participate in ergosterol pathway) or membrane lipid metabolism. Without cluster context or substrate specificity data, these alternatives are not clearly distinguishable from the correct answer by sequence reasoning. Option D is eliminable (wrong enzyme class). Option C is the correct annotation but is not uniquely inferable from sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW2 (RESG_ASPSL) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental evidence) from PubMed:39105744. The protein is named 'Short chain dehydrogenase resG' and identified as 'Restricticin biosynthesis cluster protein G.' Restricticin is a known antifungal secondary metabolite, so the pathway assignment is consistent with the protein's role in that biosynthetic cluster. The sequence matches the benchmark sequence exactly.",
    "evidence_ids": ["C5", "C4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable short-chain dehydrogenase/reductase (SDR) domain (Rossmann-fold NAD-binding motif GATSGVGLEAARQLAQLG) and a fungal signal peptide. SDRs are a very large, functionally diverse superfamily participating in steroid biosynthesis (e.g., 3β-HSD, 17β-HSD), membrane lipid metabolism, and secondary metabolite biosynthesis. Option D (cell wall degradation) can be eliminated because the protein is a dehydrogenase, not a glycosidase/hydrolase. However, among A (steroid biosynthesis), B (membrane lipid metabolism), and C (antifungal biosynthesis), the SDR domain alone does not encode sufficient information to specify the substrate or biosynthetic context. The specific assignment to 'antifungal biosynthesis' depends on knowing that this SDR is part of the restricticin biosynthesis gene cluster in Aspergillus sclerotiorum, a fact about this exact protein's genomic context and the bioactivity of its product, not a property inferable from the primary sequence or general SDR family knowledge.",
    "missing_item_specific_fact": "The specific biosynthetic gene cluster membership (restricticin cluster) and the antifungal bioactivity of the restricticin product, which together justify the non-standard pathway label 'Antifungal biosynthesis' rather than a generic SDR-associated pathway. This is a fact about this exact protein's role in a specific organism's secondary metabolism, not a transferable family-level feature.",
    "reason": "While the SDR domain and fungal signal peptide are recognizable, these features are shared across hundreds of SDRs involved in steroid, lipid, and various secondary metabolite pathways. No sequence motif or domain architecture uniquely points to antifungal compound biosynthesis over steroid or lipid metabolism. The answer requires knowing the specific biosynthetic cluster and product bioactivity of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the sequence alone, an SDR in a fungal context could plausibly be assigned to steroid biosynthesis (many fungal SDRs participate in ergosterol pathway) or membrane lipid metabolism. Without cluster context or substrate specificity data, these alternatives are not clearly distinguishable from the correct answer by sequence reasoning. Option D is eliminable (wrong enzyme class). Option C is the correct annotation but is not uniquely inferable from sequence features."
  },
  "important_caveats": [
    "The pathway label 'Antifungal biosynthesis' is a non-standard, organism-specific annotation tied to the restricticin compound's bioactivity, not a canonical metabolic pathway name.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from a 2024 publication, but the evidence code indicates the pathway was determined from functional studies of the cluster, not from sequence features of the individual protein.",
    "The protein's domain architecture (SDR plus additional regions) is not distinctive enough to predict the specific secondary metabolite pathway among the offered choices."
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
  "benchmark_sequence_length": 359,
  "benchmark_sequence_sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 359,
  "current_source_sequence_sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d",
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
  "requested_accession": "P0DXW2",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "selected_historical_source_sequence_length": 359,
  "selected_historical_source_sequence_sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d",
  "selected_historical_version": {
    "accession": "P0DXW2",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RESG_ASPSL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXW2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus sclerotiorum\",\"taxonId\":138282}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein G\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Short chain dehydrogenase resG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Antifungal biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lu Y.\",\"Li Y.\",\"Dou M.\",\"Liu D.\",\"Lin W.\",\"Fan A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39105744\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c04244\"}],\"citationType\":\"journal article\",\"firstPage\":\"18520\",\"id\":\"39105744\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"18527\",\"publicationDate\":\"2024\",\"title\":\"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.\",\"volume\":\"72\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   RESG_ASPSL              Reviewed;         359 AA.\nAC   P0DXW2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Short chain dehydrogenase resG {ECO:0000303|PubMed:39105744};\nDE            EC=1.1.1.- {ECO:0000305|PubMed:39105744};\nDE   AltName: Full=Restricticin biosynthesis cluster protein G {ECO:0000303|PubMed:39105744};\nGN   Name=resG {ECO:0000303|PubMed:39105744};\nOS   Aspergillus sclerotiorum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=138282;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;\nRA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;\nRT   \"Discovery of a hybrid molecule with phytotoxic activity by genome mining,\nRT   heterologous expression, and OSMAC strategy.\";\nRL   J. Agric. Food Chem. 72:18520-18527(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:39105744}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
