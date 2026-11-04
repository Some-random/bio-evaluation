# pathway_0061

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0061.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVVERDSDYYDSSYLADYYESLWTDHAALEDIAVYWAFFKERVLLSQSRVDSKFFLLDVGTGTGRVLHSLIDKAVNDADMSLDAMQFVGMDKSPFMLEQAQRAKQLPQEVRASWFVGTATALEDIASLADPHGKANLLIFAFSGINHLHQPGEIDQFFLSARRVLLPGGLALVSVCAPLLDIEGGDSVPNPYGQVKEVKSKRLEGILYREWETGQKIEGHLFTNSLKTDVVQVSQDGSERVIERNIHNIPLTLLTRDGLRRSAAAAKLEIIEERCIRDEVIFALRAVG

[Multiple Choices]
A. L-homoserine from L-aspartate: step 1/3. .
B. L-valine biosynthesis
C. L-isoleucine from 2-oxobutanoate: step 3/4. .
D. Secondary metabolite biosynthesis. .
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

> The sequence-matched UniProt record annotates the protein's pathway as secondary metabolite biosynthesis, citing experimental evidence (ECO:0000269). The record also identifies it as an N-methyltransferase. This supports the keyed choice, though the cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 289 amino acids long and contains a glycine-rich segment around DVGTGTG, consistent with a possible SAM-dependent methyltransferase fold. A methyltransferase-like enzyme is a better fit for secondary-metabolite biosynthesis than the listed steps in homoserine, valine, or isoleucine biosynthesis, which are generally catalyzed by other enzyme families. This supports D probabilistically without identifying the exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence feature and transferable enzyme-family knowledge provide a meaningful distinction among the offered choices. The inference is not a definitive family assignment from the sequence alone, but the choices do not require one.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered pathway is comparably supported by the sequence-level methyltransferase-like inference.


### Important caveats

