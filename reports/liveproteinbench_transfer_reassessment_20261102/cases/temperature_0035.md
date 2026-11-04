# temperature_0035

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0035.txt)

**Task:** `temperature`  
**Expected answer:** **B** — 40

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKSLIGTLGLYCLFILTNNVVSSYGDDLYPLTIMHTNDFHARFEETNVKGNPCKSGEKCIGGLARVLHTIKKIIKEQEKKNIESLYINAGDNFQGTIWYNIGRWNVTSELMNIQPPDVMVLGNHEFDHGIDGLLPFLNNMDKTEIVVANMDARDEPQVAKKIKPFTIIKKKYRNIGVIGVVVEEVPDLANTGKLKFRNESEAILEAARNLKKEDPSVNIIIVVSHVGFDVDKIIAERTGSEVDIIVGGHSHTVLYTGTPPGPEKPEDNYPYVYNHPSGNKVLVVQAVCHAKYVGNLTVFFDKKGKVVTYEGAPIYMDTKVEQDKDVLEAMKPWRKLIDEKTKLVVGRTNVDLPRDICRSEECALGNLYTDSMIYAFGGKENCKSGSTWTTAPIAFVHAGAMRSSLHQGDILYSDALLLSPFTNMVVAYDLPGAQLKAALEFSAAPKNEDEKRRFLQMSGLKVTYNMSRAANNRIVDLKVRTNVCPYDQYENLDEKKTYRVVSPSFLQGGGDGFKMLRDYAKNIQNQKIDLDALVDYLKKFSPLAPKAEGRITIIH

[Multiple Choices]
A. 23-32
B. 40
C. 37
D. 49
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The sequence-matched record reports an optimum temperature of 40°C, citing experimental evidence (ECO:0000269). This supports choice B.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The measured optimum temperature of this particular protein is needed to distinguish 40°C from the nearby offered values; the sequence does not establish that precise optimum.


**Reason**

> Sequence and transferable biological knowledge might suggest a broad thermal range, but do not provide a meaningful basis for choosing among 37°C, 40°C, and 49°C for this protein. The distinction depends on its protein-specific temperature optimum.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied experimental annotation identifies 40°C as the optimum, matching one option.


### Important caveats

