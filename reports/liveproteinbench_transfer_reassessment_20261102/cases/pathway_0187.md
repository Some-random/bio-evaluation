# pathway_0187

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0187.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATDTAVTGAPETMQLRLASGNGPVTRTVLRTPLRDALPSEVPLIDISPIFSTSVADRKAVACKIHDAATNIGFFYIQNHRVPSRDTDMAYSASLDFFRQDMEAKMKADAKKGPFDSGYRGPGTQRVNPDEGADLRETYSILYDPMLDPTVPDPARIPEPASRFLHLGRAPFESTDTLPHFKDAFVRYFQACLALARALTRTFALSLDLPESAFDSKVQYPDASLEINFYPPISTGHAVSAPADPDTRVSIGSHTDFLLFTILWQDSNGGLQVLNREGQWIRASPVEGTFVVNIGDYLQRITNDKYVSTVHRAQNWSGRQRVSMPFFWGFGMHESCQVLESCCGEDGKSKYDEVRCVDWVSRRLGNLFDLSDKG

[Multiple Choices]
A. Pyrimidine metabolism
B. peptidoglycan degradation. .
C. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
D. Secondary metabolite biosynthesis. .
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

> The historical UniProt entry for the exact matching sequence annotates its pathway as secondary metabolite biosynthesis, with experimental evidence attribution (ECO:0000269).

