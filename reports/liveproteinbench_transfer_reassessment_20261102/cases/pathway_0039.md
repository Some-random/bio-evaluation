# pathway_0039

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0039.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDMNTFPASTYCESIVRFLDAIEYHDDNLTHEERVEGLRHVHSKTAQYFTEPLPRSILKGVAPRRIAAVTRTISHFIVYCWSKLPREAQVDVSIYLSIINVLDDEISSEPSTQMTSFWSDLIQGKQPKHPFWVLFNSHLPRLLRHYGSFCAFNIMRCTFDYFEGCWIEQHNFQGYPGADCYPSFLRRLNCLGGAVAGTIFPAAKFDEQKLFAQMSCVMAQIDGPVALMNDLFSFYKEYDQDEANLVSNWCTVDGITMDQALTRLTDDTIHACVRILDILKDKDPDMLATIRGFIHGYATWHICDFRYRLREIYDREDLQESGARFREYFDKAIDVGWVDVEEWTCQVQGFEVEGPAPSGSEVQAYQANAFGFSVDTQRHHNIDYVGSSILGLFEWATRYLRGKLPLGNA

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. Amino-acid biosynthesis
C. Alkaloid biosynthesis. .
D. L-isoleucine biosynthesis
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

> The sequence-matched UniProt record places the protein in secondary metabolite and terpenoid biosynthesis. The annotation cites experimental evidence, though the primary studies were not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A transferable family-level inference is that this enzyme-sized fungal protein is compatible with a terpene cyclase: related terpene cyclases catalyze specialized terpenoid-product formation, which falls under secondary metabolite biosynthesis. That meaningfully favors A over amino-acid biosynthesis, isoleucine biosynthesis, or the narrower alkaloid option. The sequence alone does not make the family assignment certain.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered alternatives permit a broad pathway distinction, and recognition of a terpene-cyclase-like family or pattern learned from related proteins can support that distinction without recalling this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Terpenoid secondary-metabolite biosynthesis supports A; the choices do not provide another comparably fitting pathway.


### Important caveats

- The reviewer-only record matches the supplied sequence, but it was not available as an input to the evaluated model.
- The family-level inference from sequence is probabilistic; the database pathway annotation is stronger evidence for the keyed answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A transferable family-level inference is that this enzyme-sized fungal protein is compatible with a terpene cyclase: related terpene cyclases catalyze specialized terpenoid-product formation, which falls under secondary metabolite biosynthesis. That meaningfully favors A over amino-acid biosynthesis, isoleucine biosynthesis, or the narrower alkaloid option. The sequence alone does not make the family assignment certain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives permit a broad pathway distinction, and recognition of a terpene-cyclase-like family or pattern learned from related proteins can support that distinction without recalling this exact protein's annotation."
  },
  "case_id": "pathway_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record places the protein in secondary metabolite and terpenoid biosynthesis. The annotation cites experimental evidence, though the primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence, but it was not available as an input to the evaluated model.",
    "The family-level inference from sequence is probabilistic; the database pathway annotation is stronger evidence for the keyed answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Terpenoid secondary-metabolite biosynthesis supports A; the choices do not provide another comparably fitting pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record places the protein in secondary metabolite and terpenoid biosynthesis. The annotation cites experimental evidence, though the primary studies were not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A transferable family-level inference is that this enzyme-sized fungal protein is compatible with a terpene cyclase: related terpene cyclases catalyze specialized terpenoid-product formation, which falls under secondary metabolite biosynthesis. That meaningfully favors A over amino-acid biosynthesis, isoleucine biosynthesis, or the narrower alkaloid option. The sequence alone does not make the family assignment certain.",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives permit a broad pathway distinction, and recognition of a terpene-cyclase-like family or pattern learned from related proteins can support that distinction without recalling this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Terpenoid secondary-metabolite biosynthesis supports A; the choices do not provide another comparably fitting pathway."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence, but it was not available as an input to the evaluated model.",
    "The family-level inference from sequence is probabilistic; the database pathway annotation is stronger evidence for the keyed answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly states the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:29995859 and PubMed:39511739). The protein is a terpene cyclase (astA) involved in aspterric acid biosynthesis, which is a natural-product herbicide (secondary metabolite). Choice A ('Secondary metabolite biosynthesis') matches the broader pathway category stated in the annotation. The other choices (amino-acid biosynthesis, alkaloid biosynthesis, L-isoleucine biosynthesis) are not supported.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~409 aa) contains multiple aspartate-rich motifs consistent with the DDxxD motif (e.g., 'DDE' in 'NLDDEISSEPSTQ' and 'DDE' in 'KEYDQDEANLVSNW') characteristic of terpene cyclases, a well-conserved family feature learned from many other proteins (trichodiene synthase, limonene synthase, fungal sesquiterpene cyclases). The ~400 aa size is typical of fungal sesquiterpene synthases. Recognizing the enzyme as a terpene cyclase from these motifs and size, a knowledgeable model infers terpenoid biosynthesis, which falls under 'Secondary metabolite biosynthesis' (A). This rules out B and D (amino-acid biosynthetic enzymes have PLP-binding, threonine deaminase, or other specific motifs absent here) and C (alkaloid biosynthesis involves nitrogen-containing ring-forming enzymes, P450s, or methyltransferases acting on amino-acid-derived precursors, none of which match a terpene cyclase). The DDxxD motif is a transferable family-level feature distinguishing terpene cyclases from all other enzyme classes in the options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DDxxD motif and ~400 aa size are recognizable sequence features shared across the terpene cyclase superfamily. A model trained on general biochemistry and protein families can infer 'terpene cyclase → terpenoid pathway → secondary metabolite biosynthesis' and exclude amino-acid and alkaloid pathways based on the absence of their characteristic catalytic features. This is legitimate family-level transfer, not lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are mutually exclusive pathway categories. A terpene cyclase clearly belongs to secondary metabolite (terpenoid) biosynthesis, not amino-acid biosynthesis, alkaloid biosynthesis, or isoleucine biosynthesis. No ambiguity among the offered alternatives.


