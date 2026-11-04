# pathway_0128

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0128.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPILQRISKTFIKPSSPTPESLRCYNLSSSDQMITSVYISLAFFYGSPGCESSRIRQQLDNSLSRTLVYYYPFAGRLVDNDHIDCNDQGVQFVEVRIHCPISAILKQTTSYAEDLVFPRGTSACHEDSLVVVQLNRFECGGVAIAVCISHKVADGSGAIAFINDWAATARVSSHIPSPLLVADSIFPHLDNSLPVPYNLSKNCVTRRFVFPAAEIEKLKSKAVESGLQQPTRVEVVTALLYQCALLASRSTNSGLSRPSVLIQAVNLRPFLVPPLPRNSVGNIFSINFSIIEVDSLEFPELAGRLRKAKLKFQNLSQEKLYYDSQMQELGECLKQLNTGNFDVYYCSSWCRFPVYDVDFGWGKPTWVCTVKSQIKDMIVLMDSPGDEIAAFVTLEEEKMSAFQHNELLLSFASLYSAK

[Multiple Choices]
A. tetrahydrofolate biosynthesis
B. coenzyme A biosynthesis
C. ajmaline biosynthesis. .
D. Alkaloid biosynthesis. .
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

> A sequence-matched UniProt record annotates the protein's pathway as alkaloid biosynthesis and cites a publication with experimental evidence. This supports D; the evidence is an annotation tied to a cited study, not an independent review of that study.

