# EC_number_0009

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0009.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.7.2.4

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. 2.7.2.4
B. 2.7.1.39
C. 2.7.1.52
D. 2.1.1.348
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

> The sequence-matched UniProt records annotate the protein as aspartokinase, EC 2.7.2.4, with the reaction L-aspartate + ATP = 4-phospho-L-aspartate + ADP. The evidence is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the aspartokinase/Hom3 family, whose transferable family-level function is ATP-dependent phosphorylation of aspartate to 4-phosphoaspartate. That distinguishes A from the offered alternatives: B and C are other kinase activities, while D is a methyltransferase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the kinase family and its characteristic reaction provides a meaningful basis to select A from these choices without needing the exact protein's database annotation. This is a family-level inference, not proof of the exact protein's experimentally measured activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives specify distinct EC activities, and the aspartokinase-family inference favors A.


### Important caveats

- The supplied source annotation is homology-transferred rather than direct experimental evidence.
- The protein identity and annotation in the reviewer-only evidence were not original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the aspartokinase/Hom3 family, whose transferable family-level function is ATP-dependent phosphorylation of aspartate to 4-phosphoaspartate. That distinguishes A from the offered alternatives: B and C are other kinase activities, while D is a methyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the kinase family and its characteristic reaction provides a meaningful basis to select A from these choices without needing the exact protein's database annotation. This is a family-level inference, not proof of the exact protein's experimentally measured activity."
  },
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate the protein as aspartokinase, EC 2.7.2.4, with the reaction L-aspartate + ATP = 4-phospho-L-aspartate + ADP. The evidence is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supplied source annotation is homology-transferred rather than direct experimental evidence.",
    "The protein identity and annotation in the reviewer-only evidence were not original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives specify distinct EC activities, and the aspartokinase-family inference favors A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate the protein as aspartokinase, EC 2.7.2.4, with the reaction L-aspartate + ATP = 4-phospho-L-aspartate + ADP. The evidence is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the aspartokinase/Hom3 family, whose transferable family-level function is ATP-dependent phosphorylation of aspartate to 4-phosphoaspartate. That distinguishes A from the offered alternatives: B and C are other kinase activities, while D is a methyltransferase activity.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the kinase family and its characteristic reaction provides a meaningful basis to select A from these choices without needing the exact protein's database annotation. This is a family-level inference, not proof of the exact protein's experimentally measured activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives specify distinct EC activities, and the aspartokinase-family inference favors A."
  },
  "important_caveats": [
    "The supplied source annotation is homology-transferred rather than direct experimental evidence.",
    "The protein identity and annotation in the reviewer-only evidence were not original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1D8PMB8 annotates this 544-aa sequence as Aspartokinase, EC 2.7.2.4 (L-aspartate + ATP = 4-phospho-L-aspartate + ADP). The sequence matches exactly in both current and archived records. However, the evidence code is ECO:0000250 (inferred by similarity from P10869), indicating a computational transfer rather than direct experimental validation. The annotation is consistent with the amino acid kinase family fold and the reaction description.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~544 aa) exhibits features of the amino acid kinase (AAK) superfamily, recognizable by conserved motifs such as the 'CSARSS' region near the N-terminus and the characteristic kinase fold. Within the AAK superfamily, aspartokinase (EC 2.7.2.4) phosphorylates the carboxyl group of aspartate, while homoserine kinase (EC 2.7.1.39) phosphorylates a hydroxyl group. A knowledgeable model can distinguish these using transferable family-level knowledge: (1) Fungal aspartokinases are typically ~450–550 aa with an N-terminal catalytic domain followed by C-terminal regulatory (ACT-like) domains, consistent with the 544-aa length and apparent multi-domain architecture here; fungal homoserine kinases are typically ~300–350 aa. (2) The 'CSARSS' motif and surrounding residues are characteristic of the aspartate-binding pocket in aspartokinases, where the arginine coordinates the carboxylate. (3) EC 2.1.1.348 (methyltransferase) belongs to a completely different EC class (transferases of one-carbon groups) and lacks the kinase fold and P-loop/AK motifs. (4) EC 2.7.1.52 (acetate kinase) belongs to a different structural family (P-loop NTPase, ~210 aa) and is inconsistent with both the length and the AAK fold. Thus, family recognition plus length and motif analysis meaningfully favors A over B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of AAK superfamily recognition, fungal aspartokinase length (~500 aa) versus homoserine kinase (~300 aa), the CSARSS substrate-binding motif, and elimination of clearly mismatched EC classes (methyltransferase, acetate kinase) provides a credible transferable inference. The distinction between 2.7.2.4 and 2.7.1.39, while requiring specific AAK-family knowledge, is grounded in well-characterized structural and size differences across multiple fungal homologs, not a fact unique to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D (methyltransferase) and C (acetate kinase) are clearly excluded by EC class and structural family mismatch. B (homoserine kinase) is in the same AAK superfamily but is distinguished by the ~200-aa size difference in fungal homologs and the substrate-binding motif. The length and domain architecture of the 544-aa sequence strongly favor aspartokinase over homoserine kinase, leaving A as the most defensible choice.


### Important caveats

- The UniProt annotation for this entry relies on similarity transfer (ECO:0000250 from P10869), not direct experimental characterization of the Candida albicans enzyme.
- The distinction between EC 2.7.2.4 and EC 2.7.1.39 within the AAK superfamily ultimately depends on substrate specificity determined by active-site residues; the length and motif arguments are strong but probabilistic rather than definitive.
- The reviewer-only source evidence was not available to the evaluated model; the transferable argument relies on general AAK-family knowledge learned from multiple fungal homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~544 aa) exhibits features of the amino acid kinase (AAK) superfamily, recognizable by conserved motifs such as the 'CSARSS' region near the N-terminus and the characteristic kinase fold. Within the AAK superfamily, aspartokinase (EC 2.7.2.4) phosphorylates the carboxyl group of aspartate, while homoserine kinase (EC 2.7.1.39) phosphorylates a hydroxyl group. A knowledgeable model can distinguish these using transferable family-level knowledge: (1) Fungal aspartokinases are typically ~450–550 aa with an N-terminal catalytic domain followed by C-terminal regulatory (ACT-like) domains, consistent with the 544-aa length and apparent multi-domain architecture here; fungal homoserine kinases are typically ~300–350 aa. (2) The 'CSARSS' motif and surrounding residues are characteristic of the aspartate-binding pocket in aspartokinases, where the arginine coordinates the carboxylate. (3) EC 2.1.1.348 (methyltransferase) belongs to a completely different EC class (transferases of one-carbon groups) and lacks the kinase fold and P-loop/AK motifs. (4) EC 2.7.1.52 (acetate kinase) belongs to a different structural family (P-loop NTPase, ~210 aa) and is inconsistent with both the length and the AAK fold. Thus, family recognition plus length and motif analysis meaningfully favors A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of AAK superfamily recognition, fungal aspartokinase length (~500 aa) versus homoserine kinase (~300 aa), the CSARSS substrate-binding motif, and elimination of clearly mismatched EC classes (methyltransferase, acetate kinase) provides a credible transferable inference. The distinction between 2.7.2.4 and 2.7.1.39, while requiring specific AAK-family knowledge, is grounded in well-characterized structural and size differences across multiple fungal homologs, not a fact unique to this exact protein."
  },
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1D8PMB8 annotates this 544-aa sequence as Aspartokinase, EC 2.7.2.4 (L-aspartate + ATP = 4-phospho-L-aspartate + ADP). The sequence matches exactly in both current and archived records. However, the evidence code is ECO:0000250 (inferred by similarity from P10869), indicating a computational transfer rather than direct experimental validation. The annotation is consistent with the amino acid kinase family fold and the reaction description."
  },
  "important_caveats": [
    "The UniProt annotation for this entry relies on similarity transfer (ECO:0000250 from P10869), not direct experimental characterization of the Candida albicans enzyme.",
    "The distinction between EC 2.7.2.4 and EC 2.7.1.39 within the AAK superfamily ultimately depends on substrate specificity determined by active-site residues; the length and motif arguments are strong but probabilistic rather than definitive.",
    "The reviewer-only source evidence was not available to the evaluated model; the transferable argument relies on general AAK-family knowledge learned from multiple fungal homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (methyltransferase) and C (acetate kinase) are clearly excluded by EC class and structural family mismatch. B (homoserine kinase) is in the same AAK superfamily but is distinguished by the ~200-aa size difference in fungal homologs and the substrate-binding motif. The length and domain architecture of the 544-aa sequence strongly favor aspartokinase over homoserine kinase, leaving A as the most defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1D8PMB8 annotates this 544-aa sequence as Aspartokinase, EC 2.7.2.4 (L-aspartate + ATP = 4-phospho-L-aspartate + ADP). The sequence matches exactly in both current and archived records. However, the evidence code is ECO:0000250 (inferred by similarity from P10869), indicating a computational transfer rather than direct experimental validation. The annotation is consistent with the amino acid kinase family fold and the reaction description.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~544 aa) exhibits features of the amino acid kinase (AAK) superfamily, recognizable by conserved motifs such as the 'CSARSS' region near the N-terminus and the characteristic kinase fold. Within the AAK superfamily, aspartokinase (EC 2.7.2.4) phosphorylates the carboxyl group of aspartate, while homoserine kinase (EC 2.7.1.39) phosphorylates a hydroxyl group. A knowledgeable model can distinguish these using transferable family-level knowledge: (1) Fungal aspartokinases are typically ~450–550 aa with an N-terminal catalytic domain followed by C-terminal regulatory (ACT-like) domains, consistent with the 544-aa length and apparent multi-domain architecture here; fungal homoserine kinases are typically ~300–350 aa. (2) The 'CSARSS' motif and surrounding residues are characteristic of the aspartate-binding pocket in aspartokinases, where the arginine coordinates the carboxylate. (3) EC 2.1.1.348 (methyltransferase) belongs to a completely different EC class (transferases of one-carbon groups) and lacks the kinase fold and P-loop/AK motifs. (4) EC 2.7.1.52 (acetate kinase) belongs to a different structural family (P-loop NTPase, ~210 aa) and is inconsistent with both the length and the AAK fold. Thus, family recognition plus length and motif analysis meaningfully favors A over B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The combination of AAK superfamily recognition, fungal aspartokinase length (~500 aa) versus homoserine kinase (~300 aa), the CSARSS substrate-binding motif, and elimination of clearly mismatched EC classes (methyltransferase, acetate kinase) provides a credible transferable inference. The distinction between 2.7.2.4 and 2.7.1.39, while requiring specific AAK-family knowledge, is grounded in well-characterized structural and size differences across multiple fungal homologs, not a fact unique to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (methyltransferase) and C (acetate kinase) are clearly excluded by EC class and structural family mismatch. B (homoserine kinase) is in the same AAK superfamily but is distinguished by the ~200-aa size difference in fungal homologs and the substrate-binding motif. The length and domain architecture of the 544-aa sequence strongly favor aspartokinase over homoserine kinase, leaving A as the most defensible choice."
  },
  "important_caveats": [
    "The UniProt annotation for this entry relies on similarity transfer (ECO:0000250 from P10869), not direct experimental characterization of the Candida albicans enzyme.",
    "The distinction between EC 2.7.2.4 and EC 2.7.1.39 within the AAK superfamily ultimately depends on substrate specificity determined by active-site residues; the length and motif arguments are strong but probabilistic rather than definitive.",
    "The reviewer-only source evidence was not available to the evaluated model; the transferable argument relies on general AAK-family knowledge learned from multiple fungal homologs."
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
  "benchmark_sequence_length": 544,
  "benchmark_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 544,
  "current_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
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
  "requested_accession": "A0A1D8PMB8",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "selected_historical_source_sequence_length": 544,
  "selected_historical_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "selected_historical_version": {
    "accession": "A0A1D8PMB8",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1D8PMB8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23777\"}}],\"reaction\":{\"ecNumber\":\"2.7.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"name\":\"L-aspartate + ATP = 4-phospho-L-aspartate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23776\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CANAL                Reviewed;         544 AA.\nAC   A0A1D8PMB8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   18-JUN-2025, entry version 39.\nDE   RecName: Full=Aspartokinase;\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};\nGN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},\nGN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartokinase;\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;\nCC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
