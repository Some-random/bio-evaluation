# catalytic_activity_0129

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0129.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — rhazimol + acetyl-CoA = akuammiline + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPILQRISKTFIKPSSPTPESLRCYNLSSSDQMITSVYISLAFFYGSPGCESSRIRQQLDNSLSRTLVYYYPFAGRLVDNDHIDCNDQGVQFVEVRIHCPISAILKQTTSYAEDLVFPRGTSACHEDSLVVVQLNRFECGGVAIAVCISHKVADGSGAIAFINDWAATARVSSHIPSPLLVADSIFPHLDNSLPVPYNLSKNCVTRRFVFPAAEIEKLKSKAVESGLQQPTRVEVVTALLYQCALLASRSTNSGLSRPSVLIQAVNLRPFLVPPLPRNSVGNIFSINFSIIEVDSLEFPELAGRLRKAKLKFQNLSQEKLYYDSQMQELGECLKQLNTGNFDVYYCSSWCRFPVYDVDFGWGKPTWVCTVKSQIKDMIVLMDSPGDEIAAFVTLEEEKMSAFQHNELLLSFASLYSAK

[Multiple Choices]
A. 12-deshydroxyl okaramine E + 2-oxoglutarate + O2 = okaramine E + succinate + CO2
B. rhazimol + acetyl-CoA = akuammiline + CoA + H(+)
C. enterobactin + 3 H2O = 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H(+)
D. O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates this reaction with experimental-literature evidence (ECO:0000269), and the archived record available by the historical cutoff gives the same reaction. This supports choice B, though the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the C-terminal DFGWG motif characteristic of plant BAHD acyl-CoA-dependent acyltransferases. Transferable family knowledge makes an acetyl-CoA-dependent acyl transfer, as in B, a meaningful match; the other choices describe an oxygenase, a hydrolytic cleavage, or a protein phosphatase reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition provides a credible distinction among these alternatives without needing the target's database annotation. The motif supports the enzyme class more directly than the precise substrate pair, so the sequence alone would not establish every reaction detail.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction types, and the acyltransferase-family inference distinguishes B among those offered.


### Important caveats

