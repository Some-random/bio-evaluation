# pathway_0164

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0164.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVTKPTTPKPPPALGIPDSAYTVDVRVIDTGTLLHLNPSLFWQPPIDGFTGLHAPIYCFLVSHGSQHVIFDLGVRTDWENYAPKIVSIIKATTTVTPGSDVPSMLDEDTSGLGIRSADIGAVIWSHNHFDHVGDVSRFPLTTDLIVGPGVRGVSWPGWPSNPDGIVLDSDVEGRVVREVSFEAGLKIGHFDAMDFFGDGSFYLLDAPGHAVGHLCALARTTANEPTFVFMGADACHHPGLLRPSNYLPLPSASTLAGVLTGPPQCPGELLQQLTLPDEPFFTVAPRMFPDHDAATDTVRKIQELDASDNCLVLIAHDLSLRDKIPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQGIEEELGKQSSLKCS

[Multiple Choices]
A. coenzyme A biosynthesis
B. NAD(+) biosynthesis
C. Secondary metabolite biosynthesis
D. peptidoglycan biosynthesis. .
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

> The sequence-matched UniProt pathway annotation identifies secondary-metabolite and terpenoid biosynthesis, with experimental evidence attributed to a publication. This supports choice C, though the cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with a metal-dependent hydrolase, including a histidine-rich region. Transferable knowledge of this enzyme family makes a tailoring role in specialized-metabolite biosynthesis a plausible fit; the offered CoA, NAD(+), and peptidoglycan choices instead name primary-pathway enzyme groups with different characteristic functions. This favors C among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features and the contrast among the offered pathway categories provide a credible, probabilistic basis for preferring C. They do not establish the exact substrate or pathway, so this is not a definitive sequence-only assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports C, and the other options name distinct pathways. The limited specificity of the sequence-based inference does not itself establish another equally defensible choice.


### Important caveats

