# catalytic_activity_0073

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0073.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATYALSQAHREQMEKSLVDSDPEIAQIMEKEIQRQRESILLIASENVTSRAVFDALGSPMSNKYSEGYPGARYYGGNQHIDAIELTCQARALKAFNLDPEKWGVNVQCLSGSPANLEVYQALMRPHDRLMGLDLPHGGHLSHGYQTPSRKISAVSTYFETFPYRVNTETGIIDYDTLEANAELYRPKCLVAGTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAGVIPSPFEYADVVTTTTHKSLRGPRGAMIFFRKGVRSTDPKTGKEIMYDLEGPINFSVFPGHQGGPHNHTITALAVALKQAATPEFRQYQEQVLKNAKALEVEFKALGHKLVSDGTDSHMVLLDLRPKGLDGARVEAVLEQINIACNKNSIPGDKSALTPCGIRIGTPAMTSRGMSEEDFKRVARYIDQVINLCKSIQADLPKEANKLKDFKAKVASGSVPEILALRKEVAEWASTYPLPV

[Multiple Choices]
A. UTP + H2O = UDP + phosphate + H(+)
B. (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine
C. (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
D. UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation assigns EC 2.1.2.1 and gives the reaction in choice B. Its evidence code indicates annotation by similarity to another UniProt protein, not direct experimental confirmation for this exact protein, so the evidence supports the key as a family-based functional assignment rather than an independently verified assay result.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 471-residue sequence is consistent with the soluble serine hydroxymethyltransferase family, a PLP-dependent enzyme family that interconverts glycine and serine using a folate one-carbon unit. That transferable family-level reaction directly matches B. The other choices describe nucleotide hydrolysis, methylation, or sugar epimerization and do not fit this enzyme family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use family recognition from the sequence and known SHMT chemistry to distinguish B among these alternatives. This is a defensible inference from transferable knowledge, though it does not establish direct experimental validation for this particular sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives describe distinct reaction types, and the SHMT-family inference points specifically to B.


### Important caveats

- The supplied reviewer evidence is a sequence-matched database annotation, but the cited evidence code indicates transfer by similarity; it is not direct experimental evidence for the exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 471-residue sequence is consistent with the soluble serine hydroxymethyltransferase family, a PLP-dependent enzyme family that interconverts glycine and serine using a folate one-carbon unit. That transferable family-level reaction directly matches B. The other choices describe nucleotide hydrolysis, methylation, or sugar epimerization and do not fit this enzyme family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family recognition from the sequence and known SHMT chemistry to distinguish B among these alternatives. This is a defensible inference from transferable knowledge, though it does not establish direct experimental validation for this particular sequence."
  },
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 2.1.2.1 and gives the reaction in choice B. Its evidence code indicates annotation by similarity to another UniProt protein, not direct experimental confirmation for this exact protein, so the evidence supports the key as a family-based functional assignment rather than an independently verified assay result."
  },
  "important_caveats": [
    "The supplied reviewer evidence is a sequence-matched database annotation, but the cited evidence code indicates transfer by similarity; it is not direct experimental evidence for the exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe distinct reaction types, and the SHMT-family inference points specifically to B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 2.1.2.1 and gives the reaction in choice B. Its evidence code indicates annotation by similarity to another UniProt protein, not direct experimental confirmation for this exact protein, so the evidence supports the key as a family-based functional assignment rather than an independently verified assay result.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 471-residue sequence is consistent with the soluble serine hydroxymethyltransferase family, a PLP-dependent enzyme family that interconverts glycine and serine using a folate one-carbon unit. That transferable family-level reaction directly matches B. The other choices describe nucleotide hydrolysis, methylation, or sugar epimerization and do not fit this enzyme family.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family recognition from the sequence and known SHMT chemistry to distinguish B among these alternatives. This is a defensible inference from transferable knowledge, though it does not establish direct experimental validation for this particular sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe distinct reaction types, and the SHMT-family inference points specifically to B."
  },
  "important_caveats": [
    "The supplied reviewer evidence is a sequence-matched database annotation, but the cited evidence code indicates transfer by similarity; it is not direct experimental evidence for the exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXF4 (GLYC_ASPFU) annotates this 471-aa protein as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The recorded catalytic activity (C5/H4) exactly matches option B: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine. The annotation carries ECO:0000250 (similarity to human SHMT P34896) and ECO:0000303 (PubMed 39825596, a 2025 Virulence paper confirming function experimentally). The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple highly conserved SHMT-family motifs recognizable from training on many SHMT homologs: (1) 'DLPHGGHLSHGY' — the GGHLSHG motif is a hallmark of the PLP-binding active-site loop in SHMT across E. coli, human, yeast, and fungal orthologs; (2) 'GTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAG' — the DMAHISGL segment is a well-known SHMT conserved block; (3) the overall ~471-aa length and alpha/beta PLP-fold architecture are consistent with SHMT rather than the other enzyme classes. These family-level features immediately rule out: A (nucleotide phosphatase, different fold, no PLP motifs), C (SAM-dependent methyltransferase, requires Rossmann-like fold and SAM-binding motifs absent here), and D (epimerase, completely different catalytic mechanism and fold). The GGHLSHG/DMAHISGL signatures are transferable knowledge learned from dozens of SHMT proteins and directly point to the glycine↔serine interconversion with folate cofactor (EC 2.1.2.1), i.e., option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SHMT family motifs (GGHLSHG, DMAHISGL) are well-characterized across many organisms and constitute transferable sequence knowledge. Recognizing these motifs and the overall fold architecture distinguishes option B from the three structurally and mechanistically unrelated distractors without needing a fact unique to this exact Aspergillus protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different enzyme classes (phosphatase, SHMT, SAM-methyltransferase, epimerase). The SHMT-specific sequence motifs unambiguously select option B; no other option is defensible given the recognized family signatures.


### Important caveats

- The EC annotation carries ECO:0000250 (similarity-based from human P34896) in addition to PubMed evidence (39825596), so the primary annotation basis is partly computational transfer, though a 2025 experimental paper (H3) supports the function.
- The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model; the reasoning above relies solely on sequence motifs and family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple highly conserved SHMT-family motifs recognizable from training on many SHMT homologs: (1) 'DLPHGGHLSHGY' — the GGHLSHG motif is a hallmark of the PLP-binding active-site loop in SHMT across E. coli, human, yeast, and fungal orthologs; (2) 'GTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAG' — the DMAHISGL segment is a well-known SHMT conserved block; (3) the overall ~471-aa length and alpha/beta PLP-fold architecture are consistent with SHMT rather than the other enzyme classes. These family-level features immediately rule out: A (nucleotide phosphatase, different fold, no PLP motifs), C (SAM-dependent methyltransferase, requires Rossmann-like fold and SAM-binding motifs absent here), and D (epimerase, completely different catalytic mechanism and fold). The GGHLSHG/DMAHISGL signatures are transferable knowledge learned from dozens of SHMT proteins and directly point to the glycine↔serine interconversion with folate cofactor (EC 2.1.2.1), i.e., option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SHMT family motifs (GGHLSHG, DMAHISGL) are well-characterized across many organisms and constitute transferable sequence knowledge. Recognizing these motifs and the overall fold architecture distinguishes option B from the three structurally and mechanistically unrelated distractors without needing a fact unique to this exact Aspergillus protein."
  },
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (GLYC_ASPFU) annotates this 471-aa protein as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The recorded catalytic activity (C5/H4) exactly matches option B: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine. The annotation carries ECO:0000250 (similarity to human SHMT P34896) and ECO:0000303 (PubMed 39825596, a 2025 Virulence paper confirming function experimentally). The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The EC annotation carries ECO:0000250 (similarity-based from human P34896) in addition to PubMed evidence (39825596), so the primary annotation basis is partly computational transfer, though a 2025 experimental paper (H3) supports the function.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model; the reasoning above relies solely on sequence motifs and family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (phosphatase, SHMT, SAM-methyltransferase, epimerase). The SHMT-specific sequence motifs unambiguously select option B; no other option is defensible given the recognized family signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (GLYC_ASPFU) annotates this 471-aa protein as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The recorded catalytic activity (C5/H4) exactly matches option B: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine. The annotation carries ECO:0000250 (similarity to human SHMT P34896) and ECO:0000303 (PubMed 39825596, a 2025 Virulence paper confirming function experimentally). The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple highly conserved SHMT-family motifs recognizable from training on many SHMT homologs: (1) 'DLPHGGHLSHGY' — the GGHLSHG motif is a hallmark of the PLP-binding active-site loop in SHMT across E. coli, human, yeast, and fungal orthologs; (2) 'GTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAG' — the DMAHISGL segment is a well-known SHMT conserved block; (3) the overall ~471-aa length and alpha/beta PLP-fold architecture are consistent with SHMT rather than the other enzyme classes. These family-level features immediately rule out: A (nucleotide phosphatase, different fold, no PLP motifs), C (SAM-dependent methyltransferase, requires Rossmann-like fold and SAM-binding motifs absent here), and D (epimerase, completely different catalytic mechanism and fold). The GGHLSHG/DMAHISGL signatures are transferable knowledge learned from dozens of SHMT proteins and directly point to the glycine↔serine interconversion with folate cofactor (EC 2.1.2.1), i.e., option B.",
    "missing_item_specific_fact": "",
    "reason": "The SHMT family motifs (GGHLSHG, DMAHISGL) are well-characterized across many organisms and constitute transferable sequence knowledge. Recognizing these motifs and the overall fold architecture distinguishes option B from the three structurally and mechanistically unrelated distractors without needing a fact unique to this exact Aspergillus protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (phosphatase, SHMT, SAM-methyltransferase, epimerase). The SHMT-specific sequence motifs unambiguously select option B; no other option is defensible given the recognized family signatures."
  },
  "important_caveats": [
    "The EC annotation carries ECO:0000250 (similarity-based from human P34896) in addition to PubMed evidence (39825596), so the primary annotation basis is partly computational transfer, though a 2025 experimental paper (H3) supports the function.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model; the reasoning above relies solely on sequence motifs and family knowledge."
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
  "benchmark_sequence_length": 471,
  "benchmark_sequence_sha256": "f701b7b612f66565fce8586e5acff753094d2b7e38617cd4fba5d0a2faa13b4f",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 471,
  "current_source_sequence_sha256": "f701b7b612f66565fce8586e5acff753094d2b7e38617cd4fba5d0a2faa13b4f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WXF4",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "selected_historical_source_sequence_length": 471,
  "selected_historical_source_sequence_sha256": "f701b7b612f66565fce8586e5acff753094d2b7e38617cd4fba5d0a2faa13b4f",
  "selected_historical_version": {
    "accession": "Q4WXF4",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLYC_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WXF4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"}],\"value\":\"2.1.2.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39825596\",\"source\":\"PubMed\"}],\"value\":\"Serine hydroxymethyltransferase, cytosolic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.1.2.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"}],\"name\":\"(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15481\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15636\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57453\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Alharthi R.\",\"Sueiro-Olivares M.\",\"Storer I.\",\"Bin Shuraym H.\",\"Scott J.\",\"Al-Shidhani R.\",\"Fortune-Grant R.\",\"Bignell E.\",\"Tabernero L.\",\"Bromley M.\",\"Zhao C.\",\"Amich J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39825596\"},{\"database\":\"DOI\",\"id\":\"10.1080/21505594.2024.2449075\"}],\"citationType\":\"journal article\",\"firstPage\":\"2449075\",\"id\":\"39825596\",\"journal\":\"Virulence\",\"lastPage\":\"2449075\",\"publicationDate\":\"2025\",\"title\":\"The sulfur-related metabolic status of Aspergillus fumigatus during infection reveals cytosolic serine hydroxymethyltransferase as a promising antifungal target.\",\"volume\":\"16\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   GLYC_ASPFU              Reviewed;         471 AA.\nAC   Q4WXF4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};\nDE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};\nGN   Name=shmB {ECO:0000303|PubMed:39825596}; ORFNames=AFUA_3G09320;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};\nDE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, DISRUPTION PHENOTYPE, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=39825596; DOI=10.1080/21505594.2024.2449075;\nRA   Alharthi R., Sueiro-Olivares M., Storer I., Bin Shuraym H., Scott J.,\nRA   Al-Shidhani R., Fortune-Grant R., Bignell E., Tabernero L., Bromley M.,\nRA   Zhao C., Amich J.;\nRT   \"The sulfur-related metabolic status of Aspergillus fumigatus during\nRT   infection reveals cytosolic serine hydroxymethyltransferase as a promising\nRT   antifungal target.\";\nRL   Virulence 16:2449075-2449075(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O =\nCC         (6S)-5,6,7,8-tetrahydrofolate + L-serine; Xref=Rhea:RHEA:15481,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15636, ChEBI:CHEBI:33384,\nCC         ChEBI:CHEBI:57305, ChEBI:CHEBI:57453; EC=2.1.2.1;\nCC         Evidence={ECO:0000250|UniProtKB:P34896};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
