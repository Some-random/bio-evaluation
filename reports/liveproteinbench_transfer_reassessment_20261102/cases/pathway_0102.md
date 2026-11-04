# pathway_0102

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0102.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFSTLLTACTAITGALGTPDLDRRQNVTPNAQGTHNGYFYSWWSDGQSPVTYTNSAGGSYSVEWSSGGNLVGGKGWNPGSAKEIRYSASWQPTNNSNSYLTIYGWTRSPLVEYYIVESHGEYNPGSSAEPRGEIEAHGSIYKLYESTRVQQPSIDGTQTFQQYWAIRQTHRTSGTVTTGTFFNAWAAAGMPIGQHNYMIVATEAYNSAGRASVVVETPP

[Multiple Choices]
A. IMP biosynthesis via de novo pathway
B. protein ubiquitination. .
C. Glycan degradation
D. tetrahydrofolate biosynthesis
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

> The sequence-matched UniProt record assigns the pathway as glycan degradation, specifically xylan degradation, based on a PROSITE-ProRule annotation. This supports choice C as a database annotation, though it is computational rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal segment consistent with secretion and is a compact, roughly 220-residue enzyme-like protein rich in aromatic residues. That pattern is compatible with fungal endo-1,4-beta-xylanases, which act on xylan, a glycan. Family-level recognition therefore points to glycan degradation over the unrelated IMP, ubiquitination, and tetrahydrofolate choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of secreted fungal xylanases and their substrate provides a meaningful basis for distinguishing the glycan-degradation option. This is a sequence-based family inference, not a claim that the exact protein’s annotation was supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, glycan degradation is the pathway that matches the xylanase-family inference; the other choices concern unrelated processes.


### Important caveats

