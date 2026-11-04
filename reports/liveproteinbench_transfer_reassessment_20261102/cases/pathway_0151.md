# pathway_0151

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0151.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. Bacterial outer membrane biogenesis
B. Alkaloid biosynthesis
C. Glycolipid biosynthesis
D. Cell wall degradation
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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1231)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns the protein to ajmaline alkaloid biosynthesis and names it ajmaline N-methyltransferase. The annotation cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the glycine-rich motif characteristic of SAM-dependent methyltransferases and is consistent with a soluble small-molecule methyltransferase. Alkaloid N-methylation is a plausible role for that enzyme class; glycolipid biosynthesis more commonly relies on glycosyltransferases and membrane-associated machinery. This favors B over the offered alternatives, though it is not a substrate-specific identification.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of methyltransferase motifs and typical enzyme roles gives a meaningful, probabilistic distinction among these choices. The sequence alone does not establish the exact substrate or pathway, so the inference is less certain than the sequence-matched experimental annotation.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-level inference favors B, and the matched annotation supports it; no other offered option is comparably supported by the available evidence."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original input.",
    "A SAM-dependent methyltransferase motif is not by itself specific to alkaloid biosynthesis."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:27122470). The protein is Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina. The sequence matches the benchmark exactly. This directly supports Choice B.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical Class I (Rossmann-fold) SAM-dependent methyltransferase motif 'VLDVGCGIGGTCL' (residues ~85-97), along with catalytic residues 'IHC' and 'HRDL' characteristic of N-methyltransferases. This immediately identifies the enzyme as a methyltransferase. Among the four pathway options: (A) Bacterial outer membrane biogenesis involves LPS transporters and BAM complex proteins (large, multi-TM, beta-barrel), not methyltransferases, and the sequence lacks bacterial secretion signals or transmembrane helices; (C) Glycolipid biosynthesis is primarily driven by glycosyltransferases and acyltransferases, not N-methyltransferases; (D) Cell wall degradation involves hydrolases (cellulases, pectinases) with carbohydrate-binding modules, not methyltransferases. (B) Alkaloid biosynthesis is well-known for N-methylation tailoring steps (e.g., caffeine synthase, codeine O-methyltransferase, strictosidine-related N-methyltransferases in monoterpenoid indole alkaloid pathways). The combination of a clear methyltransferase fold + eukaryotic/plant-like cytosolic architecture (no TM domains, no signal peptide, ~291 aa) uniquely points to alkaloid biosynthesis among the given options. This is transferable knowledge about enzyme-class-to-pathway associations learned from many characterized methyltransferases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The VLDVGCGIGG methyltransferase motif is directly readable from the sequence and is a textbook family-level signature. Among the four offered pathways, only alkaloid biosynthesis is characterized by methyltransferase-catalyzed tailoring reactions; the other three involve fundamentally different enzyme classes (transporters, glycosyltransferases, hydrolases). A knowledgeable model can use this enzyme-class-to-pathway mapping to eliminate A, C, and D without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The methyltransferase motif cleanly separates B from A, C, and D, which involve entirely different enzyme classes. No other option is plausibly supported by a SAM-dependent N-methyltransferase.


### Important caveats