- The sequence motif supports a family-level inference, not independent proof of the exact substrates or products.
- The supporting database annotation cites experimental literature, but that primary evidence was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the C-terminal DFGWG motif characteristic of plant BAHD acyl-CoA-dependent acyltransferases. Transferable family knowledge makes an acetyl-CoA-dependent acyl transfer, as in B, a meaningful match; the other choices describe an oxygenase, a hydrolytic cleavage, or a protein phosphatase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a credible distinction among these alternatives without needing the target's database annotation. The motif supports the enzyme class more directly than the precise substrate pair, so the sequence alone would not establish every reaction detail."
  },
  "case_id": "catalytic_activity_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this reaction with experimental-literature evidence (ECO:0000269), and the archived record available by the historical cutoff gives the same reaction. This supports choice B, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence motif supports a family-level inference, not independent proof of the exact substrates or products.",
    "The supporting database annotation cites experimental literature, but that primary evidence was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and the acyltransferase-family inference distinguishes B among those offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this reaction with experimental-literature evidence (ECO:0000269), and the archived record available by the historical cutoff gives the same reaction. This supports choice B, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the C-terminal DFGWG motif characteristic of plant BAHD acyl-CoA-dependent acyltransferases. Transferable family knowledge makes an acetyl-CoA-dependent acyl transfer, as in B, a meaningful match; the other choices describe an oxygenase, a hydrolytic cleavage, or a protein phosphatase reaction.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a credible distinction among these alternatives without needing the target's database annotation. The motif supports the enzyme class more directly than the precise substrate pair, so the sequence alone would not establish every reaction detail."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and the acyltransferase-family inference distinguishes B among those offered."
  },
  "important_caveats": [
    "The sequence motif supports a family-level inference, not independent proof of the exact substrates or products.",
    "The supporting database annotation cites experimental literature, but that primary evidence was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S5E3 (AKS1_ALSSC) is annotated as 'Akuammiline synthase 1' (EC 2.3.1.322) with the catalytic activity 'rhazimol + acetyl-CoA = akuammiline + CoA + H(+)', which exactly matches choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022 Chem. Sci.). The benchmark sequence matches the source sequence exactly (SHA-256 identical, 419 aa).

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark BAHD acyltransferase motifs: 'DPGDE' (within 'MIVLMDSPGDEIAAF') and 'GWGKP' (within 'GWGKPTWVCTVKSQIKDMIVLMDSPGDE'). These are well-known, highly conserved family signatures learned from hundreds of characterized plant BAHD acyltransferases (e.g., anthocyanin O-acyltransferases, taxol acyltransferases, various hydroxycinnamoyl-CoA acyltransferases). BAHD enzymes catalyze acyl-CoA-dependent acyl transfer reactions. Among the four choices, only B involves acetyl-CoA as a substrate (an acyltransferase reaction, EC 2.3.x). Choice A is a 2-oxoglutarate-dependent dioxygenase (EC 1.14.11.x), C is a hydrolase/esterase acting on a bacterial siderophore, and D is a protein phosphatase (EC 3.1.3.x). None of these classes share the DPGDE/GWGKP motifs. The recognition of BAHD family motifs is a transferable inference from other plant acyltransferases and meaningfully eliminates A, C, and D in favor of B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DPGDE and GWGKP motifs are diagnostic family-level features of BAHD acyltransferases, a class extensively characterized across many plant species. Recognizing these motifs and knowing that BAHD enzymes use acyl-CoA substrates is transferable knowledge from other proteins. This directly selects the acyl-CoA-dependent reaction (B) and excludes the dioxygenase (A), esterase (C), and phosphatase (D) alternatives without requiring memorization of this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The DPGDE motif is unambiguous and diagnostic of BAHD acyltransferases. Only choice B represents an acyltransferase reaction using acyl-CoA. The other three choices represent entirely different enzyme classes (dioxygenase, hydrolase, phosphatase) with no sequence-level support in this protein.


### Important caveats

- The BAHD motif recognition distinguishes the enzyme class (acyltransferase) but does not by itself predict the specific substrate (rhazimol) or product (akuammiline). However, the question only requires selecting among four reaction types, and only B is consistent with BAHD chemistry.
- The annotation evidence is experimental (ECO:0000269 from PubMed:36349266), not merely computational, strengthening the expected answer.
- The sequence is from Alstonia scholaris (Apocynaceae), a plant family rich in monoterpene indole alkaloids; the akuammiline skeleton is a known Apocynaceae alkaloid, providing additional biological plausibility for B over the other choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark BAHD acyltransferase motifs: 'DPGDE' (within 'MIVLMDSPGDEIAAF') and 'GWGKP' (within 'GWGKPTWVCTVKSQIKDMIVLMDSPGDE'). These are well-known, highly conserved family signatures learned from hundreds of characterized plant BAHD acyltransferases (e.g., anthocyanin O-acyltransferases, taxol acyltransferases, various hydroxycinnamoyl-CoA acyltransferases). BAHD enzymes catalyze acyl-CoA-dependent acyl transfer reactions. Among the four choices, only B involves acetyl-CoA as a substrate (an acyltransferase reaction, EC 2.3.x). Choice A is a 2-oxoglutarate-dependent dioxygenase (EC 1.14.11.x), C is a hydrolase/esterase acting on a bacterial siderophore, and D is a protein phosphatase (EC 3.1.3.x). None of these classes share the DPGDE/GWGKP motifs. The recognition of BAHD family motifs is a transferable inference from other plant acyltransferases and meaningfully eliminates A, C, and D in favor of B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DPGDE and GWGKP motifs are diagnostic family-level features of BAHD acyltransferases, a class extensively characterized across many plant species. Recognizing these motifs and knowing that BAHD enzymes use acyl-CoA substrates is transferable knowledge from other proteins. This directly selects the acyl-CoA-dependent reaction (B) and excludes the dioxygenase (A), esterase (C), and phosphatase (D) alternatives without requiring memorization of this specific protein's database record."
  },
  "case_id": "catalytic_activity_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S5E3 (AKS1_ALSSC) is annotated as 'Akuammiline synthase 1' (EC 2.3.1.322) with the catalytic activity 'rhazimol + acetyl-CoA = akuammiline + CoA + H(+)', which exactly matches choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022 Chem. Sci.). The benchmark sequence matches the source sequence exactly (SHA-256 identical, 419 aa)."
  },
  "important_caveats": [
    "The BAHD motif recognition distinguishes the enzyme class (acyltransferase) but does not by itself predict the specific substrate (rhazimol) or product (akuammiline). However, the question only requires selecting among four reaction types, and only B is consistent with BAHD chemistry.",
    "The annotation evidence is experimental (ECO:0000269 from PubMed:36349266), not merely computational, strengthening the expected answer.",
    "The sequence is from Alstonia scholaris (Apocynaceae), a plant family rich in monoterpene indole alkaloids; the akuammiline skeleton is a known Apocynaceae alkaloid, providing additional biological plausibility for B over the other choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The DPGDE motif is unambiguous and diagnostic of BAHD acyltransferases. Only choice B represents an acyltransferase reaction using acyl-CoA. The other three choices represent entirely different enzyme classes (dioxygenase, hydrolase, phosphatase) with no sequence-level support in this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S5E3 (AKS1_ALSSC) is annotated as 'Akuammiline synthase 1' (EC 2.3.1.322) with the catalytic activity 'rhazimol + acetyl-CoA = akuammiline + CoA + H(+)', which exactly matches choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022 Chem. Sci.). The benchmark sequence matches the source sequence exactly (SHA-256 identical, 419 aa).",
    "evidence_ids": ["C5", "C4", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark BAHD acyltransferase motifs: 'DPGDE' (within 'MIVLMDSPGDEIAAF') and 'GWGKP' (within 'GWGKPTWVCTVKSQIKDMIVLMDSPGDE'). These are well-known, highly conserved family signatures learned from hundreds of characterized plant BAHD acyltransferases (e.g., anthocyanin O-acyltransferases, taxol acyltransferases, various hydroxycinnamoyl-CoA acyltransferases). BAHD enzymes catalyze acyl-CoA-dependent acyl transfer reactions. Among the four choices, only B involves acetyl-CoA as a substrate (an acyltransferase reaction, EC 2.3.x). Choice A is a 2-oxoglutarate-dependent dioxygenase (EC 1.14.11.x), C is a hydrolase/esterase acting on a bacterial siderophore, and D is a protein phosphatase (EC 3.1.3.x). None of these classes share the DPGDE/GWGKP motifs. The recognition of BAHD family motifs is a transferable inference from other plant acyltransferases and meaningfully eliminates A, C, and D in favor of B.",
    "missing_item_specific_fact": "",
    "reason": "The DPGDE and GWGKP motifs are diagnostic family-level features of BAHD acyltransferases, a class extensively characterized across many plant species. Recognizing these motifs and knowing that BAHD enzymes use acyl-CoA substrates is transferable knowledge from other proteins. This directly selects the acyl-CoA-dependent reaction (B) and excludes the dioxygenase (A), esterase (C), and phosphatase (D) alternatives without requiring memorization of this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The DPGDE motif is unambiguous and diagnostic of BAHD acyltransferases. Only choice B represents an acyltransferase reaction using acyl-CoA. The other three choices represent entirely different enzyme classes (dioxygenase, hydrolase, phosphatase) with no sequence-level support in this protein."
  },
  "important_caveats": [
    "The BAHD motif recognition distinguishes the enzyme class (acyltransferase) but does not by itself predict the specific substrate (rhazimol) or product (akuammiline). However, the question only requires selecting among four reaction types, and only B is consistent with BAHD chemistry.",
    "The annotation evidence is experimental (ECO:0000269 from PubMed:36349266), not merely computational, strengthening the expected answer.",
    "The sequence is from Alstonia scholaris (Apocynaceae), a plant family rich in monoterpene indole alkaloids; the akuammiline skeleton is a known Apocynaceae alkaloid, providing additional biological plausibility for B over the other choices."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79624\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.322\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"rhazimol + acetyl-CoA = akuammiline + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79623\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:141879\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230474\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "DE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};\nDE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=rhazimol + acetyl-CoA = akuammiline + CoA + H(+);\nCC         Xref=Rhea:RHEA:79623, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:141879, ChEBI:CHEBI:230474;\nCC         EC=2.3.1.322; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79624;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
