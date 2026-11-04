# pathway_0144

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0144.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Cell wall degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGQFRFLALIVAVLCFSVALFLPTADEPDQDSYSVPLNQSVNTSQPPSSEMVPSDIRLTPLPQPKRIHYMVKVGDTLSGIFAQLGVPYSILQKILSVDLDHLQLDMIQPGEELELMMDDMGQLSRLIYHMSIVEKAIYTRENDGSFSYDFQEISGEWREILFSGEINGSFSVSARRVGLTSSQVANITQVMKDKIDFSRSLRAGDRFDILVKQQYLGEHNTGNSEIKAISFKLAKGDVSAFLAEDGRFYDRAGNSLERAFNRYPVDKAYRQITSGFNPKRKHPVTGRVVPHNGTDFATPIGAPVYSTGDGKVIVVRKHPYAGNYLVIEHNSVYKTRYLHLDKILVKKGQLVKRGQKIALAGATGRLTGPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQANQQEVALDET

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. ajmaline biosynthesis. .
C. Cell wall degradation
D. Protein biosynthesis
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

> The sequence-matched UniProt record annotates the pathway as cell wall/peptidoglycan degradation (C5, H5). The pathway annotation carries experimental evidence code ECO:0000269, and the record names the protein as a peptidoglycan DD-endopeptidase (C4). This supports choice C, though the reviewer evidence does not independently validate the cited study.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a strongly hydrophobic N-terminal segment consistent with a bacterial export signal, followed by a soluble enzyme-sized region with histidine-containing features compatible with a metal-dependent peptidase. Transferable knowledge of bacterial secreted peptidoglycan hydrolases makes cell-wall degradation a credible choice. This fits C better than intracellular protein biosynthesis or metabolic-intermediate biosynthesis, while ajmaline biosynthesis is a specialized plant alkaloid pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide and plausible peptidase features provide a meaningful family-level inference from the sequence and distinguish the offered choices, even though they do not prove the exact substrate or pathway on their own.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, cell wall degradation is the best-supported pathway; the other choices are not comparably plausible given the sequence features.


### Important caveats