Citations as saved: [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's DFGWG motif is consistent with the plant BAHD acyltransferase family, whose members commonly participate in specialized-metabolite biosynthesis. That provides a transferable reason to favor alkaloid biosynthesis over tetrahydrofolate or coenzyme A biosynthesis, but BAHD family membership does not identify the particular alkaloid pathway.


**Missing item-specific fact**

> The target's substrate or specific pathway assignment is needed to distinguish broad alkaloid biosynthesis from the offered ajmaline-biosynthesis alternative.


**Reason**

> Family-level sequence evidence supports a broad specialized-metabolism inference, but does not meaningfully resolve the specific alkaloid-pathway choice. The exact pathway annotation is target-specific and absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broad alkaloid option and the ajmaline-specific option overlap conceptually, but the supplied sequence and reviewer evidence do not establish that this protein functions in ajmaline biosynthesis.


### Important caveats

- The reviewer-only records match the supplied sequence; their identity and annotations were not available to the evaluated model.
- The cited experimental evidence supports the database pathway annotation, but the underlying publication was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's DFGWG motif is consistent with the plant BAHD acyltransferase family, whose members commonly participate in specialized-metabolite biosynthesis. That provides a transferable reason to favor alkaloid biosynthesis over tetrahydrofolate or coenzyme A biosynthesis, but BAHD family membership does not identify the particular alkaloid pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target's substrate or specific pathway assignment is needed to distinguish broad alkaloid biosynthesis from the offered ajmaline-biosynthesis alternative.",
    "reason": "Family-level sequence evidence supports a broad specialized-metabolism inference, but does not meaningfully resolve the specific alkaloid-pathway choice. The exact pathway annotation is target-specific and absent from the original input."
  },
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "A sequence-matched UniProt record annotates the protein's pathway as alkaloid biosynthesis and cites a publication with experimental evidence. This supports D; the evidence is an annotation tied to a cited study, not an independent review of that study."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence; their identity and annotations were not available to the evaluated model.",
    "The cited experimental evidence supports the database pathway annotation, but the underlying publication was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad alkaloid option and the ajmaline-specific option overlap conceptually, but the supplied sequence and reviewer evidence do not establish that this protein functions in ajmaline biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "A sequence-matched UniProt record annotates the protein's pathway as alkaloid biosynthesis and cites a publication with experimental evidence. This supports D; the evidence is an annotation tied to a cited study, not an independent review of that study.",
    "evidence_ids": ["H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's DFGWG motif is consistent with the plant BAHD acyltransferase family, whose members commonly participate in specialized-metabolite biosynthesis. That provides a transferable reason to favor alkaloid biosynthesis over tetrahydrofolate or coenzyme A biosynthesis, but BAHD family membership does not identify the particular alkaloid pathway.",
    "missing_item_specific_fact": "The target's substrate or specific pathway assignment is needed to distinguish broad alkaloid biosynthesis from the offered ajmaline-biosynthesis alternative.",
    "reason": "Family-level sequence evidence supports a broad specialized-metabolism inference, but does not meaningfully resolve the specific alkaloid-pathway choice. The exact pathway annotation is target-specific and absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad alkaloid option and the ajmaline-specific option overlap conceptually, but the supplied sequence and reviewer evidence do not establish that this protein functions in ajmaline biosynthesis."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence; their identity and annotations were not available to the evaluated model.",
    "The cited experimental evidence supports the database pathway annotation, but the underlying publication was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9E7S5E3) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269|PubMed:36349266). The protein is Akuammiline synthase 1 (EC 2.3.1.322), a BAHD acyltransferase involved in monoterpenoid indole alkaloid (MIA) biosynthesis in Alstonia scholaris. The evidence excerpt C5/H3 directly states 'PATHWAY: Alkaloid biosynthesis.' The answer D matches the recorded annotation exactly.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable HxxDG motif ('ISHKVADG' region), which is the hallmark catalytic signature of the BAHD acyltransferase superfamily. From general knowledge of plant secondary metabolism, BAHD acyltransferases are well-known participants in alkaloid biosynthesis pathways (e.g., in vinblastine, akuammiline, and other MIA branches), but are not key enzymes in tetrahydrofolate biosynthesis (GTP cyclohydrolase I, dihydroneopterin aldolase) or coenzyme A biosynthesis (pantothenate kinase, phosphopantothenoylcysteine synthetase). This eliminates A and B. Between C (ajmaline biosynthesis) and D (Alkaloid biosynthesis): ajmaline biosynthesis is a highly specific MIA sub-pathway whose key cyclization enzyme (ajmaline synthase) is a terpene cyclase-type enzyme, not a BAHD acyltransferase. The BAHD acyltransferase family is broadly associated with multiple MIA branches and is annotated under the general 'Alkaloid biosynthesis' pathway in UniProt. Recognizing the HxxDG motif and the family-level association of BAHD acyltransferases with alkaloid biosynthesis provides a transferable inference that meaningfully favors D over C, A, and B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HxxDG BAHD acyltransferase motif is identifiable from the raw sequence. The association of BAHD acyltransferases with plant alkaloid biosynthesis (and their absence from folate/CoA pathways and from the ajmaline-specific pathway) is a well-established family-level pattern learned from many other plant proteins. This permits a knowledgeable model to narrow to D without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although ajmaline is technically an alkaloid, option C refers to the specific ajmaline biosynthetic sub-pathway, whose key enzymes differ from BAHD acyltransferases. The enzyme in question is not part of the ajmaline branch. The standard UniProt pathway annotation is 'Alkaloid biosynthesis,' making D the unambiguous correct choice among the four options.


### Important caveats

- The HxxDG motif identification from a 419-aa sequence requires careful scanning and is not trivially obvious to all models; however, it is a well-known family marker.
- The distinction between C and D relies on knowing that ajmaline biosynthesis uses different key enzymes (terpene cyclase-type ajmaline synthase) rather than BAHD acyltransferases, which is transferable family-level knowledge but not universally memorized.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning above relies solely on sequence features and general biological knowledge.
- The trailing period and extra space in options C and D ('biosynthesis. .') are minor formatting artifacts and do not affect interpretation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable HxxDG motif ('ISHKVADG' region), which is the hallmark catalytic signature of the BAHD acyltransferase superfamily. From general knowledge of plant secondary metabolism, BAHD acyltransferases are well-known participants in alkaloid biosynthesis pathways (e.g., in vinblastine, akuammiline, and other MIA branches), but are not key enzymes in tetrahydrofolate biosynthesis (GTP cyclohydrolase I, dihydroneopterin aldolase) or coenzyme A biosynthesis (pantothenate kinase, phosphopantothenoylcysteine synthetase). This eliminates A and B. Between C (ajmaline biosynthesis) and D (Alkaloid biosynthesis): ajmaline biosynthesis is a highly specific MIA sub-pathway whose key cyclization enzyme (ajmaline synthase) is a terpene cyclase-type enzyme, not a BAHD acyltransferase. The BAHD acyltransferase family is broadly associated with multiple MIA branches and is annotated under the general 'Alkaloid biosynthesis' pathway in UniProt. Recognizing the HxxDG motif and the family-level association of BAHD acyltransferases with alkaloid biosynthesis provides a transferable inference that meaningfully favors D over C, A, and B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HxxDG BAHD acyltransferase motif is identifiable from the raw sequence. The association of BAHD acyltransferases with plant alkaloid biosynthesis (and their absence from folate/CoA pathways and from the ajmaline-specific pathway) is a well-established family-level pattern learned from many other plant proteins. This permits a knowledgeable model to narrow to D without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S5E3) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269|PubMed:36349266). The protein is Akuammiline synthase 1 (EC 2.3.1.322), a BAHD acyltransferase involved in monoterpenoid indole alkaloid (MIA) biosynthesis in Alstonia scholaris. The evidence excerpt C5/H3 directly states 'PATHWAY: Alkaloid biosynthesis.' The answer D matches the recorded annotation exactly."
  },
  "important_caveats": [
    "The HxxDG motif identification from a 419-aa sequence requires careful scanning and is not trivially obvious to all models; however, it is a well-known family marker.",
    "The distinction between C and D relies on knowing that ajmaline biosynthesis uses different key enzymes (terpene cyclase-type ajmaline synthase) rather than BAHD acyltransferases, which is transferable family-level knowledge but not universally memorized.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning above relies solely on sequence features and general biological knowledge.",
    "The trailing period and extra space in options C and D ('biosynthesis. .') are minor formatting artifacts and do not affect interpretation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although ajmaline is technically an alkaloid, option C refers to the specific ajmaline biosynthetic sub-pathway, whose key enzymes differ from BAHD acyltransferases. The enzyme in question is not part of the ajmaline branch. The standard UniProt pathway annotation is 'Alkaloid biosynthesis,' making D the unambiguous correct choice among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S5E3) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269|PubMed:36349266). The protein is Akuammiline synthase 1 (EC 2.3.1.322), a BAHD acyltransferase involved in monoterpenoid indole alkaloid (MIA) biosynthesis in Alstonia scholaris. The evidence excerpt C5/H3 directly states 'PATHWAY: Alkaloid biosynthesis.' The answer D matches the recorded annotation exactly.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable HxxDG motif ('ISHKVADG' region), which is the hallmark catalytic signature of the BAHD acyltransferase superfamily. From general knowledge of plant secondary metabolism, BAHD acyltransferases are well-known participants in alkaloid biosynthesis pathways (e.g., in vinblastine, akuammiline, and other MIA branches), but are not key enzymes in tetrahydrofolate biosynthesis (GTP cyclohydrolase I, dihydroneopterin aldolase) or coenzyme A biosynthesis (pantothenate kinase, phosphopantothenoylcysteine synthetase). This eliminates A and B. Between C (ajmaline biosynthesis) and D (Alkaloid biosynthesis): ajmaline biosynthesis is a highly specific MIA sub-pathway whose key cyclization enzyme (ajmaline synthase) is a terpene cyclase-type enzyme, not a BAHD acyltransferase. The BAHD acyltransferase family is broadly associated with multiple MIA branches and is annotated under the general 'Alkaloid biosynthesis' pathway in UniProt. Recognizing the HxxDG motif and the family-level association of BAHD acyltransferases with alkaloid biosynthesis provides a transferable inference that meaningfully favors D over C, A, and B.",
    "missing_item_specific_fact": "",
    "reason": "The HxxDG BAHD acyltransferase motif is identifiable from the raw sequence. The association of BAHD acyltransferases with plant alkaloid biosynthesis (and their absence from folate/CoA pathways and from the ajmaline-specific pathway) is a well-established family-level pattern learned from many other plant proteins. This permits a knowledgeable model to narrow to D without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although ajmaline is technically an alkaloid, option C refers to the specific ajmaline biosynthetic sub-pathway, whose key enzymes differ from BAHD acyltransferases. The enzyme in question is not part of the ajmaline branch. The standard UniProt pathway annotation is 'Alkaloid biosynthesis,' making D the unambiguous correct choice among the four options."
  },
  "important_caveats": [
    "The HxxDG motif identification from a 419-aa sequence requires careful scanning and is not trivially obvious to all models; however, it is a well-known family marker.",
    "The distinction between C and D relies on knowing that ajmaline biosynthesis uses different key enzymes (terpene cyclase-type ajmaline synthase) rather than BAHD acyltransferases, which is transferable family-level knowledge but not universally memorized.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning above relies solely on sequence features and general biological knowledge.",
    "The trailing period and extra space in options C and D ('biosynthesis. .') are minor formatting artifacts and do not affect interpretation."
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
  "benchmark_sequence_length": 419,
  "benchmark_sequence_sha256": "4d53f81259ad6ebf110d3f0389144aaa3ab73e2a4032a10a17048eaa8c40b8bf",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 419,
  "current_source_sequence_sha256": "4d53f81259ad6ebf110d3f0389144aaa3ab73e2a4032a10a17048eaa8c40b8bf",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S5E3",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "selected_historical_source_sequence_length": 419,
  "selected_historical_source_sequence_sha256": "4d53f81259ad6ebf110d3f0389144aaa3ab73e2a4032a10a17048eaa8c40b8bf",
  "selected_historical_version": {
    "accession": "A0A9E7S5E3",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AKS1_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S5E3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.322\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Akuammiline synthase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsAKS1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65387.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   AKS1_ALSSC              Reviewed;         419 AA.\nAC   A0A9E7S5E3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};\nDE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};\nGN   Name=AKS1 {ECO:0000303|PubMed:36349266};\nGN   Synonyms=BAHD3 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65387.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