### Important caveats

- The UniProt annotation uses the broader term 'Secondary metabolite biosynthesis' as the pathway category with 'terpenoid biosynthesis' as the sub-pathway; Choice A matches the broader term exactly.
- The DDxxD motif recognition is probabilistic from sequence alone; some fungal terpene cyclases have degenerate motifs. However, the combination of multiple Asp-rich regions, size, and absence of other enzyme-class signatures makes the inference credible.
- The reviewer-only evidence confirms experimental support (ECO:0000269) for the pathway annotation, but this was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~409 aa) contains multiple aspartate-rich motifs consistent with the DDxxD motif (e.g., 'DDE' in 'NLDDEISSEPSTQ' and 'DDE' in 'KEYDQDEANLVSNW') characteristic of terpene cyclases, a well-conserved family feature learned from many other proteins (trichodiene synthase, limonene synthase, fungal sesquiterpene cyclases). The ~400 aa size is typical of fungal sesquiterpene synthases. Recognizing the enzyme as a terpene cyclase from these motifs and size, a knowledgeable model infers terpenoid biosynthesis, which falls under 'Secondary metabolite biosynthesis' (A). This rules out B and D (amino-acid biosynthetic enzymes have PLP-binding, threonine deaminase, or other specific motifs absent here) and C (alkaloid biosynthesis involves nitrogen-containing ring-forming enzymes, P450s, or methyltransferases acting on amino-acid-derived precursors, none of which match a terpene cyclase). The DDxxD motif is a transferable family-level feature distinguishing terpene cyclases from all other enzyme classes in the options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DDxxD motif and ~400 aa size are recognizable sequence features shared across the terpene cyclase superfamily. A model trained on general biochemistry and protein families can infer 'terpene cyclase → terpenoid pathway → secondary metabolite biosynthesis' and exclude amino-acid and alkaloid pathways based on the absence of their characteristic catalytic features. This is legitimate family-level transfer, not lookup of this specific protein's annotation."
  },
  "case_id": "pathway_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly states the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:29995859 and PubMed:39511739). The protein is a terpene cyclase (astA) involved in aspterric acid biosynthesis, which is a natural-product herbicide (secondary metabolite). Choice A ('Secondary metabolite biosynthesis') matches the broader pathway category stated in the annotation. The other choices (amino-acid biosynthesis, alkaloid biosynthesis, L-isoleucine biosynthesis) are not supported."
  },
  "important_caveats": [
    "The UniProt annotation uses the broader term 'Secondary metabolite biosynthesis' as the pathway category with 'terpenoid biosynthesis' as the sub-pathway; Choice A matches the broader term exactly.",
    "The DDxxD motif recognition is probabilistic from sequence alone; some fungal terpene cyclases have degenerate motifs. However, the combination of multiple Asp-rich regions, size, and absence of other enzyme-class signatures makes the inference credible.",
    "The reviewer-only evidence confirms experimental support (ECO:0000269) for the pathway annotation, but this was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are mutually exclusive pathway categories. A terpene cyclase clearly belongs to secondary metabolite (terpenoid) biosynthesis, not amino-acid biosynthesis, alkaloid biosynthesis, or isoleucine biosynthesis. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly states the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:29995859 and PubMed:39511739). The protein is a terpene cyclase (astA) involved in aspterric acid biosynthesis, which is a natural-product herbicide (secondary metabolite). Choice A ('Secondary metabolite biosynthesis') matches the broader pathway category stated in the annotation. The other choices (amino-acid biosynthesis, alkaloid biosynthesis, L-isoleucine biosynthesis) are not supported.",
    "evidence_ids": ["C5", "H4", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~409 aa) contains multiple aspartate-rich motifs consistent with the DDxxD motif (e.g., 'DDE' in 'NLDDEISSEPSTQ' and 'DDE' in 'KEYDQDEANLVSNW') characteristic of terpene cyclases, a well-conserved family feature learned from many other proteins (trichodiene synthase, limonene synthase, fungal sesquiterpene cyclases). The ~400 aa size is typical of fungal sesquiterpene synthases. Recognizing the enzyme as a terpene cyclase from these motifs and size, a knowledgeable model infers terpenoid biosynthesis, which falls under 'Secondary metabolite biosynthesis' (A). This rules out B and D (amino-acid biosynthetic enzymes have PLP-binding, threonine deaminase, or other specific motifs absent here) and C (alkaloid biosynthesis involves nitrogen-containing ring-forming enzymes, P450s, or methyltransferases acting on amino-acid-derived precursors, none of which match a terpene cyclase). The DDxxD motif is a transferable family-level feature distinguishing terpene cyclases from all other enzyme classes in the options.",
    "missing_item_specific_fact": "",
    "reason": "The DDxxD motif and ~400 aa size are recognizable sequence features shared across the terpene cyclase superfamily. A model trained on general biochemistry and protein families can infer 'terpene cyclase → terpenoid pathway → secondary metabolite biosynthesis' and exclude amino-acid and alkaloid pathways based on the absence of their characteristic catalytic features. This is legitimate family-level transfer, not lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are mutually exclusive pathway categories. A terpene cyclase clearly belongs to secondary metabolite (terpenoid) biosynthesis, not amino-acid biosynthesis, alkaloid biosynthesis, or isoleucine biosynthesis. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt annotation uses the broader term 'Secondary metabolite biosynthesis' as the pathway category with 'terpenoid biosynthesis' as the sub-pathway; Choice A matches the broader term exactly.",
    "The DDxxD motif recognition is probabilistic from sequence alone; some fungal terpene cyclases have degenerate motifs. However, the combination of multiple Asp-rich regions, size, and absence of other enzyme-class signatures makes the inference credible.",
    "The reviewer-only evidence confirms experimental support (ECO:0000269) for the pathway annotation, but this was not available to the evaluated model."
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
  "benchmark_sequence_length": 409,
  "benchmark_sequence_sha256": "a8bdca14275904fa582aa8697339e5415804e0c32861786fd957a494391b298d",
  "current_entry_audit": {
    "entryVersion": 74,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 409,
  "current_source_sequence_sha256": "a8bdca14275904fa582aa8697339e5415804e0c32861786fd957a494391b298d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 72,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG8",
  "selected_historical_entry_version": 72,
  "selected_historical_record_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "selected_historical_source_sequence_length": 409,
  "selected_historical_source_sequence_sha256": "a8bdca14275904fa582aa8697339e5415804e0c32861786fd957a494391b298d",
  "selected_historical_version": {
    "accession": "Q0CPG8",
    "database": "Swiss-Prot",
    "entryVersion": 72,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTA_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":74,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase astA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhou Z.\",\"Zhang Y.\",\"Wu Q.\",\"Hou X.\",\"Zhang B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39511739\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c08468\"}],\"citationType\":\"journal article\",\"firstPage\":\"25755\",\"id\":\"39511739\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"25766\",\"publicationDate\":\"2024\",\"title\":\"Yeast synthesis and herbicidal activity evaluation of aspterric acid.\",\"volume\":\"72\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H1",
  "excerpt": "ID   ASTA_ASPTN              Reviewed;         409 AA.\nAC   Q0CPG8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 72.\nDE   RecName: Full=Terpene cyclase astA {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.3.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein A {ECO:0000303|PubMed:29995859};\nGN   Name=astA {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04416;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39511739; DOI=10.1021/acs.jafc.4c08468;\nRA   Zhou Z., Zhang Y., Wu Q., Hou X., Zhang B.;\nRT   \"Yeast synthesis and herbicidal activity evaluation of aspterric acid.\";\nRL   J. Agric. Food Chem. 72:25755-25766(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:29995859, ECO:0000269|PubMed:39511739}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
