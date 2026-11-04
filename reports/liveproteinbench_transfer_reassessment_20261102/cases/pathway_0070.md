# pathway_0070

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0070.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWSLIPLTAIVLVLVAILHRLFFHPLSHVPGPFLARFSSLYLHSICYLGIEATVLRQLHIKYKTKVLRVAPNSVSISDSEAVGEIYVRGGGFPKDDRYKNFNLGPIVSIFSSLDREYRDVRAKAVAPLFSPAQLRAESGPQGVIGGCIAEFVDQLRKSKEAGIGADLMDMCARLSIDVVTGYLLGQKYGGLQENAHLPPQERQSHKLSANPFIFSIVAFSRFSLLPHRIFQFLYSTSQRLSTNDEVTESFLKLDRFTNNVLEGTTAGEKVSEKPNGGYYHERLISQAGISRMEAAAQSQAVLFAGADSTAVMLATILFHLVQNGAARSRLLCEVRSDKPQDMRFLRAVVKEGLRLGMANPTRMTRVVPKSGPGLRVGDVLLSPGTIVGCAAYNLHHDPEVFPDPFTFRPERWLDDGTDRGLRRPGMEKSMIPFGVGSRACIGKNLAQQQLHDTVVAVIDSEVLEGARTCQERIEIIEWFNADIKGHHLDIKWS

[Multiple Choices]
A. Alkaloid biosynthesis
B. Secondary metabolite biosynthesis
C. Antifungal biosynthesis. .
D. Purine metabolism
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

> The sequence-matched UniProt record annotates the protein to secondary metabolite biosynthesis and terpenoid biosynthesis, citing experimental evidence. This supports choice B; the cited paper was not independently reviewed here.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment and cysteine-containing region are consistent with a membrane-associated cytochrome P450. From other fungal P450s, one can reasonably infer oxidative tailoring in specialized-metabolite biosynthesis, favoring the broad secondary-metabolite option over purine metabolism. This is a family-level probabilistic inference, not a way to identify the exact product pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable P450 and fungal specialized-metabolism patterns provide a meaningful basis for choice B among these alternatives, though they do not establish the exact substrate or pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Alkaloid and antifungal biosynthesis can be forms of secondary-metabolite biosynthesis, but the supplied sequence offers no particular basis to select either narrower category over the broad choice B.


### Important caveats

