# EC_number_0074

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0074.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.3.2.27

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQPVGLSNTPASSLLNETAELRHQTTPRQLGGIRIVGEIVDISYEPNDVVFFGVGRGVMIGDILFPGSSADIMRELLMAHSGVRGILQQQENAPSSLQTRISECTFSVSQEKLQCPEEEMRCPVTLETPEKGVFVKNSGDSSVCTLFDSSSFSRLVRDGGVHPLTREPIKASMIVSSDKCVYDNAKGNFVIKNS

[Multiple Choices]
A. 2.3.1.319
B. 2.3.2.27
C. 3.2.2.19
D. 1.1.1.336
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

> The sequence-matched UniProt record assigns EC 2.3.2.27 and describes the corresponding ubiquitin-transfer reaction. The annotation is qualified as probable and supported by similarity evidence (ECO:0000250), rather than presented as direct experimental confirmation for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence supports recognition of a small bacterial NleG-type E3 ubiquitin-ligase family protein, whose transferable functional association is E2-to-substrate ubiquitin transfer. That activity matches EC 2.3.2.27 (B), unlike the acyltransferase, hydrolase, and dehydrogenase classes in the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known activity of NleG-type ubiquitin ligases provide a meaningful basis for choosing B from these alternatives without needing the exact protein's database record. The family assignment from sequence alone is an inference, not an experimental demonstration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives identify distinct reaction classes, and the inferred ubiquitin-ligase activity points specifically to B.


### Important caveats

- The reviewer-only annotation supports the key by similarity transfer; it does not establish that this exact protein's activity was experimentally measured.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence supports recognition of a small bacterial NleG-type E3 ubiquitin-ligase family protein, whose transferable functional association is E2-to-substrate ubiquitin transfer. That activity matches EC 2.3.2.27 (B), unlike the acyltransferase, hydrolase, and dehydrogenase classes in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known activity of NleG-type ubiquitin ligases provide a meaningful basis for choosing B from these alternatives without needing the exact protein's database record. The family assignment from sequence alone is an inference, not an experimental demonstration."
  },
  "case_id": "EC_number_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.2.27 and describes the corresponding ubiquitin-transfer reaction. The annotation is qualified as probable and supported by similarity evidence (ECO:0000250), rather than presented as direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key by similarity transfer; it does not establish that this exact protein's activity was experimentally measured."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives identify distinct reaction classes, and the inferred ubiquitin-ligase activity points specifically to B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.2.27 and describes the corresponding ubiquitin-transfer reaction. The annotation is qualified as probable and supported by similarity evidence (ECO:0000250), rather than presented as direct experimental confirmation for this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence supports recognition of a small bacterial NleG-type E3 ubiquitin-ligase family protein, whose transferable functional association is E2-to-substrate ubiquitin transfer. That activity matches EC 2.3.2.27 (B), unlike the acyltransferase, hydrolase, and dehydrogenase classes in the other choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known activity of NleG-type ubiquitin ligases provide a meaningful basis for choosing B from these alternatives without needing the exact protein's database record. The family assignment from sequence alone is an inference, not an experimental demonstration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives identify distinct reaction classes, and the inferred ubiquitin-ligase activity points specifically to B."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key by similarity transfer; it does not establish that this exact protein's activity was experimentally measured."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A482PJF5 annotates this protein (NleG1 from Citrobacter rodentium) as EC 2.3.2.27 with the recommended name 'Probable E3 ubiquitin-protein ligase NleG1.' The annotation carries evidence code ECO:0000250 (inferred by similarity from A0A482PDI9) and the 'Probable' qualifier, indicating computational transfer rather than direct experimental validation. The catalytic activity comment confirms the ubiquitin-transfer reaction. While the annotation is inferred by similarity, it is the recorded database annotation and is consistent with the known biology of NleG-family U-box E3 ligases.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of this 194-residue protein contains a recognizable U-box domain motif: the 'CP' nucleation motif followed by a cross-brace arrangement of Cys residues and conserved hydrophobic/polar spacing characteristic of U-box domains (e.g., 'RCPVTLETPEKGVFVKNSGDSSVCTLFDSSSFSRLVRDGGVHPLTREPIKASMIVSSDKCVYDNAKGNFVIKNS'). The U-box domain is a well-characterized domain found across many proteins (Plant U-box/PUB proteins, ARC1, TRIM proteins, bacterial NleG/SseL/SseT effectors) and is specifically associated with E3 ubiquitin-protein ligase activity, which corresponds to EC class 2.3.2 (protein-ubiquitin ligase). Among the four options, only B (2.3.2.27) falls within EC 2.3.2. Option A (2.3.1.319) is a general acyltransferase, C (3.2.2.19) is a glycosylase/hydrolase, and D (1.1.1.336) is an oxidoreductase—none of which are associated with U-box domains. A model trained on diverse protein families can recognize the U-box fold signature and map it to E3 ubiquitin ligase activity, thereby selecting B over the other three enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The U-box domain is a transferable structural/sequence motif recognized across many protein families. Its association with E3 ubiquitin ligase (EC 2.3.2) activity is a well-established biological regularity. The four options span four different EC top-level classes (2.3.1, 2.3.2, 3.2.2, 1.1.1), and U-box recognition cleanly eliminates all non-2.3.2 options. Since only one option (B) belongs to EC 2.3.2, the domain-level inference is sufficient to select the correct answer without needing to memorize this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to four distinct EC top-level categories (oxidoreductase, transferase-acyltransferase-ubiquitin ligase, transferase-acyltransferase-other, hydrolase-glycosylase). The U-box domain signature points unambiguously to E3 ubiquitin ligase (EC 2.3.2), and only option B falls in that sub-class. No other option is defensible given the domain evidence.


