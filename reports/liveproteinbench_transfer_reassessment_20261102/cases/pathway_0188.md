# pathway_0188

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0188.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEIMNFSLNSPVFLLLSFFFLLMVLMQLTGSRKYKGKRLPPGPKKLPIIGNLHQMVGSLPHRVLKNLADQYGPVMHLQIGELSAIVISSADKAKEVLNTHGILVADRPQTTVAKIMLYNSLGATFAPYGDYLKQLRQIYALELLSPKTVRSFWTIMEDELSTMVTSVKAEAGQPIVLHDRMLTYLYATLCRATVGSVCNGRETLIMAAKETSALSAAIRIEDLFPSVKILPVVSGLRTRLTNLLKQLDTVLEDIIGEREKKMFSSNNIQPSTEEEDMLGVLLLYKNGKGKDTKFRITNNDIKAIIFELILAGTLSSSAIVEWCMSEMIKNPRVMKKAQDEVRQVLKDKKKVSGSDLAKLEYVKMVIKESVRLHPPAPLLFPREVREDFEMDGMIIPKKSWVIINYWAVGIDPKIWDDAERFEPERFSNSPIDFYGSHFELIPFGAGRRICPGILFGTTNVELLLASFLYHFDWKLPGGMKPEELDMNELFGAGCIRENPLCLIPSISVAGN

[Multiple Choices]
A. Protein modification
B. Alkaloid biosynthesis
C. dTTP biosynthesis. .
D. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
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

> The sequence-matched UniProt record annotates the protein in alkaloid biosynthesis, specifically ajmaline biosynthesis, with ECO:0000269 evidence linked to a publication. This supports choice B, though it is database-reported evidence rather than an independent review of the underlying experiments.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal segment and a conserved C-terminal cysteine-containing region characteristic of a membrane-associated cytochrome P450. P450 enzymes commonly catalyze oxidative steps in plant specialized metabolism, including alkaloid biosynthesis. Among these options, that provides a meaningful basis for B over the specific nucleotide and folate biosynthesis choices, while the sequence alone does not establish the exact alkaloid pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable P450-family inference meaningfully favors alkaloid biosynthesis among the offered alternatives. It is probabilistic: P450s have diverse functions, and the sequence motifs alone do not identify the particular product or pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are distinct enough that the P450-based inference favors B; no other listed option is comparably supported by the sequence features.


### Important caveats

