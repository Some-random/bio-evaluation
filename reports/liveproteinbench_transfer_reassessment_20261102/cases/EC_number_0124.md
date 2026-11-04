# EC_number_0124

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0124.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRFSASLLLALTGSAAASPIRAEEEIRVYDLPISLFDDLQGLDAAMKAAGREYIGTSLTVRNDFQEQNIIRTEFGSITPENAQKWDATEPNRGQFTFGSADQHMDWARQNGKHVRCHTLVWYSQLPGWVSNSGFNNATLQQVMQNHINQVMGRYRGRCNHWDVVNEAPRLMAMRLQIGEAYIPIAFRMAAQADPSAKLYYNDYNLEYLGPKVEGAARIVRLVKQYGARIDGVGYQAHLVTEPTPTQSTPTPSEEDLIKALRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN

[Multiple Choices]
A. 3.2.1.8
B. 3.2.1.18
C. 2.1.1.394
D. 5.3.3.21
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

> The matched-sequence UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation cites PubMed with experimental evidence code ECO:0000269; the historical record also reports this assignment. The primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the remaining sequence has the size and acidic/aromatic enzyme features expected of a secreted fungal carbohydrate-active enzyme, plausibly an endo-xylanase. Transferable recognition of fungal xylanase families and their conserved catalytic features meaningfully favors EC 3.2.1.8 over the unrelated methyltransferase and isomerase choices, and over the distinct exo-glucosidase activity in B. This is a family-level probabilistic inference, not proof of the exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A plausible family and enzyme-class inference from the sequence distinguishes the offered alternatives without needing the exact protein's database record. Reviewer-only evidence supports the key, but is not needed for the transferability judgment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second offered EC number is comparably supported by the sequence-level family inference.


### Important caveats

