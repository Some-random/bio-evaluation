# EC_number_0162

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0162.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.18

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQLSSIADKIRESATMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATIRTGKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYISMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPTGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGNQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. 3.2.1.18
B. 3.2.1.8
C. 4.3.1.24
D. 1.1.1.122
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

> The supplied sequence matches the reviewed source sequence, whose catalytic-activity annotation assigns EC 3.2.1.18 and describes hydrolysis of terminal sialic-acid linkages. The annotation cites experimental evidence; the underlying publication was not independently assessed here.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral hemagglutinin-neuraminidase-type glycoprotein. Transferable knowledge of this protein family connects its conserved sialidase domain to removal of terminal sialic acids, hence EC 3.2.1.18. That meaningfully distinguishes A from the offered xylanase, lyase, and dehydrogenase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level catalytic pattern provide a credible distinction among these choices without requiring the exact protein’s database annotation. The family inference is probabilistic, not a substitute for experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the sialidase EC number is meaningfully distinguished by the sequence’s viral membrane-glycoprotein and family-level features.


### Important caveats

- The protein’s organism and exact identity come from reviewer-only evidence, not the original input.
- The experimental support is reported by the matched database annotation; the cited study was not independently reviewed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral hemagglutinin-neuraminidase-type glycoprotein. Transferable knowledge of this protein family connects its conserved sialidase domain to removal of terminal sialic acids, hence EC 3.2.1.18. That meaningfully distinguishes A from the offered xylanase, lyase, and dehydrogenase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level catalytic pattern provide a credible distinction among these choices without requiring the exact protein’s database annotation. The family inference is probabilistic, not a substitute for experimental characterization."
  },
  "case_id": "EC_number_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed source sequence, whose catalytic-activity annotation assigns EC 3.2.1.18 and describes hydrolysis of terminal sialic-acid linkages. The annotation cites experimental evidence; the underlying publication was not independently assessed here."
  },
  "important_caveats": [
    "The protein’s organism and exact identity come from reviewer-only evidence, not the original input.",
    "The experimental support is reported by the matched database annotation; the cited study was not independently reviewed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sialidase EC number is meaningfully distinguished by the sequence’s viral membrane-glycoprotein and family-level features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed source sequence, whose catalytic-activity annotation assigns EC 3.2.1.18 and describes hydrolysis of terminal sialic-acid linkages. The annotation cites experimental evidence; the underlying publication was not independently assessed here.",
    "evidence_ids": ["C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral hemagglutinin-neuraminidase-type glycoprotein. Transferable knowledge of this protein family connects its conserved sialidase domain to removal of terminal sialic acids, hence EC 3.2.1.18. That meaningfully distinguishes A from the offered xylanase, lyase, and dehydrogenase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level catalytic pattern provide a credible distinction among these choices without requiring the exact protein’s database annotation. The family inference is probabilistic, not a substitute for experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sialidase EC number is meaningfully distinguished by the sequence’s viral membrane-glycoprotein and family-level features."
  },
  "important_caveats": [
    "The protein’s organism and exact identity come from reviewer-only evidence, not the original input.",
    "The experimental support is reported by the matched database annotation; the cited study was not independently reviewed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9WAF5 (HN_MUMPV, Hemagglutinin-neuraminidase from Mumps orthorubulavirus) annotates EC 3.2.1.18 with experimental evidence (ECO:0000269, PubMed:39088577). The catalytic activity is explicitly stated as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues, which is the definition of EC 3.2.1.18 (sialidase/neuraminidase). The sequence matches the benchmark sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits the hallmark architecture of a paramyxovirus surface glycoprotein: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKK...), a type-II transmembrane domain (hydrophobic stretch ~residues 95-130: FRILVLSVQAVTLILVIVTLGELVRMINDQ), and a large C-terminal ectodomain (~450 aa) with multiple conserved cysteines and paramyxovirus HN-specific motifs. The 'ING'/'TIG'-like motif (FINGINKFIIEDYATHDFSIGHPLNMP...) and the 'NRT' region are conserved active-site features of paramyxovirus hemagglutinin-neuraminidase proteins. Family-level knowledge establishes that paramyxovirus HN proteins (mumps, NDV, parainfluenza) possess neuraminidase/sialidase activity, corresponding to EC 3.2.1.18. The three distractors are structurally incompatible: 3.2.1.8 (xylanase) is a small bacterial/fungal GH10/GH11 enzyme without signal peptide or TM domain; 4.3.1.24 (histidine ammonia-lyase) is a bacterial lyase with a completely different fold; 1.1.1.122 (sorbitol dehydrogenase) is a ~350-aa Rossmann-fold oxidoreductase requiring a GxGxxG NAD-binding motif absent here. The viral glycoprotein architecture plus paramyxovirus HN motif recognition, combined with well-known family-level sialidase activity, meaningfully distinguishes option A from all others.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of paramyxovirus HN protein family features (signal peptide + TM + large ectodomain, conserved TIG/NRT motifs, sialidase activity as a family property) can identify the correct EC number without memorizing this specific entry. The distractors are eliminated by incompatible protein architecture and enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four entirely different enzyme classes (glycosidase vs. xylanase vs. lyase vs. oxidoreductase). The viral glycoprotein architecture and paramyxovirus HN motifs uniquely point to a glycosidase with sialidase activity (3.2.1.18), leaving no genuine ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for EC 3.2.1.18 carries experimental evidence (ECO:0000269, PubMed:39088577, 2024), confirming the enzymatic activity was experimentally demonstrated.
- The sequence identity to Q9WAF5 is exact (SHA-256 match), confirming the reviewer evidence applies to the benchmark sequence.
- Some paramyxovirus HN proteins have lost sialidase activity (e.g., measles virus uses F for attachment), but mumps HN retains it, and the conserved active-site motifs visible in this sequence are consistent with an active sialidase.
- The reviewer-only evidence (accession, organism, PubMed reference) was not available to the evaluated model; the reasoning argument relies solely on sequence features and family-level biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits the hallmark architecture of a paramyxovirus surface glycoprotein: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKK...), a type-II transmembrane domain (hydrophobic stretch ~residues 95-130: FRILVLSVQAVTLILVIVTLGELVRMINDQ), and a large C-terminal ectodomain (~450 aa) with multiple conserved cysteines and paramyxovirus HN-specific motifs. The 'ING'/'TIG'-like motif (FINGINKFIIEDYATHDFSIGHPLNMP...) and the 'NRT' region are conserved active-site features of paramyxovirus hemagglutinin-neuraminidase proteins. Family-level knowledge establishes that paramyxovirus HN proteins (mumps, NDV, parainfluenza) possess neuraminidase/sialidase activity, corresponding to EC 3.2.1.18. The three distractors are structurally incompatible: 3.2.1.8 (xylanase) is a small bacterial/fungal GH10/GH11 enzyme without signal peptide or TM domain; 4.3.1.24 (histidine ammonia-lyase) is a bacterial lyase with a completely different fold; 1.1.1.122 (sorbitol dehydrogenase) is a ~350-aa Rossmann-fold oxidoreductase requiring a GxGxxG NAD-binding motif absent here. The viral glycoprotein architecture plus paramyxovirus HN motif recognition, combined with well-known family-level sialidase activity, meaningfully distinguishes option A from all others.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of paramyxovirus HN protein family features (signal peptide + TM + large ectodomain, conserved TIG/NRT motifs, sialidase activity as a family property) can identify the correct EC number without memorizing this specific entry. The distractors are eliminated by incompatible protein architecture and enzyme class."
  },
  "case_id": "EC_number_0162",
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
    "reason": "The UniProt entry Q9WAF5 (HN_MUMPV, Hemagglutinin-neuraminidase from Mumps orthorubulavirus) annotates EC 3.2.1.18 with experimental evidence (ECO:0000269, PubMed:39088577). The catalytic activity is explicitly stated as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues, which is the definition of EC 3.2.1.18 (sialidase/neuraminidase). The sequence matches the benchmark sequence exactly."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.18 carries experimental evidence (ECO:0000269, PubMed:39088577, 2024), confirming the enzymatic activity was experimentally demonstrated.",
    "The sequence identity to Q9WAF5 is exact (SHA-256 match), confirming the reviewer evidence applies to the benchmark sequence.",
    "Some paramyxovirus HN proteins have lost sialidase activity (e.g., measles virus uses F for attachment), but mumps HN retains it, and the conserved active-site motifs visible in this sequence are consistent with an active sialidase.",
    "The reviewer-only evidence (accession, organism, PubMed reference) was not available to the evaluated model; the reasoning argument relies solely on sequence features and family-level biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four entirely different enzyme classes (glycosidase vs. xylanase vs. lyase vs. oxidoreductase). The viral glycoprotein architecture and paramyxovirus HN motifs uniquely point to a glycosidase with sialidase activity (3.2.1.18), leaving no genuine ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9WAF5 (HN_MUMPV, Hemagglutinin-neuraminidase from Mumps orthorubulavirus) annotates EC 3.2.1.18 with experimental evidence (ECO:0000269, PubMed:39088577). The catalytic activity is explicitly stated as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues, which is the definition of EC 3.2.1.18 (sialidase/neuraminidase). The sequence matches the benchmark sequence exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits the hallmark architecture of a paramyxovirus surface glycoprotein: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKK...), a type-II transmembrane domain (hydrophobic stretch ~residues 95-130: FRILVLSVQAVTLILVIVTLGELVRMINDQ), and a large C-terminal ectodomain (~450 aa) with multiple conserved cysteines and paramyxovirus HN-specific motifs. The 'ING'/'TIG'-like motif (FINGINKFIIEDYATHDFSIGHPLNMP...) and the 'NRT' region are conserved active-site features of paramyxovirus hemagglutinin-neuraminidase proteins. Family-level knowledge establishes that paramyxovirus HN proteins (mumps, NDV, parainfluenza) possess neuraminidase/sialidase activity, corresponding to EC 3.2.1.18. The three distractors are structurally incompatible: 3.2.1.8 (xylanase) is a small bacterial/fungal GH10/GH11 enzyme without signal peptide or TM domain; 4.3.1.24 (histidine ammonia-lyase) is a bacterial lyase with a completely different fold; 1.1.1.122 (sorbitol dehydrogenase) is a ~350-aa Rossmann-fold oxidoreductase requiring a GxGxxG NAD-binding motif absent here. The viral glycoprotein architecture plus paramyxovirus HN motif recognition, combined with well-known family-level sialidase activity, meaningfully distinguishes option A from all others.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of paramyxovirus HN protein family features (signal peptide + TM + large ectodomain, conserved TIG/NRT motifs, sialidase activity as a family property) can identify the correct EC number without memorizing this specific entry. The distractors are eliminated by incompatible protein architecture and enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four entirely different enzyme classes (glycosidase vs. xylanase vs. lyase vs. oxidoreductase). The viral glycoprotein architecture and paramyxovirus HN motifs uniquely point to a glycosidase with sialidase activity (3.2.1.18), leaving no genuine ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.18 carries experimental evidence (ECO:0000269, PubMed:39088577, 2024), confirming the enzymatic activity was experimentally demonstrated.",
    "The sequence identity to Q9WAF5 is exact (SHA-256 match), confirming the reviewer evidence applies to the benchmark sequence.",
    "Some paramyxovirus HN proteins have lost sialidase activity (e.g., measles virus uses F for attachment), but mumps HN retains it, and the conserved active-site motifs visible in this sequence are consistent with an active sialidase.",
    "The reviewer-only evidence (accession, organism, PubMed reference) was not available to the evaluated model; the reasoning argument relies solely on sequence features and family-level biological knowledge."
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
  "benchmark_sequence_length": 582,
  "benchmark_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "current_entry_audit": {
    "entryVersion": 132,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 582,
  "current_source_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 130,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9WAF5",
  "selected_historical_entry_version": 130,
  "selected_historical_record_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "selected_historical_source_sequence_length": 582,
  "selected_historical_source_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "selected_historical_version": {
    "accession": "Q9WAF5",
    "database": "Swiss-Prot",
    "entryVersion": 130,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9WAF5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":132,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\"],\"scientificName\":\"Mumps orthorubulavirus\",\"taxonId\":2560602}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39088577\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39088577\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Takahashi T.\",\"Kurebayashi Y.\",\"Otsubo T.\",\"Ikeda K.\",\"Konagaya K.\",\"Suzuki S.\",\"Yamazaki M.\",\"Suzuki K.\",\"Narimichi Y.\",\"Minami A.\",\"Takeuchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39088577\"},{\"database\":\"DOI\",\"id\":\"10.1093/glycob/cwae059\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39088577\",\"journal\":\"Glycobiology\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Novel sialidase inhibitors suppress mumps virus replication and infection.\",\"volume\":\"34\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"13V165E2\"}],\"referenceNumber\":6,\"referencePositions\":[\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H1",
  "excerpt": "ID   HN_MUMPV                Reviewed;         582 AA.\nAC   Q9WAF5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1999, sequence version 1.\nDT   28-JAN-2026, entry version 130.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};\nGN   Name=HN {ECO:0000312|EMBL:BAG84572.1};\nOS   Mumps orthorubulavirus (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis.\nOX   NCBI_TaxID=2560602;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H3",
  "excerpt": "RN   [6]\nRP   CATALYTIC ACTIVITY.\nRC   STRAIN=13V165E2;\nRX   PubMed=39088577; DOI=10.1093/glycob/cwae059;\nRA   Takahashi T., Kurebayashi Y., Otsubo T., Ikeda K., Konagaya K., Suzuki S.,\nRA   Yamazaki M., Suzuki K., Narimichi Y., Minami A., Takeuchi H.;\nRT   \"Novel sialidase inhibitors suppress mumps virus replication and\nRT   infection.\";\nRL   Glycobiology 34:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-\nCC         (2->8)- glycosidic linkages of terminal sialic acid residues in\nCC         oligosaccharides, glycoproteins, glycolipids, colominic acid and\nCC         synthetic substrates.; EC=3.2.1.18;\nCC         Evidence={ECO:0000269|PubMed:39088577};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