- The sequence motif-based family inference is suggestive rather than conclusive.
- The reviewer-only database annotation supports the key but was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 289 amino acids long and contains a glycine-rich segment around DVGTGTG, consistent with a possible SAM-dependent methyltransferase fold. A methyltransferase-like enzyme is a better fit for secondary-metabolite biosynthesis than the listed steps in homoserine, valine, or isoleucine biosynthesis, which are generally catalyzed by other enzyme families. This supports D probabilistically without identifying the exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence feature and transferable enzyme-family knowledge provide a meaningful distinction among the offered choices. The inference is not a definitive family assignment from the sequence alone, but the choices do not require one."
  },
  "case_id": "pathway_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein's pathway as secondary metabolite biosynthesis, citing experimental evidence (ECO:0000269). The record also identifies it as an N-methyltransferase. This supports the keyed choice, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence motif-based family inference is suggestive rather than conclusive.",
    "The reviewer-only database annotation supports the key but was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered pathway is comparably supported by the sequence-level methyltransferase-like inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein's pathway as secondary metabolite biosynthesis, citing experimental evidence (ECO:0000269). The record also identifies it as an N-methyltransferase. This supports the keyed choice, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 289 amino acids long and contains a glycine-rich segment around DVGTGTG, consistent with a possible SAM-dependent methyltransferase fold. A methyltransferase-like enzyme is a better fit for secondary-metabolite biosynthesis than the listed steps in homoserine, valine, or isoleucine biosynthesis, which are generally catalyzed by other enzyme families. This supports D probabilistically without identifying the exact protein.",
    "missing_item_specific_fact": "",
    "reason": "The sequence feature and transferable enzyme-family knowledge provide a meaningful distinction among the offered choices. The inference is not a definitive family assignment from the sequence alone, but the choices do not require one."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered pathway is comparably supported by the sequence-level methyltransferase-like inference."
  },
  "important_caveats": [
    "The sequence motif-based family inference is suggestive rather than conclusive.",
    "The reviewer-only database annotation supports the key but was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8F1L3) annotates this protein as N-methyltransferase FrzE (EC 2.1.1.-), a component of the FR901483 biosynthesis cluster, with pathway explicitly stated as 'Secondary metabolite biosynthesis' under evidence code ECO:0000269 (experimental, PubMed:33372776). The sequence matches exactly (289 AA, SHA256 match). This directly supports choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence (approximately residues 195-289) contains hallmark motifs of a Class I SAM-dependent methyltransferase fold: the 'REWI…GQ…GHLF…TNS…DGS…ERNI' pattern (specifically GILYREWETGQKIEGHLFTNSLKTDVVQVSQDGSERVIERNIHNIPLTLLTRDGLRRSAAAAKLEIIEERCIRDEVIFALRAVG). The N-terminal region also shows a classic Rossmann-fold NAD(P)-binding motif (DVGTGTGRVLHS, GxGxG pattern). A knowledgeable model can reason: (1) Methyltransferases are NOT components of standard amino acid biosynthesis pathways — aspartate kinase (A), valine biosynthesis enzymes (B, e.g., acetohydroxyacid synthase, dihydroxy-acid dehydratase), and isoleucine biosynthesis enzymes (C, e.g., branched-chain aminotransferase) use kinases, dehydratases, transaminases, and dehydrogenases, never SAM-dependent methyltransferases. (2) Methyltransferases are extremely common in secondary metabolite biosynthesis gene clusters, where methylation is a standard tailoring/modification step. (3) The dual-domain architecture (NAD(P)H-binding Rossmann fold + SAM methyltransferase) is a well-known configuration in secondary metabolite cluster enzymes. Therefore, the presence of a methyltransferase domain effectively rules out A, B, and C while pointing to D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The methyltransferase fold is a well-recognized protein family identifiable from sequence motifs (GHLF, DGS, REWI patterns). The biochemical principle that standard amino acid biosynthesis (choices A, B, C) does not involve methyltransferases is general pathway knowledge. The association of methyltransferases with secondary metabolite tailoring is a widely established pattern across many natural product biosynthesis clusters. This constitutes a concrete, transferable inference from protein family recognition and pathway biochemistry that meaningfully distinguishes D from the amino acid biosynthesis distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The methyltransferase domain clearly excludes standard amino acid biosynthesis pathways (A, B, C), which do not employ SAM-dependent methyltransferases. Only D (secondary metabolite biosynthesis) is consistent with the observed protein architecture.


### Important caveats

- The N-terminal Rossmann fold (DVGTGTGRVLHS) could superficially resemble NAD(P)-dependent reductases found in some amino acid pathways, but the C-terminal methyltransferase domain definitively excludes that interpretation.
- The reviewer-only evidence confirms experimental pathway assignment (ECO:0000269), but the evaluated model only had the sequence and choices; the reasoning relies on protein family recognition and general pathway biochemistry.
- FR901483 is a specific immunosuppressant secondary metabolite; the model need not know this specific compound, only the general principle that methyltransferases are hallmarks of secondary metabolite tailoring rather than primary amino acid biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence (approximately residues 195-289) contains hallmark motifs of a Class I SAM-dependent methyltransferase fold: the 'REWI…GQ…GHLF…TNS…DGS…ERNI' pattern (specifically GILYREWETGQKIEGHLFTNSLKTDVVQVSQDGSERVIERNIHNIPLTLLTRDGLRRSAAAAKLEIIEERCIRDEVIFALRAVG). The N-terminal region also shows a classic Rossmann-fold NAD(P)-binding motif (DVGTGTGRVLHS, GxGxG pattern). A knowledgeable model can reason: (1) Methyltransferases are NOT components of standard amino acid biosynthesis pathways — aspartate kinase (A), valine biosynthesis enzymes (B, e.g., acetohydroxyacid synthase, dihydroxy-acid dehydratase), and isoleucine biosynthesis enzymes (C, e.g., branched-chain aminotransferase) use kinases, dehydratases, transaminases, and dehydrogenases, never SAM-dependent methyltransferases. (2) Methyltransferases are extremely common in secondary metabolite biosynthesis gene clusters, where methylation is a standard tailoring/modification step. (3) The dual-domain architecture (NAD(P)H-binding Rossmann fold + SAM methyltransferase) is a well-known configuration in secondary metabolite cluster enzymes. Therefore, the presence of a methyltransferase domain effectively rules out A, B, and C while pointing to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The methyltransferase fold is a well-recognized protein family identifiable from sequence motifs (GHLF, DGS, REWI patterns). The biochemical principle that standard amino acid biosynthesis (choices A, B, C) does not involve methyltransferases is general pathway knowledge. The association of methyltransferases with secondary metabolite tailoring is a widely established pattern across many natural product biosynthesis clusters. This constitutes a concrete, transferable inference from protein family recognition and pathway biochemistry that meaningfully distinguishes D from the amino acid biosynthesis distractors."
  },
  "case_id": "pathway_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1L3) annotates this protein as N-methyltransferase FrzE (EC 2.1.1.-), a component of the FR901483 biosynthesis cluster, with pathway explicitly stated as 'Secondary metabolite biosynthesis' under evidence code ECO:0000269 (experimental, PubMed:33372776). The sequence matches exactly (289 AA, SHA256 match). This directly supports choice D."
  },
  "important_caveats": [
    "The N-terminal Rossmann fold (DVGTGTGRVLHS) could superficially resemble NAD(P)-dependent reductases found in some amino acid pathways, but the C-terminal methyltransferase domain definitively excludes that interpretation.",
    "The reviewer-only evidence confirms experimental pathway assignment (ECO:0000269), but the evaluated model only had the sequence and choices; the reasoning relies on protein family recognition and general pathway biochemistry.",
    "FR901483 is a specific immunosuppressant secondary metabolite; the model need not know this specific compound, only the general principle that methyltransferases are hallmarks of secondary metabolite tailoring rather than primary amino acid biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The methyltransferase domain clearly excludes standard amino acid biosynthesis pathways (A, B, C), which do not employ SAM-dependent methyltransferases. Only D (secondary metabolite biosynthesis) is consistent with the observed protein architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1L3) annotates this protein as N-methyltransferase FrzE (EC 2.1.1.-), a component of the FR901483 biosynthesis cluster, with pathway explicitly stated as 'Secondary metabolite biosynthesis' under evidence code ECO:0000269 (experimental, PubMed:33372776). The sequence matches exactly (289 AA, SHA256 match). This directly supports choice D.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence (approximately residues 195-289) contains hallmark motifs of a Class I SAM-dependent methyltransferase fold: the 'REWI…GQ…GHLF…TNS…DGS…ERNI' pattern (specifically GILYREWETGQKIEGHLFTNSLKTDVVQVSQDGSERVIERNIHNIPLTLLTRDGLRRSAAAAKLEIIEERCIRDEVIFALRAVG). The N-terminal region also shows a classic Rossmann-fold NAD(P)-binding motif (DVGTGTGRVLHS, GxGxG pattern). A knowledgeable model can reason: (1) Methyltransferases are NOT components of standard amino acid biosynthesis pathways — aspartate kinase (A), valine biosynthesis enzymes (B, e.g., acetohydroxyacid synthase, dihydroxy-acid dehydratase), and isoleucine biosynthesis enzymes (C, e.g., branched-chain aminotransferase) use kinases, dehydratases, transaminases, and dehydrogenases, never SAM-dependent methyltransferases. (2) Methyltransferases are extremely common in secondary metabolite biosynthesis gene clusters, where methylation is a standard tailoring/modification step. (3) The dual-domain architecture (NAD(P)H-binding Rossmann fold + SAM methyltransferase) is a well-known configuration in secondary metabolite cluster enzymes. Therefore, the presence of a methyltransferase domain effectively rules out A, B, and C while pointing to D.",
    "missing_item_specific_fact": "",
    "reason": "The methyltransferase fold is a well-recognized protein family identifiable from sequence motifs (GHLF, DGS, REWI patterns). The biochemical principle that standard amino acid biosynthesis (choices A, B, C) does not involve methyltransferases is general pathway knowledge. The association of methyltransferases with secondary metabolite tailoring is a widely established pattern across many natural product biosynthesis clusters. This constitutes a concrete, transferable inference from protein family recognition and pathway biochemistry that meaningfully distinguishes D from the amino acid biosynthesis distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The methyltransferase domain clearly excludes standard amino acid biosynthesis pathways (A, B, C), which do not employ SAM-dependent methyltransferases. Only D (secondary metabolite biosynthesis) is consistent with the observed protein architecture."
  },
  "important_caveats": [
    "The N-terminal Rossmann fold (DVGTGTGRVLHS) could superficially resemble NAD(P)-dependent reductases found in some amino acid pathways, but the C-terminal methyltransferase domain definitively excludes that interpretation.",
    "The reviewer-only evidence confirms experimental pathway assignment (ECO:0000269), but the evaluated model only had the sequence and choices; the reasoning relies on protein family recognition and general pathway biochemistry.",
    "FR901483 is a specific immunosuppressant secondary metabolite; the model need not know this specific compound, only the general principle that methyltransferases are hallmarks of secondary metabolite tailoring rather than primary amino acid biosynthesis."
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
  "benchmark_sequence_length": 289,
  "benchmark_sequence_sha256": "ac16c3877a03a11f2374eb7829d8849eaaf1341f6b4a54416145c28c6bfae31d",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 289,
  "current_source_sequence_sha256": "ac16c3877a03a11f2374eb7829d8849eaaf1341f6b4a54416145c28c6bfae31d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 11,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1L3",
  "selected_historical_entry_version": 11,
  "selected_historical_record_sha256": "02a95973abcefb95c240893b88e697665cd99234a9c35783731b0c3171f26890",
  "selected_historical_source_sequence_length": 289,
  "selected_historical_source_sequence_sha256": "ac16c3877a03a11f2374eb7829d8849eaaf1341f6b4a54416145c28c6bfae31d",
  "selected_historical_version": {
    "accession": "A0A7T8F1L3",
    "database": "Swiss-Prot",
    "entryVersion": 11,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZE_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1L3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:48.298817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:48.298817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:48.298817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein E\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"N-methyltransferase FrzE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:48.298817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:48.298817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:48.298817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8bf8f6b54a22924ce3e29b7871caafa0c559fc8abe3d986ff31d11379636d5a4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L3?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H1",
  "excerpt": "ID   FRZE_CLASX              Reviewed;         289 AA.\nAC   A0A7T8F1L3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 11.\nDE   RecName: Full=N-methyltransferase FrzE {ECO:0000303|PubMed:33372776};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein E {ECO:0000303|PubMed:33372776};\nGN   Name=FrzE {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.153846+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02a95973abcefb95c240893b88e697665cd99234a9c35783731b0c3171f26890",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L3?format=txt&versions=11"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L3?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.153846+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02a95973abcefb95c240893b88e697665cd99234a9c35783731b0c3171f26890",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L3?format=txt&versions=11"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L3?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.153846+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02a95973abcefb95c240893b88e697665cd99234a9c35783731b0c3171f26890",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L3?format=txt&versions=11"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