- A secretion signal and peptidase-like features are suggestive rather than conclusive from sequence alone.
- The source annotation supports the key, but its cited experimental evidence was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a strongly hydrophobic N-terminal segment consistent with a bacterial export signal, followed by a soluble enzyme-sized region with histidine-containing features compatible with a metal-dependent peptidase. Transferable knowledge of bacterial secreted peptidoglycan hydrolases makes cell-wall degradation a credible choice. This fits C better than intracellular protein biosynthesis or metabolic-intermediate biosynthesis, while ajmaline biosynthesis is a specialized plant alkaloid pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide and plausible peptidase features provide a meaningful family-level inference from the sequence and distinguish the offered choices, even though they do not prove the exact substrate or pathway on their own."
  },
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the pathway as cell wall/peptidoglycan degradation (C5, H5). The pathway annotation carries experimental evidence code ECO:0000269, and the record names the protein as a peptidoglycan DD-endopeptidase (C4). This supports choice C, though the reviewer evidence does not independently validate the cited study."
  },
  "important_caveats": [
    "A secretion signal and peptidase-like features are suggestive rather than conclusive from sequence alone.",
    "The source annotation supports the key, but its cited experimental evidence was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cell wall degradation is the best-supported pathway; the other choices are not comparably plausible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the pathway as cell wall/peptidoglycan degradation (C5, H5). The pathway annotation carries experimental evidence code ECO:0000269, and the record names the protein as a peptidoglycan DD-endopeptidase (C4). This supports choice C, though the reviewer evidence does not independently validate the cited study.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a strongly hydrophobic N-terminal segment consistent with a bacterial export signal, followed by a soluble enzyme-sized region with histidine-containing features compatible with a metal-dependent peptidase. Transferable knowledge of bacterial secreted peptidoglycan hydrolases makes cell-wall degradation a credible choice. This fits C better than intracellular protein biosynthesis or metabolic-intermediate biosynthesis, while ajmaline biosynthesis is a specialized plant alkaloid pathway.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide and plausible peptidase features provide a meaningful family-level inference from the sequence and distinguish the offered choices, even though they do not prove the exact substrate or pathway on their own."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cell wall degradation is the best-supported pathway; the other choices are not comparably plausible given the sequence features."
  },
  "important_caveats": [
    "A secretion signal and peptidase-like features are suggestive rather than conclusive from sequence alone.",
    "The source annotation supports the key, but its cited experimental evidence was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9KUL5 (ShyB, Peptidoglycan DD-endopeptidase) explicitly annotates the pathway as 'Cell wall degradation; peptidoglycan degradation' with experimental evidence (ECO:0000269|PubMed:30782657). The protein is an M23-family peptidoglycan endopeptidase that cleaves peptide cross-links in peptidoglycan, consistent with cell wall degradation. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly diagnostic GATGRLTGPHLH motif (residues ~395-406), which is the hallmark signature of the M23 peptidase family (lysostaphin-type peptidases). Additionally, multiple HxxH zinc-binding motifs (e.g., HPYAG, HPVTGRVVPH) are present, confirming a zinc metalloprotease active site. The N-terminal hydrophobic stretch (MGQFRFLALIVAVLCFSVALFLP) is a classic signal peptide indicating secretion, consistent with a cell-wall-targeting enzyme. From transferable knowledge of the M23 family (e.g., lysostaphin from Staphylococcus, other bacterial peptidoglycan endopeptidases), these enzymes cleave the peptide cross-links in peptidoglycan, the principal structural polymer of bacterial cell walls. Among the four options: (A) metabolic intermediate biosynthesis requires biosynthetic enzymes (e.g., dehydrogenases, synthases); (B) ajmaline biosynthesis is a plant monoterpene indole alkaloid pathway irrelevant to a bacterial protein; (D) protein biosynthesis requires ribosomal/translational components. Only (C) cell wall degradation matches a secreted peptidoglycan endopeptidase. The M23 family signature is well-established across many bacterial genomes and is directly transferable knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GATGRLTGPHLH M23-family motif and zinc-binding HxxH motifs are visible in the raw sequence and are well-known signatures of peptidoglycan endopeptidases across the bacterial kingdom. This family-level inference reliably distinguishes 'cell wall degradation' from the other three options without needing to recall the specific ShyB annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The M23 peptidase signature unambiguously points to peptidoglycan/cell wall degradation. The other three options (metabolic intermediate biosynthesis, ajmaline biosynthesis, protein biosynthesis) are mechanistically incompatible with a secreted zinc metalloprotease targeting peptidoglycan cross-links.


### Important caveats

- The UniProt pathway annotation carries experimental evidence code ECO:0000269 (PubMed:30782657), confirming the cell wall degradation assignment is experimentally validated, not merely computational.
- The protein was initially annotated as a 'putative lysostaphin-type peptidase' (PubMed:18498110, 2008 crystal structure) before its specific peptidoglycan endopeptidase function was experimentally confirmed (2013, 2019 papers).
- Option B ('ajmaline biosynthesis. .') contains formatting artifacts (extra period and space) but is clearly a distractor referencing a plant alkaloid pathway irrelevant to a bacterial protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly diagnostic GATGRLTGPHLH motif (residues ~395-406), which is the hallmark signature of the M23 peptidase family (lysostaphin-type peptidases). Additionally, multiple HxxH zinc-binding motifs (e.g., HPYAG, HPVTGRVVPH) are present, confirming a zinc metalloprotease active site. The N-terminal hydrophobic stretch (MGQFRFLALIVAVLCFSVALFLP) is a classic signal peptide indicating secretion, consistent with a cell-wall-targeting enzyme. From transferable knowledge of the M23 family (e.g., lysostaphin from Staphylococcus, other bacterial peptidoglycan endopeptidases), these enzymes cleave the peptide cross-links in peptidoglycan, the principal structural polymer of bacterial cell walls. Among the four options: (A) metabolic intermediate biosynthesis requires biosynthetic enzymes (e.g., dehydrogenases, synthases); (B) ajmaline biosynthesis is a plant monoterpene indole alkaloid pathway irrelevant to a bacterial protein; (D) protein biosynthesis requires ribosomal/translational components. Only (C) cell wall degradation matches a secreted peptidoglycan endopeptidase. The M23 family signature is well-established across many bacterial genomes and is directly transferable knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GATGRLTGPHLH M23-family motif and zinc-binding HxxH motifs are visible in the raw sequence and are well-known signatures of peptidoglycan endopeptidases across the bacterial kingdom. This family-level inference reliably distinguishes 'cell wall degradation' from the other three options without needing to recall the specific ShyB annotation."
  },
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9KUL5 (ShyB, Peptidoglycan DD-endopeptidase) explicitly annotates the pathway as 'Cell wall degradation; peptidoglycan degradation' with experimental evidence (ECO:0000269|PubMed:30782657). The protein is an M23-family peptidoglycan endopeptidase that cleaves peptide cross-links in peptidoglycan, consistent with cell wall degradation. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence code ECO:0000269 (PubMed:30782657), confirming the cell wall degradation assignment is experimentally validated, not merely computational.",
    "The protein was initially annotated as a 'putative lysostaphin-type peptidase' (PubMed:18498110, 2008 crystal structure) before its specific peptidoglycan endopeptidase function was experimentally confirmed (2013, 2019 papers).",
    "Option B ('ajmaline biosynthesis. .') contains formatting artifacts (extra period and space) but is clearly a distractor referencing a plant alkaloid pathway irrelevant to a bacterial protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The M23 peptidase signature unambiguously points to peptidoglycan/cell wall degradation. The other three options (metabolic intermediate biosynthesis, ajmaline biosynthesis, protein biosynthesis) are mechanistically incompatible with a secreted zinc metalloprotease targeting peptidoglycan cross-links."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9KUL5 (ShyB, Peptidoglycan DD-endopeptidase) explicitly annotates the pathway as 'Cell wall degradation; peptidoglycan degradation' with experimental evidence (ECO:0000269|PubMed:30782657). The protein is an M23-family peptidoglycan endopeptidase that cleaves peptide cross-links in peptidoglycan, consistent with cell wall degradation. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H5", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly diagnostic GATGRLTGPHLH motif (residues ~395-406), which is the hallmark signature of the M23 peptidase family (lysostaphin-type peptidases). Additionally, multiple HxxH zinc-binding motifs (e.g., HPYAG, HPVTGRVVPH) are present, confirming a zinc metalloprotease active site. The N-terminal hydrophobic stretch (MGQFRFLALIVAVLCFSVALFLP) is a classic signal peptide indicating secretion, consistent with a cell-wall-targeting enzyme. From transferable knowledge of the M23 family (e.g., lysostaphin from Staphylococcus, other bacterial peptidoglycan endopeptidases), these enzymes cleave the peptide cross-links in peptidoglycan, the principal structural polymer of bacterial cell walls. Among the four options: (A) metabolic intermediate biosynthesis requires biosynthetic enzymes (e.g., dehydrogenases, synthases); (B) ajmaline biosynthesis is a plant monoterpene indole alkaloid pathway irrelevant to a bacterial protein; (D) protein biosynthesis requires ribosomal/translational components. Only (C) cell wall degradation matches a secreted peptidoglycan endopeptidase. The M23 family signature is well-established across many bacterial genomes and is directly transferable knowledge.",
    "missing_item_specific_fact": "",
    "reason": "The GATGRLTGPHLH M23-family motif and zinc-binding HxxH motifs are visible in the raw sequence and are well-known signatures of peptidoglycan endopeptidases across the bacterial kingdom. This family-level inference reliably distinguishes 'cell wall degradation' from the other three options without needing to recall the specific ShyB annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The M23 peptidase signature unambiguously points to peptidoglycan/cell wall degradation. The other three options (metabolic intermediate biosynthesis, ajmaline biosynthesis, protein biosynthesis) are mechanistically incompatible with a secreted zinc metalloprotease targeting peptidoglycan cross-links."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence code ECO:0000269 (PubMed:30782657), confirming the cell wall degradation assignment is experimentally validated, not merely computational.",
    "The protein was initially annotated as a 'putative lysostaphin-type peptidase' (PubMed:18498110, 2008 crystal structure) before its specific peptidoglycan endopeptidase function was experimentally confirmed (2013, 2019 papers).",
    "Option B ('ajmaline biosynthesis. .') contains formatting artifacts (extra period and space) but is clearly a distractor referencing a plant alkaloid pathway irrelevant to a bacterial protein."
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
  "benchmark_sequence_length": 426,
  "benchmark_sequence_sha256": "34584a20856bfb24b4e9d3cd47bf32ba3f960017eb05fdba40f5b8f0c5608054",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 426,
  "current_source_sequence_sha256": "34584a20856bfb24b4e9d3cd47bf32ba3f960017eb05fdba40f5b8f0c5608054",
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
  "requested_accession": "Q9KUL5",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "selected_historical_source_sequence_length": 426,
  "selected_historical_source_sequence_sha256": "34584a20856bfb24b4e9d3cd47bf32ba3f960017eb05fdba40f5b8f0c5608054",
  "selected_historical_version": {
    "accession": "Q9KUL5",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHYB_VIBCH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KUL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF93673.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000584\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Vibrionales\",\"Vibrionaceae\",\"Vibrio\"],\"scientificName\":\"Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)\",\"taxonId\":243277}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Autolysin ShyB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18498110\",\"source\":\"PubMed\"}],\"value\":\"Putative lysostaphin-type peptidase P01\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Sidewall hydrolase B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Peptidoglycan DD-endopeptidase ShyB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Cell wall degradation; peptidoglycan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Doerr T.\",\"Cava F.\",\"Lam H.\",\"Davis B.M.\",\"Waldor M.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23834664\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12323\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"23834664\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"962\",\"publicationDate\":\"2013\",\"title\":\"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.\",\"volume\":\"89\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Murphy S.G.\",\"Alvarez L.\",\"Adams M.C.\",\"Liu S.\",\"Chappie J.S.\",\"Cava F.\",\"Doerr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30782657\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02620-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30782657\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.\",\"volume\":\"10\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-372\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Ragumani S.\",\"Kumaran D.\",\"Burley S.K.\",\"Swaminathan S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18498110\"},{\"database\":\"DOI\",\"id\":\"10.1002/prot.22095\"}],\"citationType\":\"journal article\",\"firstPage\":\"1096\",\"id\":\"18498110\",\"journal\":\"Proteins\",\"lastPage\":\"1103\",\"publicationDate\":\"2008\",\"title\":\"Crystal structure of a putative lysostaphin peptidase from Vibrio cholerae.\",\"volume\":\"72\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"2GU1\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS) OF 63-412 IN COMPLEX WITH ZINC\",\"COFACTOR\",\"SUBUNIT\",\"REACTION MECHANISM\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   SHYB_VIBCH              Reviewed;         426 AA.\nAC   Q9KUL5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=Peptidoglycan DD-endopeptidase ShyB {ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};\nDE   AltName: Full=Autolysin ShyB {ECO:0000303|PubMed:30782657};\nDE   AltName: Full=Putative lysostaphin-type peptidase P01 {ECO:0000303|PubMed:18498110};\nDE   AltName: Full=Sidewall hydrolase B {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\nGN   Name=shyB {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nGN   OrderedLocusNames=VC_0503 {ECO:0000303|PubMed:23834664,\nGN   ECO:0000312|EMBL:AAF93673.1};\nOS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;\nOC   Vibrionaceae; Vibrio.\nOX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF93673.1, ECO:0000312|Proteomes:UP000000584};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};\nRX   PubMed=23834664; DOI=10.1111/mmi.12323;\nRA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;\nRT   \"Substrate specificity of an elongation-specific peptidoglycan\nRT   endopeptidase and its implications for cell wall architecture and growth of\nRT   Vibrio cholerae.\";\nRL   Mol. Microbiol. 89:949-962(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, INDUCTION,\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-372.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};\nRX   PubMed=30782657; DOI=10.1128/mbio.02620-18;\nRA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,\nRA   Doerr T.;\nRT   \"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc\nRT   Starvation Response.\";\nRL   MBio 10:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:2GU1}\nRP   X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS) OF 63-412 IN COMPLEX WITH ZINC,\nRP   COFACTOR, SUBUNIT, AND REACTION MECHANISM.\nRX   PubMed=18498110; DOI=10.1002/prot.22095;\nRA   Ragumani S., Kumaran D., Burley S.K., Swaminathan S.;\nRT   \"Crystal structure of a putative lysostaphin peptidase from Vibrio\nRT   cholerae.\";\nRL   Proteins 72:1096-1103(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Cell wall degradation; peptidoglycan degradation.\nCC       {ECO:0000269|PubMed:30782657}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