- The reviewer evidence supports the key through a PROSITE-ProRule pathway annotation; it does not establish direct experimental validation of the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment consistent with secretion and is a compact, roughly 220-residue enzyme-like protein rich in aromatic residues. That pattern is compatible with fungal endo-1,4-beta-xylanases, which act on xylan, a glycan. Family-level recognition therefore points to glycan degradation over the unrelated IMP, ubiquitination, and tetrahydrofolate choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of secreted fungal xylanases and their substrate provides a meaningful basis for distinguishing the glycan-degradation option. This is a sequence-based family inference, not a claim that the exact protein’s annotation was supplied in the original input."
  },
  "case_id": "pathway_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the pathway as glycan degradation, specifically xylan degradation, based on a PROSITE-ProRule annotation. This supports choice C as a database annotation, though it is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer evidence supports the key through a PROSITE-ProRule pathway annotation; it does not establish direct experimental validation of the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, glycan degradation is the pathway that matches the xylanase-family inference; the other choices concern unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the pathway as glycan degradation, specifically xylan degradation, based on a PROSITE-ProRule annotation. This supports choice C as a database annotation, though it is computational rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment consistent with secretion and is a compact, roughly 220-residue enzyme-like protein rich in aromatic residues. That pattern is compatible with fungal endo-1,4-beta-xylanases, which act on xylan, a glycan. Family-level recognition therefore points to glycan degradation over the unrelated IMP, ubiquitination, and tetrahydrofolate choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of secreted fungal xylanases and their substrate provides a meaningful basis for distinguishing the glycan-degradation option. This is a sequence-based family inference, not a claim that the exact protein’s annotation was supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, glycan degradation is the pathway that matches the xylanase-family inference; the other choices concern unrelated processes."
  },
  "important_caveats": [
    "The reviewer evidence supports the key through a PROSITE-ProRule pathway annotation; it does not establish direct experimental validation of the pathway assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X5X8 annotates this protein as Ethylene-inducing xylanase 4 (EIX4), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with pathway annotation 'Glycan degradation; xylan degradation' (evidence code ECO:0000255, PROSITE-ProRule PRU01097). EC 3.2.1.8 hydrolyzes xylan, a glycan/polysaccharide, which falls squarely under glycan degradation. The expected answer C is directly supported by the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence MVSFSTLLTACTAITGALGTP is a classic eukaryotic signal peptide (hydrophobic core of ~15 residues followed by a cleavage site), indicating the protein is secreted/extracellular. Among the four options, only glycan degradation (C) is a pathway whose key enzymes (glycoside hydrolases, glycosidases) are secreted to act on extracellular polysaccharides such as plant cell wall xylan and cellulose. IMP biosynthesis (A), protein ubiquitination (B), and tetrahydrofolate biosynthesis (D) are all intracellular metabolic/signaling pathways whose enzymes lack signal peptides. The small protein size (221 aa) is also consistent with a typical glycoside hydrolase (e.g., GH10/GH11 xylanases are 180–300 aa). The sequence composition (abundant Ser, Thr, Gly, Asn, Tyr) and motifs such as 'YYIVESHG' (potentially containing the catalytic Glu of a xylanase) and 'Q' residues are consistent with glycoside hydrolase family features learned from other fungal xylanases. A knowledgeable model can thus eliminate A, B, D based on the signal peptide and intracellular nature of those pathways, and select C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide is directly visible in the input sequence and is a well-known, transferable feature indicating secretion. The distinction between extracellular glycan-degrading enzymes and intracellular metabolic/signaling enzymes is a fundamental biological principle applicable across many protein families. The small size and sequence composition further support a glycoside hydrolase assignment. No target-specific database lookup is required to reach the correct answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct pathway categories. The presence of a signal peptide unambiguously points to a secreted enzyme, eliminating the three intracellular pathway options. No option is partially defensible given the sequence features.


### Important caveats

- The PROSITE-ProRule annotation (ECO:0000255) is a computational inference from sequence motifs, not direct experimental validation of xylanase activity, though a functional study (PubMed:33205907) supports the protein's role in plant-pathogen interactions.
- The reviewer-only evidence confirms the protein is from Verticillium dahliae, a fungal plant pathogen, which is consistent with secretion of cell-wall-degrading enzymes, but the organism name was not provided to the evaluated model.
- The model would not need to identify the specific enzyme as a xylanase; recognizing it as a secreted glycoside hydrolase acting on glycans is sufficient to select option C over the other three intracellular pathways.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence MVSFSTLLTACTAITGALGTP is a classic eukaryotic signal peptide (hydrophobic core of ~15 residues followed by a cleavage site), indicating the protein is secreted/extracellular. Among the four options, only glycan degradation (C) is a pathway whose key enzymes (glycoside hydrolases, glycosidases) are secreted to act on extracellular polysaccharides such as plant cell wall xylan and cellulose. IMP biosynthesis (A), protein ubiquitination (B), and tetrahydrofolate biosynthesis (D) are all intracellular metabolic/signaling pathways whose enzymes lack signal peptides. The small protein size (221 aa) is also consistent with a typical glycoside hydrolase (e.g., GH10/GH11 xylanases are 180–300 aa). The sequence composition (abundant Ser, Thr, Gly, Asn, Tyr) and motifs such as 'YYIVESHG' (potentially containing the catalytic Glu of a xylanase) and 'Q' residues are consistent with glycoside hydrolase family features learned from other fungal xylanases. A knowledgeable model can thus eliminate A, B, D based on the signal peptide and intracellular nature of those pathways, and select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide is directly visible in the input sequence and is a well-known, transferable feature indicating secretion. The distinction between extracellular glycan-degrading enzymes and intracellular metabolic/signaling enzymes is a fundamental biological principle applicable across many protein families. The small size and sequence composition further support a glycoside hydrolase assignment. No target-specific database lookup is required to reach the correct answer."
  },
  "case_id": "pathway_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 annotates this protein as Ethylene-inducing xylanase 4 (EIX4), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with pathway annotation 'Glycan degradation; xylan degradation' (evidence code ECO:0000255, PROSITE-ProRule PRU01097). EC 3.2.1.8 hydrolyzes xylan, a glycan/polysaccharide, which falls squarely under glycan degradation. The expected answer C is directly supported by the database annotation."
  },
  "important_caveats": [
    "The PROSITE-ProRule annotation (ECO:0000255) is a computational inference from sequence motifs, not direct experimental validation of xylanase activity, though a functional study (PubMed:33205907) supports the protein's role in plant-pathogen interactions.",
    "The reviewer-only evidence confirms the protein is from Verticillium dahliae, a fungal plant pathogen, which is consistent with secretion of cell-wall-degrading enzymes, but the organism name was not provided to the evaluated model.",
    "The model would not need to identify the specific enzyme as a xylanase; recognizing it as a secreted glycoside hydrolase acting on glycans is sufficient to select option C over the other three intracellular pathways."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct pathway categories. The presence of a signal peptide unambiguously points to a secreted enzyme, eliminating the three intracellular pathway options. No option is partially defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 annotates this protein as Ethylene-inducing xylanase 4 (EIX4), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with pathway annotation 'Glycan degradation; xylan degradation' (evidence code ECO:0000255, PROSITE-ProRule PRU01097). EC 3.2.1.8 hydrolyzes xylan, a glycan/polysaccharide, which falls squarely under glycan degradation. The expected answer C is directly supported by the database annotation.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence MVSFSTLLTACTAITGALGTP is a classic eukaryotic signal peptide (hydrophobic core of ~15 residues followed by a cleavage site), indicating the protein is secreted/extracellular. Among the four options, only glycan degradation (C) is a pathway whose key enzymes (glycoside hydrolases, glycosidases) are secreted to act on extracellular polysaccharides such as plant cell wall xylan and cellulose. IMP biosynthesis (A), protein ubiquitination (B), and tetrahydrofolate biosynthesis (D) are all intracellular metabolic/signaling pathways whose enzymes lack signal peptides. The small protein size (221 aa) is also consistent with a typical glycoside hydrolase (e.g., GH10/GH11 xylanases are 180–300 aa). The sequence composition (abundant Ser, Thr, Gly, Asn, Tyr) and motifs such as 'YYIVESHG' (potentially containing the catalytic Glu of a xylanase) and 'Q' residues are consistent with glycoside hydrolase family features learned from other fungal xylanases. A knowledgeable model can thus eliminate A, B, D based on the signal peptide and intracellular nature of those pathways, and select C.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide is directly visible in the input sequence and is a well-known, transferable feature indicating secretion. The distinction between extracellular glycan-degrading enzymes and intracellular metabolic/signaling enzymes is a fundamental biological principle applicable across many protein families. The small size and sequence composition further support a glycoside hydrolase assignment. No target-specific database lookup is required to reach the correct answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct pathway categories. The presence of a signal peptide unambiguously points to a secreted enzyme, eliminating the three intracellular pathway options. No option is partially defensible given the sequence features."
  },
  "important_caveats": [
    "The PROSITE-ProRule annotation (ECO:0000255) is a computational inference from sequence motifs, not direct experimental validation of xylanase activity, though a functional study (PubMed:33205907) supports the protein's role in plant-pathogen interactions.",
    "The reviewer-only evidence confirms the protein is from Verticillium dahliae, a fungal plant pathogen, which is consistent with secretion of cell-wall-degrading enzymes, but the organism name was not provided to the evaluated model.",
    "The model would not need to identify the specific enzyme as a xylanase; recognizing it as a secreted glycoside hydrolase acting on glycans is sufficient to select option C over the other three intracellular pathways."
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
  "benchmark_sequence_length": 221,
  "benchmark_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 221,
  "current_source_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X5X8",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "selected_historical_source_sequence_length": 221,
  "selected_historical_source_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "selected_historical_version": {
    "accession": "G2X5X8",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX4_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X5X8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX4\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   EIX4_VERDV              Reviewed;         221 AA.\nAC   G2X5X8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX4 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX4 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05294;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-\nCC       ProRule:PRU01097}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
