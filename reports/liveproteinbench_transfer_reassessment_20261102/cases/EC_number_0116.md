# EC_number_0116

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0116.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.7.11.11

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLPDTGILSPFTTAVNPDPPQSQTLRVPRPTPVLDRPTTDSTANKRVKLDPTVSKVPWEPSVKPSSSKVEGASGLEQDSFMPTLGSVFKKKKKDKEATRLKDSSGNPDTIIEDSPVTPSTERSLSQSLGSAPSTATTANSHGGLSTVTSATSQTPTSPIATGGQAEKDHPMTTPVNESAGHSRSDSQTLQKAENAVRATKGKYTLQDFNFQRTLGTGSFGRVHLVQSKHNLRFYAVKVLKKAQVVKMKQVEHTNDERRMLQRVKHPFLITLWGTFQDAKNLYMVMDFIEGGELFSLLRKSQRFPNPVAKFYAAEVALALDYLHSMNIIYRDLKPENLLLDRHGHLKITDFGFAKEVPDITWTLCGTPDYLAPEVVASKGYNKSVDWWSLGILIFEMLCGYTPFWDGGSPMKIYENILRGRVKYPAYIHPDAMNLLQQLITPDLTKRLGNLYHGSRSVLEHPWFAEVNWERLLSKQIEPPYVPPVRGGIGDASLFDKYPEETEEYGKDGPDQYGHFFTDF

[Multiple Choices]
A. 2.7.11.11
B. 2.7.11.24
C. 2.3.1.322
D. 1.5.1.38
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

> The sequence contains a eukaryotic protein-kinase catalytic domain, and the matched UniProt record assigns it to the cAMP-dependent protein kinase catalytic subunit with EC 2.7.11.11. The EC and catalytic-activity annotations cite evidence transferred from another UniProt protein (ECO:0000250), so this supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the conserved eukaryotic protein-kinase catalytic motifs, including the glycine-rich region, catalytic-loop HRD motif, and DFG motif. More specifically, its kinase-domain sequence is consistent with the PKA catalytic-subunit family; transferable family recognition can distinguish the PKA EC choice (A) from the other kinase EC choice (B), while C and D describe unrelated reaction classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference meaningfully favors a cAMP-dependent protein kinase catalytic subunit and EC 2.7.11.11. The precise activity is inferred from shared sequence-family knowledge, not guaranteed by catalytic-domain motifs alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a protein kinase, and the PKA-family inference favors A over the offered alternatives; no other option is comparably supported.


### Important caveats