- The supplied sequence supports recognition of a P450-like enzyme but does not by itself prove its specific pathway assignment.
- The reviewer-only annotation applies to the sequence-matched record and reports experimental evidence, but the underlying study was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment and a conserved C-terminal cysteine-containing region characteristic of a membrane-associated cytochrome P450. P450 enzymes commonly catalyze oxidative steps in plant specialized metabolism, including alkaloid biosynthesis. Among these options, that provides a meaningful basis for B over the specific nucleotide and folate biosynthesis choices, while the sequence alone does not establish the exact alkaloid pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable P450-family inference meaningfully favors alkaloid biosynthesis among the offered alternatives. It is probabilistic: P450s have diverse functions, and the sequence motifs alone do not identify the particular product or pathway."
  },
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein in alkaloid biosynthesis, specifically ajmaline biosynthesis, with ECO:0000269 evidence linked to a publication. This supports choice B, though it is database-reported evidence rather than an independent review of the underlying experiments."
  },
  "important_caveats": [
    "The supplied sequence supports recognition of a P450-like enzyme but does not by itself prove its specific pathway assignment.",
    "The reviewer-only annotation applies to the sequence-matched record and reports experimental evidence, but the underlying study was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are distinct enough that the P450-based inference favors B; no other listed option is comparably supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein in alkaloid biosynthesis, specifically ajmaline biosynthesis, with ECO:0000269 evidence linked to a publication. This supports choice B, though it is database-reported evidence rather than an independent review of the underlying experiments.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment and a conserved C-terminal cysteine-containing region characteristic of a membrane-associated cytochrome P450. P450 enzymes commonly catalyze oxidative steps in plant specialized metabolism, including alkaloid biosynthesis. Among these options, that provides a meaningful basis for B over the specific nucleotide and folate biosynthesis choices, while the sequence alone does not establish the exact alkaloid pathway.",
    "missing_item_specific_fact": "",
    "reason": "A transferable P450-family inference meaningfully favors alkaloid biosynthesis among the offered alternatives. It is probabilistic: P450s have diverse functions, and the sequence motifs alone do not identify the particular product or pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are distinct enough that the P450-based inference favors B; no other listed option is comparably supported by the sequence features."
  },
  "important_caveats": [
    "The supplied sequence supports recognition of a P450-like enzyme but does not by itself prove its specific pathway assignment.",
    "The reviewer-only annotation applies to the sequence-matched record and reports experimental evidence, but the underlying study was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ2 (Sarpagan bridge enzyme 2, RsSBE2) from Rauvolfia serpentina is annotated with PATHWAY: 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:38212296, a 2024 Nature Communications paper on de novo biosynthesis of the antiarrhythmic alkaloid ajmaline). The sequence matches exactly. Answer B 'Alkaloid biosynthesis' is directly supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable cytochrome P450 heme-binding motif (FGAGRRICPGILFGTTNVELLL near the C-terminus, matching the canonical FGxxxCxG pattern with the conserved cysteine that ligates heme iron). The ~511 aa length, hydrophobic N-terminal membrane anchor, and overall architecture are consistent with a plant microsomal P450. Recognizing the protein as a P450 eliminates options C (dTTP biosynthesis: uses ribonucleotide reductase, thymidylate synthase, dUTPase — none are P450s) and D (dihydrofolate biosynthesis: uses GTP cyclohydrolase, dihydropteroate synthase, folylpolyglutamate synthase — none are P450s). Option A (Protein modification) is atypical for P450s, which oxidize small-molecule substrates rather than modifying proteins. Plant P450s are overwhelmingly associated with secondary metabolism, particularly alkaloid biosynthesis (e.g., terpenoid indole alkaloids in Apocynaceae/Rubiaceae, morphine biosynthesis in Papaver, etc.), making B the most probable pathway among the remaining choices. This is a well-established family-level pattern learned from many other plant P450s.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the P450 signature from sequence, eliminate non-P450 pathways (C, D), reject protein modification (A) as inconsistent with P450 chemistry, and use the strong empirical association between plant P450s and alkaloid/secondary metabolism to select B. This relies on transferable family knowledge and sequence motif recognition, not on recalling this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes and metabolic contexts. P450 recognition cleanly eliminates C and D; the chemistry of P450s eliminates A. Only B remains as a plausible pathway for a plant P450. Minor trailing-period formatting in C and D does not affect interpretation.


### Important caveats

- The P450 heme-binding motif is identifiable but requires careful inspection; a model unfamiliar with the FGxxxCxG pattern might struggle, though the overall sequence architecture still suggests a P450.
- The specific sub-pathway (ajmaline biosynthesis) is not asked; the broader category 'Alkaloid biosynthesis' is the correct answer level.
- The entry was first published in June 2025 and the supporting paper appeared in 2024; the benchmark author's source snapshot is unknown but the sequence matches exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGAGRRICPGILFGTTNVELLL near the C-terminus, matching the canonical FGxxxCxG pattern with the conserved cysteine that ligates heme iron). The ~511 aa length, hydrophobic N-terminal membrane anchor, and overall architecture are consistent with a plant microsomal P450. Recognizing the protein as a P450 eliminates options C (dTTP biosynthesis: uses ribonucleotide reductase, thymidylate synthase, dUTPase — none are P450s) and D (dihydrofolate biosynthesis: uses GTP cyclohydrolase, dihydropteroate synthase, folylpolyglutamate synthase — none are P450s). Option A (Protein modification) is atypical for P450s, which oxidize small-molecule substrates rather than modifying proteins. Plant P450s are overwhelmingly associated with secondary metabolism, particularly alkaloid biosynthesis (e.g., terpenoid indole alkaloids in Apocynaceae/Rubiaceae, morphine biosynthesis in Papaver, etc.), making B the most probable pathway among the remaining choices. This is a well-established family-level pattern learned from many other plant P450s.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 signature from sequence, eliminate non-P450 pathways (C, D), reject protein modification (A) as inconsistent with P450 chemistry, and use the strong empirical association between plant P450s and alkaloid/secondary metabolism to select B. This relies on transferable family knowledge and sequence motif recognition, not on recalling this specific entry's annotation."
  },
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ2 (Sarpagan bridge enzyme 2, RsSBE2) from Rauvolfia serpentina is annotated with PATHWAY: 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:38212296, a 2024 Nature Communications paper on de novo biosynthesis of the antiarrhythmic alkaloid ajmaline). The sequence matches exactly. Answer B 'Alkaloid biosynthesis' is directly supported."
  },
  "important_caveats": [
    "The P450 heme-binding motif is identifiable but requires careful inspection; a model unfamiliar with the FGxxxCxG pattern might struggle, though the overall sequence architecture still suggests a P450.",
    "The specific sub-pathway (ajmaline biosynthesis) is not asked; the broader category 'Alkaloid biosynthesis' is the correct answer level.",
    "The entry was first published in June 2025 and the supporting paper appeared in 2024; the benchmark author's source snapshot is unknown but the sequence matches exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes and metabolic contexts. P450 recognition cleanly eliminates C and D; the chemistry of P450s eliminates A. Only B remains as a plausible pathway for a plant P450. Minor trailing-period formatting in C and D does not affect interpretation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ2 (Sarpagan bridge enzyme 2, RsSBE2) from Rauvolfia serpentina is annotated with PATHWAY: 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:38212296, a 2024 Nature Communications paper on de novo biosynthesis of the antiarrhythmic alkaloid ajmaline). The sequence matches exactly. Answer B 'Alkaloid biosynthesis' is directly supported.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGAGRRICPGILFGTTNVELLL near the C-terminus, matching the canonical FGxxxCxG pattern with the conserved cysteine that ligates heme iron). The ~511 aa length, hydrophobic N-terminal membrane anchor, and overall architecture are consistent with a plant microsomal P450. Recognizing the protein as a P450 eliminates options C (dTTP biosynthesis: uses ribonucleotide reductase, thymidylate synthase, dUTPase — none are P450s) and D (dihydrofolate biosynthesis: uses GTP cyclohydrolase, dihydropteroate synthase, folylpolyglutamate synthase — none are P450s). Option A (Protein modification) is atypical for P450s, which oxidize small-molecule substrates rather than modifying proteins. Plant P450s are overwhelmingly associated with secondary metabolism, particularly alkaloid biosynthesis (e.g., terpenoid indole alkaloids in Apocynaceae/Rubiaceae, morphine biosynthesis in Papaver, etc.), making B the most probable pathway among the remaining choices. This is a well-established family-level pattern learned from many other plant P450s.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 signature from sequence, eliminate non-P450 pathways (C, D), reject protein modification (A) as inconsistent with P450 chemistry, and use the strong empirical association between plant P450s and alkaloid/secondary metabolism to select B. This relies on transferable family knowledge and sequence motif recognition, not on recalling this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes and metabolic contexts. P450 recognition cleanly eliminates C and D; the chemistry of P450s eliminates A. Only B remains as a plausible pathway for a plant P450. Minor trailing-period formatting in C and D does not affect interpretation."
  },
  "important_caveats": [
    "The P450 heme-binding motif is identifiable but requires careful inspection; a model unfamiliar with the FGxxxCxG pattern might struggle, though the overall sequence architecture still suggests a P450.",
    "The specific sub-pathway (ajmaline biosynthesis) is not asked; the broader category 'Alkaloid biosynthesis' is the correct answer level.",
    "The entry was first published in June 2025 and the supporting paper appeared in 2024; the benchmark author's source snapshot is unknown but the sequence matches exactly."
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
  "benchmark_sequence_length": 511,
  "benchmark_sequence_sha256": "706fd69d57783df7add38c44c3e1cf2feb5cbcbc3afb9480407dd97165056ba4",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 511,
  "current_source_sequence_sha256": "706fd69d57783df7add38c44c3e1cf2feb5cbcbc3afb9480407dd97165056ba4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ2",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "selected_historical_source_sequence_length": 511,
  "selected_historical_source_sequence_sha256": "706fd69d57783df7add38c44c3e1cf2feb5cbcbc3afb9480407dd97165056ba4",
  "selected_historical_version": {
    "accession": "P0DXJ2",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SBE2_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cytochrome P450 SBE2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0DO13\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.14.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Sarpagan bridge enzyme 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsSBE2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   SBE2_RAUSE              Reviewed;         511 AA.\nAC   P0DXJ2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Sarpagan bridge enzyme 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsSBE2 {ECO:0000303|PubMed:38212296};\nDE            EC=1.14.14.- {ECO:0000250|UniProtKB:P0DO13};\nDE   AltName: Full=Cytochrome P450 SBE2 {ECO:0000305};\nGN   Name=SBE2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.434063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "url": "https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.434063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "url": "https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.434063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "url": "https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 188. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
