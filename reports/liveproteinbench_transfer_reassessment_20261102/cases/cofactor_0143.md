# cofactor_0143

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0143.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — pyridoxal 5&#x27;-phosphate

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
A. pyridoxal 5'-phosphate
B. Na(+)
C. Mn(2+)
D. FMN
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates pyridoxal 5'-phosphate as the cofactor. That annotation is transferred from a homolog, rather than direct experimental evidence for this exact protein, but it is consistent with the known PLP dependence of serine hydroxymethyltransferases.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is compatible with the serine hydroxymethyltransferase family, whose conserved catalytic machinery uses PLP. Family recognition and the established PLP-dependent mechanism meaningfully favor A over Na(+), Mn(2+), or FMN.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and transferable knowledge of serine hydroxymethyltransferases distinguishes the offered cofactor choices without needing the exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, PLP is the well-supported cofactor for this enzyme family.


### Important caveats

- The supplied source annotations support the key but transfer the cofactor assignment from a homolog; the excerpts do not establish direct experimental measurement on this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with the serine hydroxymethyltransferase family, whose conserved catalytic machinery uses PLP. Family recognition and the established PLP-dependent mechanism meaningfully favor A over Na(+), Mn(2+), or FMN.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and transferable knowledge of serine hydroxymethyltransferases distinguishes the offered cofactor choices without needing the exact protein's database entry."
  },
  "case_id": "cofactor_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pyridoxal 5'-phosphate as the cofactor. That annotation is transferred from a homolog, rather than direct experimental evidence for this exact protein, but it is consistent with the known PLP dependence of serine hydroxymethyltransferases."
  },
  "important_caveats": [
    "The supplied source annotations support the key but transfer the cofactor assignment from a homolog; the excerpts do not establish direct experimental measurement on this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, PLP is the well-supported cofactor for this enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pyridoxal 5'-phosphate as the cofactor. That annotation is transferred from a homolog, rather than direct experimental evidence for this exact protein, but it is consistent with the known PLP dependence of serine hydroxymethyltransferases.",
    "evidence_ids": ["H4", "C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is compatible with the serine hydroxymethyltransferase family, whose conserved catalytic machinery uses PLP. Family recognition and the established PLP-dependent mechanism meaningfully favor A over Na(+), Mn(2+), or FMN.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and transferable knowledge of serine hydroxymethyltransferases distinguishes the offered cofactor choices without needing the exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, PLP is the well-supported cofactor for this enzyme family."
  },
  "important_caveats": [
    "The supplied source annotations support the key but transfer the cofactor assignment from a homolog; the excerpts do not establish direct experimental measurement on this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000250, inferred by similarity to human SHMT P34896) explicitly lists pyridoxal 5'-phosphate (CHEBI:597326) as the cofactor for this serine hydroxymethyltransferase (EC 2.1.2.1). The protein is identified as cytosolic SHMT from Aspergillus fumigatus, a well-established PLP-dependent enzyme family. The evidence code indicates computational transfer rather than direct experimental measurement on this exact protein, but the family-level biochemistry of SHMT as a PLP-dependent enzyme is extensively characterized.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple conserved motifs diagnostic of PLP-dependent serine hydroxymethyltransferases across the alpha-family of PLP enzymes: (1) The 'THK' motif (in 'TTTHKSLRGPRGAMIFFRKG') where the lysine forms the internal aldimine (Schiff base) with PLP — a hallmark of alpha-family PLP enzymes; (2) The 'DLRP' motif (in 'LLDLRPKGLDGARVEAVLEQ') specific to SHMT; (3) The 'GTS' glycine-rich region (in 'GTSAYCRLIDYGRMRKIADK') characteristic of SHMT. These motifs are shared across hundreds of characterized SHMT orthologs and other PLP-dependent transferases. None of the distractors (Na+, Mn2+, FMN) have corresponding binding-site motifs in this sequence: there is no Rossmann-fold pattern for FMN, no metal-coordinating His/Asp/Glu cluster typical of Mn-dependent oxidoreductases, and no Na+ binding site. The PLP-binding lysine in the THK motif is a universally recognized family-level feature that distinguishes this enzyme class from flavin- or metal-dependent enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable biochemist can identify the PLP-binding THK lysine motif and SHMT-specific DLRP motif from the sequence, recognize these as family-level features shared with many other PLP-dependent enzymes (e.g., aminotransferases, glycine cleavage system T-protein homologs), and rule out FMN (no flavin-binding domain), Mn2+ (no metal-binding cluster), and Na+ (no ion channel/pump motifs). This is standard protein-family recognition, not lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved PLP-binding and SHMT-specific motifs unambiguously point to pyridoxal 5'-phosphate. The distractors (Na+, Mn2+, FMN) lack any corresponding structural or sequence features in this protein. No other option is defensible.


### Important caveats

- The cofactor annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity to human SHMT P34896), meaning it is a computational transfer rather than direct experimental measurement on this exact A. fumigatus protein. However, the family-level biochemistry of SHMT as PLP-dependent is extremely well-established.
- The protein was first integrated into Swiss-Prot on 2025-06-18, so it was not a long-standing Swiss-Prot entry at the time of benchmark construction, but the sequence and motifs are clearly recognizable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple conserved motifs diagnostic of PLP-dependent serine hydroxymethyltransferases across the alpha-family of PLP enzymes: (1) The 'THK' motif (in 'TTTHKSLRGPRGAMIFFRKG') where the lysine forms the internal aldimine (Schiff base) with PLP — a hallmark of alpha-family PLP enzymes; (2) The 'DLRP' motif (in 'LLDLRPKGLDGARVEAVLEQ') specific to SHMT; (3) The 'GTS' glycine-rich region (in 'GTSAYCRLIDYGRMRKIADK') characteristic of SHMT. These motifs are shared across hundreds of characterized SHMT orthologs and other PLP-dependent transferases. None of the distractors (Na+, Mn2+, FMN) have corresponding binding-site motifs in this sequence: there is no Rossmann-fold pattern for FMN, no metal-coordinating His/Asp/Glu cluster typical of Mn-dependent oxidoreductases, and no Na+ binding site. The PLP-binding lysine in the THK motif is a universally recognized family-level feature that distinguishes this enzyme class from flavin- or metal-dependent enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable biochemist can identify the PLP-binding THK lysine motif and SHMT-specific DLRP motif from the sequence, recognize these as family-level features shared with many other PLP-dependent enzymes (e.g., aminotransferases, glycine cleavage system T-protein homologs), and rule out FMN (no flavin-binding domain), Mn2+ (no metal-binding cluster), and Na+ (no ion channel/pump motifs). This is standard protein-family recognition, not lookup of this specific protein's annotation."
  },
  "case_id": "cofactor_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000250, inferred by similarity to human SHMT P34896) explicitly lists pyridoxal 5'-phosphate (CHEBI:597326) as the cofactor for this serine hydroxymethyltransferase (EC 2.1.2.1). The protein is identified as cytosolic SHMT from Aspergillus fumigatus, a well-established PLP-dependent enzyme family. The evidence code indicates computational transfer rather than direct experimental measurement on this exact protein, but the family-level biochemistry of SHMT as a PLP-dependent enzyme is extensively characterized."
  },
  "important_caveats": [
    "The cofactor annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity to human SHMT P34896), meaning it is a computational transfer rather than direct experimental measurement on this exact A. fumigatus protein. However, the family-level biochemistry of SHMT as PLP-dependent is extremely well-established.",
    "The protein was first integrated into Swiss-Prot on 2025-06-18, so it was not a long-standing Swiss-Prot entry at the time of benchmark construction, but the sequence and motifs are clearly recognizable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved PLP-binding and SHMT-specific motifs unambiguously point to pyridoxal 5'-phosphate. The distractors (Na+, Mn2+, FMN) lack any corresponding structural or sequence features in this protein. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000250, inferred by similarity to human SHMT P34896) explicitly lists pyridoxal 5'-phosphate (CHEBI:597326) as the cofactor for this serine hydroxymethyltransferase (EC 2.1.2.1). The protein is identified as cytosolic SHMT from Aspergillus fumigatus, a well-established PLP-dependent enzyme family. The evidence code indicates computational transfer rather than direct experimental measurement on this exact protein, but the family-level biochemistry of SHMT as a PLP-dependent enzyme is extensively characterized.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple conserved motifs diagnostic of PLP-dependent serine hydroxymethyltransferases across the alpha-family of PLP enzymes: (1) The 'THK' motif (in 'TTTHKSLRGPRGAMIFFRKG') where the lysine forms the internal aldimine (Schiff base) with PLP — a hallmark of alpha-family PLP enzymes; (2) The 'DLRP' motif (in 'LLDLRPKGLDGARVEAVLEQ') specific to SHMT; (3) The 'GTS' glycine-rich region (in 'GTSAYCRLIDYGRMRKIADK') characteristic of SHMT. These motifs are shared across hundreds of characterized SHMT orthologs and other PLP-dependent transferases. None of the distractors (Na+, Mn2+, FMN) have corresponding binding-site motifs in this sequence: there is no Rossmann-fold pattern for FMN, no metal-coordinating His/Asp/Glu cluster typical of Mn-dependent oxidoreductases, and no Na+ binding site. The PLP-binding lysine in the THK motif is a universally recognized family-level feature that distinguishes this enzyme class from flavin- or metal-dependent enzymes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable biochemist can identify the PLP-binding THK lysine motif and SHMT-specific DLRP motif from the sequence, recognize these as family-level features shared with many other PLP-dependent enzymes (e.g., aminotransferases, glycine cleavage system T-protein homologs), and rule out FMN (no flavin-binding domain), Mn2+ (no metal-binding cluster), and Na+ (no ion channel/pump motifs). This is standard protein-family recognition, not lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved PLP-binding and SHMT-specific motifs unambiguously point to pyridoxal 5'-phosphate. The distractors (Na+, Mn2+, FMN) lack any corresponding structural or sequence features in this protein. No other option is defensible."
  },
  "important_caveats": [
    "The cofactor annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity to human SHMT P34896), meaning it is a computational transfer rather than direct experimental measurement on this exact A. fumigatus protein. However, the family-level biochemistry of SHMT as PLP-dependent is extremely well-established.",
    "The protein was first integrated into Swiss-Prot on 2025-06-18, so it was not a long-standing Swiss-Prot entry at the time of benchmark construction, but the sequence and motifs are clearly recognizable."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000250|UniProtKB:P34896};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 143. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