- The supplied evidence supports the annotation through sequence similarity to another protein; it does not establish direct biochemical testing of this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the conserved eukaryotic protein-kinase catalytic motifs, including the glycine-rich region, catalytic-loop HRD motif, and DFG motif. More specifically, its kinase-domain sequence is consistent with the PKA catalytic-subunit family; transferable family recognition can distinguish the PKA EC choice (A) from the other kinase EC choice (B), while C and D describe unrelated reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully favors a cAMP-dependent protein kinase catalytic subunit and EC 2.7.11.11. The precise activity is inferred from shared sequence-family knowledge, not guaranteed by catalytic-domain motifs alone."
  },
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence contains a eukaryotic protein-kinase catalytic domain, and the matched UniProt record assigns it to the cAMP-dependent protein kinase catalytic subunit with EC 2.7.11.11. The EC and catalytic-activity annotations cite evidence transferred from another UniProt protein (ECO:0000250), so this supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied evidence supports the annotation through sequence similarity to another protein; it does not establish direct biochemical testing of this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a protein kinase, and the PKA-family inference favors A over the offered alternatives; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence contains a eukaryotic protein-kinase catalytic domain, and the matched UniProt record assigns it to the cAMP-dependent protein kinase catalytic subunit with EC 2.7.11.11. The EC and catalytic-activity annotations cite evidence transferred from another UniProt protein (ECO:0000250), so this supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the conserved eukaryotic protein-kinase catalytic motifs, including the glycine-rich region, catalytic-loop HRD motif, and DFG motif. More specifically, its kinase-domain sequence is consistent with the PKA catalytic-subunit family; transferable family recognition can distinguish the PKA EC choice (A) from the other kinase EC choice (B), while C and D describe unrelated reaction classes.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully favors a cAMP-dependent protein kinase catalytic subunit and EC 2.7.11.11. The precise activity is inferred from shared sequence-family knowledge, not guaranteed by catalytic-domain motifs alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a protein kinase, and the PKA-family inference favors A over the offered alternatives; no other option is comparably supported."
  },
  "important_caveats": [
    "The supplied evidence supports the annotation through sequence similarity to another protein; it does not establish direct biochemical testing of this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G1X456 annotates this protein as 'cAMP-dependent protein kinase catalytic subunit' with EC 2.7.11.11 (C4, C5, C6, H2, H4, H5). The evidence code is ECO:0000250 (inferred by similarity from P17612), meaning the annotation is computational rather than experimentally derived. However, the sequence itself contains canonical PKA/AGC kinase motifs (GTGSFGR glycine-rich loop, DLKPEN catalytic loop with conserved Glu, DFG motif, APE motif, WWSLG activation segment), which are consistent with the assigned EC number. The annotation is a similarity-based transfer, not direct experimental validation, but the sequence features independently corroborate the assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase domain features: (1) GTGSFGR glycine-rich loop, (2) IIYRDLKPEN catalytic loop with the conserved Glu residue, (3) DFGFAKE DFG motif, (4) DYLAPEV APE motif, (5) WWSLG activation segment. These immediately eliminate C (acyltransferase, EC 2.3.1.x) and D (oxidoreductase, EC 1.5.1.x), which catalyze entirely different reaction types. To distinguish A (2.7.11.11, PKA) from B (2.7.11.24, MAP3K/MEKK), the critical transferable feature is the AGC kinase catalytic-loop signature 'DLKPE' with the invariant Glu, which is a hallmark of the AGC kinase superfamily (PKA, PKC, PKG, RSK). MAP3Ks belong to the STE11/RAF/MAP3K kinase family and have different catalytic-loop sequences and often additional regulatory domains (SH3, SH2, CRD, PH domains). The presence of DLKPEN plus GTGSFGR strongly points to an AGC kinase rather than a MAP3K. Among the offered choices, only 2.7.11.11 corresponds to an AGC kinase, making A the most defensible answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the protein kinase fold from conserved motifs, then use the AGC-specific DLKPE signature (well-characterized across the PKA/PKC/PKG family) to distinguish 2.7.11.11 from 2.7.11.24 (MAP3K, a different kinase family). This is a family-level inference from transferable kinase classification knowledge, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly non-kinase EC numbers and are eliminated by the obvious kinase motifs. Between A and B, the AGC catalytic-loop signature (DLKPE) and glycine-rich loop (GTGSFGR) are well-established family markers that distinguish PKA-type kinases from MAP3Ks. No other AGC kinase EC number is offered, so A is uniquely supported among the choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000250 (similarity to P17612), so the EC assignment is computationally inferred by homology rather than experimentally validated for this specific fungal protein.
- The N-terminal region is unusually long and proline-rich for a canonical PKA catalytic subunit, which is consistent with fungal PKA catalytic subunits that can have extended regulatory N-termini.
- The annotation is for Arthrobotrys oligospora (a nematode-trapping fungus); the organism context was not provided to the evaluated model but is not needed for the kinase-family inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase domain features: (1) GTGSFGR glycine-rich loop, (2) IIYRDLKPEN catalytic loop with the conserved Glu residue, (3) DFGFAKE DFG motif, (4) DYLAPEV APE motif, (5) WWSLG activation segment. These immediately eliminate C (acyltransferase, EC 2.3.1.x) and D (oxidoreductase, EC 1.5.1.x), which catalyze entirely different reaction types. To distinguish A (2.7.11.11, PKA) from B (2.7.11.24, MAP3K/MEKK), the critical transferable feature is the AGC kinase catalytic-loop signature 'DLKPE' with the invariant Glu, which is a hallmark of the AGC kinase superfamily (PKA, PKC, PKG, RSK). MAP3Ks belong to the STE11/RAF/MAP3K kinase family and have different catalytic-loop sequences and often additional regulatory domains (SH3, SH2, CRD, PH domains). The presence of DLKPEN plus GTGSFGR strongly points to an AGC kinase rather than a MAP3K. Among the offered choices, only 2.7.11.11 corresponds to an AGC kinase, making A the most defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein kinase fold from conserved motifs, then use the AGC-specific DLKPE signature (well-characterized across the PKA/PKC/PKG family) to distinguish 2.7.11.11 from 2.7.11.24 (MAP3K, a different kinase family). This is a family-level inference from transferable kinase classification knowledge, not a lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G1X456 annotates this protein as 'cAMP-dependent protein kinase catalytic subunit' with EC 2.7.11.11 (C4, C5, C6, H2, H4, H5). The evidence code is ECO:0000250 (inferred by similarity from P17612), meaning the annotation is computational rather than experimentally derived. However, the sequence itself contains canonical PKA/AGC kinase motifs (GTGSFGR glycine-rich loop, DLKPEN catalytic loop with conserved Glu, DFG motif, APE motif, WWSLG activation segment), which are consistent with the assigned EC number. The annotation is a similarity-based transfer, not direct experimental validation, but the sequence features independently corroborate the assignment."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to P17612), so the EC assignment is computationally inferred by homology rather than experimentally validated for this specific fungal protein.",
    "The N-terminal region is unusually long and proline-rich for a canonical PKA catalytic subunit, which is consistent with fungal PKA catalytic subunits that can have extended regulatory N-termini.",
    "The annotation is for Arthrobotrys oligospora (a nematode-trapping fungus); the organism context was not provided to the evaluated model but is not needed for the kinase-family inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly non-kinase EC numbers and are eliminated by the obvious kinase motifs. Between A and B, the AGC catalytic-loop signature (DLKPE) and glycine-rich loop (GTGSFGR) are well-established family markers that distinguish PKA-type kinases from MAP3Ks. No other AGC kinase EC number is offered, so A is uniquely supported among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G1X456 annotates this protein as 'cAMP-dependent protein kinase catalytic subunit' with EC 2.7.11.11 (C4, C5, C6, H2, H4, H5). The evidence code is ECO:0000250 (inferred by similarity from P17612), meaning the annotation is computational rather than experimentally derived. However, the sequence itself contains canonical PKA/AGC kinase motifs (GTGSFGR glycine-rich loop, DLKPEN catalytic loop with conserved Glu, DFG motif, APE motif, WWSLG activation segment), which are consistent with the assigned EC number. The annotation is a similarity-based transfer, not direct experimental validation, but the sequence features independently corroborate the assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase domain features: (1) GTGSFGR glycine-rich loop, (2) IIYRDLKPEN catalytic loop with the conserved Glu residue, (3) DFGFAKE DFG motif, (4) DYLAPEV APE motif, (5) WWSLG activation segment. These immediately eliminate C (acyltransferase, EC 2.3.1.x) and D (oxidoreductase, EC 1.5.1.x), which catalyze entirely different reaction types. To distinguish A (2.7.11.11, PKA) from B (2.7.11.24, MAP3K/MEKK), the critical transferable feature is the AGC kinase catalytic-loop signature 'DLKPE' with the invariant Glu, which is a hallmark of the AGC kinase superfamily (PKA, PKC, PKG, RSK). MAP3Ks belong to the STE11/RAF/MAP3K kinase family and have different catalytic-loop sequences and often additional regulatory domains (SH3, SH2, CRD, PH domains). The presence of DLKPEN plus GTGSFGR strongly points to an AGC kinase rather than a MAP3K. Among the offered choices, only 2.7.11.11 corresponds to an AGC kinase, making A the most defensible answer.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein kinase fold from conserved motifs, then use the AGC-specific DLKPE signature (well-characterized across the PKA/PKC/PKG family) to distinguish 2.7.11.11 from 2.7.11.24 (MAP3K, a different kinase family). This is a family-level inference from transferable kinase classification knowledge, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly non-kinase EC numbers and are eliminated by the obvious kinase motifs. Between A and B, the AGC catalytic-loop signature (DLKPE) and glycine-rich loop (GTGSFGR) are well-established family markers that distinguish PKA-type kinases from MAP3Ks. No other AGC kinase EC number is offered, so A is uniquely supported among the choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to P17612), so the EC assignment is computationally inferred by homology rather than experimentally validated for this specific fungal protein.",
    "The N-terminal region is unusually long and proline-rich for a canonical PKA catalytic subunit, which is consistent with fungal PKA catalytic subunits that can have extended regulatory N-termini.",
    "The annotation is for Arthrobotrys oligospora (a nematode-trapping fungus); the organism context was not provided to the evaluated model but is not needed for the kinase-family inference."
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
  "benchmark_sequence_length": 519,
  "benchmark_sequence_sha256": "331e937113a10945cd5f0c38946f6c59ef8767f9b9a290b3ef9ac6473537853b",
  "current_entry_audit": {
    "entryVersion": 70,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 519,
  "current_source_sequence_sha256": "331e937113a10945cd5f0c38946f6c59ef8767f9b9a290b3ef9ac6473537853b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 68,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G1X456",
  "selected_historical_entry_version": 68,
  "selected_historical_record_sha256": "1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a",
  "selected_historical_source_sequence_length": 519,
  "selected_historical_source_sequence_sha256": "331e937113a10945cd5f0c38946f6c59ef8767f9b9a290b3ef9ac6473537853b",
  "selected_historical_version": {
    "accession": "G1X456",
    "database": "Swiss-Prot",
    "entryVersion": 68,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KAPB_ARTOA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G1X456\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:31.104931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "url": "https://rest.uniprot.org/uniprotkb/G1X456.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":70,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:31.104931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "url": "https://rest.uniprot.org/uniprotkb/G1X456.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Nematode-trapping fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008784\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Orbiliomycetes\",\"Orbiliales\",\"Orbiliaceae\",\"Orbilia\",\"Orbilia oligospora\"],\"scientificName\":\"Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\",\"synonyms\":[\"Didymozoophaga oligospora\"],\"taxonId\":756982}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:31.104931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "url": "https://rest.uniprot.org/uniprotkb/G1X456.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17612\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.11.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"cAMP-dependent protein kinase catalytic subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:31.104931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "url": "https://rest.uniprot.org/uniprotkb/G1X456.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17612\",\"source\":\"UniProtKB\"}],\"name\":\"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17989\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:31.104931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "url": "https://rest.uniprot.org/uniprotkb/G1X456.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17612\",\"source\":\"UniProtKB\"}],\"name\":\"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46608\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:31.104931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5",
  "url": "https://rest.uniprot.org/uniprotkb/G1X456.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H1",
  "excerpt": "ID   KAPB_ARTOA              Reviewed;         519 AA.\nAC   G1X456;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 68.\nDE   RecName: Full=cAMP-dependent protein kinase catalytic subunit {ECO:0000305};\nDE            EC=2.7.11.11 {ECO:0000250|UniProtKB:P17612};\nGN   Name=TPK2 {ECO:0000303|PubMed:35993904};\nGN   ORFNames=AOL_s00043g480 {ECO:0000312|EMBL:EGX52090.1};\nOS   Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\nOS   (Nematode-trapping fungus) (Didymozoophaga oligospora).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Orbiliomycetes;\nOC   Orbiliales; Orbiliaceae; Orbilia; Orbilia oligospora.\nOX   NCBI_TaxID=756982 {ECO:0000312|Proteomes:UP000008784};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:35.157757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a",
  "url": "https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=cAMP-dependent protein kinase catalytic subunit {ECO:0000305};\nDE            EC=2.7.11.11 {ECO:0000250|UniProtKB:P17612};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:35.157757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a",
  "url": "https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=35993904; DOI=10.1093/g3journal/jkac217;\nRA   Chen S.A., Lin H.C., Hsueh Y.P.;\nRT   \"The cAMP-PKA pathway regulates prey sensing and trap morphogenesis in the\nRT   nematode-trapping fungus Arthrobotrys oligospora.\";\nRL   G3 (Bethesda) 12:jkac217-jkac217(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:35.157757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a",
  "url": "https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +\nCC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.11;\nCC         Evidence={ECO:0000250|UniProtKB:P17612};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:35.157757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a",
  "url": "https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +\nCC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.11;\nCC         Evidence={ECO:0000250|UniProtKB:P17612};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:35.157757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a",
  "url": "https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
