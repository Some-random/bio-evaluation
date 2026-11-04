# EC_number_0165

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0165.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDKKEVQHHRSQQAMTKSLYAIGMGLLGKSATNMDCANTNLESAGKSSSTNYNRNRFYNERFVPMASGTMPSVSGTNHHSRHQQLLLQQAPKCTADLNEKLVKINRQNANKELSTIQAKDMQSVDKNEEALKELQESIPEINKIFDVHCRIGSGTFSTVLLGTLQRERGLVETQRRRFAIKHHNPTNHPERILRELECMYRIGGVENVIGINCCIRYNDNVAFIMPYMTHDRFHDIYRSLNFPEIRDYLRNLLIALRHVHKFNVIHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGSVVQSSDLSSREVFSILRDLENGRSVTLTDGNSAQAEAEDYMARRRMRALGGGGSVERAVTGPPSIQKLREQAGGHLTKKDVANQRADTMRLLNRLRLVSPNADPNNYVVSTNTSKKEMHASRAGTPGYRPPEVLLRYPKQSTAVDVWAAGVIMLSLLSGLHPFFKAPHDCGALAEIINLFGDMPVRKTAFLLDRLILLAQKVNTLDLRRVCMRFRHADFFLAPEIQRKYQRPDGTTEMCRSCEQPTFNCLCSNSGHNLERYDGLDIFPAVAYDLLSRLLEVNPQKRITAEEALKHPFFSDQHRITPGIPLHQQQLIMHQQQHIMQHQQHLQRSRETLPSSAARTLKAFVCYPMEITSTASQAAGNI

[Multiple Choices]
A. 2.7.11.11
B. 1.1.1.138
C. 2.7.11.1
D. 1.3.1.36
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

> The matched sequence is annotated as a non-specific serine/threonine protein kinase with EC 2.7.11.1. The cited support is computational, via a PROSITE-ProRule, rather than direct experimental evidence, so it supports the key without establishing experimental validation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable eukaryotic protein-kinase catalytic region, including the HRD and DFG motifs, supporting a protein Ser/Thr kinase rather than either oxidoreductase choice (B or D). Its long sequence and internal kinase domain are unlike the compact catalytic subunit expected for the cAMP-dependent kinase in A; among the offered kinase choices, the broad protein Ser/Thr kinase classification in C is a credible fit.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable kinase-family and domain-architecture knowledge meaningfully distinguishes C among these alternatives. The motifs alone would not prove the exact EC classification or substrate specificity, but the choices make the broad Ser/Thr kinase option a defensible inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase motifs and sequence architecture favor C over the cAMP-dependent kinase alternative, while B and D are oxidoreductases.


### Important caveats