- The reviewer-only evidence is sequence-matched, but the annotation's experimental support was not independently verified against the cited paper.
- A metallo-hydrolase family assignment alone does not uniquely determine a pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a metal-dependent hydrolase, including a histidine-rich region. Transferable knowledge of this enzyme family makes a tailoring role in specialized-metabolite biosynthesis a plausible fit; the offered CoA, NAD(+), and peptidoglycan choices instead name primary-pathway enzyme groups with different characteristic functions. This favors C among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the contrast among the offered pathway categories provide a credible, probabilistic basis for preferring C. They do not establish the exact substrate or pathway, so this is not a definitive sequence-only assignment."
  },
  "case_id": "pathway_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation identifies secondary-metabolite and terpenoid biosynthesis, with experimental evidence attributed to a publication. This supports choice C, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only evidence is sequence-matched, but the annotation's experimental support was not independently verified against the cited paper.",
    "A metallo-hydrolase family assignment alone does not uniquely determine a pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C, and the other options name distinct pathways. The limited specificity of the sequence-based inference does not itself establish another equally defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation identifies secondary-metabolite and terpenoid biosynthesis, with experimental evidence attributed to a publication. This supports choice C, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a metal-dependent hydrolase, including a histidine-rich region. Transferable knowledge of this enzyme family makes a tailoring role in specialized-metabolite biosynthesis a plausible fit; the offered CoA, NAD(+), and peptidoglycan choices instead name primary-pathway enzyme groups with different characteristic functions. This favors C among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the contrast among the offered pathway categories provide a credible, probabilistic basis for preferring C. They do not establish the exact substrate or pathway, so this is not a definitive sequence-only assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C, and the other options name distinct pathways. The limited specificity of the sequence-based inference does not itself establish another equally defensible choice."
  },
  "important_caveats": [
    "The reviewer-only evidence is sequence-matched, but the annotation's experimental support was not independently verified against the cited paper.",
    "A metallo-hydrolase family assignment alone does not uniquely determine a pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this exact sequence (P9WEG2, MFMC_ANNMO) annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:38404388). The protein is a metallo-hydrolase mfmC, part of the 11'-O-desmethylfendlerol biosynthesis gene cluster in the fungus Annulohypoxylon moriforme. The expected answer 'Secondary metabolite biosynthesis' directly matches the UniProt pathway annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of the metallo-beta-lactamase (MBL) superfamily / metallo-hydrolase fold: a conserved HD/HHLD metal-binding motif (visible in 'IPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQ' and 'IPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQ'), two β-sandwich halves separated by a long insert region, and a C-terminal region with additional metal-coordinating residues. (1) Coenzyme A biosynthesis (A) and NAD+ biosynthesis (B) are eliminated because their enzyme complements (pantothenate kinase, PCPS/PCDC, CoA ligase; NAPRT, NMNAT, NAD synthetase, NAD kinase) belong to entirely different enzyme families (kinases, transferases, synthetases) and do not employ the MBL/metallo-hydrolase fold. (2) Peptidoglycan biosynthesis (D) is primarily a bacterial pathway; while some peptidoglycan-related enzymes (e.g., D-Ala-D-Ala carboxypeptidases, certain amidases) use an MBL-like fold, the specific architecture here—long eukaryotic-style insert loops, the particular HD/HHLD spacing, and the overall 377-aa size with a C-terminal tail—does not match known peptidoglycan-pathway MBL enzymes. (3) Metallo-hydrolases are well-documented tailoring enzymes in fungal secondary metabolite gene clusters (polyketide-terpenoid hybrid pathways), where they perform hydrolytic modifications on cluster intermediates. The long insert regions and the overall architecture are consistent with this role. Therefore, the metallo-hydrolase fold plus the specific sequence architecture meaningfully distinguishes C from A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A and B is straightforward from enzyme-family knowledge (MBL fold is incompatible with CoA/NAD+ biosynthetic enzymes). The C vs D distinction relies on recognizing that the specific MBL architecture (long inserts, HD/HHLD motif arrangement, eukaryotic-like complexity) is more consistent with secondary metabolite tailoring enzymes than with peptidoglycan-pathway MBL enzymes. This is a transferable structural-biology argument based on known MBL subclass distributions across pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the C vs D distinction is less airtight than the elimination of A and B, the architectural features of the MBL fold in this sequence (long insert regions, HD/HHLD motif arrangement, eukaryotic-like complexity) provide a reasonable basis to favor secondary metabolite tailoring over peptidoglycan metabolism. No other option is seriously defensible.


### Important caveats

- The model is not told the organism is a fungus. The inference that this is a eukaryotic protein (and thus unlikely to participate in peptidoglycan biosynthesis) relies on sequence architecture rather than explicit organism information.
- The MBL superfamily is extremely broad and found across many unrelated pathways. The specific subclass assignment from sequence alone is approximate; the argument that this particular architecture matches secondary metabolite tailoring rather than peptidoglycan enzymes is plausible but not airtight from sequence alone.
- The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:38404388), so the key is well-grounded.
- The entry was first published in April 2025, so the specific annotation may not have been available in all training corpora, but the transferable reasoning argument does not depend on this specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of the metallo-beta-lactamase (MBL) superfamily / metallo-hydrolase fold: a conserved HD/HHLD metal-binding motif (visible in 'IPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQ' and 'IPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQ'), two β-sandwich halves separated by a long insert region, and a C-terminal region with additional metal-coordinating residues. (1) Coenzyme A biosynthesis (A) and NAD+ biosynthesis (B) are eliminated because their enzyme complements (pantothenate kinase, PCPS/PCDC, CoA ligase; NAPRT, NMNAT, NAD synthetase, NAD kinase) belong to entirely different enzyme families (kinases, transferases, synthetases) and do not employ the MBL/metallo-hydrolase fold. (2) Peptidoglycan biosynthesis (D) is primarily a bacterial pathway; while some peptidoglycan-related enzymes (e.g., D-Ala-D-Ala carboxypeptidases, certain amidases) use an MBL-like fold, the specific architecture here—long eukaryotic-style insert loops, the particular HD/HHLD spacing, and the overall 377-aa size with a C-terminal tail—does not match known peptidoglycan-pathway MBL enzymes. (3) Metallo-hydrolases are well-documented tailoring enzymes in fungal secondary metabolite gene clusters (polyketide-terpenoid hybrid pathways), where they perform hydrolytic modifications on cluster intermediates. The long insert regions and the overall architecture are consistent with this role. Therefore, the metallo-hydrolase fold plus the specific sequence architecture meaningfully distinguishes C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and B is straightforward from enzyme-family knowledge (MBL fold is incompatible with CoA/NAD+ biosynthetic enzymes). The C vs D distinction relies on recognizing that the specific MBL architecture (long inserts, HD/HHLD motif arrangement, eukaryotic-like complexity) is more consistent with secondary metabolite tailoring enzymes than with peptidoglycan-pathway MBL enzymes. This is a transferable structural-biology argument based on known MBL subclass distributions across pathways."
  },
  "case_id": "pathway_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (P9WEG2, MFMC_ANNMO) annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:38404388). The protein is a metallo-hydrolase mfmC, part of the 11'-O-desmethylfendlerol biosynthesis gene cluster in the fungus Annulohypoxylon moriforme. The expected answer 'Secondary metabolite biosynthesis' directly matches the UniProt pathway annotation."
  },
  "important_caveats": [
    "The model is not told the organism is a fungus. The inference that this is a eukaryotic protein (and thus unlikely to participate in peptidoglycan biosynthesis) relies on sequence architecture rather than explicit organism information.",
    "The MBL superfamily is extremely broad and found across many unrelated pathways. The specific subclass assignment from sequence alone is approximate; the argument that this particular architecture matches secondary metabolite tailoring rather than peptidoglycan enzymes is plausible but not airtight from sequence alone.",
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:38404388), so the key is well-grounded.",
    "The entry was first published in April 2025, so the specific annotation may not have been available in all training corpora, but the transferable reasoning argument does not depend on this specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C vs D distinction is less airtight than the elimination of A and B, the architectural features of the MBL fold in this sequence (long insert regions, HD/HHLD motif arrangement, eukaryotic-like complexity) provide a reasonable basis to favor secondary metabolite tailoring over peptidoglycan metabolism. No other option is seriously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (P9WEG2, MFMC_ANNMO) annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:38404388). The protein is a metallo-hydrolase mfmC, part of the 11'-O-desmethylfendlerol biosynthesis gene cluster in the fungus Annulohypoxylon moriforme. The expected answer 'Secondary metabolite biosynthesis' directly matches the UniProt pathway annotation.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of the metallo-beta-lactamase (MBL) superfamily / metallo-hydrolase fold: a conserved HD/HHLD metal-binding motif (visible in 'IPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQ' and 'IPLFPKTINGWKESQVKTETRWLFCNDFMPALHHLDNKQ'), two β-sandwich halves separated by a long insert region, and a C-terminal region with additional metal-coordinating residues. (1) Coenzyme A biosynthesis (A) and NAD+ biosynthesis (B) are eliminated because their enzyme complements (pantothenate kinase, PCPS/PCDC, CoA ligase; NAPRT, NMNAT, NAD synthetase, NAD kinase) belong to entirely different enzyme families (kinases, transferases, synthetases) and do not employ the MBL/metallo-hydrolase fold. (2) Peptidoglycan biosynthesis (D) is primarily a bacterial pathway; while some peptidoglycan-related enzymes (e.g., D-Ala-D-Ala carboxypeptidases, certain amidases) use an MBL-like fold, the specific architecture here—long eukaryotic-style insert loops, the particular HD/HHLD spacing, and the overall 377-aa size with a C-terminal tail—does not match known peptidoglycan-pathway MBL enzymes. (3) Metallo-hydrolases are well-documented tailoring enzymes in fungal secondary metabolite gene clusters (polyketide-terpenoid hybrid pathways), where they perform hydrolytic modifications on cluster intermediates. The long insert regions and the overall architecture are consistent with this role. Therefore, the metallo-hydrolase fold plus the specific sequence architecture meaningfully distinguishes C from A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and B is straightforward from enzyme-family knowledge (MBL fold is incompatible with CoA/NAD+ biosynthetic enzymes). The C vs D distinction relies on recognizing that the specific MBL architecture (long inserts, HD/HHLD motif arrangement, eukaryotic-like complexity) is more consistent with secondary metabolite tailoring enzymes than with peptidoglycan-pathway MBL enzymes. This is a transferable structural-biology argument based on known MBL subclass distributions across pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C vs D distinction is less airtight than the elimination of A and B, the architectural features of the MBL fold in this sequence (long insert regions, HD/HHLD motif arrangement, eukaryotic-like complexity) provide a reasonable basis to favor secondary metabolite tailoring over peptidoglycan metabolism. No other option is seriously defensible."
  },
  "important_caveats": [
    "The model is not told the organism is a fungus. The inference that this is a eukaryotic protein (and thus unlikely to participate in peptidoglycan biosynthesis) relies on sequence architecture rather than explicit organism information.",
    "The MBL superfamily is extremely broad and found across many unrelated pathways. The specific subclass assignment from sequence alone is approximate; the argument that this particular architecture matches secondary metabolite tailoring rather than peptidoglycan enzymes is plausible but not airtight from sequence alone.",
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:38404388), so the key is well-grounded.",
    "The entry was first published in April 2025, so the specific annotation may not have been available in all training corpora, but the transferable reasoning argument does not depend on this specific annotation."
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
  "benchmark_sequence_length": 377,
  "benchmark_sequence_sha256": "6cff3d484fea2e655c9567dfa5220e1597a25bb07c99d3fe88752467ea0f10bf",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 377,
  "current_source_sequence_sha256": "6cff3d484fea2e655c9567dfa5220e1597a25bb07c99d3fe88752467ea0f10bf",
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
  "requested_accession": "P9WEG2",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "c05a1fcecec48703c5f973a861007f25f3687df65cd0f360945ab7c419ba8357",
  "selected_historical_source_sequence_length": 377,
  "selected_historical_source_sequence_sha256": "6cff3d484fea2e655c9567dfa5220e1597a25bb07c99d3fe88752467ea0f10bf",
  "selected_historical_version": {
    "accession": "P9WEG2",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMC_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:13.447356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:13.447356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:13.447356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein C\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Metallo-beta-lactamase mfmC\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Metallo-hydrolase mfmC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:13.447356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:13.447356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:13.447356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dd99405fa002f0a7774c31c454f14654a28e0270cd747422c8361c13759ef740",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMC_ANNMO              Reviewed;         377 AA.\nAC   P9WEG2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Metallo-hydrolase mfmC {ECO:0000303|PubMed:38404388};\nDE            EC=3.1.1.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein C {ECO:0000303|PubMed:38404388};\nDE   AltName: Full=Metallo-beta-lactamase mfmC {ECO:0000305};\nGN   Name=mfmC {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_462786;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:16.833538+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05a1fcecec48703c5f973a861007f25f3687df65cd0f360945ab7c419ba8357",
  "url": "https://rest.uniprot.org/unisave/P9WEG2?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:16.833538+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05a1fcecec48703c5f973a861007f25f3687df65cd0f360945ab7c419ba8357",
  "url": "https://rest.uniprot.org/unisave/P9WEG2?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:38404388}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:16.833538+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05a1fcecec48703c5f973a861007f25f3687df65cd0f360945ab7c419ba8357",
  "url": "https://rest.uniprot.org/unisave/P9WEG2?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
