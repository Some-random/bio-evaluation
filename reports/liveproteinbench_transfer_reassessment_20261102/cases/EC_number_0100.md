# EC_number_0100

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0100.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.1.1.348

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTAATLFESTDGTVVLLDLPRSIEDAQQHPAAVTLPEAPSLVTNSCRDGTSWTRRLISSPPPETPFVTPEPKNGPSPLPAAAQVAQLMIQASVTGALEELRTNYSGPYLLPRQLSPQRMIADGGKAVDDYKSPHACDLESCSTTAEDATKGRYYFPPESHHVLGTIQETKTLLLQSAPNFNVIVLDPPWPNRSAKRKKGGYKVATTTDDIRALLSDVPIPSLLARDGLVAIWVTNKPAFLDMLTSPRDGILSEWGLELVGEWSWLKITTSAEPILPIDSAHRKPWEPLLIAQRKGSKRVFPPFWRRRVIVSVPDTHSRKPNIRDLVNPMLPPRSRGLEIFARNLTAGWWAWGDDVLHFQERSNWVMAESKSPATGC

[Multiple Choices]
A. 2.1.1.395
B. 3.1.3.112
C. 2.1.1.348
D. 3.2.1.183
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

> The sequence-matched UniProt annotation assigns EC 2.1.1.348 and describes the reaction as mRNA adenosine N6-methylation. The annotation cites experimental evidence for the EC number and catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conserved DPPW motif associated with the MT-A70-like family of SAM-dependent RNA methyltransferases. Family-level recognition supports an mRNA m6A-writer function, which fits option C; the other options describe a different methyltransferase reaction or unrelated enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family/function inference gives a meaningful basis for choosing C from these alternatives without needing the exact protein's database entry. The sequence alone may not establish the precise substrate and EC subtype with certainty, but the family-level inference is relevant to the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options distinguish the mRNA N6-methylation activity from unrelated reaction types, and no other option is comparably supported by the sequence-family inference.


### Important caveats

