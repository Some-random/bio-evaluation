# pathway_0040

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0040.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSVSPQSTMARIPERRVRTLDFAQFRHGEPSGSRGFCRELVDCLSSVGFVKIRNHGISGQEIENVFVMSQLFFSLPQAAKGKAAHPPEANPHRGYSYVGQEKLSRVKDYEKGKREITDVYDIKHYPIDRDARQESYDQGAAVDNLYPNRWPDEQDIPGFRVLMETFYERCHEVHQDILRAIAIGFDLSPSFLTDLCCQNTSELRLNHYPSVHPSSLRKGAKRISEHTDFGTVTLLFQDSVGGLEIEDQNTPGTYFPVLSERKSDIIVNIGDCIQRWTNDKIHSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREFVKEGEKPKYNDISAWQYNQEKLVLTY

[Multiple Choices]
A. Aromatic compound metabolism. .
B. protein ubiquitination. .
C. sterol biosynthesis. .
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

> The sequence-matched UniProt record directly assigns this protein to secondary metabolite biosynthesis, with experimental evidence code ECO:0000269. This supports the keyed pathway.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein’s actual substrate or its association with a particular biosynthetic pathway or gene cluster.


**Reason**

> The input provides only the sequence and choices. It does not give a pathway-specific annotation or context, and no clearly distinguishing sequence feature separates aromatic compound metabolism from secondary metabolite biosynthesis. Knowing the enzyme’s exact role would be needed to choose meaningfully between them.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D, but the original sequence and choices alone do not establish a second specific pathway as defensible.


### Important caveats

- The pathway assignment is supported by reviewer-only evidence, which was not available to the evaluated model.
- The reviewer record is sequence-matched; its source snapshot is not known to be the author's exact snapshot.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s actual substrate or its association with a particular biosynthetic pathway or gene cluster.",
    "reason": "The input provides only the sequence and choices. It does not give a pathway-specific annotation or context, and no clearly distinguishing sequence feature separates aromatic compound metabolism from secondary metabolite biosynthesis. Knowing the enzyme’s exact role would be needed to choose meaningfully between them."
  },
  "case_id": "pathway_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record directly assigns this protein to secondary metabolite biosynthesis, with experimental evidence code ECO:0000269. This supports the keyed pathway."
  },
  "important_caveats": [
    "The pathway assignment is supported by reviewer-only evidence, which was not available to the evaluated model.",
    "The reviewer record is sequence-matched; its source snapshot is not known to be the author's exact snapshot."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D, but the original sequence and choices alone do not establish a second specific pathway as defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record directly assigns this protein to secondary metabolite biosynthesis, with experimental evidence code ECO:0000269. This supports the keyed pathway.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein’s actual substrate or its association with a particular biosynthetic pathway or gene cluster.",
    "reason": "The input provides only the sequence and choices. It does not give a pathway-specific annotation or context, and no clearly distinguishing sequence feature separates aromatic compound metabolism from secondary metabolite biosynthesis. Knowing the enzyme’s exact role would be needed to choose meaningfully between them."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D, but the original sequence and choices alone do not establish a second specific pathway as defensible."
  },
  "important_caveats": [
    "The pathway assignment is supported by reviewer-only evidence, which was not available to the evaluated model.",
    "The reviewer record is sequence-matched; its source snapshot is not known to be the author's exact snapshot."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A455ZMR3) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence code ECO:0000269 from PubMed:38578094. The protein is ppzD, a 2-oxoglutarate-Fe(II) type oxidoreductase in the pyrrolopyrazine biosynthetic gene cluster of Metarhizium majus. Pyrrolopyrazine is a fungal secondary metabolite, confirming the pathway assignment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable 2-oxoglutarate-Fe(II) oxygenase (2OG-Fe(II)) motifs: an HxD triad element 'HTDFGTV' (H-T-D, 1-residue spacing) and a second His in 'HSTSHRVV', consistent with the canonical HxD...H facial triad of the 2OG oxygenase superfamily. The protein is ~350 AA, matching the DSBH-fold size of this family. This immediately eliminates B (protein ubiquitination: no RING C3HC4, U-box, or HECT domain present) and C (sterol biosynthesis: no CYP450 FxxGxxxCxG heme motif, no squalene synthase or sterol methyltransferase features). Between A (aromatic compound metabolism) and D (secondary metabolite biosynthesis): aromatic ring-cleaving dioxygenases in fungi are typically extradiol/intradiol catechol dioxygenases with different motif geometry, or CYP450s. The HxD spacing and overall architecture here match the 2OG oxygenase subfamily commonly embedded in fungal secondary metabolite biosynthetic gene clusters (NRPS/PKS clusters), a well-documented pattern across many fungal species. Thus, family-level knowledge of 2OG oxygenases in fungal biosynthetic clusters meaningfully favors D over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 2OG oxygenase motifs are identifiable from the sequence. Elimination of B and C relies on absence of domain features. The choice between A and D is supported by the well-known association of 2OG oxygenases with fungal secondary metabolite biosynthetic gene clusters versus the different enzyme families (ring-cleaving dioxygenases, CYP450s) typically used in aromatic compound catabolism. This is transferable family-level knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While 2OG oxygenases can occasionally participate in aromatic compound catabolism, the specific motif geometry, protein size, and absence of ring-cleaving enzyme features make D the clearly favored choice. B and C are readily eliminated by absence of relevant domain architectures.