Citations as saved: [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an HxD motif and a downstream histidine consistent with the metal-binding features of Fe(II)/2-oxoglutarate-dependent oxygenases. Such enzymes commonly act in specialized-metabolite biosynthesis, making D a credible choice among these alternatives. The fungal sequence context and the options also weigh against peptidoglycan degradation, while the other choices describe more specific pathways with no evident supporting sequence signature here.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable enzyme-family inference meaningfully favors secondary metabolite biosynthesis among the offered choices, although the motifs alone do not prove this enzyme's exact substrate or pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered pathways are distinguishable enough for the sequence-family and biological-context inference to favor D.


### Important caveats

- The sequence motifs support an oxygenase-family inference, not a definitive assignment of the exact pathway.
- The reviewer-only pathway annotation applies to the sequence-matched historical record; it was not available as an original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an HxD motif and a downstream histidine consistent with the metal-binding features of Fe(II)/2-oxoglutarate-dependent oxygenases. Such enzymes commonly act in specialized-metabolite biosynthesis, making D a credible choice among these alternatives. The fungal sequence context and the options also weigh against peptidoglycan degradation, while the other choices describe more specific pathways with no evident supporting sequence signature here.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference meaningfully favors secondary metabolite biosynthesis among the offered choices, although the motifs alone do not prove this enzyme's exact substrate or pathway."
  },
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "H4"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt entry for the exact matching sequence annotates its pathway as secondary metabolite biosynthesis, with experimental evidence attribution (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence motifs support an oxygenase-family inference, not a definitive assignment of the exact pathway.",
    "The reviewer-only pathway annotation applies to the sequence-matched historical record; it was not available as an original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered pathways are distinguishable enough for the sequence-family and biological-context inference to favor D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt entry for the exact matching sequence annotates its pathway as secondary metabolite biosynthesis, with experimental evidence attribution (ECO:0000269).",
    "evidence_ids": ["H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an HxD motif and a downstream histidine consistent with the metal-binding features of Fe(II)/2-oxoglutarate-dependent oxygenases. Such enzymes commonly act in specialized-metabolite biosynthesis, making D a credible choice among these alternatives. The fungal sequence context and the options also weigh against peptidoglycan degradation, while the other choices describe more specific pathways with no evident supporting sequence signature here.",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference meaningfully favors secondary metabolite biosynthesis among the offered choices, although the motifs alone do not prove this enzyme's exact substrate or pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered pathways are distinguishable enough for the sequence-family and biological-context inference to favor D."
  },
  "important_caveats": [
    "The sequence motifs support an oxygenase-family inference, not a definitive assignment of the exact pathway.",
    "The reviewer-only pathway annotation applies to the sequence-matched historical record; it was not available as an original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A455ZKR7 (PPZC_METMF) annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:38578094). The protein is a 2-oxoglutarate-Fe(II) type oxidoreductase (ppzC) in the pyrrolopyrazine biosynthesis gene cluster of Metarhizium majus. The pathway annotation is directly stated in the record.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable 2-oxoglutarate/Fe(II) oxygenase (2OG-Fe(II) dioxygenase) facial triad motif: 'HESCQ' (H-E, the first His-Asp/Glu pair), 'GDYLQ' (the D carboxylate), and 'VHRA' (the second His) — the canonical HxD/E...H 2-His-1-carboxylate triad. This enzyme family is overwhelmingly associated with secondary metabolite biosynthesis, particularly in fungi (e.g., fumitremorgin, gliotoxin, ergot alkaloid, and peramine/pyrrolopyrazine pathways). None of the other options match: pyrimidine metabolism enzymes (carbamoyl phosphate synthetase, dihydroorotase, thymidylate synthase, etc.) have completely different folds and motifs; peptidoglycan degradation involves lysozymes/amidases/transglycosidases with unrelated domains; chorismate synthase (step 7/7 of shikimate pathway) is an FMN-dependent enzyme with a distinct fold. The presence of the 2OG oxygenase triad in a fungal protein context strongly and specifically points to secondary metabolite biosynthesis among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HxD/E...H facial triad motif is a well-characterized, transferable family signature. The association of 2-oxoglutarate/Fe(II) oxygenases with secondary metabolite biosynthesis (especially in fungi) is a strong, widely documented pattern learned from numerous other proteins (e.g., FtmO1A, GliJ, PptN, various NRPS/PKS tailoring enzymes). This family-level inference meaningfully distinguishes option D from A, B, and C, which require entirely different enzyme classes with no 2OG oxygenase motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The 2-oxoglutarate/Fe(II) oxygenase motif is incompatible with pyrimidine metabolism enzymes, peptidoglycan-degrading enzymes, and chorismate synthase. Only secondary metabolite biosynthesis is consistent with this enzyme family in a fungal context.


### Important caveats

- 2-oxoglutarate/Fe(II) oxygenases can occasionally participate in primary metabolic processes (e.g., collagen hydroxylation, DNA demethylation), but among the four offered choices, secondary metabolite biosynthesis is the overwhelmingly dominant and specific association, especially for fungal members of this family.
- The specific identity as ppzC in the pyrrolopyrazine cluster is a target-specific annotation; however, the family-level reasoning (2OG oxygenase → secondary metabolite biosynthesis in fungi) is sufficient to distinguish the offered alternatives without knowing the exact protein name.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable 2-oxoglutarate/Fe(II) oxygenase (2OG-Fe(II) dioxygenase) facial triad motif: 'HESCQ' (H-E, the first His-Asp/Glu pair), 'GDYLQ' (the D carboxylate), and 'VHRA' (the second His) — the canonical HxD/E...H 2-His-1-carboxylate triad. This enzyme family is overwhelmingly associated with secondary metabolite biosynthesis, particularly in fungi (e.g., fumitremorgin, gliotoxin, ergot alkaloid, and peramine/pyrrolopyrazine pathways). None of the other options match: pyrimidine metabolism enzymes (carbamoyl phosphate synthetase, dihydroorotase, thymidylate synthase, etc.) have completely different folds and motifs; peptidoglycan degradation involves lysozymes/amidases/transglycosidases with unrelated domains; chorismate synthase (step 7/7 of shikimate pathway) is an FMN-dependent enzyme with a distinct fold. The presence of the 2OG oxygenase triad in a fungal protein context strongly and specifically points to secondary metabolite biosynthesis among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HxD/E...H facial triad motif is a well-characterized, transferable family signature. The association of 2-oxoglutarate/Fe(II) oxygenases with secondary metabolite biosynthesis (especially in fungi) is a strong, widely documented pattern learned from numerous other proteins (e.g., FtmO1A, GliJ, PptN, various NRPS/PKS tailoring enzymes). This family-level inference meaningfully distinguishes option D from A, B, and C, which require entirely different enzyme classes with no 2OG oxygenase motifs."
  },
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A455ZKR7 (PPZC_METMF) annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:38578094). The protein is a 2-oxoglutarate-Fe(II) type oxidoreductase (ppzC) in the pyrrolopyrazine biosynthesis gene cluster of Metarhizium majus. The pathway annotation is directly stated in the record."
  },
  "important_caveats": [
    "2-oxoglutarate/Fe(II) oxygenases can occasionally participate in primary metabolic processes (e.g., collagen hydroxylation, DNA demethylation), but among the four offered choices, secondary metabolite biosynthesis is the overwhelmingly dominant and specific association, especially for fungal members of this family.",
    "The specific identity as ppzC in the pyrrolopyrazine cluster is a target-specific annotation; however, the family-level reasoning (2OG oxygenase → secondary metabolite biosynthesis in fungi) is sufficient to distinguish the offered alternatives without knowing the exact protein name."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 2-oxoglutarate/Fe(II) oxygenase motif is incompatible with pyrimidine metabolism enzymes, peptidoglycan-degrading enzymes, and chorismate synthase. Only secondary metabolite biosynthesis is consistent with this enzyme family in a fungal context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A455ZKR7 (PPZC_METMF) annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:38578094). The protein is a 2-oxoglutarate-Fe(II) type oxidoreductase (ppzC) in the pyrrolopyrazine biosynthesis gene cluster of Metarhizium majus. The pathway annotation is directly stated in the record.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable 2-oxoglutarate/Fe(II) oxygenase (2OG-Fe(II) dioxygenase) facial triad motif: 'HESCQ' (H-E, the first His-Asp/Glu pair), 'GDYLQ' (the D carboxylate), and 'VHRA' (the second His) — the canonical HxD/E...H 2-His-1-carboxylate triad. This enzyme family is overwhelmingly associated with secondary metabolite biosynthesis, particularly in fungi (e.g., fumitremorgin, gliotoxin, ergot alkaloid, and peramine/pyrrolopyrazine pathways). None of the other options match: pyrimidine metabolism enzymes (carbamoyl phosphate synthetase, dihydroorotase, thymidylate synthase, etc.) have completely different folds and motifs; peptidoglycan degradation involves lysozymes/amidases/transglycosidases with unrelated domains; chorismate synthase (step 7/7 of shikimate pathway) is an FMN-dependent enzyme with a distinct fold. The presence of the 2OG oxygenase triad in a fungal protein context strongly and specifically points to secondary metabolite biosynthesis among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "The HxD/E...H facial triad motif is a well-characterized, transferable family signature. The association of 2-oxoglutarate/Fe(II) oxygenases with secondary metabolite biosynthesis (especially in fungi) is a strong, widely documented pattern learned from numerous other proteins (e.g., FtmO1A, GliJ, PptN, various NRPS/PKS tailoring enzymes). This family-level inference meaningfully distinguishes option D from A, B, and C, which require entirely different enzyme classes with no 2OG oxygenase motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 2-oxoglutarate/Fe(II) oxygenase motif is incompatible with pyrimidine metabolism enzymes, peptidoglycan-degrading enzymes, and chorismate synthase. Only secondary metabolite biosynthesis is consistent with this enzyme family in a fungal context."
  },
  "important_caveats": [
    "2-oxoglutarate/Fe(II) oxygenases can occasionally participate in primary metabolic processes (e.g., collagen hydroxylation, DNA demethylation), but among the four offered choices, secondary metabolite biosynthesis is the overwhelmingly dominant and specific association, especially for fungal members of this family.",
    "The specific identity as ppzC in the pyrrolopyrazine cluster is a target-specific annotation; however, the family-level reasoning (2OG oxygenase → secondary metabolite biosynthesis in fungi) is sufficient to distinguish the offered alternatives without knowing the exact protein name."
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
  "benchmark_sequence_length": 374,
  "benchmark_sequence_sha256": "15799a948141cc834792097224072e0866bb99a08601d2dffad614221d57bc06",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 374,
  "current_source_sequence_sha256": "15799a948141cc834792097224072e0866bb99a08601d2dffad614221d57bc06",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZKR7",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "selected_historical_source_sequence_length": 374,
  "selected_historical_source_sequence_sha256": "15799a948141cc834792097224072e0866bb99a08601d2dffad614221d57bc06",
  "selected_historical_version": {
    "accession": "A0A455ZKR7",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZC_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZKR7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2-oxoglutarate-Fe(II) type oxidoreductase ppzC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Rothchild K.W.\",\"Hagar M.\",\"Berry D.\",\"Ryan K.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38578094\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.4c01419\"}],\"citationType\":\"journal article\",\"firstPage\":\"10263\",\"id\":\"38578094\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"10267\",\"publicationDate\":\"2024\",\"title\":\"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\",\"volume\":\"146\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   PPZC_METMF              Reviewed;         374 AA.\nAC   A0A455ZKR7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzC {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein C {ECO:0000303|PubMed:30452111};\nGN   Name=ppzC;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:38578094}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