- The methyltransferase motif alone does not specify which alkaloid; the 'ajmaline biosynthesis' sub-pathway requires knowledge of Rauvolfia serpentina's specific indole alkaloid pathway, but the question only asks for the broad pathway category (alkaloid biosynthesis), which is inferable from the enzyme class.
- The sequence's eukaryotic/plant character (no bacterial secretion signals, no TM domains, cytosolic methyltransferase architecture) helps rule out option A but does not by itself confirm alkaloid vs. other secondary metabolite pathways; however, among the four given choices, only B involves methyltransferases.
- The UniProt annotation carries experimental evidence (ECO:0000269) from the 2016 Plant J. paper, confirming the pathway assignment is experimentally supported rather than purely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical Class I (Rossmann-fold) SAM-dependent methyltransferase motif 'VLDVGCGIGGTCL' (residues ~85-97), along with catalytic residues 'IHC' and 'HRDL' characteristic of N-methyltransferases. This immediately identifies the enzyme as a methyltransferase. Among the four pathway options: (A) Bacterial outer membrane biogenesis involves LPS transporters and BAM complex proteins (large, multi-TM, beta-barrel), not methyltransferases, and the sequence lacks bacterial secretion signals or transmembrane helices; (C) Glycolipid biosynthesis is primarily driven by glycosyltransferases and acyltransferases, not N-methyltransferases; (D) Cell wall degradation involves hydrolases (cellulases, pectinases) with carbohydrate-binding modules, not methyltransferases. (B) Alkaloid biosynthesis is well-known for N-methylation tailoring steps (e.g., caffeine synthase, codeine O-methyltransferase, strictosidine-related N-methyltransferases in monoterpenoid indole alkaloid pathways). The combination of a clear methyltransferase fold + eukaryotic/plant-like cytosolic architecture (no TM domains, no signal peptide, ~291 aa) uniquely points to alkaloid biosynthesis among the given options. This is transferable knowledge about enzyme-class-to-pathway associations learned from many characterized methyltransferases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The VLDVGCGIGG methyltransferase motif is directly readable from the sequence and is a textbook family-level signature. Among the four offered pathways, only alkaloid biosynthesis is characterized by methyltransferase-catalyzed tailoring reactions; the other three involve fundamentally different enzyme classes (transporters, glycosyltransferases, hydrolases). A knowledgeable model can use this enzyme-class-to-pathway mapping to eliminate A, C, and D without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "pathway_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:27122470). The protein is Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina. The sequence matches the benchmark exactly. This directly supports Choice B."
  },
  "important_caveats": [
    "The methyltransferase motif alone does not specify which alkaloid; the 'ajmaline biosynthesis' sub-pathway requires knowledge of Rauvolfia serpentina's specific indole alkaloid pathway, but the question only asks for the broad pathway category (alkaloid biosynthesis), which is inferable from the enzyme class.",
    "The sequence's eukaryotic/plant character (no bacterial secretion signals, no TM domains, cytosolic methyltransferase architecture) helps rule out option A but does not by itself confirm alkaloid vs. other secondary metabolite pathways; however, among the four given choices, only B involves methyltransferases.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from the 2016 Plant J. paper, confirming the pathway assignment is experimentally supported rather than purely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The methyltransferase motif cleanly separates B from A, C, and D, which involve entirely different enzyme classes. No other option is plausibly supported by a SAM-dependent N-methyltransferase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:27122470). The protein is Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina. The sequence matches the benchmark exactly. This directly supports Choice B.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical Class I (Rossmann-fold) SAM-dependent methyltransferase motif 'VLDVGCGIGGTCL' (residues ~85-97), along with catalytic residues 'IHC' and 'HRDL' characteristic of N-methyltransferases. This immediately identifies the enzyme as a methyltransferase. Among the four pathway options: (A) Bacterial outer membrane biogenesis involves LPS transporters and BAM complex proteins (large, multi-TM, beta-barrel), not methyltransferases, and the sequence lacks bacterial secretion signals or transmembrane helices; (C) Glycolipid biosynthesis is primarily driven by glycosyltransferases and acyltransferases, not N-methyltransferases; (D) Cell wall degradation involves hydrolases (cellulases, pectinases) with carbohydrate-binding modules, not methyltransferases. (B) Alkaloid biosynthesis is well-known for N-methylation tailoring steps (e.g., caffeine synthase, codeine O-methyltransferase, strictosidine-related N-methyltransferases in monoterpenoid indole alkaloid pathways). The combination of a clear methyltransferase fold + eukaryotic/plant-like cytosolic architecture (no TM domains, no signal peptide, ~291 aa) uniquely points to alkaloid biosynthesis among the given options. This is transferable knowledge about enzyme-class-to-pathway associations learned from many characterized methyltransferases.",
    "missing_item_specific_fact": "",
    "reason": "The VLDVGCGIGG methyltransferase motif is directly readable from the sequence and is a textbook family-level signature. Among the four offered pathways, only alkaloid biosynthesis is characterized by methyltransferase-catalyzed tailoring reactions; the other three involve fundamentally different enzyme classes (transporters, glycosyltransferases, hydrolases). A knowledgeable model can use this enzyme-class-to-pathway mapping to eliminate A, C, and D without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The methyltransferase motif cleanly separates B from A, C, and D, which involve entirely different enzyme classes. No other option is plausibly supported by a SAM-dependent N-methyltransferase."
  },
  "important_caveats": [
    "The methyltransferase motif alone does not specify which alkaloid; the 'ajmaline biosynthesis' sub-pathway requires knowledge of Rauvolfia serpentina's specific indole alkaloid pathway, but the question only asks for the broad pathway category (alkaloid biosynthesis), which is inferable from the enzyme class.",
    "The sequence's eukaryotic/plant character (no bacterial secretion signals, no TM domains, cytosolic methyltransferase architecture) helps rule out option A but does not by itself confirm alkaloid vs. other secondary metabolite pathways; however, among the four given choices, only B involves methyltransferases.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from the 2016 Plant J. paper, confirming the pathway assignment is experimentally supported rather than purely computational."
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
  "benchmark_sequence_length": 291,
  "benchmark_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 291,
  "current_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A075D654",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "selected_historical_source_sequence_length": 291,
  "selected_historical_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "selected_historical_version": {
    "accession": "A0A075D654",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ANMT_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A075D654\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHH02777.1\",\"source\":\"EMBL\"}],\"value\":\"Gamma-tocopherol-like methyltransferase ANMT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.393\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Ajmaline N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"RsANMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Cazares-Flores P.\",\"Levac D.\",\"De Luca V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27122470\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.13186\"}],\"citationType\":\"journal article\",\"firstPage\":\"335\",\"id\":\"27122470\",\"journal\":\"Plant J.\",\"lastPage\":\"342\",\"publicationDate\":\"2016\",\"title\":\"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.\",\"volume\":\"87\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   ANMT_RAUSE              Reviewed;         291 AA.\nAC   A0A075D654;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};\nDE            Short=RsANMT {ECO:0000303|PubMed:27122470};\nDE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};\nGN   Name=ANMT {ECO:0000303|PubMed:27122470};\nGN   Synonyms=Rs820 {ECO:0000312|EMBL:AHH02777.1};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRX   PubMed=27122470; DOI=10.1111/tpj.13186;\nRA   Cazares-Flores P., Levac D., De Luca V.;\nRT   \"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta\nRT   -methylajmaline biosynthesis belong to a gene family derived from gamma-\nRT   tocopherol C-methyltransferase.\";\nRL   Plant J. 87:335-342(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:27122470}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
