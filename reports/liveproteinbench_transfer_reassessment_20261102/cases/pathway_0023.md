# pathway_0023

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0023.txt)

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
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. spheroidene biosynthesis. .
B. Lipid metabolism
C. Amino-acid biosynthesis
D. Cell wall biogenesis
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

> The sequence matches the cited UniProt record. That record annotates the protein as cystathionine gamma-synthase and assigns it to de novo L-methionine/amino-acid biosynthesis. The enzyme and pathway annotations cite experimental evidence and a characterization study, supporting choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conserved enzyme-like core compatible with the cystathionine gamma-synthase family. Transferable knowledge of this family links its homologs to sulfur amino-acid, including methionine, biosynthesis. That meaningfully favors amino-acid biosynthesis over lipid metabolism, cell-wall biogenesis, or spheroidene biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a credible basis for distinguishing the offered choices without relying on the exact protein's database record. The sequence alone may not establish every functional detail, but the alternatives are broad enough that recognizing the enzyme family is meaningfully discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered categories, amino-acid biosynthesis is the clear fit for the inferred enzyme family.


### Important caveats

- The organism, accession, and exact annotation in the reviewer-only evidence were not part of the original input and are not used as the basis for the answerability judgment.
- The supporting database annotation cites experimental work; that citation is not an independent review of the primary study.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conserved enzyme-like core compatible with the cystathionine gamma-synthase family. Transferable knowledge of this family links its homologs to sulfur amino-acid, including methionine, biosynthesis. That meaningfully favors amino-acid biosynthesis over lipid metabolism, cell-wall biogenesis, or spheroidene biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a credible basis for distinguishing the offered choices without relying on the exact protein's database record. The sequence alone may not establish every functional detail, but the alternatives are broad enough that recognizing the enzyme family is meaningfully discriminating."
  },
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record. That record annotates the protein as cystathionine gamma-synthase and assigns it to de novo L-methionine/amino-acid biosynthesis. The enzyme and pathway annotations cite experimental evidence and a characterization study, supporting choice C."
  },
  "important_caveats": [
    "The organism, accession, and exact annotation in the reviewer-only evidence were not part of the original input and are not used as the basis for the answerability judgment.",
    "The supporting database annotation cites experimental work; that citation is not an independent review of the primary study."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered categories, amino-acid biosynthesis is the clear fit for the inferred enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record. That record annotates the protein as cystathionine gamma-synthase and assigns it to de novo L-methionine/amino-acid biosynthesis. The enzyme and pathway annotations cite experimental evidence and a characterization study, supporting choice C.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conserved enzyme-like core compatible with the cystathionine gamma-synthase family. Transferable knowledge of this family links its homologs to sulfur amino-acid, including methionine, biosynthesis. That meaningfully favors amino-acid biosynthesis over lipid metabolism, cell-wall biogenesis, or spheroidene biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a credible basis for distinguishing the offered choices without relying on the exact protein's database record. The sequence alone may not establish every functional detail, but the alternatives are broad enough that recognizing the enzyme family is meaningfully discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered categories, amino-acid biosynthesis is the clear fit for the inferred enzyme family."
  },
  "important_caveats": [
    "The organism, accession, and exact annotation in the reviewer-only evidence were not part of the original input and are not used as the basis for the answerability judgment.",
    "The supporting database annotation cites experimental work; that citation is not an independent review of the primary study."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9ZPL5, CGS1_TOBAC) explicitly annotates this protein as Cystathionine gamma-synthase 1, chloroplastic (EC 2.5.1.160) with the pathway comment 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1' backed by experimental evidence (ECO:0000269|PubMed:10595588). The sequence matches the benchmark input exactly (540 AA, SHA-256 match). The expected answer C (Amino-acid biosynthesis) is directly and experimentally supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several transferable diagnostic features. (1) The N-terminal ~50 residues are rich in Ser, Thr, Ala, and Arg with a bipartite character typical of a chloroplastic transit peptide, indicating a plastid-localized enzyme. (2) Near the C-terminus, the motif 'SFGG' (in 'IAPSFGGCESIVDQ') and the 'GG' dinucleotide are well-known signatures of fold-type II PLP-dependent trans-sulfuration enzymes, a family that includes cystathionine beta-synthase (CBS), cystathionine gamma-synthase (CGS), O-acetylserine sulfhydrylase (OASS/cysteine synthase), and methionine gamma-lyase, all characterized across bacteria, fungi, and plants. (3) The region 'GADLVLHS' and the overall domain architecture are consistent with the CGS/CBS subfamily. (4) Trans-sulfuration enzymes catalyze steps in methionine and cysteine biosynthesis, placing them squarely in amino-acid biosynthesis. Against the other options: spheroidene biosynthesis involves phytoene synthase, carotenoid hydroxylases, and ketolases with entirely different folds and motifs; lipid metabolism enzymes (FAS, desaturases, thioesterases) lack PLP-binding 'GG' motifs; cell wall biogenesis enzymes (cellulose synthases, glycosyltransferases, pectin-modifying enzymes) have no PLP or trans-sulfuration signatures. Thus, recognizing the trans-sulfuration family from homologs in Arabidopsis, E. coli, and yeast is sufficient to select C over A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the chloroplastic transit peptide, recognize the 'SFGG' and 'GG' motifs diagnostic of fold-type II PLP trans-sulfuration enzymes (CBS, CGS, OASS family), and connect this enzyme family to amino-acid biosynthesis. This is a legitimate family-level inference from well-characterized homologs, not a lookup of this specific protein's annotation. The four offered choices are sufficiently distinct that family recognition eliminates A, B, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The trans-sulfuration family motifs and chloroplastic localization unambiguously point to amino-acid biosynthesis (C). The other three options (carotenoid biosynthesis, lipid metabolism, cell wall biogenesis) involve entirely different enzyme families with no PLP fold-type II or 'SFGG' signatures. No alternative is defensible.


