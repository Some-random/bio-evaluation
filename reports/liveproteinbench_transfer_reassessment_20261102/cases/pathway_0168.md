# pathway_0168

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0168.txt)

**Task:** `pathway`  
**Expected answer:** **D** — One-carbon metabolism

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
A. Protein modification
B. L-leucine degradation
C. deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1. .
D. One-carbon metabolism
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

> The exact sequence matches the annotated protein. Its annotation identifies it as cytosolic serine hydroxymethyltransferase and assigns it to one-carbon metabolism. The enzyme annotation and pathway assignment are supported by transferred evidence (ECO:0000250), so this supports the key but is not, by itself, direct experimental confirmation for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the serine hydroxymethyltransferase family. Transferable knowledge of this enzyme family provides a meaningful distinction: serine hydroxymethyltransferase transfers a one-carbon unit from serine to tetrahydrofolate, placing its primary role in one-carbon metabolism rather than leucine degradation or NAD biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the offered choices credibly favors D. It need not establish every annotation detail to distinguish D from these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, one-carbon metabolism is the clear pathway-level fit for serine hydroxymethyltransferase.


### Important caveats

- The supplied reviewer evidence records a pathway assignment based on similarity to another protein; it does not independently establish direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the serine hydroxymethyltransferase family. Transferable knowledge of this enzyme family provides a meaningful distinction: serine hydroxymethyltransferase transfers a one-carbon unit from serine to tetrahydrofolate, placing its primary role in one-carbon metabolism rather than leucine degradation or NAD biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the offered choices credibly favors D. It need not establish every annotation detail to distinguish D from these alternatives."
  },
  "case_id": "pathway_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated protein. Its annotation identifies it as cytosolic serine hydroxymethyltransferase and assigns it to one-carbon metabolism. The enzyme annotation and pathway assignment are supported by transferred evidence (ECO:0000250), so this supports the key but is not, by itself, direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The supplied reviewer evidence records a pathway assignment based on similarity to another protein; it does not independently establish direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, one-carbon metabolism is the clear pathway-level fit for serine hydroxymethyltransferase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated protein. Its annotation identifies it as cytosolic serine hydroxymethyltransferase and assigns it to one-carbon metabolism. The enzyme annotation and pathway assignment are supported by transferred evidence (ECO:0000250), so this supports the key but is not, by itself, direct experimental confirmation for this exact protein.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the serine hydroxymethyltransferase family. Transferable knowledge of this enzyme family provides a meaningful distinction: serine hydroxymethyltransferase transfers a one-carbon unit from serine to tetrahydrofolate, placing its primary role in one-carbon metabolism rather than leucine degradation or NAD biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the offered choices credibly favors D. It need not establish every annotation detail to distinguish D from these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, one-carbon metabolism is the clear pathway-level fit for serine hydroxymethyltransferase."
  },
  "important_caveats": [
    "The supplied reviewer evidence records a pathway assignment based on similarity to another protein; it does not independently establish direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXF4 (GLYC_ASPFU) is annotated as Serine hydroxymethyltransferase, cytosolic (EC 2.1.2.1), with the pathway explicitly listed as 'One-carbon metabolism; tetrahydrofolate interconversion' (evidence C5, H3). The EC number 2.1.2.1 corresponds to SHMT, which catalyzes the reversible conversion of serine + tetrahydrofolate → glycine + 5,10-methylenetetrahydrofolate, a core reaction in one-carbon/folate metabolism. The annotation is supported by both computational transfer (ECO:0000250 from P34896) and experimental evidence (PubMed:39825596, reference C6/H2). The expected answer D is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'GGN' motif (visible in 'GGNQHIDAIEL'), which is a hallmark family-level signature of Serine Hydroxymethyltransferase (SHMT) proteins across bacteria, fungi, and eukaryotes. Additional SHMT-family features include the ~470 aa length, the PLP-dependent enzyme architecture (the GGN motif participates in pyridoxal-5'-phosphate binding), and the overall domain organization matching the SHMT fold. SHMT catalyzes the reversible conversion of serine + tetrahydrofolate → glycine + 5,10-methylenetetrahydrofolate, which is a defining reaction of one-carbon (folate) metabolism. This is standard biochemistry knowledge transferable from SHMT homologs in E. coli (P34896), human, and other organisms. Against the other options: (A) Protein modification requires kinase/phosphatase/ligase motifs absent here; (B) L-leucine degradation involves branched-chain aminotransferases and dehydrogenases with different folds; (C) NAD+ biosynthesis (NMNAT) has a distinct nucleotidyltransferase fold and no GGN/PLP motifs. The GGN motif plus family-level knowledge of SHMT's folate-cycle role meaningfully distinguishes D from A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GGN motif is a well-known, transferable SHMT-family signature. Recognizing it as SHMT and recalling that SHMT sits in the tetrahydrofolate/one-carbon metabolism pathway is legitimate family-level inference from homologs, not a lookup of this specific protein's record. The four answer choices are sufficiently distinct (modification enzyme, amino acid degradation, NAD+ biosynthesis, one-carbon metabolism) that family recognition of SHMT cleanly selects D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices target clearly different enzyme classes and pathways. Once the sequence is recognized as SHMT via the GGN motif and PLP-binding architecture, only D (one-carbon metabolism) is consistent. The other three options correspond to unrelated enzyme families with distinct sequence signatures.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000250 (similarity-based transfer from P34896, E. coli SHMT), supplemented by experimental evidence from PubMed:39825596 confirming SHMT function in A. fumigatus.
- The GGN motif is a strong but not absolutely unique SHMT signature; however, combined with overall sequence architecture and the four-way choice set, it provides a clear discriminator.
- The reviewer-only evidence confirms sequence match (sha256 identical) and entry identity (Q4WXF4), but this accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GGN' motif (visible in 'GGNQHIDAIEL'), which is a hallmark family-level signature of Serine Hydroxymethyltransferase (SHMT) proteins across bacteria, fungi, and eukaryotes. Additional SHMT-family features include the ~470 aa length, the PLP-dependent enzyme architecture (the GGN motif participates in pyridoxal-5'-phosphate binding), and the overall domain organization matching the SHMT fold. SHMT catalyzes the reversible conversion of serine + tetrahydrofolate → glycine + 5,10-methylenetetrahydrofolate, which is a defining reaction of one-carbon (folate) metabolism. This is standard biochemistry knowledge transferable from SHMT homologs in E. coli (P34896), human, and other organisms. Against the other options: (A) Protein modification requires kinase/phosphatase/ligase motifs absent here; (B) L-leucine degradation involves branched-chain aminotransferases and dehydrogenases with different folds; (C) NAD+ biosynthesis (NMNAT) has a distinct nucleotidyltransferase fold and no GGN/PLP motifs. The GGN motif plus family-level knowledge of SHMT's folate-cycle role meaningfully distinguishes D from A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GGN motif is a well-known, transferable SHMT-family signature. Recognizing it as SHMT and recalling that SHMT sits in the tetrahydrofolate/one-carbon metabolism pathway is legitimate family-level inference from homologs, not a lookup of this specific protein's record. The four answer choices are sufficiently distinct (modification enzyme, amino acid degradation, NAD+ biosynthesis, one-carbon metabolism) that family recognition of SHMT cleanly selects D."
  },
  "case_id": "pathway_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (GLYC_ASPFU) is annotated as Serine hydroxymethyltransferase, cytosolic (EC 2.1.2.1), with the pathway explicitly listed as 'One-carbon metabolism; tetrahydrofolate interconversion' (evidence C5, H3). The EC number 2.1.2.1 corresponds to SHMT, which catalyzes the reversible conversion of serine + tetrahydrofolate → glycine + 5,10-methylenetetrahydrofolate, a core reaction in one-carbon/folate metabolism. The annotation is supported by both computational transfer (ECO:0000250 from P34896) and experimental evidence (PubMed:39825596, reference C6/H2). The expected answer D is well-supported."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (similarity-based transfer from P34896, E. coli SHMT), supplemented by experimental evidence from PubMed:39825596 confirming SHMT function in A. fumigatus.",
    "The GGN motif is a strong but not absolutely unique SHMT signature; however, combined with overall sequence architecture and the four-way choice set, it provides a clear discriminator.",
    "The reviewer-only evidence confirms sequence match (sha256 identical) and entry identity (Q4WXF4), but this accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices target clearly different enzyme classes and pathways. Once the sequence is recognized as SHMT via the GGN motif and PLP-binding architecture, only D (one-carbon metabolism) is consistent. The other three options correspond to unrelated enzyme families with distinct sequence signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (GLYC_ASPFU) is annotated as Serine hydroxymethyltransferase, cytosolic (EC 2.1.2.1), with the pathway explicitly listed as 'One-carbon metabolism; tetrahydrofolate interconversion' (evidence C5, H3). The EC number 2.1.2.1 corresponds to SHMT, which catalyzes the reversible conversion of serine + tetrahydrofolate → glycine + 5,10-methylenetetrahydrofolate, a core reaction in one-carbon/folate metabolism. The annotation is supported by both computational transfer (ECO:0000250 from P34896) and experimental evidence (PubMed:39825596, reference C6/H2). The expected answer D is well-supported.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GGN' motif (visible in 'GGNQHIDAIEL'), which is a hallmark family-level signature of Serine Hydroxymethyltransferase (SHMT) proteins across bacteria, fungi, and eukaryotes. Additional SHMT-family features include the ~470 aa length, the PLP-dependent enzyme architecture (the GGN motif participates in pyridoxal-5'-phosphate binding), and the overall domain organization matching the SHMT fold. SHMT catalyzes the reversible conversion of serine + tetrahydrofolate → glycine + 5,10-methylenetetrahydrofolate, which is a defining reaction of one-carbon (folate) metabolism. This is standard biochemistry knowledge transferable from SHMT homologs in E. coli (P34896), human, and other organisms. Against the other options: (A) Protein modification requires kinase/phosphatase/ligase motifs absent here; (B) L-leucine degradation involves branched-chain aminotransferases and dehydrogenases with different folds; (C) NAD+ biosynthesis (NMNAT) has a distinct nucleotidyltransferase fold and no GGN/PLP motifs. The GGN motif plus family-level knowledge of SHMT's folate-cycle role meaningfully distinguishes D from A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The GGN motif is a well-known, transferable SHMT-family signature. Recognizing it as SHMT and recalling that SHMT sits in the tetrahydrofolate/one-carbon metabolism pathway is legitimate family-level inference from homologs, not a lookup of this specific protein's record. The four answer choices are sufficiently distinct (modification enzyme, amino acid degradation, NAD+ biosynthesis, one-carbon metabolism) that family recognition of SHMT cleanly selects D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices target clearly different enzyme classes and pathways. Once the sequence is recognized as SHMT via the GGN motif and PLP-binding architecture, only D (one-carbon metabolism) is consistent. The other three options correspond to unrelated enzyme families with distinct sequence signatures."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (similarity-based transfer from P34896, E. coli SHMT), supplemented by experimental evidence from PubMed:39825596 confirming SHMT function in A. fumigatus.",
    "The GGN motif is a strong but not absolutely unique SHMT signature; however, combined with overall sequence architecture and the four-way choice set, it provides a clear discriminator.",
    "The reviewer-only evidence confirms sequence match (sha256 identical) and entry identity (Q4WXF4), but this accession was not available to the evaluated model."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"}],\"value\":\"One-carbon metabolism; tetrahydrofolate interconversion\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: One-carbon metabolism; tetrahydrofolate interconversion.\nCC       {ECO:0000250|UniProtKB:P34896}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 168. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