- The pathway annotation is cited as experimentally supported in the sequence-matched source record, but the cited primary study was not independently evaluated.
- The family-level inference does not by itself identify the protein's specific natural-product pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-containing region are consistent with a membrane-associated cytochrome P450. From other fungal P450s, one can reasonably infer oxidative tailoring in specialized-metabolite biosynthesis, favoring the broad secondary-metabolite option over purine metabolism. This is a family-level probabilistic inference, not a way to identify the exact product pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable P450 and fungal specialized-metabolism patterns provide a meaningful basis for choice B among these alternatives, though they do not establish the exact substrate or pathway."
  },
  "case_id": "pathway_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to secondary metabolite biosynthesis and terpenoid biosynthesis, citing experimental evidence. This supports choice B; the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway annotation is cited as experimentally supported in the sequence-matched source record, but the cited primary study was not independently evaluated.",
    "The family-level inference does not by itself identify the protein's specific natural-product pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Alkaloid and antifungal biosynthesis can be forms of secondary-metabolite biosynthesis, but the supplied sequence offers no particular basis to select either narrower category over the broad choice B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to secondary metabolite biosynthesis and terpenoid biosynthesis, citing experimental evidence. This supports choice B; the cited paper was not independently reviewed here.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-containing region are consistent with a membrane-associated cytochrome P450. From other fungal P450s, one can reasonably infer oxidative tailoring in specialized-metabolite biosynthesis, favoring the broad secondary-metabolite option over purine metabolism. This is a family-level probabilistic inference, not a way to identify the exact product pathway.",
    "missing_item_specific_fact": "",
    "reason": "Transferable P450 and fungal specialized-metabolism patterns provide a meaningful basis for choice B among these alternatives, though they do not establish the exact substrate or pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Alkaloid and antifungal biosynthesis can be forms of secondary-metabolite biosynthesis, but the supplied sequence offers no particular basis to select either narrower category over the broad choice B."
  },
  "important_caveats": [
    "The pathway annotation is cited as experimentally supported in the sequence-matched source record, but the cited primary study was not independently evaluated.",
    "The family-level inference does not by itself identify the protein's specific natural-product pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates this protein (P9WEG5, Cytochrome P450 monooxygenase mfmF from Annulohypoxylon moriforme) under the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:38404388). The author's expected answer B ('Secondary metabolite biosynthesis') matches the pathway-level annotation in the database record.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~493 aa) contains the hallmark cytochrome P450 heme-binding motif 'GGFPK' and the overall architecture (length, conserved FxxGxxxCxG-like region, I-helix) is diagnostic of a fungal P450. Transferable knowledge from the large body of characterized fungal P450s (e.g., ergot alkaloid P450s, terpenoid cyclase-associated P450s, polyketide tailoring P450s) establishes that fungal P450s are overwhelmingly assigned to 'Secondary metabolite biosynthesis' as their pathway-level annotation in databases like UniProt. Option D (Purine metabolism) is eliminated because P450s catalyze oxidative transformations of hydrophobic substrates, not nucleotide interconversions handled by transferases, synthetases, and hydrolases. Option C ('Antifungal biosynthesis') is not a recognized pathway category in standard pathway taxonomies and is an implausible biological label. Between A (Alkaloid biosynthesis) and B (Secondary metabolite biosynthesis): alkaloid-biosynthesis P450s (e.g., in ergot or indole-diterpene pathways) occupy specific gene clusters and often show distinctive sequence signatures (e.g., specific N-terminal extensions, cluster-specific motifs); none are apparent here. The broad 'Secondary metabolite biosynthesis' is the standard UniProt pathway-level annotation for fungal P450s involved in natural-product tailoring, making B the most defensible default when no specific alkaloid-biosynthesis evidence is present in the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the P450 from sequence motifs, eliminate purine metabolism by enzyme-class mismatch, dismiss 'Antifungal biosynthesis' as a non-standard category, and apply the learned generalization that fungal P450s without specific alkaloid-cluster features are annotated under the broad 'Secondary metabolite biosynthesis' pathway. This provides a concrete, transferable basis for selecting B over the other offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is eliminated by enzyme-class mismatch. C is not a recognized pathway name. A (Alkaloid biosynthesis) is a narrower subcategory that would require specific evidence (gene-cluster context, substrate specificity) absent from the sequence; without such evidence, the standard pathway-level assignment B is the most defensible. No two options are equally supported by the available reasoning.


### Important caveats

- The specific sub-pathway is terpenoid biosynthesis (a subcategory of secondary metabolite biosynthesis); the question's option B captures the parent pathway level, which is the standard UniProt pathway annotation.
- The P450 identification from sequence is robust, but distinguishing among secondary-metabolite sub-pathways (terpenoid vs. polyketide vs. alkaloid) from sequence alone is generally not possible; the question is answerable because it offers the broad parent category as an option.
- Option C ('Antifungal biosynthesis') has a trailing period and space in the original text, suggesting a minor formatting artifact; this does not affect the biological assessment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~493 aa) contains the hallmark cytochrome P450 heme-binding motif 'GGFPK' and the overall architecture (length, conserved FxxGxxxCxG-like region, I-helix) is diagnostic of a fungal P450. Transferable knowledge from the large body of characterized fungal P450s (e.g., ergot alkaloid P450s, terpenoid cyclase-associated P450s, polyketide tailoring P450s) establishes that fungal P450s are overwhelmingly assigned to 'Secondary metabolite biosynthesis' as their pathway-level annotation in databases like UniProt. Option D (Purine metabolism) is eliminated because P450s catalyze oxidative transformations of hydrophobic substrates, not nucleotide interconversions handled by transferases, synthetases, and hydrolases. Option C ('Antifungal biosynthesis') is not a recognized pathway category in standard pathway taxonomies and is an implausible biological label. Between A (Alkaloid biosynthesis) and B (Secondary metabolite biosynthesis): alkaloid-biosynthesis P450s (e.g., in ergot or indole-diterpene pathways) occupy specific gene clusters and often show distinctive sequence signatures (e.g., specific N-terminal extensions, cluster-specific motifs); none are apparent here. The broad 'Secondary metabolite biosynthesis' is the standard UniProt pathway-level annotation for fungal P450s involved in natural-product tailoring, making B the most defensible default when no specific alkaloid-biosynthesis evidence is present in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 from sequence motifs, eliminate purine metabolism by enzyme-class mismatch, dismiss 'Antifungal biosynthesis' as a non-standard category, and apply the learned generalization that fungal P450s without specific alkaloid-cluster features are annotated under the broad 'Secondary metabolite biosynthesis' pathway. This provides a concrete, transferable basis for selecting B over the other offered choices."
  },
  "case_id": "pathway_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates this protein (P9WEG5, Cytochrome P450 monooxygenase mfmF from Annulohypoxylon moriforme) under the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:38404388). The author's expected answer B ('Secondary metabolite biosynthesis') matches the pathway-level annotation in the database record."
  },
  "important_caveats": [
    "The specific sub-pathway is terpenoid biosynthesis (a subcategory of secondary metabolite biosynthesis); the question's option B captures the parent pathway level, which is the standard UniProt pathway annotation.",
    "The P450 identification from sequence is robust, but distinguishing among secondary-metabolite sub-pathways (terpenoid vs. polyketide vs. alkaloid) from sequence alone is generally not possible; the question is answerable because it offers the broad parent category as an option.",
    "Option C ('Antifungal biosynthesis') has a trailing period and space in the original text, suggesting a minor formatting artifact; this does not affect the biological assessment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is eliminated by enzyme-class mismatch. C is not a recognized pathway name. A (Alkaloid biosynthesis) is a narrower subcategory that would require specific evidence (gene-cluster context, substrate specificity) absent from the sequence; without such evidence, the standard pathway-level assignment B is the most defensible. No two options are equally supported by the available reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates this protein (P9WEG5, Cytochrome P450 monooxygenase mfmF from Annulohypoxylon moriforme) under the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:38404388). The author's expected answer B ('Secondary metabolite biosynthesis') matches the pathway-level annotation in the database record.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~493 aa) contains the hallmark cytochrome P450 heme-binding motif 'GGFPK' and the overall architecture (length, conserved FxxGxxxCxG-like region, I-helix) is diagnostic of a fungal P450. Transferable knowledge from the large body of characterized fungal P450s (e.g., ergot alkaloid P450s, terpenoid cyclase-associated P450s, polyketide tailoring P450s) establishes that fungal P450s are overwhelmingly assigned to 'Secondary metabolite biosynthesis' as their pathway-level annotation in databases like UniProt. Option D (Purine metabolism) is eliminated because P450s catalyze oxidative transformations of hydrophobic substrates, not nucleotide interconversions handled by transferases, synthetases, and hydrolases. Option C ('Antifungal biosynthesis') is not a recognized pathway category in standard pathway taxonomies and is an implausible biological label. Between A (Alkaloid biosynthesis) and B (Secondary metabolite biosynthesis): alkaloid-biosynthesis P450s (e.g., in ergot or indole-diterpene pathways) occupy specific gene clusters and often show distinctive sequence signatures (e.g., specific N-terminal extensions, cluster-specific motifs); none are apparent here. The broad 'Secondary metabolite biosynthesis' is the standard UniProt pathway-level annotation for fungal P450s involved in natural-product tailoring, making B the most defensible default when no specific alkaloid-biosynthesis evidence is present in the sequence.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 from sequence motifs, eliminate purine metabolism by enzyme-class mismatch, dismiss 'Antifungal biosynthesis' as a non-standard category, and apply the learned generalization that fungal P450s without specific alkaloid-cluster features are annotated under the broad 'Secondary metabolite biosynthesis' pathway. This provides a concrete, transferable basis for selecting B over the other offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is eliminated by enzyme-class mismatch. C is not a recognized pathway name. A (Alkaloid biosynthesis) is a narrower subcategory that would require specific evidence (gene-cluster context, substrate specificity) absent from the sequence; without such evidence, the standard pathway-level assignment B is the most defensible. No two options are equally supported by the available reasoning."
  },
  "important_caveats": [
    "The specific sub-pathway is terpenoid biosynthesis (a subcategory of secondary metabolite biosynthesis); the question's option B captures the parent pathway level, which is the standard UniProt pathway annotation.",
    "The P450 identification from sequence is robust, but distinguishing among secondary-metabolite sub-pathways (terpenoid vs. polyketide vs. alkaloid) from sequence alone is generally not possible; the question is answerable because it offers the broad parent category as an option.",
    "Option C ('Antifungal biosynthesis') has a trailing period and space in the original text, suggesting a minor formatting artifact; this does not affect the biological assessment."
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
  "benchmark_sequence_length": 493,
  "benchmark_sequence_sha256": "5f1ec0eac26ac312febaccb3855fd0772573fc6cede2b531165b6dbd6fc868e2",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 493,
  "current_source_sequence_sha256": "5f1ec0eac26ac312febaccb3855fd0772573fc6cede2b531165b6dbd6fc868e2",
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
  "requested_accession": "P9WEG5",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "selected_historical_source_sequence_length": 493,
  "selected_historical_source_sequence_sha256": "5f1ec0eac26ac312febaccb3855fd0772573fc6cede2b531165b6dbd6fc868e2",
  "selected_historical_version": {
    "accession": "P9WEG5",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMF_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase mfmF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMF_ANNMO              Reviewed;         493 AA.\nAC   P9WEG5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Cytochrome P450 monooxygenase mfmF {ECO:0000303|PubMed:38404388};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein F {ECO:0000303|PubMed:38404388};\nGN   Name=mfmF {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_472414;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:38404388}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