- The secretory signal supports extracellular enzyme context but does not by itself establish substrate specificity.
- The exact EC assignment is supported by a database annotation citing experimental evidence; the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the remaining sequence has the size and acidic/aromatic enzyme features expected of a secreted fungal carbohydrate-active enzyme, plausibly an endo-xylanase. Transferable recognition of fungal xylanase families and their conserved catalytic features meaningfully favors EC 3.2.1.8 over the unrelated methyltransferase and isomerase choices, and over the distinct exo-glucosidase activity in B. This is a family-level probabilistic inference, not proof of the exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A plausible family and enzyme-class inference from the sequence distinguishes the offered alternatives without needing the exact protein's database record. Reviewer-only evidence supports the key, but is not needed for the transferability judgment."
  },
  "case_id": "EC_number_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation cites PubMed with experimental evidence code ECO:0000269; the historical record also reports this assignment. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The secretory signal supports extracellular enzyme context but does not by itself establish substrate specificity.",
    "The exact EC assignment is supported by a database annotation citing experimental evidence; the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered EC number is comparably supported by the sequence-level family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation cites PubMed with experimental evidence code ECO:0000269; the historical record also reports this assignment. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the remaining sequence has the size and acidic/aromatic enzyme features expected of a secreted fungal carbohydrate-active enzyme, plausibly an endo-xylanase. Transferable recognition of fungal xylanase families and their conserved catalytic features meaningfully favors EC 3.2.1.8 over the unrelated methyltransferase and isomerase choices, and over the distinct exo-glucosidase activity in B. This is a family-level probabilistic inference, not proof of the exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A plausible family and enzyme-class inference from the sequence distinguishes the offered alternatives without needing the exact protein's database record. Reviewer-only evidence supports the key, but is not needed for the transferability judgment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered EC number is comparably supported by the sequence-level family inference."
  },
  "important_caveats": [
    "The secretory signal supports extracellular enzyme context but does not by itself establish substrate specificity.",
    "The exact EC assignment is supported by a database annotation citing experimental evidence; the cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry M4MLB5 (XYNB_HUMIN) annotates this exact sequence as Endo-1,4-beta-xylanase B with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The catalytic activity is described as 'Endohydrolysis of (1→4)-beta-D-xylosidic linkages in xylans.' The sequence in the question matches the source record exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~358 aa with a hydrophobic signal peptide MRFSASLLLALTGSAAASPI, leaving ~330 mature residues) contains hallmark motifs of glycoside hydrolase family 10 (GH10) endo-xylanases: (1) the conserved 'NE' catalytic motif visible in 'WDVVNEAPRL' (catalytic nucleophile context), (2) the 'YRL' motif in 'IRRLVKQYGARIDGVGYQAHLVTE', (3) multiple conserved Glu residues in the (β/α)8 barrel catalytic region, and (4) the 'DATE' motif near the acid/base Glu. GH10 xylanases are typically 300–400 aa secreted proteins with these motifs, matching this sequence. This distinguishes it from EC 3.2.1.18 (α-L-arabinofuranosidase, GH43/GH51 families, typically 200–300 aa with different motifs such as the 'HxxxD' catalytic set and no NEP/YRL signature). EC 2.1.1.394 (methyltransferase) and EC 5.3.3.21 (isomerase) are entirely different enzyme classes lacking any glycosidase catalytic architecture; no SAM-binding Rossmann fold or isomerase motifs are present. The signal peptide and overall length further exclude transferase and isomerase classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize GH10 xylanase family motifs (NEP/NE catalytic motif, YRL motif, catalytic Glu residues, (β/α)8 barrel length) from general biochemistry and glycoside hydrolase family knowledge learned from many characterized xylanases. These features meaningfully distinguish 3.2.1.8 from the other three options without needing to recall this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (hydrolase, transferase, isomerase) and within hydrolases two different GH families. The sequence features unambiguously point to a GH10 xylanase (EC 3.2.1.8). No other option is defensible given the family-specific motifs and overall architecture.


### Important caveats

- The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:23306124), not merely computational transfer.
- The sequence matches the source record exactly (SHA-256 confirmed in both current and historical snapshots).
- The 'NE' motif here reads as 'NEA' (in WDVVNEAPRL) rather than the canonical 'NEP'; this is a known variant within GH10 and does not change the family assignment or EC number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~358 aa with a hydrophobic signal peptide MRFSASLLLALTGSAAASPI, leaving ~330 mature residues) contains hallmark motifs of glycoside hydrolase family 10 (GH10) endo-xylanases: (1) the conserved 'NE' catalytic motif visible in 'WDVVNEAPRL' (catalytic nucleophile context), (2) the 'YRL' motif in 'IRRLVKQYGARIDGVGYQAHLVTE', (3) multiple conserved Glu residues in the (β/α)8 barrel catalytic region, and (4) the 'DATE' motif near the acid/base Glu. GH10 xylanases are typically 300–400 aa secreted proteins with these motifs, matching this sequence. This distinguishes it from EC 3.2.1.18 (α-L-arabinofuranosidase, GH43/GH51 families, typically 200–300 aa with different motifs such as the 'HxxxD' catalytic set and no NEP/YRL signature). EC 2.1.1.394 (methyltransferase) and EC 5.3.3.21 (isomerase) are entirely different enzyme classes lacking any glycosidase catalytic architecture; no SAM-binding Rossmann fold or isomerase motifs are present. The signal peptide and overall length further exclude transferase and isomerase classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize GH10 xylanase family motifs (NEP/NE catalytic motif, YRL motif, catalytic Glu residues, (β/α)8 barrel length) from general biochemistry and glycoside hydrolase family knowledge learned from many characterized xylanases. These features meaningfully distinguish 3.2.1.8 from the other three options without needing to recall this specific protein's database entry."
  },
  "case_id": "EC_number_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry M4MLB5 (XYNB_HUMIN) annotates this exact sequence as Endo-1,4-beta-xylanase B with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The catalytic activity is described as 'Endohydrolysis of (1→4)-beta-D-xylosidic linkages in xylans.' The sequence in the question matches the source record exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:23306124), not merely computational transfer.",
    "The sequence matches the source record exactly (SHA-256 confirmed in both current and historical snapshots).",
    "The 'NE' motif here reads as 'NEA' (in WDVVNEAPRL) rather than the canonical 'NEP'; this is a known variant within GH10 and does not change the family assignment or EC number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase, transferase, isomerase) and within hydrolases two different GH families. The sequence features unambiguously point to a GH10 xylanase (EC 3.2.1.8). No other option is defensible given the family-specific motifs and overall architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry M4MLB5 (XYNB_HUMIN) annotates this exact sequence as Endo-1,4-beta-xylanase B with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The catalytic activity is described as 'Endohydrolysis of (1→4)-beta-D-xylosidic linkages in xylans.' The sequence in the question matches the source record exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~358 aa with a hydrophobic signal peptide MRFSASLLLALTGSAAASPI, leaving ~330 mature residues) contains hallmark motifs of glycoside hydrolase family 10 (GH10) endo-xylanases: (1) the conserved 'NE' catalytic motif visible in 'WDVVNEAPRL' (catalytic nucleophile context), (2) the 'YRL' motif in 'IRRLVKQYGARIDGVGYQAHLVTE', (3) multiple conserved Glu residues in the (β/α)8 barrel catalytic region, and (4) the 'DATE' motif near the acid/base Glu. GH10 xylanases are typically 300–400 aa secreted proteins with these motifs, matching this sequence. This distinguishes it from EC 3.2.1.18 (α-L-arabinofuranosidase, GH43/GH51 families, typically 200–300 aa with different motifs such as the 'HxxxD' catalytic set and no NEP/YRL signature). EC 2.1.1.394 (methyltransferase) and EC 5.3.3.21 (isomerase) are entirely different enzyme classes lacking any glycosidase catalytic architecture; no SAM-binding Rossmann fold or isomerase motifs are present. The signal peptide and overall length further exclude transferase and isomerase classes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize GH10 xylanase family motifs (NEP/NE catalytic motif, YRL motif, catalytic Glu residues, (β/α)8 barrel length) from general biochemistry and glycoside hydrolase family knowledge learned from many characterized xylanases. These features meaningfully distinguish 3.2.1.8 from the other three options without needing to recall this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase, transferase, isomerase) and within hydrolases two different GH families. The sequence features unambiguously point to a GH10 xylanase (EC 3.2.1.8). No other option is defensible given the family-specific motifs and overall architecture."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed:23306124), not merely computational transfer.",
    "The sequence matches the source record exactly (SHA-256 confirmed in both current and historical snapshots).",
    "The 'NE' motif here reads as 'NEA' (in WDVVNEAPRL) rather than the canonical 'NEP'; this is a known variant within GH10 and does not change the family assignment or EC number."
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
  "benchmark_sequence_length": 358,
  "benchmark_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 358,
  "current_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MLB5",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "selected_historical_source_sequence_length": 358,
  "selected_historical_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "selected_historical_version": {
    "accession": "M4MLB5",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNB_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MLB5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNB_HUMIN              Reviewed;         358 AA.\nAC   M4MLB5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynB {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