### Important caveats

- The UniProt annotation for this protein carries evidence code ECO:0000250 (inferred by similarity) and the 'Probable' qualifier, meaning the EC assignment is computational transfer from a homolog (A0A482PDI9), not direct experimental enzymatic characterization.
- U-box domain recognition from raw sequence is probabilistic; the domain boundary and exact residue spacing can vary among U-box proteins, so a model may not always cleanly identify the domain in every instance.
- The N-terminal ~140 residues of this protein likely correspond to the transmembrane/signal region of the NleG effector, which is not directly informative for EC classification but is consistent with the known architecture of NleG-family proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of this 194-residue protein contains a recognizable U-box domain motif: the 'CP' nucleation motif followed by a cross-brace arrangement of Cys residues and conserved hydrophobic/polar spacing characteristic of U-box domains (e.g., 'RCPVTLETPEKGVFVKNSGDSSVCTLFDSSSFSRLVRDGGVHPLTREPIKASMIVSSDKCVYDNAKGNFVIKNS'). The U-box domain is a well-characterized domain found across many proteins (Plant U-box/PUB proteins, ARC1, TRIM proteins, bacterial NleG/SseL/SseT effectors) and is specifically associated with E3 ubiquitin-protein ligase activity, which corresponds to EC class 2.3.2 (protein-ubiquitin ligase). Among the four options, only B (2.3.2.27) falls within EC 2.3.2. Option A (2.3.1.319) is a general acyltransferase, C (3.2.2.19) is a glycosylase/hydrolase, and D (1.1.1.336) is an oxidoreductase—none of which are associated with U-box domains. A model trained on diverse protein families can recognize the U-box fold signature and map it to E3 ubiquitin ligase activity, thereby selecting B over the other three enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The U-box domain is a transferable structural/sequence motif recognized across many protein families. Its association with E3 ubiquitin ligase (EC 2.3.2) activity is a well-established biological regularity. The four options span four different EC top-level classes (2.3.1, 2.3.2, 3.2.2, 1.1.1), and U-box recognition cleanly eliminates all non-2.3.2 options. Since only one option (B) belongs to EC 2.3.2, the domain-level inference is sufficient to select the correct answer without needing to memorize this specific protein's annotation."
  },
  "case_id": "EC_number_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A482PJF5 annotates this protein (NleG1 from Citrobacter rodentium) as EC 2.3.2.27 with the recommended name 'Probable E3 ubiquitin-protein ligase NleG1.' The annotation carries evidence code ECO:0000250 (inferred by similarity from A0A482PDI9) and the 'Probable' qualifier, indicating computational transfer rather than direct experimental validation. The catalytic activity comment confirms the ubiquitin-transfer reaction. While the annotation is inferred by similarity, it is the recorded database annotation and is consistent with the known biology of NleG-family U-box E3 ligases."
  },
  "important_caveats": [
    "The UniProt annotation for this protein carries evidence code ECO:0000250 (inferred by similarity) and the 'Probable' qualifier, meaning the EC assignment is computational transfer from a homolog (A0A482PDI9), not direct experimental enzymatic characterization.",
    "U-box domain recognition from raw sequence is probabilistic; the domain boundary and exact residue spacing can vary among U-box proteins, so a model may not always cleanly identify the domain in every instance.",
    "The N-terminal ~140 residues of this protein likely correspond to the transmembrane/signal region of the NleG effector, which is not directly informative for EC classification but is consistent with the known architecture of NleG-family proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four distinct EC top-level categories (oxidoreductase, transferase-acyltransferase-ubiquitin ligase, transferase-acyltransferase-other, hydrolase-glycosylase). The U-box domain signature points unambiguously to E3 ubiquitin ligase (EC 2.3.2), and only option B falls in that sub-class. No other option is defensible given the domain evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A482PJF5 annotates this protein (NleG1 from Citrobacter rodentium) as EC 2.3.2.27 with the recommended name 'Probable E3 ubiquitin-protein ligase NleG1.' The annotation carries evidence code ECO:0000250 (inferred by similarity from A0A482PDI9) and the 'Probable' qualifier, indicating computational transfer rather than direct experimental validation. The catalytic activity comment confirms the ubiquitin-transfer reaction. While the annotation is inferred by similarity, it is the recorded database annotation and is consistent with the known biology of NleG-family U-box E3 ligases.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of this 194-residue protein contains a recognizable U-box domain motif: the 'CP' nucleation motif followed by a cross-brace arrangement of Cys residues and conserved hydrophobic/polar spacing characteristic of U-box domains (e.g., 'RCPVTLETPEKGVFVKNSGDSSVCTLFDSSSFSRLVRDGGVHPLTREPIKASMIVSSDKCVYDNAKGNFVIKNS'). The U-box domain is a well-characterized domain found across many proteins (Plant U-box/PUB proteins, ARC1, TRIM proteins, bacterial NleG/SseL/SseT effectors) and is specifically associated with E3 ubiquitin-protein ligase activity, which corresponds to EC class 2.3.2 (protein-ubiquitin ligase). Among the four options, only B (2.3.2.27) falls within EC 2.3.2. Option A (2.3.1.319) is a general acyltransferase, C (3.2.2.19) is a glycosylase/hydrolase, and D (1.1.1.336) is an oxidoreductase—none of which are associated with U-box domains. A model trained on diverse protein families can recognize the U-box fold signature and map it to E3 ubiquitin ligase activity, thereby selecting B over the other three enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "The U-box domain is a transferable structural/sequence motif recognized across many protein families. Its association with E3 ubiquitin ligase (EC 2.3.2) activity is a well-established biological regularity. The four options span four different EC top-level classes (2.3.1, 2.3.2, 3.2.2, 1.1.1), and U-box recognition cleanly eliminates all non-2.3.2 options. Since only one option (B) belongs to EC 2.3.2, the domain-level inference is sufficient to select the correct answer without needing to memorize this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four distinct EC top-level categories (oxidoreductase, transferase-acyltransferase-ubiquitin ligase, transferase-acyltransferase-other, hydrolase-glycosylase). The U-box domain signature points unambiguously to E3 ubiquitin ligase (EC 2.3.2), and only option B falls in that sub-class. No other option is defensible given the domain evidence."
  },
  "important_caveats": [
    "The UniProt annotation for this protein carries evidence code ECO:0000250 (inferred by similarity) and the 'Probable' qualifier, meaning the EC assignment is computational transfer from a homolog (A0A482PDI9), not direct experimental enzymatic characterization.",
    "U-box domain recognition from raw sequence is probabilistic; the domain boundary and exact residue spacing can vary among U-box proteins, so a model may not always cleanly identify the domain in every instance.",
    "The N-terminal ~140 residues of this protein likely correspond to the transmembrane/signal region of the NleG effector, which is not directly informative for EC classification but is consistent with the known architecture of NleG-family proteins."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "17a28673ea92d670244ad260f112490615dd461a6534eadb8fb2e57c4e73267c",
  "current_entry_audit": {
    "entryVersion": 12,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "17a28673ea92d670244ad260f112490615dd461a6534eadb8fb2e57c4e73267c",
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
  "requested_accession": "A0A482PJF5",
  "selected_historical_entry_version": 11,
  "selected_historical_record_sha256": "f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "17a28673ea92d670244ad260f112490615dd461a6534eadb8fb2e57c4e73267c",
  "selected_historical_version": {
    "accession": "A0A482PJF5",
    "database": "Swiss-Prot",
    "entryVersion": 11,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NLEG1_CITRO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A482PJF5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:19.612966+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJF5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":12,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:19.612966+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJF5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Citrobacter\"],\"scientificName\":\"Citrobacter rodentium\",\"taxonId\":67825}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:19.612966+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJF5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A482PDI9\",\"source\":\"UniProtKB\"}],\"value\":\"2.3.2.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable E3 ubiquitin-protein ligase NleG1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:19.612966+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJF5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.2.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A482PDI9\",\"source\":\"UniProtKB\"}],\"name\":\"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:19.612966+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJF5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H1",
  "excerpt": "ID   NLEG1_CITRO             Reviewed;         194 AA.\nAC   A0A482PJF5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 11.\nDE   RecName: Full=Probable E3 ubiquitin-protein ligase NleG1 {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000250|UniProtKB:A0A482PDI9};\nGN   Name=nleG1 {ECO:0000303|PubMed:36511702};\nGN   ORFNames=E2R62_04780 {ECO:0000312|EMBL:QBY28229.1};\nOS   Citrobacter rodentium.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Citrobacter.\nOX   NCBI_TaxID=67825;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:21.816588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c",
  "url": "https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Probable E3 ubiquitin-protein ligase NleG1 {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000250|UniProtKB:A0A482PDI9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:21.816588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c",
  "url": "https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION, INDUCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=DBS100;\nRX   PubMed=36511702; DOI=10.1128/iai.00505-22;\nRA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,\nRA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;\nRT   \"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for\nRT   Different Roles during Citrobacter rodentium Infection in Mice.\";\nRL   Infect. Immun. 91:e0050522-e0050522(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:21.816588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c",
  "url": "https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +\nCC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-\nCC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;\nCC         EC=2.3.2.27; Evidence={ECO:0000250|UniProtKB:A0A482PDI9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:21.816588+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c",
  "url": "https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 74. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