- The supporting database annotation cites experimental evidence, but the underlying paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured optimum temperature of this particular protein is needed to distinguish 40°C from the nearby offered values; the sequence does not establish that precise optimum.",
    "reason": "Sequence and transferable biological knowledge might suggest a broad thermal range, but do not provide a meaningful basis for choosing among 37°C, 40°C, and 49°C for this protein. The distinction depends on its protein-specific temperature optimum."
  },
  "case_id": "temperature_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports an optimum temperature of 40°C, citing experimental evidence (ECO:0000269). This supports choice B."
  },
  "important_caveats": [
    "The supporting database annotation cites experimental evidence, but the underlying paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation identifies 40°C as the optimum, matching one option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports an optimum temperature of 40°C, citing experimental evidence (ECO:0000269). This supports choice B.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The measured optimum temperature of this particular protein is needed to distinguish 40°C from the nearby offered values; the sequence does not establish that precise optimum.",
    "reason": "Sequence and transferable biological knowledge might suggest a broad thermal range, but do not provide a meaningful basis for choosing among 37°C, 40°C, and 49°C for this protein. The distinction depends on its protein-specific temperature optimum."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation identifies 40°C as the optimum, matching one option."
  },
  "important_caveats": [
    "The supporting database annotation cites experimental evidence, but the underlying paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q95P65 explicitly states 'Optimum temperature is 40 degrees Celsius. Active from 20 to 47 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:20351782). The sequence matches exactly (555 AA, SHA256 confirmed). The expected answer B (40) is directly supported by the experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific experimentally measured optimum temperature of 40°C for this particular 5'-nucleotidase-related salivary protein from Glossina morsitans morsitans (PubMed:20351782). The choices 37, 40, and 49 are all within the mesophilic range and differ by only a few degrees. No sequence-composition feature, family-level thermal preference, or general biological principle reliably distinguishes 40°C from 37°C or 49°C for this protein. While one might eliminate very cold (23-32 as a range suggesting psychrophily) or very hot categories, the fine distinction among three close mesophilic values requires the specific experimental measurement.


**Reason**

> The three main competing choices (37, 40, 49) are all within the mesophilic temperature range, separated by only a few degrees. From the 555-aa sequence alone, without knowing the organism, protein family, or function, no transferable feature (amino acid composition, charge distribution, proline/glycine content, etc.) reliably distinguishes an optimum of 40°C from 37°C or 49°C. Even if one recognized it as an insect salivary protein (encountering ~37°C host blood), the measured optimum being 40°C rather than 37°C is a specific experimental finding. The protein family (5'-nucleotidase-related) does not carry a strong family-level thermal preference that would select 40 over 37 or 49. The answer requires recalling the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C",
  "D"
]
```

> Without the specific experimental measurement, choices B (40), C (37), and D (49) are all plausible mesophilic optima for a secreted insect salivary enzyme. A model reasoning from general biology might argue for 37°C (host body temperature for a salivary protein) or 40°C (slightly elevated, common for insect enzymes) or even 49°C (warm mesophilic). The sequence alone does not provide a basis to confidently select among these three close values.


### Important caveats

- The UniProt annotation reports a single experimental measurement from one study (Caljon et al., 2010, PLoS ONE). The activity range is 20-47°C, so the protein is functional across a broad range.
- The protein is a salivary protein from a blood-feeding insect (tsetse fly), which encounters mammalian host blood at ~37°C. The measured optimum of 40°C is slightly above this, which is a specific experimental observation not trivially predictable.
- Choice A (23-32) is formatted as a range rather than a single value, which is inconsistent with the other options and the question format asking for a category/optimum.
- The reviewer-only evidence confirms the sequence matches Q95P65 exactly, but this identification was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimentally measured optimum temperature of 40°C for this particular 5'-nucleotidase-related salivary protein from Glossina morsitans morsitans (PubMed:20351782). The choices 37, 40, and 49 are all within the mesophilic range and differ by only a few degrees. No sequence-composition feature, family-level thermal preference, or general biological principle reliably distinguishes 40°C from 37°C or 49°C for this protein. While one might eliminate very cold (23-32 as a range suggesting psychrophily) or very hot categories, the fine distinction among three close mesophilic values requires the specific experimental measurement.",
    "reason": "The three main competing choices (37, 40, 49) are all within the mesophilic temperature range, separated by only a few degrees. From the 555-aa sequence alone, without knowing the organism, protein family, or function, no transferable feature (amino acid composition, charge distribution, proline/glycine content, etc.) reliably distinguishes an optimum of 40°C from 37°C or 49°C. Even if one recognized it as an insect salivary protein (encountering ~37°C host blood), the measured optimum being 40°C rather than 37°C is a specific experimental finding. The protein family (5'-nucleotidase-related) does not carry a strong family-level thermal preference that would select 40 over 37 or 49. The answer requires recalling the specific UniProt annotation for this exact protein."
  },
  "case_id": "temperature_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q95P65 explicitly states 'Optimum temperature is 40 degrees Celsius. Active from 20 to 47 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:20351782). The sequence matches exactly (555 AA, SHA256 confirmed). The expected answer B (40) is directly supported by the experimental measurement."
  },
  "important_caveats": [
    "The UniProt annotation reports a single experimental measurement from one study (Caljon et al., 2010, PLoS ONE). The activity range is 20-47°C, so the protein is functional across a broad range.",
    "The protein is a salivary protein from a blood-feeding insect (tsetse fly), which encounters mammalian host blood at ~37°C. The measured optimum of 40°C is slightly above this, which is a specific experimental observation not trivially predictable.",
    "Choice A (23-32) is formatted as a range rather than a single value, which is inconsistent with the other options and the question format asking for a category/optimum.",
    "The reviewer-only evidence confirms the sequence matches Q95P65 exactly, but this identification was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C",
      "D"
    ],
    "reason": "Without the specific experimental measurement, choices B (40), C (37), and D (49) are all plausible mesophilic optima for a secreted insect salivary enzyme. A model reasoning from general biology might argue for 37°C (host body temperature for a salivary protein) or 40°C (slightly elevated, common for insect enzymes) or even 49°C (warm mesophilic). The sequence alone does not provide a basis to confidently select among these three close values."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q95P65 explicitly states 'Optimum temperature is 40 degrees Celsius. Active from 20 to 47 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:20351782). The sequence matches exactly (555 AA, SHA256 confirmed). The expected answer B (40) is directly supported by the experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific experimentally measured optimum temperature of 40°C for this particular 5'-nucleotidase-related salivary protein from Glossina morsitans morsitans (PubMed:20351782). The choices 37, 40, and 49 are all within the mesophilic range and differ by only a few degrees. No sequence-composition feature, family-level thermal preference, or general biological principle reliably distinguishes 40°C from 37°C or 49°C for this protein. While one might eliminate very cold (23-32 as a range suggesting psychrophily) or very hot categories, the fine distinction among three close mesophilic values requires the specific experimental measurement.",
    "reason": "The three main competing choices (37, 40, 49) are all within the mesophilic temperature range, separated by only a few degrees. From the 555-aa sequence alone, without knowing the organism, protein family, or function, no transferable feature (amino acid composition, charge distribution, proline/glycine content, etc.) reliably distinguishes an optimum of 40°C from 37°C or 49°C. Even if one recognized it as an insect salivary protein (encountering ~37°C host blood), the measured optimum being 40°C rather than 37°C is a specific experimental finding. The protein family (5'-nucleotidase-related) does not carry a strong family-level thermal preference that would select 40 over 37 or 49. The answer requires recalling the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C", "D"],
    "reason": "Without the specific experimental measurement, choices B (40), C (37), and D (49) are all plausible mesophilic optima for a secreted insect salivary enzyme. A model reasoning from general biology might argue for 37°C (host body temperature for a salivary protein) or 40°C (slightly elevated, common for insect enzymes) or even 49°C (warm mesophilic). The sequence alone does not provide a basis to confidently select among these three close values."
  },
  "important_caveats": [
    "The UniProt annotation reports a single experimental measurement from one study (Caljon et al., 2010, PLoS ONE). The activity range is 20-47°C, so the protein is functional across a broad range.",
    "The protein is a salivary protein from a blood-feeding insect (tsetse fly), which encounters mammalian host blood at ~37°C. The measured optimum of 40°C is slightly above this, which is a specific experimental observation not trivially predictable.",
    "Choice A (23-32) is formatted as a range rather than a single value, which is inconsistent with the other options and the question format asking for a category/optimum.",
    "The reviewer-only evidence confirms the sequence matches Q95P65 exactly, but this identification was not available to the evaluated model."
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
  "benchmark_sequence_length": 555,
  "benchmark_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 555,
  "current_source_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q95P65",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "selected_historical_source_sequence_length": 555,
  "selected_historical_source_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "selected_historical_version": {
    "accession": "Q95P65",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "APY_GLOMM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q95P65\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Savannah tsetse fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAK63848.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Hippoboscoidea\",\"Glossinidae\",\"Glossina\"],\"scientificName\":\"Glossina morsitans morsitans\",\"taxonId\":37546}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"3.6.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"5'-nucleotidase-related protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"5'Nuc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with ATP as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":684.0},{\"enzyme\":\"enzyme with ADP as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":177.0}],\"michaelisConstants\":[{\"constant\":43.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"substrate\":\"ATP\",\"unit\":\"uM\"},{\"constant\":49.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"substrate\":\"ADP\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"kcat is 48.9 min(-1) with ATP as substrate. kcat is 12.7 min(-1) with ADP as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 8.0.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 40 degrees Celsius. Active from 20 to 47 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Caljon G.\",\"De Ridder K.\",\"De Baetselier P.\",\"Coosemans M.\",\"Van Den Abbeele J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20351782\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0009671\"}],\"citationType\":\"journal article\",\"firstPage\":\"e9671\",\"id\":\"20351782\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e9671\",\"publicationDate\":\"2010\",\"title\":\"Identification of a tsetse fly salivary protein with dual inhibitory action on human platelet aggregation.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   APY_GLOMM               Reviewed;         555 AA.\nAC   Q95P65; D3TRV7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=5'-nucleotidase-related protein {ECO:0000303|PubMed:20351782};\nDE            Short=5'Nuc {ECO:0000303|PubMed:20351782};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:20351782};\nDE   Flags: Precursor;\nOS   Glossina morsitans morsitans (Savannah tsetse fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Hippoboscoidea;\nOC   Glossinidae; Glossina.\nOX   NCBI_TaxID=37546 {ECO:0000312|EMBL:AAK63848.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   AND DISRUPTION PHENOTYPE.\nRX   PubMed=20351782; DOI=10.1371/journal.pone.0009671;\nRA   Caljon G., De Ridder K., De Baetselier P., Coosemans M.,\nRA   Van Den Abbeele J.;\nRT   \"Identification of a tsetse fly salivary protein with dual inhibitory\nRT   action on human platelet aggregation.\";\nRL   PLoS ONE 5:e9671-e9671(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=43 uM for ATP {ECO:0000269|PubMed:20351782};\nCC         KM=49 uM for ADP {ECO:0000269|PubMed:20351782};\nCC         Vmax=684 nmol/min/mg enzyme with ATP as substrate\nCC         {ECO:0000269|PubMed:20351782};\nCC         Vmax=177 nmol/min/mg enzyme with ADP as substrate\nCC         {ECO:0000269|PubMed:20351782};\nCC         Note=kcat is 48.9 min(-1) with ATP as substrate. kcat is 12.7 min(-1)\nCC         with ADP as substrate. {ECO:0000269|PubMed:20351782};\nCC       pH dependence:\nCC         Optimum pH is 8.0. {ECO:0000269|PubMed:20351782};\nCC       Temperature dependence:\nCC         Optimum temperature is 40 degrees Celsius. Active from 20 to 47\nCC         degrees Celsius. {ECO:0000269|PubMed:20351782};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