### Important caveats

- The 'SFGG' motif is shared across the broader trans-sulfuration family (CBS, CGS, OASS, threonine synthase), so it identifies the superfamily but not the exact EC. However, among the four broad pathway choices offered, this is sufficient to select amino-acid biosynthesis.
- The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:10595588, Clausen et al. 1999), not merely computational inference.
- The sequence-to-accession match is exact (540 AA, SHA-256 match), so the reviewer evidence applies directly to the benchmark input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several transferable diagnostic features. (1) The N-terminal ~50 residues are rich in Ser, Thr, Ala, and Arg with a bipartite character typical of a chloroplastic transit peptide, indicating a plastid-localized enzyme. (2) Near the C-terminus, the motif 'SFGG' (in 'IAPSFGGCESIVDQ') and the 'GG' dinucleotide are well-known signatures of fold-type II PLP-dependent trans-sulfuration enzymes, a family that includes cystathionine beta-synthase (CBS), cystathionine gamma-synthase (CGS), O-acetylserine sulfhydrylase (OASS/cysteine synthase), and methionine gamma-lyase, all characterized across bacteria, fungi, and plants. (3) The region 'GADLVLHS' and the overall domain architecture are consistent with the CGS/CBS subfamily. (4) Trans-sulfuration enzymes catalyze steps in methionine and cysteine biosynthesis, placing them squarely in amino-acid biosynthesis. Against the other options: spheroidene biosynthesis involves phytoene synthase, carotenoid hydroxylases, and ketolases with entirely different folds and motifs; lipid metabolism enzymes (FAS, desaturases, thioesterases) lack PLP-binding 'GG' motifs; cell wall biogenesis enzymes (cellulose synthases, glycosyltransferases, pectin-modifying enzymes) have no PLP or trans-sulfuration signatures. Thus, recognizing the trans-sulfuration family from homologs in Arabidopsis, E. coli, and yeast is sufficient to select C over A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the chloroplastic transit peptide, recognize the 'SFGG' and 'GG' motifs diagnostic of fold-type II PLP trans-sulfuration enzymes (CBS, CGS, OASS family), and connect this enzyme family to amino-acid biosynthesis. This is a legitimate family-level inference from well-characterized homologs, not a lookup of this specific protein's annotation. The four offered choices are sufficiently distinct that family recognition eliminates A, B, and D."
  },
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9ZPL5, CGS1_TOBAC) explicitly annotates this protein as Cystathionine gamma-synthase 1, chloroplastic (EC 2.5.1.160) with the pathway comment 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1' backed by experimental evidence (ECO:0000269|PubMed:10595588). The sequence matches the benchmark input exactly (540 AA, SHA-256 match). The expected answer C (Amino-acid biosynthesis) is directly and experimentally supported."
  },
  "important_caveats": [
    "The 'SFGG' motif is shared across the broader trans-sulfuration family (CBS, CGS, OASS, threonine synthase), so it identifies the superfamily but not the exact EC. However, among the four broad pathway choices offered, this is sufficient to select amino-acid biosynthesis.",
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:10595588, Clausen et al. 1999), not merely computational inference.",
    "The sequence-to-accession match is exact (540 AA, SHA-256 match), so the reviewer evidence applies directly to the benchmark input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The trans-sulfuration family motifs and chloroplastic localization unambiguously point to amino-acid biosynthesis (C). The other three options (carotenoid biosynthesis, lipid metabolism, cell wall biogenesis) involve entirely different enzyme families with no PLP fold-type II or 'SFGG' signatures. No alternative is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9ZPL5, CGS1_TOBAC) explicitly annotates this protein as Cystathionine gamma-synthase 1, chloroplastic (EC 2.5.1.160) with the pathway comment 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1' backed by experimental evidence (ECO:0000269|PubMed:10595588). The sequence matches the benchmark input exactly (540 AA, SHA-256 match). The expected answer C (Amino-acid biosynthesis) is directly and experimentally supported.",
    "evidence_ids": ["C5", "H3", "C4", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several transferable diagnostic features. (1) The N-terminal ~50 residues are rich in Ser, Thr, Ala, and Arg with a bipartite character typical of a chloroplastic transit peptide, indicating a plastid-localized enzyme. (2) Near the C-terminus, the motif 'SFGG' (in 'IAPSFGGCESIVDQ') and the 'GG' dinucleotide are well-known signatures of fold-type II PLP-dependent trans-sulfuration enzymes, a family that includes cystathionine beta-synthase (CBS), cystathionine gamma-synthase (CGS), O-acetylserine sulfhydrylase (OASS/cysteine synthase), and methionine gamma-lyase, all characterized across bacteria, fungi, and plants. (3) The region 'GADLVLHS' and the overall domain architecture are consistent with the CGS/CBS subfamily. (4) Trans-sulfuration enzymes catalyze steps in methionine and cysteine biosynthesis, placing them squarely in amino-acid biosynthesis. Against the other options: spheroidene biosynthesis involves phytoene synthase, carotenoid hydroxylases, and ketolases with entirely different folds and motifs; lipid metabolism enzymes (FAS, desaturases, thioesterases) lack PLP-binding 'GG' motifs; cell wall biogenesis enzymes (cellulose synthases, glycosyltransferases, pectin-modifying enzymes) have no PLP or trans-sulfuration signatures. Thus, recognizing the trans-sulfuration family from homologs in Arabidopsis, E. coli, and yeast is sufficient to select C over A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the chloroplastic transit peptide, recognize the 'SFGG' and 'GG' motifs diagnostic of fold-type II PLP trans-sulfuration enzymes (CBS, CGS, OASS family), and connect this enzyme family to amino-acid biosynthesis. This is a legitimate family-level inference from well-characterized homologs, not a lookup of this specific protein's annotation. The four offered choices are sufficiently distinct that family recognition eliminates A, B, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The trans-sulfuration family motifs and chloroplastic localization unambiguously point to amino-acid biosynthesis (C). The other three options (carotenoid biosynthesis, lipid metabolism, cell wall biogenesis) involve entirely different enzyme families with no PLP fold-type II or 'SFGG' signatures. No alternative is defensible."
  },
  "important_caveats": [
    "The 'SFGG' motif is shared across the broader trans-sulfuration family (CBS, CGS, OASS, threonine synthase), so it identifies the superfamily but not the exact EC. However, among the four broad pathway choices offered, this is sufficient to select amino-acid biosynthesis.",
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:10595588, Clausen et al. 1999), not merely computational inference.",
    "The sequence-to-accession match is exact (540 AA, SHA-256 match), so the reviewer evidence applies directly to the benchmark input."
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
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9ZPL5",
  "selected_historical_entry_version": 110,
  "selected_historical_record_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "selected_historical_version": {
    "accession": "Q9ZPL5",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CGS1_TOBAC",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9ZPL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common tobacco\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Solanales\",\"Solanaceae\",\"Nicotianoideae\",\"Nicotianeae\",\"Nicotiana\"],\"scientificName\":\"Nicotiana tabacum\",\"taxonId\":4097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.160\"}],\"fullName\":{\"value\":\"Cystathionine gamma-synthase 1, chloroplastic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Clausen T.\",\"Wahl M.C.\",\"Messerschmidt A.\",\"Huber R.\",\"Fuhrmann J.C.\",\"Laber B.\",\"Streber W.\",\"Steegborn C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10595588\"},{\"database\":\"DOI\",\"id\":\"10.1515/bc.1999.157\"}],\"citationType\":\"journal article\",\"firstPage\":\"1237\",\"id\":\"10595588\",\"journal\":\"Biol. Chem.\",\"lastPage\":\"1242\",\"publicationDate\":\"1999\",\"title\":\"Cloning, purification and characterisation of cystathionine gamma-synthase from Nicotiana tabacum.\",\"volume\":\"380\"},\"referenceNumber\":3,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] OF 97-540\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H1",
  "excerpt": "ID   CGS1_TOBAC              Reviewed;         540 AA.\nAC   Q9ZPL5; W8SGH6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;\nDE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};\nDE   Flags: Precursor;\nGN   Name=CGS1 {ECO:0000305}; ORFNames=LOC107822634;\nOS   Nicotiana tabacum (Common tobacco).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;\nOC   Nicotiana.\nOX   NCBI_TaxID=4097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   NUCLEOTIDE SEQUENCE [MRNA] OF 97-540, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRX   PubMed=10595588; DOI=10.1515/bc.1999.157;\nRA   Clausen T., Wahl M.C., Messerschmidt A., Huber R., Fuhrmann J.C., Laber B.,\nRA   Streber W., Steegborn C.;\nRT   \"Cloning, purification and characterisation of cystathionine gamma-synthase\nRT   from Nicotiana tabacum.\";\nRL   Biol. Chem. 380:1237-1242(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1.\nCC       {ECO:0000269|PubMed:10595588}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
