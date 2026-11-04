# EC_number_0198

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0198.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.97.1.14

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MENQHQKFISRRNFIKTSALLGGTAFLGTGLPNIKKTYSKELDYVGNFEYPLAKPENILYSACLQCTVACSIKVKINNGVCMKIDGNPYSAMNLGENLPYDLSPKEAVSIDGKLCPKGQAGIQHAYDPYRLRKVIKRDGPRGSGKWKTIPYDQAIDEIVNGGNIFKDIGENQNVEGLKDIFVLKDPKVAKAMADDVTKIRKKEMTVDEFKAKHKDNLDVLIDPNHPDLGPKNNQFLFQVGRIHNGRIEFTKRFVNDSFGSVNWIEKTTLCGQTSNKAWVHSTREYLEGKWTGGIKSPRPDHRNTEFLLVFGSIVFEANYGPVQETEPITEGLESGRLKIAVVDPRLTKVASKAWKWVPIKPGNDAAFALGMIRWIIENERYDTKFLQNATRLAATNSDEPSYSNATYLVKVEKDGRAAKHLRANEIGIGTEKEFVVISNGKPAAVDPENSNLAIQGELFVDTNLEGIKVKSPLQLIKEEAYSKELAEWAELSGAKQKDIEDISKEFTSHGKKAAVEFYRGAIKHTNGWYNGQALIVLNHLIGNMNWQGGISNTGGGWSYIGDKEGQPYPMANLHPNKLSKFGVPITKEGWKYEESTLFEGYPAKRPWYPFSGNVAQETWPSISDGYPYKIKAALISSHSPMYSLPGGHVQLKTLLDTEKVPLLIASDIVIGDSSQYVDYIFPDLTYLERWATPGQSHHIRVKVNQVRQPVIAPLTENATVFGEEVPISLEALMMSISEKVGLSGFGKDAFGPGKDLNRMEDFYLKLVANIASGNKQGELVKAADSEEMELFKSSHRHLPKTVYDIEKWQQTLTSDEWKRVVYVLNRGGRFASSDDAYEGSFIKKKIPGLARLYLEEIADSRNSISGNYFTGYPKYLPIMDMAENLINDEGEFHLITNKEVFGTQSRTITNYWAQLALQPENFVVLNSVDAKKLKVDNGDKVLVTSTSNPKGEHLIAADESRPTIGKVKIVEGIRPGVVAISTHYGHWGYGARDIQIDGEVVKGEEVRGLGIHPNPLFRLDDNLRGTTLSDPIGGSASYYDTRVNIQRV

[Multiple Choices]
A. 1.16.1.10
B. 4.2.3.1
C. 1.11.1.24
D. 1.97.1.14
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

> The sequence-matched UniProt record identifies this protein as selenate reductase subunit A and assigns EC 1.97.1.14, with a catalytic-activity annotation and a cited study on the selenate reductase complex. This supports the key, though the excerpts do not independently reproduce the underlying experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence, N-terminal hydrophobic segment with an RR motif, and enzyme-like architecture are consistent with a Tat-exported catalytic subunit of a respiratory molybdoenzyme. Transferable knowledge of this family supports an oxyanion-reductase interpretation, unlike the lyase choice or peroxide-acting oxidoreductase choice; among the offered alternatives, the selenate-reductase EC is a credible fit. This is a family-level inference, not a definitive identification of substrate from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers meaningful family and localization clues that can distinguish the respiratory reductase choice from the other listed enzyme classes. Exact substrate specificity is less certain from sequence alone, but the choices do not require a more detailed distinction that defeats this inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the sequence and the offered enzyme classes.


### Important caveats