- The supplied annotation is computationally supported by a PROSITE-ProRule; the evidence shown does not establish experimental characterization of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic region, including the HRD and DFG motifs, supporting a protein Ser/Thr kinase rather than either oxidoreductase choice (B or D). Its long sequence and internal kinase domain are unlike the compact catalytic subunit expected for the cAMP-dependent kinase in A; among the offered kinase choices, the broad protein Ser/Thr kinase classification in C is a credible fit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family and domain-architecture knowledge meaningfully distinguishes C among these alternatives. The motifs alone would not prove the exact EC classification or substrate specificity, but the choices make the broad Ser/Thr kinase option a defensible inference."
  },
  "case_id": "EC_number_0165",
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
    "reason": "The matched sequence is annotated as a non-specific serine/threonine protein kinase with EC 2.7.11.1. The cited support is computational, via a PROSITE-ProRule, rather than direct experimental evidence, so it supports the key without establishing experimental validation."
  },
  "important_caveats": [
    "The supplied annotation is computationally supported by a PROSITE-ProRule; the evidence shown does not establish experimental characterization of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase motifs and sequence architecture favor C over the cAMP-dependent kinase alternative, while B and D are oxidoreductases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a non-specific serine/threonine protein kinase with EC 2.7.11.1. The cited support is computational, via a PROSITE-ProRule, rather than direct experimental evidence, so it supports the key without establishing experimental validation.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic region, including the HRD and DFG motifs, supporting a protein Ser/Thr kinase rather than either oxidoreductase choice (B or D). Its long sequence and internal kinase domain are unlike the compact catalytic subunit expected for the cAMP-dependent kinase in A; among the offered kinase choices, the broad protein Ser/Thr kinase classification in C is a credible fit.",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family and domain-architecture knowledge meaningfully distinguishes C among these alternatives. The motifs alone would not prove the exact EC classification or substrate specificity, but the choices make the broad Ser/Thr kinase option a defensible inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase motifs and sequence architecture favor C over the cAMP-dependent kinase alternative, while B and D are oxidoreductases."
  },
  "important_caveats": [
    "The supplied annotation is computationally supported by a PROSITE-ProRule; the evidence shown does not establish experimental characterization of this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VJ90 (CDC7B_DROME) is annotated with EC 2.7.11.1 (non-specific serine/threonine protein kinase), with catalytic activities for both L-seryl-&#91;protein&#93; and L-threonyl-&#91;protein&#93; phosphorylation by ATP. The evidence code is ECO:0000255 (PROSITE-ProRule), indicating a curated computational inference from sequence motifs rather than direct experimental assay, but the annotation is consistent across multiple fields (protein description, catalytic activity comments). The sequence in the question matches the UniProt entry exactly (665 aa, SHA256 match). The expected answer C is supported by the database record.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple unambiguous protein kinase domain motifs: a glycine-rich loop (GSGTFSTVLLG, GxGxxG pattern), a VAIK-equivalent lysine (FAIK), the catalytic loop HRDVKPSN (HRD...N), the DFG motif (CDFGLAQRI), and an APE-equivalent motif (LAPEIQRKYQRP). These motifs immediately eliminate options B (1.1.1.138, a steroid dehydrogenase) and D (1.3.1.36, dihydroorotate dehydrogenase), which are oxidoreductases with entirely different fold and motif architecture. Between the two remaining kinase options—A (2.7.11.11, tyrosine protein kinase) and C (2.7.11.1, non-specific serine/threonine protein kinase)—the catalytic loop reads 'HRDVKPSN', where the 'KPSN' pattern (catalytic aspartate followed by lysine-proline-serine-asparagine) is the hallmark of the Ser/Thr kinase catalytic loop. Tyrosine kinases share the HRD motif but differ in the substrate-binding pocket and typically have a shorter, more defined activation loop with an autophosphorylatable tyrosine. Here the activation segment following DFG is long and lacks a canonical tyrosine kinase activation-loop tyrosine, and the overall architecture (kinase domain followed by multiple additional regulatory domains including a C-terminal region with poly-Q/QH repeats) matches the CDC7/DRF family of Ser/Thr kinases involved in DNA replication initiation, a well-characterized family of non-specific Ser/Thr protein kinases. Thus, family-level recognition of the CDC7-type kinase domain and the catalytic-loop pattern meaningfully distinguishes C from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The kinase motifs are directly readable from the sequence, eliminating B and D. The Ser/Thr vs Tyr distinction is supported by the catalytic loop pattern (HRDVKPSN), the long activation segment, and the overall multi-domain architecture consistent with the CDC7 family of Ser/Thr kinases—knowledge transferable from other members of that kinase family. This constitutes a credible, concrete inference from the original sequence and general kinase biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are oxidoreductases with no kinase motifs and are clearly eliminated. Between A and C, the catalytic loop pattern and domain architecture favor C (Ser/Thr kinase). While both are protein kinases, the HRDVKPSN catalytic loop and the absence of tyrosine-kinase-specific activation-loop features make C the more defensible choice. The distinction, while requiring kinase-family knowledge, is supported by observable sequence features.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (PROSITE-ProRule), a computational/curated motif-based inference rather than direct experimental enzyme assay. The EC number assignment is therefore a database annotation, not an experimentally verified catalytic measurement.
- Distinguishing EC 2.7.11.1 from EC 2.7.11.11 purely from primary sequence can be subtle; the HRD motif is shared by both Ser/Thr and Tyr kinases. The argument relies on the KPSN catalytic-loop pattern, activation-loop length, and overall domain architecture, which are probabilistic family-level indicators rather than absolute determinants.
- The CDC7 family identity (CDC7B_DROME) is confirmed by the reviewer-only UniProt accession and name, which were not available to the evaluated model. The model must rely on recognizing the kinase domain architecture and catalytic-loop pattern as consistent with a Ser/Thr kinase family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple unambiguous protein kinase domain motifs: a glycine-rich loop (GSGTFSTVLLG, GxGxxG pattern), a VAIK-equivalent lysine (FAIK), the catalytic loop HRDVKPSN (HRD...N), the DFG motif (CDFGLAQRI), and an APE-equivalent motif (LAPEIQRKYQRP). These motifs immediately eliminate options B (1.1.1.138, a steroid dehydrogenase) and D (1.3.1.36, dihydroorotate dehydrogenase), which are oxidoreductases with entirely different fold and motif architecture. Between the two remaining kinase options—A (2.7.11.11, tyrosine protein kinase) and C (2.7.11.1, non-specific serine/threonine protein kinase)—the catalytic loop reads 'HRDVKPSN', where the 'KPSN' pattern (catalytic aspartate followed by lysine-proline-serine-asparagine) is the hallmark of the Ser/Thr kinase catalytic loop. Tyrosine kinases share the HRD motif but differ in the substrate-binding pocket and typically have a shorter, more defined activation loop with an autophosphorylatable tyrosine. Here the activation segment following DFG is long and lacks a canonical tyrosine kinase activation-loop tyrosine, and the overall architecture (kinase domain followed by multiple additional regulatory domains including a C-terminal region with poly-Q/QH repeats) matches the CDC7/DRF family of Ser/Thr kinases involved in DNA replication initiation, a well-characterized family of non-specific Ser/Thr protein kinases. Thus, family-level recognition of the CDC7-type kinase domain and the catalytic-loop pattern meaningfully distinguishes C from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The kinase motifs are directly readable from the sequence, eliminating B and D. The Ser/Thr vs Tyr distinction is supported by the catalytic loop pattern (HRDVKPSN), the long activation segment, and the overall multi-domain architecture consistent with the CDC7 family of Ser/Thr kinases—knowledge transferable from other members of that kinase family. This constitutes a credible, concrete inference from the original sequence and general kinase biology."
  },
  "case_id": "EC_number_0165",
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
    "reason": "The UniProt entry Q9VJ90 (CDC7B_DROME) is annotated with EC 2.7.11.1 (non-specific serine/threonine protein kinase), with catalytic activities for both L-seryl-[protein] and L-threonyl-[protein] phosphorylation by ATP. The evidence code is ECO:0000255 (PROSITE-ProRule), indicating a curated computational inference from sequence motifs rather than direct experimental assay, but the annotation is consistent across multiple fields (protein description, catalytic activity comments). The sequence in the question matches the UniProt entry exactly (665 aa, SHA256 match). The expected answer C is supported by the database record."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (PROSITE-ProRule), a computational/curated motif-based inference rather than direct experimental enzyme assay. The EC number assignment is therefore a database annotation, not an experimentally verified catalytic measurement.",
    "Distinguishing EC 2.7.11.1 from EC 2.7.11.11 purely from primary sequence can be subtle; the HRD motif is shared by both Ser/Thr and Tyr kinases. The argument relies on the KPSN catalytic-loop pattern, activation-loop length, and overall domain architecture, which are probabilistic family-level indicators rather than absolute determinants.",
    "The CDC7 family identity (CDC7B_DROME) is confirmed by the reviewer-only UniProt accession and name, which were not available to the evaluated model. The model must rely on recognizing the kinase domain architecture and catalytic-loop pattern as consistent with a Ser/Thr kinase family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are oxidoreductases with no kinase motifs and are clearly eliminated. Between A and C, the catalytic loop pattern and domain architecture favor C (Ser/Thr kinase). While both are protein kinases, the HRDVKPSN catalytic loop and the absence of tyrosine-kinase-specific activation-loop features make C the more defensible choice. The distinction, while requiring kinase-family knowledge, is supported by observable sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ90 (CDC7B_DROME) is annotated with EC 2.7.11.1 (non-specific serine/threonine protein kinase), with catalytic activities for both L-seryl-[protein] and L-threonyl-[protein] phosphorylation by ATP. The evidence code is ECO:0000255 (PROSITE-ProRule), indicating a curated computational inference from sequence motifs rather than direct experimental assay, but the annotation is consistent across multiple fields (protein description, catalytic activity comments). The sequence in the question matches the UniProt entry exactly (665 aa, SHA256 match). The expected answer C is supported by the database record.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple unambiguous protein kinase domain motifs: a glycine-rich loop (GSGTFSTVLLG, GxGxxG pattern), a VAIK-equivalent lysine (FAIK), the catalytic loop HRDVKPSN (HRD...N), the DFG motif (CDFGLAQRI), and an APE-equivalent motif (LAPEIQRKYQRP). These motifs immediately eliminate options B (1.1.1.138, a steroid dehydrogenase) and D (1.3.1.36, dihydroorotate dehydrogenase), which are oxidoreductases with entirely different fold and motif architecture. Between the two remaining kinase options—A (2.7.11.11, tyrosine protein kinase) and C (2.7.11.1, non-specific serine/threonine protein kinase)—the catalytic loop reads 'HRDVKPSN', where the 'KPSN' pattern (catalytic aspartate followed by lysine-proline-serine-asparagine) is the hallmark of the Ser/Thr kinase catalytic loop. Tyrosine kinases share the HRD motif but differ in the substrate-binding pocket and typically have a shorter, more defined activation loop with an autophosphorylatable tyrosine. Here the activation segment following DFG is long and lacks a canonical tyrosine kinase activation-loop tyrosine, and the overall architecture (kinase domain followed by multiple additional regulatory domains including a C-terminal region with poly-Q/QH repeats) matches the CDC7/DRF family of Ser/Thr kinases involved in DNA replication initiation, a well-characterized family of non-specific Ser/Thr protein kinases. Thus, family-level recognition of the CDC7-type kinase domain and the catalytic-loop pattern meaningfully distinguishes C from A.",
    "missing_item_specific_fact": "",
    "reason": "The kinase motifs are directly readable from the sequence, eliminating B and D. The Ser/Thr vs Tyr distinction is supported by the catalytic loop pattern (HRDVKPSN), the long activation segment, and the overall multi-domain architecture consistent with the CDC7 family of Ser/Thr kinases—knowledge transferable from other members of that kinase family. This constitutes a credible, concrete inference from the original sequence and general kinase biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are oxidoreductases with no kinase motifs and are clearly eliminated. Between A and C, the catalytic loop pattern and domain architecture favor C (Ser/Thr kinase). While both are protein kinases, the HRDVKPSN catalytic loop and the absence of tyrosine-kinase-specific activation-loop features make C the more defensible choice. The distinction, while requiring kinase-family knowledge, is supported by observable sequence features."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (PROSITE-ProRule), a computational/curated motif-based inference rather than direct experimental enzyme assay. The EC number assignment is therefore a database annotation, not an experimentally verified catalytic measurement.",
    "Distinguishing EC 2.7.11.1 from EC 2.7.11.11 purely from primary sequence can be subtle; the HRD motif is shared by both Ser/Thr and Tyr kinases. The argument relies on the KPSN catalytic-loop pattern, activation-loop length, and overall domain architecture, which are probabilistic family-level indicators rather than absolute determinants.",
    "The CDC7 family identity (CDC7B_DROME) is confirmed by the reviewer-only UniProt accession and name, which were not available to the evaluated model. The model must rely on recognizing the kinase domain architecture and catalytic-loop pattern as consistent with a Ser/Thr kinase family."
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
  "benchmark_sequence_length": 665,
  "benchmark_sequence_sha256": "e772503ceee0473a9439108a470ab22fcda9dad41cd55889bd2ac731880b7fbf",
  "current_entry_audit": {
    "entryVersion": 213,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 665,
  "current_source_sequence_sha256": "e772503ceee0473a9439108a470ab22fcda9dad41cd55889bd2ac731880b7fbf",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 211,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VJ90",
  "selected_historical_entry_version": 211,
  "selected_historical_record_sha256": "c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54",
  "selected_historical_source_sequence_length": 665,
  "selected_historical_source_sequence_sha256": "e772503ceee0473a9439108a470ab22fcda9dad41cd55889bd2ac731880b7fbf",
  "selected_historical_version": {
    "accession": "Q9VJ90",
    "database": "Swiss-Prot",
    "entryVersion": 211,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CDC7B_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VJ90\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:29.717422+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ90.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":213,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:29.717422+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ90.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:29.717422+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ90.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0032677\",\"source\":\"FlyBase\"}],\"value\":\"non-specific serine/threonine protein kinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:29.717422+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ90.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17989\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:29.717422+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ90.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46608\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:29.717422+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ90.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)

```json
{
  "entry_version": 211,
  "evidence_id": "H1",
  "excerpt": "ID   CDC7B_DROME             Reviewed;         665 AA.\nAC   Q9VJ90; Q8T0Q5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 211.\nDE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};\nDE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};\nGN   ORFNames=CG5790 {ECO:0000312|FlyBase:FBgn0032677};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:52.103896+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54",
  "url": "https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)

```json
{
  "entry_version": 211,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};\nDE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:52.103896+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54",
  "url": "https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)

```json
{
  "entry_version": 211,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +\nCC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:52.103896+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54",
  "url": "https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)

```json
{
  "entry_version": 211,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +\nCC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:52.103896+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54",
  "url": "https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 165. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