### Important caveats

- The model does not receive organism identity from the input; the fungal biosynthetic gene cluster association must be inferred from the 2OG oxygenase subfamily features rather than from knowing the organism.
- The 2OG oxygenase superfamily is large and participates in many pathways; the argument relies on the specific subfamily context (fungal BGC-type 2OG oxygenase) rather than the superfamily alone.
- The HxD motif identification from sequence is approximate without structural confirmation, but the spacing and flanking context are consistent with 2OG oxygenase annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable 2-oxoglutarate-Fe(II) oxygenase (2OG-Fe(II)) motifs: an HxD triad element 'HTDFGTV' (H-T-D, 1-residue spacing) and a second His in 'HSTSHRVV', consistent with the canonical HxD...H facial triad of the 2OG oxygenase superfamily. The protein is ~350 AA, matching the DSBH-fold size of this family. This immediately eliminates B (protein ubiquitination: no RING C3HC4, U-box, or HECT domain present) and C (sterol biosynthesis: no CYP450 FxxGxxxCxG heme motif, no squalene synthase or sterol methyltransferase features). Between A (aromatic compound metabolism) and D (secondary metabolite biosynthesis): aromatic ring-cleaving dioxygenases in fungi are typically extradiol/intradiol catechol dioxygenases with different motif geometry, or CYP450s. The HxD spacing and overall architecture here match the 2OG oxygenase subfamily commonly embedded in fungal secondary metabolite biosynthetic gene clusters (NRPS/PKS clusters), a well-documented pattern across many fungal species. Thus, family-level knowledge of 2OG oxygenases in fungal biosynthetic clusters meaningfully favors D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 2OG oxygenase motifs are identifiable from the sequence. Elimination of B and C relies on absence of domain features. The choice between A and D is supported by the well-known association of 2OG oxygenases with fungal secondary metabolite biosynthetic gene clusters versus the different enzyme families (ring-cleaving dioxygenases, CYP450s) typically used in aromatic compound catabolism. This is transferable family-level knowledge."
  },
  "case_id": "pathway_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZMR3) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence code ECO:0000269 from PubMed:38578094. The protein is ppzD, a 2-oxoglutarate-Fe(II) type oxidoreductase in the pyrrolopyrazine biosynthetic gene cluster of Metarhizium majus. Pyrrolopyrazine is a fungal secondary metabolite, confirming the pathway assignment."
  },
  "important_caveats": [
    "The model does not receive organism identity from the input; the fungal biosynthetic gene cluster association must be inferred from the 2OG oxygenase subfamily features rather than from knowing the organism.",
    "The 2OG oxygenase superfamily is large and participates in many pathways; the argument relies on the specific subfamily context (fungal BGC-type 2OG oxygenase) rather than the superfamily alone.",
    "The HxD motif identification from sequence is approximate without structural confirmation, but the spacing and flanking context are consistent with 2OG oxygenase annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 2OG oxygenases can occasionally participate in aromatic compound catabolism, the specific motif geometry, protein size, and absence of ring-cleaving enzyme features make D the clearly favored choice. B and C are readily eliminated by absence of relevant domain architectures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZMR3) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence code ECO:0000269 from PubMed:38578094. The protein is ppzD, a 2-oxoglutarate-Fe(II) type oxidoreductase in the pyrrolopyrazine biosynthetic gene cluster of Metarhizium majus. Pyrrolopyrazine is a fungal secondary metabolite, confirming the pathway assignment.",
    "evidence_ids": ["C5", "H4", "C4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable 2-oxoglutarate-Fe(II) oxygenase (2OG-Fe(II)) motifs: an HxD triad element 'HTDFGTV' (H-T-D, 1-residue spacing) and a second His in 'HSTSHRVV', consistent with the canonical HxD...H facial triad of the 2OG oxygenase superfamily. The protein is ~350 AA, matching the DSBH-fold size of this family. This immediately eliminates B (protein ubiquitination: no RING C3HC4, U-box, or HECT domain present) and C (sterol biosynthesis: no CYP450 FxxGxxxCxG heme motif, no squalene synthase or sterol methyltransferase features). Between A (aromatic compound metabolism) and D (secondary metabolite biosynthesis): aromatic ring-cleaving dioxygenases in fungi are typically extradiol/intradiol catechol dioxygenases with different motif geometry, or CYP450s. The HxD spacing and overall architecture here match the 2OG oxygenase subfamily commonly embedded in fungal secondary metabolite biosynthetic gene clusters (NRPS/PKS clusters), a well-documented pattern across many fungal species. Thus, family-level knowledge of 2OG oxygenases in fungal biosynthetic clusters meaningfully favors D over A.",
    "missing_item_specific_fact": "",
    "reason": "The 2OG oxygenase motifs are identifiable from the sequence. Elimination of B and C relies on absence of domain features. The choice between A and D is supported by the well-known association of 2OG oxygenases with fungal secondary metabolite biosynthetic gene clusters versus the different enzyme families (ring-cleaving dioxygenases, CYP450s) typically used in aromatic compound catabolism. This is transferable family-level knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 2OG oxygenases can occasionally participate in aromatic compound catabolism, the specific motif geometry, protein size, and absence of ring-cleaving enzyme features make D the clearly favored choice. B and C are readily eliminated by absence of relevant domain architectures."
  },
  "important_caveats": [
    "The model does not receive organism identity from the input; the fungal biosynthetic gene cluster association must be inferred from the 2OG oxygenase subfamily features rather than from knowing the organism.",
    "The 2OG oxygenase superfamily is large and participates in many pathways; the argument relies on the specific subfamily context (fungal BGC-type 2OG oxygenase) rather than the superfamily alone.",
    "The HxD motif identification from sequence is approximate without structural confirmation, but the spacing and flanking context are consistent with 2OG oxygenase annotation."
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
  "benchmark_sequence_length": 349,
  "benchmark_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZMR3",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "selected_historical_version": {
    "accession": "A0A455ZMR3",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZD_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZMR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein D\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.57\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2-oxoglutarate-Fe(II) type oxidoreductase ppzD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Rothchild K.W.\",\"Hagar M.\",\"Berry D.\",\"Ryan K.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38578094\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.4c01419\"}],\"citationType\":\"journal article\",\"firstPage\":\"10263\",\"id\":\"38578094\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"10267\",\"publicationDate\":\"2024\",\"title\":\"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\",\"volume\":\"146\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   PPZD_METMF              Reviewed;         349 AA.\nAC   A0A455ZMR3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};\nGN   Name=ppzD;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:38578094}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