- The reviewer-only source record and its target-specific annotation were not part of the original input and are used only to assess whether the key is supported.
- The sequence-based identification is probabilistic; the original sequence alone does not establish the experimental reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence, N-terminal hydrophobic segment with an RR motif, and enzyme-like architecture are consistent with a Tat-exported catalytic subunit of a respiratory molybdoenzyme. Transferable knowledge of this family supports an oxyanion-reductase interpretation, unlike the lyase choice or peroxide-acting oxidoreductase choice; among the offered alternatives, the selenate-reductase EC is a credible fit. This is a family-level inference, not a definitive identification of substrate from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers meaningful family and localization clues that can distinguish the respiratory reductase choice from the other listed enzyme classes. Exact substrate specificity is less certain from sequence alone, but the choices do not require a more detailed distinction that defeats this inference."
  },
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies this protein as selenate reductase subunit A and assigns EC 1.97.1.14, with a catalytic-activity annotation and a cited study on the selenate reductase complex. This supports the key, though the excerpts do not independently reproduce the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only source record and its target-specific annotation were not part of the original input and are used only to assess whether the key is supported.",
    "The sequence-based identification is probabilistic; the original sequence alone does not establish the experimental reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence and the offered enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies this protein as selenate reductase subunit A and assigns EC 1.97.1.14, with a catalytic-activity annotation and a cited study on the selenate reductase complex. This supports the key, though the excerpts do not independently reproduce the underlying experiments.",
    "evidence_ids": ["C4", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence, N-terminal hydrophobic segment with an RR motif, and enzyme-like architecture are consistent with a Tat-exported catalytic subunit of a respiratory molybdoenzyme. Transferable knowledge of this family supports an oxyanion-reductase interpretation, unlike the lyase choice or peroxide-acting oxidoreductase choice; among the offered alternatives, the selenate-reductase EC is a credible fit. This is a family-level inference, not a definitive identification of substrate from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers meaningful family and localization clues that can distinguish the respiratory reductase choice from the other listed enzyme classes. Exact substrate specificity is less certain from sequence alone, but the choices do not require a more detailed distinction that defeats this inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence and the offered enzyme classes."
  },
  "important_caveats": [
    "The reviewer-only source record and its target-specific annotation were not part of the original input and are used only to assess whether the key is supported.",
    "The sequence-based identification is probabilistic; the original sequence alone does not establish the experimental reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0A8X0K1 (sequence matched, 1048 AA) is annotated as 'Selenate reductase subunit A' with EC=1.97.1.14, citing PubMed:21357486 (Kuroda et al., 2011, J. Bacteriol.), which characterized the srdBCA operon encoding the respiratory selenate reductase complex from Mesobacillus selenatarsenatis SF-1. The catalytic activity (selenite + quinone + H2O = selenate + quinol, Rhea:RHEA:51636) is consistent. The evidence code is ECO:0000305 (inferred by similarity) with a functional-genomics reference, which is a standard annotation level for well-characterized operon products.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1048-aa sequence contains hallmark features of the DMSO reductase family (Mo-bis-MGD cofactor enzymes): (1) the conserved 'IDP' motif in the Mo-cofactor binding domain (visible around residue ~200 as 'IDPNHPDLG'), (2) N-terminal Cys-rich motifs ('CLQCTVACSIK', 'CPKG') consistent with &#91;4Fe-4S&#93; or &#91;2Fe-2S&#93; cluster binding, (3) additional 'DP' motifs ('DPRLTKVASKAW', 'DPENSNLAI') in the catalytic domain, and (4) overall large catalytic-subunit architecture. Among the four choices, only EC 1.97.1.14 (selenate reductase) belongs to the DMSO reductase family. EC 1.16.1.10 (ferritin oxidoreductase) is an iron-metabolism enzyme without Mo-bis-MGD cofactor. EC 4.2.3.1 (terpene cyclase) is a lyase with an entirely different fold and mechanism. EC 1.11.1.24 (chloroperoxidase) is a heme peroxidase lacking Mo-cofactor and Fe-S clusters. Thus, recognizing the DMSO-reductase-family architecture from the sequence meaningfully eliminates A, B, and C and points to D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the Mo-bis-MGD cofactor-binding domain signature (IDP motif, Fe-S cluster Cys motifs, ~1000-aa catalytic subunit architecture) can classify this as a DMSO reductase family enzyme. Since only option D falls within that family while the other three belong to structurally and mechanistically unrelated enzyme classes (iron oxidoreductase, terpene lyase, heme peroxidase), the family-level inference is sufficient to select D without needing the exact substrate specificity annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (EC 1 oxidoreductases in A, C, D; EC 4 lyases in B) and within EC 1 they belong to distinct subclasses (1.16 iron-related, 1.11 peroxidase, 1.97 other oxidoreductases). The Mo-bis-MGD/Fe-S architecture cleanly excludes A, B, and C.


### Important caveats

- The UniProt annotation uses ECO:0000305 (inferred by similarity) rather than a direct enzyme-assay evidence code, though the cited 2011 paper provides functional characterization of the srdBCA operon.
- Within the DMSO reductase family, distinguishing selenate reductase (1.97.1.14) from nitrate reductase or chlorate reductase would require additional substrate-specific knowledge; however, the multiple-choice options do not include other DMSO-reductase-family members, so family-level identification suffices.
- The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1048-aa sequence contains hallmark features of the DMSO reductase family (Mo-bis-MGD cofactor enzymes): (1) the conserved 'IDP' motif in the Mo-cofactor binding domain (visible around residue ~200 as 'IDPNHPDLG'), (2) N-terminal Cys-rich motifs ('CLQCTVACSIK', 'CPKG') consistent with [4Fe-4S] or [2Fe-2S] cluster binding, (3) additional 'DP' motifs ('DPRLTKVASKAW', 'DPENSNLAI') in the catalytic domain, and (4) overall large catalytic-subunit architecture. Among the four choices, only EC 1.97.1.14 (selenate reductase) belongs to the DMSO reductase family. EC 1.16.1.10 (ferritin oxidoreductase) is an iron-metabolism enzyme without Mo-bis-MGD cofactor. EC 4.2.3.1 (terpene cyclase) is a lyase with an entirely different fold and mechanism. EC 1.11.1.24 (chloroperoxidase) is a heme peroxidase lacking Mo-cofactor and Fe-S clusters. Thus, recognizing the DMSO-reductase-family architecture from the sequence meaningfully eliminates A, B, and C and points to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the Mo-bis-MGD cofactor-binding domain signature (IDP motif, Fe-S cluster Cys motifs, ~1000-aa catalytic subunit architecture) can classify this as a DMSO reductase family enzyme. Since only option D falls within that family while the other three belong to structurally and mechanistically unrelated enzyme classes (iron oxidoreductase, terpene lyase, heme peroxidase), the family-level inference is sufficient to select D without needing the exact substrate specificity annotation."
  },
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0A8X0K1 (sequence matched, 1048 AA) is annotated as 'Selenate reductase subunit A' with EC=1.97.1.14, citing PubMed:21357486 (Kuroda et al., 2011, J. Bacteriol.), which characterized the srdBCA operon encoding the respiratory selenate reductase complex from Mesobacillus selenatarsenatis SF-1. The catalytic activity (selenite + quinone + H2O = selenate + quinol, Rhea:RHEA:51636) is consistent. The evidence code is ECO:0000305 (inferred by similarity) with a functional-genomics reference, which is a standard annotation level for well-characterized operon products."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by similarity) rather than a direct enzyme-assay evidence code, though the cited 2011 paper provides functional characterization of the srdBCA operon.",
    "Within the DMSO reductase family, distinguishing selenate reductase (1.97.1.14) from nitrate reductase or chlorate reductase would require additional substrate-specific knowledge; however, the multiple-choice options do not include other DMSO-reductase-family members, so family-level identification suffices.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (EC 1 oxidoreductases in A, C, D; EC 4 lyases in B) and within EC 1 they belong to distinct subclasses (1.16 iron-related, 1.11 peroxidase, 1.97 other oxidoreductases). The Mo-bis-MGD/Fe-S architecture cleanly excludes A, B, and C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0A8X0K1 (sequence matched, 1048 AA) is annotated as 'Selenate reductase subunit A' with EC=1.97.1.14, citing PubMed:21357486 (Kuroda et al., 2011, J. Bacteriol.), which characterized the srdBCA operon encoding the respiratory selenate reductase complex from Mesobacillus selenatarsenatis SF-1. The catalytic activity (selenite + quinone + H2O = selenate + quinol, Rhea:RHEA:51636) is consistent. The evidence code is ECO:0000305 (inferred by similarity) with a functional-genomics reference, which is a standard annotation level for well-characterized operon products.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1048-aa sequence contains hallmark features of the DMSO reductase family (Mo-bis-MGD cofactor enzymes): (1) the conserved 'IDP' motif in the Mo-cofactor binding domain (visible around residue ~200 as 'IDPNHPDLG'), (2) N-terminal Cys-rich motifs ('CLQCTVACSIK', 'CPKG') consistent with [4Fe-4S] or [2Fe-2S] cluster binding, (3) additional 'DP' motifs ('DPRLTKVASKAW', 'DPENSNLAI') in the catalytic domain, and (4) overall large catalytic-subunit architecture. Among the four choices, only EC 1.97.1.14 (selenate reductase) belongs to the DMSO reductase family. EC 1.16.1.10 (ferritin oxidoreductase) is an iron-metabolism enzyme without Mo-bis-MGD cofactor. EC 4.2.3.1 (terpene cyclase) is a lyase with an entirely different fold and mechanism. EC 1.11.1.24 (chloroperoxidase) is a heme peroxidase lacking Mo-cofactor and Fe-S clusters. Thus, recognizing the DMSO-reductase-family architecture from the sequence meaningfully eliminates A, B, and C and points to D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the Mo-bis-MGD cofactor-binding domain signature (IDP motif, Fe-S cluster Cys motifs, ~1000-aa catalytic subunit architecture) can classify this as a DMSO reductase family enzyme. Since only option D falls within that family while the other three belong to structurally and mechanistically unrelated enzyme classes (iron oxidoreductase, terpene lyase, heme peroxidase), the family-level inference is sufficient to select D without needing the exact substrate specificity annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (EC 1 oxidoreductases in A, C, D; EC 4 lyases in B) and within EC 1 they belong to distinct subclasses (1.16 iron-related, 1.11 peroxidase, 1.97 other oxidoreductases). The Mo-bis-MGD/Fe-S architecture cleanly excludes A, B, and C."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by similarity) rather than a direct enzyme-assay evidence code, though the cited 2011 paper provides functional characterization of the srdBCA operon.",
    "Within the DMSO reductase family, distinguishing selenate reductase (1.97.1.14) from nitrate reductase or chlorate reductase would require additional substrate-specific knowledge; however, the multiple-choice options do not include other DMSO-reductase-family members, so family-level identification suffices.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model."
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
  "benchmark_sequence_length": 1048,
  "benchmark_sequence_sha256": "4b1947e94f45c86a28644819df4590bb0bb0e1b9ad81e938aff624a0220113d3",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-03-04",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1048,
  "current_source_sequence_sha256": "4b1947e94f45c86a28644819df4590bb0bb0e1b9ad81e938aff624a0220113d3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 39,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0A8X0K1",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa",
  "selected_historical_source_sequence_length": 1048,
  "selected_historical_source_sequence_sha256": "4b1947e94f45c86a28644819df4590bb0bb0e1b9ad81e938aff624a0220113d3",
  "selected_historical_version": {
    "accession": "A0A0A8X0K1",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SRDA_MESS1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0A8X0K1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:55.467166+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-03-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:55.467166+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Mesobacillus\"],\"scientificName\":\"Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431 / SF-1)\",\"taxonId\":1321606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:55.467166+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase subunit A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:55.467166+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"name\":\"selenite + a quinone + H2O = selenate + a quinol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:51636\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15075\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18212\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:24646\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132124\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:23:55.467166+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuroda M.\",\"Yamashita M.\",\"Miwa E.\",\"Imao K.\",\"Fujimoto N.\",\"Ono H.\",\"Nagano K.\",\"Sei K.\",\"Ike M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21357486\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01197-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"2141\",\"id\":\"21357486\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2148\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.\",\"volume\":\"193\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ83594.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION AS A SELENATE REDUCTASE\",\"SUBUNIT\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:23:55.467166+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   SRDA_MESS1              Reviewed;        1048 AA.\nAC   A0A0A8X0K1; E9RFD1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-MAR-2015, sequence version 1.\nDT   09-APR-2025, entry version 39.\nDE   RecName: Full=Selenate reductase subunit A {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   Flags: Precursor;\nGN   Name=srdA {ECO:0000303|PubMed:21357486};\nGN   ORFNames=SAMD00020551_1552 {ECO:0000312|EMBL:GAM13408.1};\nOS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431\nOS   / SF-1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;\nOC   Mesobacillus.\nOX   NCBI_TaxID=1321606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.438981+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Selenate reductase subunit A {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.438981+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ83594.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE,\nRP   SUBUNIT, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;\nRX   PubMed=21357486; DOI=10.1128/jb.01197-10;\nRA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,\nRA   Sei K., Ike M.;\nRT   \"Molecular cloning and characterization of the srdBCA operon, encoding the\nRT   respiratory selenate reductase complex, from the selenate-reducing\nRT   bacterium Bacillus selenatarsenatis SF-1.\";\nRL   J. Bacteriol. 193:2141-2148(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.438981+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=selenite + a quinone + H2O = selenate + a quinol;\nCC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;\nCC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.438981+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 198. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