- The cited source annotation is reviewer-only; it supports the key but was not available as an input to the evaluated model.
- The source assigns experimental evidence codes, but the underlying papers were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conserved DPPW motif associated with the MT-A70-like family of SAM-dependent RNA methyltransferases. Family-level recognition supports an mRNA m6A-writer function, which fits option C; the other options describe a different methyltransferase reaction or unrelated enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family/function inference gives a meaningful basis for choosing C from these alternatives without needing the exact protein's database entry. The sequence alone may not establish the precise substrate and EC subtype with certainty, but the family-level inference is relevant to the choices."
  },
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.1.1.348 and describes the reaction as mRNA adenosine N6-methylation. The annotation cites experimental evidence for the EC number and catalytic activity."
  },
  "important_caveats": [
    "The cited source annotation is reviewer-only; it supports the key but was not available as an input to the evaluated model.",
    "The source assigns experimental evidence codes, but the underlying papers were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options distinguish the mRNA N6-methylation activity from unrelated reaction types, and no other option is comparably supported by the sequence-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.1.1.348 and describes the reaction as mRNA adenosine N6-methylation. The annotation cites experimental evidence for the EC number and catalytic activity.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conserved DPPW motif associated with the MT-A70-like family of SAM-dependent RNA methyltransferases. Family-level recognition supports an mRNA m6A-writer function, which fits option C; the other options describe a different methyltransferase reaction or unrelated enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family/function inference gives a meaningful basis for choosing C from these alternatives without needing the exact protein's database entry. The sequence alone may not establish the precise substrate and EC subtype with certainty, but the family-level inference is relevant to the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options distinguish the mRNA N6-methylation activity from unrelated reaction types, and no other option is comparably supported by the sequence-family inference."
  },
  "important_caveats": [
    "The cited source annotation is reviewer-only; it supports the key but was not available as an input to the evaluated model.",
    "The source assigns experimental evidence codes, but the underlying papers were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4MSY9 (MTA1_PYRO7) annotates EC 2.1.1.348 with evidence code ECO:0000269 (experimental evidence) from two independent studies (PubMed:30535195 and PubMed:35338654). The catalytic activity is explicitly defined as: adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+. The benchmark sequence (376 AA) matches the source sequence (SHA256 match confirmed). The annotation is experimentally determined, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable features of the m6A RNA methyltransferase (MTA1/IME4/METTL3) family: (1) The DPP motif in the region 'IVLDPPWPNRSAKRKK' (~pos 180) is a hallmark of the Rossmann-fold methyltransferase catalytic center found in m6A writers. (2) The conserved tryptophan residues in hydrophobic contexts ('GLVAIWVTNK') are characteristic of the SAM-binding pocket in this family. (3) The protein length of 376 AA is consistent with fungal MTA1/IME4 homologs (typically 350-400 AA), distinguishing them from larger human METTL3 (~580 AA) or small-molecule methyltransferases. (4) The overall domain architecture—a single methyltransferase domain with an N-terminal extension—is consistent with the m6A writer fold known from many characterized homologs. These features eliminate B (3.1.3.112, phosphatase) and D (3.2.1.183, glycosidase) as entirely different enzyme classes, and the specific m6A-writer architecture distinguishes C (2.1.1.348) from A (2.1.1.395, a different methyltransferase). The m6A writer family is among the most extensively characterized methyltransferase families, with homologs identified across fungi, plants, and animals, making this a legitimate transfer from family-level knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the methyltransferase fold from conserved motifs (DPP, W residues), use the 376 AA length consistent with fungal MTA1/IME4 homologs, and apply family-level knowledge of the well-characterized m6A writer architecture to select 2.1.1.348 over the other methyltransferase option. The phosphatase and glycosidase distractors are eliminated by recognizing the methyltransferase motifs. The distinction between two methyltransferase EC numbers relies on recognizing the specific m6A writer family architecture, which is extensively documented across many homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (phosphatase) and D (glycosidase) are clearly different enzyme classes eliminable by methyltransferase motif recognition. Between A (2.1.1.395) and C (2.1.1.348), the m6A writer family features (DPP motif, W residues, 376 AA length, overall architecture) provide a meaningful basis to prefer C. No two options are equally defensible given the sequence features.


### Important caveats

- The exact identity of EC 2.1.1.395 was not independently verified; if it were a very closely related RNA methyltransferase, the distinction between A and C might be less clear from sequence alone.
- The m6A writer family recognition argument relies on the DPP motif and overall architecture being sufficiently distinctive; some other methyltransferase families also contain DPP motifs, though the combination with length and other features strengthens the m6A writer assignment.
- The experimental evidence (ECO:0000269) for the expected answer comes from two independent studies, providing strong support for the annotation.
- The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model; the reasoning argument is constructed from the original sequence and permitted family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable features of the m6A RNA methyltransferase (MTA1/IME4/METTL3) family: (1) The DPP motif in the region 'IVLDPPWPNRSAKRKK' (~pos 180) is a hallmark of the Rossmann-fold methyltransferase catalytic center found in m6A writers. (2) The conserved tryptophan residues in hydrophobic contexts ('GLVAIWVTNK') are characteristic of the SAM-binding pocket in this family. (3) The protein length of 376 AA is consistent with fungal MTA1/IME4 homologs (typically 350-400 AA), distinguishing them from larger human METTL3 (~580 AA) or small-molecule methyltransferases. (4) The overall domain architecture—a single methyltransferase domain with an N-terminal extension—is consistent with the m6A writer fold known from many characterized homologs. These features eliminate B (3.1.3.112, phosphatase) and D (3.2.1.183, glycosidase) as entirely different enzyme classes, and the specific m6A-writer architecture distinguishes C (2.1.1.348) from A (2.1.1.395, a different methyltransferase). The m6A writer family is among the most extensively characterized methyltransferase families, with homologs identified across fungi, plants, and animals, making this a legitimate transfer from family-level knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the methyltransferase fold from conserved motifs (DPP, W residues), use the 376 AA length consistent with fungal MTA1/IME4 homologs, and apply family-level knowledge of the well-characterized m6A writer architecture to select 2.1.1.348 over the other methyltransferase option. The phosphatase and glycosidase distractors are eliminated by recognizing the methyltransferase motifs. The distinction between two methyltransferase EC numbers relies on recognizing the specific m6A writer family architecture, which is extensively documented across many homologs."
  },
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4MSY9 (MTA1_PYRO7) annotates EC 2.1.1.348 with evidence code ECO:0000269 (experimental evidence) from two independent studies (PubMed:30535195 and PubMed:35338654). The catalytic activity is explicitly defined as: adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+. The benchmark sequence (376 AA) matches the source sequence (SHA256 match confirmed). The annotation is experimentally determined, not merely computational."
  },
  "important_caveats": [
    "The exact identity of EC 2.1.1.395 was not independently verified; if it were a very closely related RNA methyltransferase, the distinction between A and C might be less clear from sequence alone.",
    "The m6A writer family recognition argument relies on the DPP motif and overall architecture being sufficiently distinctive; some other methyltransferase families also contain DPP motifs, though the combination with length and other features strengthens the m6A writer assignment.",
    "The experimental evidence (ECO:0000269) for the expected answer comes from two independent studies, providing strong support for the annotation.",
    "The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model; the reasoning argument is constructed from the original sequence and permitted family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (phosphatase) and D (glycosidase) are clearly different enzyme classes eliminable by methyltransferase motif recognition. Between A (2.1.1.395) and C (2.1.1.348), the m6A writer family features (DPP motif, W residues, 376 AA length, overall architecture) provide a meaningful basis to prefer C. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4MSY9 (MTA1_PYRO7) annotates EC 2.1.1.348 with evidence code ECO:0000269 (experimental evidence) from two independent studies (PubMed:30535195 and PubMed:35338654). The catalytic activity is explicitly defined as: adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+. The benchmark sequence (376 AA) matches the source sequence (SHA256 match confirmed). The annotation is experimentally determined, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable features of the m6A RNA methyltransferase (MTA1/IME4/METTL3) family: (1) The DPP motif in the region 'IVLDPPWPNRSAKRKK' (~pos 180) is a hallmark of the Rossmann-fold methyltransferase catalytic center found in m6A writers. (2) The conserved tryptophan residues in hydrophobic contexts ('GLVAIWVTNK') are characteristic of the SAM-binding pocket in this family. (3) The protein length of 376 AA is consistent with fungal MTA1/IME4 homologs (typically 350-400 AA), distinguishing them from larger human METTL3 (~580 AA) or small-molecule methyltransferases. (4) The overall domain architecture—a single methyltransferase domain with an N-terminal extension—is consistent with the m6A writer fold known from many characterized homologs. These features eliminate B (3.1.3.112, phosphatase) and D (3.2.1.183, glycosidase) as entirely different enzyme classes, and the specific m6A-writer architecture distinguishes C (2.1.1.348) from A (2.1.1.395, a different methyltransferase). The m6A writer family is among the most extensively characterized methyltransferase families, with homologs identified across fungi, plants, and animals, making this a legitimate transfer from family-level knowledge.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the methyltransferase fold from conserved motifs (DPP, W residues), use the 376 AA length consistent with fungal MTA1/IME4 homologs, and apply family-level knowledge of the well-characterized m6A writer architecture to select 2.1.1.348 over the other methyltransferase option. The phosphatase and glycosidase distractors are eliminated by recognizing the methyltransferase motifs. The distinction between two methyltransferase EC numbers relies on recognizing the specific m6A writer family architecture, which is extensively documented across many homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (phosphatase) and D (glycosidase) are clearly different enzyme classes eliminable by methyltransferase motif recognition. Between A (2.1.1.395) and C (2.1.1.348), the m6A writer family features (DPP motif, W residues, 376 AA length, overall architecture) provide a meaningful basis to prefer C. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The exact identity of EC 2.1.1.395 was not independently verified; if it were a very closely related RNA methyltransferase, the distinction between A and C might be less clear from sequence alone.",
    "The m6A writer family recognition argument relies on the DPP motif and overall architecture being sufficiently distinctive; some other methyltransferase families also contain DPP motifs, though the combination with length and other features strengthens the m6A writer assignment.",
    "The experimental evidence (ECO:0000269) for the expected answer comes from two independent studies, providing strong support for the annotation.",
    "The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model; the reasoning argument is constructed from the original sequence and permitted family-level knowledge."
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
  "benchmark_sequence_length": 376,
  "benchmark_sequence_sha256": "87c5800fed93eacc087bc034161e057456bee27ffe729600d0b1fd8270c623f1",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "87c5800fed93eacc087bc034161e057456bee27ffe729600d0b1fd8270c623f1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4MSY9",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "87c5800fed93eacc087bc034161e057456bee27ffe729600d0b1fd8270c623f1",
  "selected_historical_version": {
    "accession": "G4MSY9",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "MTA1_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4MSY9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"M6A writer MTA1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35338654\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.348\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35338654\",\"source\":\"PubMed\"}],\"value\":\"N6-methyladenosine RNA methyltransferase MTA1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30535195\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35338654\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:55585\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.348\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30535195\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35338654\",\"source\":\"PubMed\"}],\"name\":\"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:55584\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12414\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12417\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74411\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74449\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi Y.\",\"Wang H.\",\"Wang J.\",\"Liu X.\",\"Lin F.\",\"Lu J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30535195\"},{\"database\":\"DOI\",\"id\":\"10.1093/femsle/fny286\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30535195\",\"journal\":\"FEMS Microbiol. Lett.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"N6-methyladenosine RNA methylation is involved in virulence of the rice blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).\",\"volume\":\"366\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Ren Z.\",\"Tang B.\",\"Xing J.\",\"Liu C.\",\"Cai X.\",\"Hendy A.\",\"Kamran M.\",\"Liu H.\",\"Zheng L.\",\"Huang J.\",\"Chen X.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35338654\"},{\"database\":\"DOI\",\"id\":\"10.1111/nph.18117\"}],\"citationType\":\"journal article\",\"firstPage\":\"247\",\"id\":\"35338654\",\"journal\":\"New Phytol.\",\"lastPage\":\"262\",\"publicationDate\":\"2022\",\"title\":\"MTA1-mediated RNA m6 A modification regulates autophagy and is required for infection of the rice blast fungus.\",\"volume\":\"235\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:07.225373+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834",
  "url": "https://rest.uniprot.org/uniprotkb/G4MSY9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   MTA1_PYRO7              Reviewed;         376 AA.\nAC   G4MSY9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:35338654};\nDE            EC=2.1.1.348 {ECO:0000269|PubMed:35338654};\nDE   AltName: Full=M6A writer MTA1 {ECO:0000305};\nGN   Name=MTA1 {ECO:0000303|PubMed:35338654};\nGN   Synonyms=IME4 {ECO:0000303|PubMed:30535195}; ORFNames=MGG_01492;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.307350+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa",
  "url": "https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:35338654};\nDE            EC=2.1.1.348 {ECO:0000269|PubMed:35338654};\nDE   AltName: Full=M6A writer MTA1 {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.307350+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa",
  "url": "https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30535195; DOI=10.1093/femsle/fny286;\nRA   Shi Y., Wang H., Wang J., Liu X., Lin F., Lu J.;\nRT   \"N6-methyladenosine RNA methylation is involved in virulence of the rice\nRT   blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).\";\nRL   FEMS Microbiol. Lett. 366:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.307350+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa",
  "url": "https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=35338654; DOI=10.1111/nph.18117;\nRA   Ren Z., Tang B., Xing J., Liu C., Cai X., Hendy A., Kamran M., Liu H.,\nRA   Zheng L., Huang J., Chen X.L.;\nRT   \"MTA1-mediated RNA m6 A modification regulates autophagy and is required\nRT   for infection of the rice blast fungus.\";\nRL   New Phytol. 235:247-262(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.307350+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa",
  "url": "https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-\nCC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;\nCC         Evidence={ECO:0000269|PubMed:30535195, ECO:0000269|PubMed:35338654};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;\nCC         Evidence={ECO:0000269|PubMed:30535195, ECO:0000269|PubMed:35338654};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.307350+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa",
  "url": "https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
