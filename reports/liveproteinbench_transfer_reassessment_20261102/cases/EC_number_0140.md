# EC_number_0140

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0140.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.1.2.1

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
A. 2.1.1.27
B. 3.5.2.6
C. 2.1.1.34
D. 2.1.2.1
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as EC 2.1.2.1, and the annotation specifies the serine hydroxymethyltransferase reaction. The cited evidence is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the PLP-dependent serine hydroxymethyltransferase family. Family recognition and its characteristic role in transferring a one-carbon unit between glycine and tetrahydrofolate point to EC 2.1.2.1 (D), distinguishing it from the methyltransferases in A and C and the hydrolase in B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for choosing D among the offered alternatives; recalling this exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives classify substantially different reaction types, and the sequence-family inference favors EC 2.1.2.1.


### Important caveats

- The reviewer-only annotation supports EC 2.1.2.1 by similarity to a homolog; the supplied evidence does not establish direct experimental characterization of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the PLP-dependent serine hydroxymethyltransferase family. Family recognition and its characteristic role in transferring a one-carbon unit between glycine and tetrahydrofolate point to EC 2.1.2.1 (D), distinguishing it from the methyltransferases in A and C and the hydrolase in B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing D among the offered alternatives; recalling this exact protein's database record is not necessary."
  },
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as EC 2.1.2.1, and the annotation specifies the serine hydroxymethyltransferase reaction. The cited evidence is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The reviewer-only annotation supports EC 2.1.2.1 by similarity to a homolog; the supplied evidence does not establish direct experimental characterization of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives classify substantially different reaction types, and the sequence-family inference favors EC 2.1.2.1."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as EC 2.1.2.1, and the annotation specifies the serine hydroxymethyltransferase reaction. The cited evidence is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the PLP-dependent serine hydroxymethyltransferase family. Family recognition and its characteristic role in transferring a one-carbon unit between glycine and tetrahydrofolate point to EC 2.1.2.1 (D), distinguishing it from the methyltransferases in A and C and the hydrolase in B.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing D among the offered alternatives; recalling this exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives classify substantially different reaction types, and the sequence-family inference favors EC 2.1.2.1."
  },
  "important_caveats": [
    "The reviewer-only annotation supports EC 2.1.2.1 by similarity to a homolog; the supplied evidence does not establish direct experimental characterization of this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXF4 (GLYC_ASPFU) annotates this protein as Serine hydroxymethyltransferase, cytosolic with EC=2.1.2.1. The EC annotation is supported by both similarity evidence (ECO:0000250 to P34896, human SHMT) and experimental evidence from PubMed 39825596 (Alharthi et al. 2025, Virulence), which confirmed the cytosolic SHMT function in Aspergillus fumigatus. The catalytic activity (methylene-THF + glycine + H2O = THF + L-serine) is consistent with EC 2.1.2.1. The sequence matches exactly (471 aa, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved PLP-binding lysine motif 'KCLVAGTSAYC' (around residue ~220), which is a hallmark of the serine hydroxymethyltransferase (SHMT) family. SHMT is a pyridoxal-5'-phosphate (PLP)-dependent enzyme, whereas methyltransferases (EC 2.1.1.x, options A and C) use S-adenosylmethionine as a cofactor and do not require PLP. The presence of this PLP-binding lysine motif eliminates options A (2.1.1.27, glycine N-methyltransferase) and C (2.1.1.34, a methyltransferase). Additionally, the sequence length of ~471 residues is far too large for dihydrofolate dehydrogenase (EC 3.5.2.6, option B), which is typically 160-200 residues with a completely different Rossmann-fold architecture. The remaining option D (2.1.2.1, serine hydroxymethyltransferase) is the only PLP-dependent hydroxymethyltransferase among the choices, and the specific 'KCLVAGTSAYC' motif matches the well-characterized SHMT active-site lysine region found in homologs across species (e.g., human P34896, E. coli GcvT). The 'TTTHK' motif further downstream is also consistent with the SHMT family active-site architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use family-level recognition of PLP-binding motifs (conserved lysine in SHMT family), sequence-length constraints (eliminating DHFR), and cofactor logic (PLP vs. SAM) to distinguish the four options. SHMT is one of the most extensively characterized PLP enzymes, and its diagnostic sequence motifs are well-documented across homologs. This constitutes legitimate transferable knowledge from the SHMT protein family rather than memorization of this specific Aspergillus entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three distinct enzyme classes (methyltransferases, hydrolase/dehydrogenase, hydroxymethyltransferase). PLP-dependence and sequence length cleanly separate them. No two options are defensible for the same sequence.


### Important caveats

- The UniProt EC annotation for Q4WXF4 uses evidence code ECO:0000250 (inferred by similarity to P34896), supplemented by experimental data from PubMed 39825596. The primary EC assignment is by homology, though the 2025 paper provides functional validation.
- EC 2.1.1.34 is an uncommon or possibly obsolete EC number; its identity as a methyltransferase is assumed based on the EC 2.1.1.x class definition.
- The PLP-binding motif argument relies on recognizing the 'KCLVAGTSAYC' pattern as SHMT-diagnostic; while this is well-established in the SHMT literature, a model without specific SHMT-family training data might not make this connection.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved PLP-binding lysine motif 'KCLVAGTSAYC' (around residue ~220), which is a hallmark of the serine hydroxymethyltransferase (SHMT) family. SHMT is a pyridoxal-5'-phosphate (PLP)-dependent enzyme, whereas methyltransferases (EC 2.1.1.x, options A and C) use S-adenosylmethionine as a cofactor and do not require PLP. The presence of this PLP-binding lysine motif eliminates options A (2.1.1.27, glycine N-methyltransferase) and C (2.1.1.34, a methyltransferase). Additionally, the sequence length of ~471 residues is far too large for dihydrofolate dehydrogenase (EC 3.5.2.6, option B), which is typically 160-200 residues with a completely different Rossmann-fold architecture. The remaining option D (2.1.2.1, serine hydroxymethyltransferase) is the only PLP-dependent hydroxymethyltransferase among the choices, and the specific 'KCLVAGTSAYC' motif matches the well-characterized SHMT active-site lysine region found in homologs across species (e.g., human P34896, E. coli GcvT). The 'TTTHK' motif further downstream is also consistent with the SHMT family active-site architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family-level recognition of PLP-binding motifs (conserved lysine in SHMT family), sequence-length constraints (eliminating DHFR), and cofactor logic (PLP vs. SAM) to distinguish the four options. SHMT is one of the most extensively characterized PLP enzymes, and its diagnostic sequence motifs are well-documented across homologs. This constitutes legitimate transferable knowledge from the SHMT protein family rather than memorization of this specific Aspergillus entry."
  },
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (GLYC_ASPFU) annotates this protein as Serine hydroxymethyltransferase, cytosolic with EC=2.1.2.1. The EC annotation is supported by both similarity evidence (ECO:0000250 to P34896, human SHMT) and experimental evidence from PubMed 39825596 (Alharthi et al. 2025, Virulence), which confirmed the cytosolic SHMT function in Aspergillus fumigatus. The catalytic activity (methylene-THF + glycine + H2O = THF + L-serine) is consistent with EC 2.1.2.1. The sequence matches exactly (471 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "The UniProt EC annotation for Q4WXF4 uses evidence code ECO:0000250 (inferred by similarity to P34896), supplemented by experimental data from PubMed 39825596. The primary EC assignment is by homology, though the 2025 paper provides functional validation.",
    "EC 2.1.1.34 is an uncommon or possibly obsolete EC number; its identity as a methyltransferase is assumed based on the EC 2.1.1.x class definition.",
    "The PLP-binding motif argument relies on recognizing the 'KCLVAGTSAYC' pattern as SHMT-diagnostic; while this is well-established in the SHMT literature, a model without specific SHMT-family training data might not make this connection."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct enzyme classes (methyltransferases, hydrolase/dehydrogenase, hydroxymethyltransferase). PLP-dependence and sequence length cleanly separate them. No two options are defensible for the same sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (GLYC_ASPFU) annotates this protein as Serine hydroxymethyltransferase, cytosolic with EC=2.1.2.1. The EC annotation is supported by both similarity evidence (ECO:0000250 to P34896, human SHMT) and experimental evidence from PubMed 39825596 (Alharthi et al. 2025, Virulence), which confirmed the cytosolic SHMT function in Aspergillus fumigatus. The catalytic activity (methylene-THF + glycine + H2O = THF + L-serine) is consistent with EC 2.1.2.1. The sequence matches exactly (471 aa, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved PLP-binding lysine motif 'KCLVAGTSAYC' (around residue ~220), which is a hallmark of the serine hydroxymethyltransferase (SHMT) family. SHMT is a pyridoxal-5'-phosphate (PLP)-dependent enzyme, whereas methyltransferases (EC 2.1.1.x, options A and C) use S-adenosylmethionine as a cofactor and do not require PLP. The presence of this PLP-binding lysine motif eliminates options A (2.1.1.27, glycine N-methyltransferase) and C (2.1.1.34, a methyltransferase). Additionally, the sequence length of ~471 residues is far too large for dihydrofolate dehydrogenase (EC 3.5.2.6, option B), which is typically 160-200 residues with a completely different Rossmann-fold architecture. The remaining option D (2.1.2.1, serine hydroxymethyltransferase) is the only PLP-dependent hydroxymethyltransferase among the choices, and the specific 'KCLVAGTSAYC' motif matches the well-characterized SHMT active-site lysine region found in homologs across species (e.g., human P34896, E. coli GcvT). The 'TTTHK' motif further downstream is also consistent with the SHMT family active-site architecture.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family-level recognition of PLP-binding motifs (conserved lysine in SHMT family), sequence-length constraints (eliminating DHFR), and cofactor logic (PLP vs. SAM) to distinguish the four options. SHMT is one of the most extensively characterized PLP enzymes, and its diagnostic sequence motifs are well-documented across homologs. This constitutes legitimate transferable knowledge from the SHMT protein family rather than memorization of this specific Aspergillus entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct enzyme classes (methyltransferases, hydrolase/dehydrogenase, hydroxymethyltransferase). PLP-dependence and sequence length cleanly separate them. No two options are defensible for the same sequence."
  },
  "important_caveats": [
    "The UniProt EC annotation for Q4WXF4 uses evidence code ECO:0000250 (inferred by similarity to P34896), supplemented by experimental data from PubMed 39825596. The primary EC assignment is by homology, though the 2025 paper provides functional validation.",
    "EC 2.1.1.34 is an uncommon or possibly obsolete EC number; its identity as a methyltransferase is assumed based on the EC 2.1.1.x class definition.",
    "The PLP-binding motif argument relies on recognizing the 'KCLVAGTSAYC' pattern as SHMT-diagnostic; while this is well-established in the SHMT literature, a model without specific SHMT-family training data might not make this connection."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
