# GO_molecular_function_0111

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0111.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — methyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKYAHVGLNVTNLEKSIEFYSKLFGAEPVKVKPDYAKFLLESPGLNFTLNLRDEVNGNQVGHFGIQVESTEEVVAHKNRLAENGILSQYDEINTTCCYALQDKFWIHDPDGNEWEFFYTKTTVEENSTHPPTCCVNEPNVEKAECCSPTASSNKDTSNCCS

[Multiple Choices]
A. nicotinate-nucleotide adenylyltransferase activity
B. snRNA methyltransferase activity
C. iron-sulfur cluster chaperone activity
D. methyltransferase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The sequence-matched record describes an experimentally supported nonheme iron-dependent dioxygenase that oxidatively demethylates methylarsonous acid and cleaves carbon–arsenic bonds. Demethylation is not methyl-group transfer, so it does not support methyltransferase activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence alone provides no sufficiently clear transferable feature to select one of these alternatives, and the actual enzyme activity is not represented by any option. Thus there is no defensible choice among the offered answers based on the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the options describes the documented dioxygenase activity; the problem is a missing correct alternative, not multiple equally defensible choices.


### Important caveats

- The supporting functional evidence is reviewer-only, not information supplied to the evaluated model.
- The sequence matches the cited UniProt record; the cited functional claims are experimentally evidenced in that record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "",
    "reason": "The sequence alone provides no sufficiently clear transferable feature to select one of these alternatives, and the actual enzyme activity is not represented by any option. Thus there is no defensible choice among the offered answers based on the original input."
  },
  "case_id": "GO_molecular_function_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record describes an experimentally supported nonheme iron-dependent dioxygenase that oxidatively demethylates methylarsonous acid and cleaves carbon–arsenic bonds. Demethylation is not methyl-group transfer, so it does not support methyltransferase activity."
  },
  "important_caveats": [
    "The supporting functional evidence is reviewer-only, not information supplied to the evaluated model.",
    "The sequence matches the cited UniProt record; the cited functional claims are experimentally evidenced in that record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the options describes the documented dioxygenase activity; the problem is a missing correct alternative, not multiple equally defensible choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0111",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record describes an experimentally supported nonheme iron-dependent dioxygenase that oxidatively demethylates methylarsonous acid and cleaves carbon–arsenic bonds. Demethylation is not methyl-group transfer, so it does not support methyltransferase activity.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "",
    "reason": "The sequence alone provides no sufficiently clear transferable feature to select one of these alternatives, and the actual enzyme activity is not represented by any option. Thus there is no defensible choice among the offered answers based on the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the options describes the documented dioxygenase activity; the problem is a missing correct alternative, not multiple equally defensible choices."
  },
  "important_caveats": [
    "The supporting functional evidence is reviewer-only, not information supplied to the evaluated model.",
    "The sequence matches the cited UniProt record; the cited functional claims are experimentally evidenced in that record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt entry (A0A059WI14, ARSI_BACX0) annotates this protein as a nonheme iron-dependent dioxygenase (GO:0051213, EC 1.13.11.-) that catalyzes oxygen-dependent demethylation of methylarsonous acid: methylarsonous acid + AH2 + O2 → arsenite + methanol + A + H(+). This is a C-As lyase/dioxygenase reaction, NOT a methyltransferase reaction. Methyltransferase activity (GO:0008168, EC 2.1.1.-) is defined as 'Catalysis of the transfer of a methyl group to an acceptor molecule,' which is mechanistically opposite to what this enzyme does (it removes a methyl group via oxygen-dependent cleavage, releasing methanol). The GO annotations present are dioxygenase activity and metal ion binding; methyltransferase activity is not annotated. The expected answer D is contradicted by the experimental evidence (PubMed:24821808, PubMed:28936873).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [H9](#evidence-h9), [H10](#evidence-h10), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The correct molecular function for this protein is dioxygenase activity (GO:0051213, EC 1.13.11.-), which is not offered among the four choices. The expected answer 'methyltransferase activity' is scientifically incorrect for this protein. No legitimate sequence-based reasoning from the 161-residue sequence would lead to 'methyltransferase activity': the protein lacks a Rossmann-fold SAM-binding motif typical of methyltransferases, is unusually small for a methyltransferase (161 aa vs. typical 200-400+ aa), and its cysteine-rich C-terminal region is more consistent with a small metalloenzyme. The only path to selecting D would be an erroneous annotation lookup conflating 'demethylase' with 'methyltransferase,' which are mechanistically opposite activities.


**Reason**

> The expected answer D is contradicted by the evidence. The protein is a dioxygenase (C-As lyase), not a methyltransferase. The correct GO term (dioxygenase activity) is absent from the options. Among the four offered choices, none correctly describes this protein's molecular function. A model reasoning from sequence features (small size, lack of SAM-binding motifs, cysteine clusters) would not arrive at 'methyltransferase activity.' The expected answer appears to stem from a confusion between 'demethylase' (removes methyl groups via oxygen-dependent cleavage) and 'methyltransferase' (transfers methyl groups to acceptors), which are opposite activities. No transferable biological knowledge supports selecting D over the other options for this sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options correctly describes this protein's molecular function. The correct answer (dioxygenase activity / C-As lyase activity) is not offered. The expected answer D is scientifically contradicted by experimental evidence. The question is fundamentally flawed because the correct function is absent from the choices.


### Important caveats

- The expected answer D (methyltransferase activity) is contradicted by the protein's experimentally characterized function as a nonheme iron-dependent dioxygenase (EC 1.13.11.-). The confusion likely arises from the alternative name 'Methylarsonous acid demethylase,' but demethylation via oxygen-dependent C-As bond cleavage is mechanistically distinct from methyltransferase (EC 2.1.1.-) activity.
- The correct GO molecular function term (GO:0051213, dioxygenase activity) annotated in UniProt is not among the offered options, making the question unanswerable as posed.
- The UniProt entry was first public on 2025-04-09; the benchmark construction date is unknown, but the sequence and experimental annotations (from 2014 and 2017 papers) are consistent regardless of entry version.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and the UniProt entry, so the annotation applies to the exact protein in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The correct molecular function for this protein is dioxygenase activity (GO:0051213, EC 1.13.11.-), which is not offered among the four choices. The expected answer 'methyltransferase activity' is scientifically incorrect for this protein. No legitimate sequence-based reasoning from the 161-residue sequence would lead to 'methyltransferase activity': the protein lacks a Rossmann-fold SAM-binding motif typical of methyltransferases, is unusually small for a methyltransferase (161 aa vs. typical 200-400+ aa), and its cysteine-rich C-terminal region is more consistent with a small metalloenzyme. The only path to selecting D would be an erroneous annotation lookup conflating 'demethylase' with 'methyltransferase,' which are mechanistically opposite activities.",
    "reason": "The expected answer D is contradicted by the evidence. The protein is a dioxygenase (C-As lyase), not a methyltransferase. The correct GO term (dioxygenase activity) is absent from the options. Among the four offered choices, none correctly describes this protein's molecular function. A model reasoning from sequence features (small size, lack of SAM-binding motifs, cysteine clusters) would not arrive at 'methyltransferase activity.' The expected answer appears to stem from a confusion between 'demethylase' (removes methyl groups via oxygen-dependent cleavage) and 'methyltransferase' (transfers methyl groups to acceptors), which are opposite activities. No transferable biological knowledge supports selecting D over the other options for this sequence."
  },
  "case_id": "GO_molecular_function_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "H9",
      "H10",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry (A0A059WI14, ARSI_BACX0) annotates this protein as a nonheme iron-dependent dioxygenase (GO:0051213, EC 1.13.11.-) that catalyzes oxygen-dependent demethylation of methylarsonous acid: methylarsonous acid + AH2 + O2 → arsenite + methanol + A + H(+). This is a C-As lyase/dioxygenase reaction, NOT a methyltransferase reaction. Methyltransferase activity (GO:0008168, EC 2.1.1.-) is defined as 'Catalysis of the transfer of a methyl group to an acceptor molecule,' which is mechanistically opposite to what this enzyme does (it removes a methyl group via oxygen-dependent cleavage, releasing methanol). The GO annotations present are dioxygenase activity and metal ion binding; methyltransferase activity is not annotated. The expected answer D is contradicted by the experimental evidence (PubMed:24821808, PubMed:28936873)."
  },
  "important_caveats": [
    "The expected answer D (methyltransferase activity) is contradicted by the protein's experimentally characterized function as a nonheme iron-dependent dioxygenase (EC 1.13.11.-). The confusion likely arises from the alternative name 'Methylarsonous acid demethylase,' but demethylation via oxygen-dependent C-As bond cleavage is mechanistically distinct from methyltransferase (EC 2.1.1.-) activity.",
    "The correct GO molecular function term (GO:0051213, dioxygenase activity) annotated in UniProt is not among the offered options, making the question unanswerable as posed.",
    "The UniProt entry was first public on 2025-04-09; the benchmark construction date is unknown, but the sequence and experimental annotations (from 2014 and 2017 papers) are consistent regardless of entry version.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and the UniProt entry, so the annotation applies to the exact protein in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options correctly describes this protein's molecular function. The correct answer (dioxygenase activity / C-As lyase activity) is not offered. The expected answer D is scientifically contradicted by experimental evidence. The question is fundamentally flawed because the correct function is absent from the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0111",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry (A0A059WI14, ARSI_BACX0) annotates this protein as a nonheme iron-dependent dioxygenase (GO:0051213, EC 1.13.11.-) that catalyzes oxygen-dependent demethylation of methylarsonous acid: methylarsonous acid + AH2 + O2 → arsenite + methanol + A + H(+). This is a C-As lyase/dioxygenase reaction, NOT a methyltransferase reaction. Methyltransferase activity (GO:0008168, EC 2.1.1.-) is defined as 'Catalysis of the transfer of a methyl group to an acceptor molecule,' which is mechanistically opposite to what this enzyme does (it removes a methyl group via oxygen-dependent cleavage, releasing methanol). The GO annotations present are dioxygenase activity and metal ion binding; methyltransferase activity is not annotated. The expected answer D is contradicted by the experimental evidence (PubMed:24821808, PubMed:28936873).",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5", "H9", "H10", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The correct molecular function for this protein is dioxygenase activity (GO:0051213, EC 1.13.11.-), which is not offered among the four choices. The expected answer 'methyltransferase activity' is scientifically incorrect for this protein. No legitimate sequence-based reasoning from the 161-residue sequence would lead to 'methyltransferase activity': the protein lacks a Rossmann-fold SAM-binding motif typical of methyltransferases, is unusually small for a methyltransferase (161 aa vs. typical 200-400+ aa), and its cysteine-rich C-terminal region is more consistent with a small metalloenzyme. The only path to selecting D would be an erroneous annotation lookup conflating 'demethylase' with 'methyltransferase,' which are mechanistically opposite activities.",
    "reason": "The expected answer D is contradicted by the evidence. The protein is a dioxygenase (C-As lyase), not a methyltransferase. The correct GO term (dioxygenase activity) is absent from the options. Among the four offered choices, none correctly describes this protein's molecular function. A model reasoning from sequence features (small size, lack of SAM-binding motifs, cysteine clusters) would not arrive at 'methyltransferase activity.' The expected answer appears to stem from a confusion between 'demethylase' (removes methyl groups via oxygen-dependent cleavage) and 'methyltransferase' (transfers methyl groups to acceptors), which are opposite activities. No transferable biological knowledge supports selecting D over the other options for this sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options correctly describes this protein's molecular function. The correct answer (dioxygenase activity / C-As lyase activity) is not offered. The expected answer D is scientifically contradicted by experimental evidence. The question is fundamentally flawed because the correct function is absent from the choices."
  },
  "important_caveats": [
    "The expected answer D (methyltransferase activity) is contradicted by the protein's experimentally characterized function as a nonheme iron-dependent dioxygenase (EC 1.13.11.-). The confusion likely arises from the alternative name 'Methylarsonous acid demethylase,' but demethylation via oxygen-dependent C-As bond cleavage is mechanistically distinct from methyltransferase (EC 2.1.1.-) activity.",
    "The correct GO molecular function term (GO:0051213, dioxygenase activity) annotated in UniProt is not among the offered options, making the question unanswerable as posed.",
    "The UniProt entry was first public on 2025-04-09; the benchmark construction date is unknown, but the sequence and experimental annotations (from 2014 and 2017 papers) are consistent regardless of entry version.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and the UniProt entry, so the annotation applies to the exact protein in the question."
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
  "benchmark_sequence_length": 161,
  "benchmark_sequence_sha256": "630a5e1022193a240664c838cafc0c7d8aba4c00729a8de18bb80e3a504feff9",
  "current_entry_audit": {
    "entryVersion": 23,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-09-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 161,
  "current_source_sequence_sha256": "630a5e1022193a240664c838cafc0c7d8aba4c00729a8de18bb80e3a504feff9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 22,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A059WI14",
  "selected_historical_entry_version": 22,
  "selected_historical_record_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "selected_historical_source_sequence_length": 161,
  "selected_historical_source_sequence_sha256": "630a5e1022193a240664c838cafc0c7d8aba4c00729a8de18bb80e3a504feff9",
  "selected_historical_version": {
    "accession": "A0A059WI14",
    "database": "Swiss-Prot",
    "entryVersion": 22,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ARSI_BACX0",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A059WI14\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":23,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-09-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\"],\"scientificName\":\"Bacillus sp. (strain MD1)\",\"taxonId\":1501233}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"Arsenic inducible gene ArsI\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"value\":\"C-As lyase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"Methylarsonous acid demethylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"MAs(III) demethylase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"value\":\"1.13.11.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"Trivalent organoarsenical cleaving enzyme\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"value\":\"Nonheme iron-dependent dioxygenase that can break carbon-arsenic bonds, playing a role in the detoxification of environmental organoarsenical compounds. Catalyzes the oxygen-dependent demethylation of highly toxic methylarsonous acid (MAs(III)) to arsenite, which can then be exported out of the cell. Can also cleave the C-As bond in several trivalent aromatic arsenicals, including roxarsone (III), nitarsone (III) and (4-aminophenyl)arsonous acid. Organoarsenical degradation by this enzyme is proposed to have a significant impact on the arsenic biogeocycle that maintains a balance between organic and inorganic species\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82324\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"name\":\"methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82323\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17790\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17826\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82364\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"name\":\"roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82363\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231974\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231975\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82440\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"name\":\"nitarsone (III) + AH2 + O2 = 4-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82439\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232329\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82444\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"name\":\"4-aminophenylarsonous acid + AH2 + O2 = 4-aminocyclohexa-2,5-dien-1-one + arsenite + A\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82443\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:50022\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232331\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Yoshinaga M.\",\"Rosen B.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24821808\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1403057111\"}],\"citationType\":\"journal article\",\"firstPage\":\"7701\",\"id\":\"24821808\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"7706\",\"publicationDate\":\"2014\",\"title\":\"A C-As lyase for degradation of environmental organoarsenical herbicides and animal husbandry growth promoters.\",\"volume\":\"111\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"MD1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Pawitwar S.S.\",\"Nadar V.S.\",\"Kandegedara A.\",\"Stemmler T.L.\",\"Rosen B.P.\",\"Yoshinaga M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28936873\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.est.7b03180\"}],\"citationType\":\"journal article\",\"firstPage\":\"11115\",\"id\":\"28936873\",\"journal\":\"Environ. Sci. Technol.\",\"lastPage\":\"11125\",\"publicationDate\":\"2017\",\"title\":\"Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation of Environmental Organoarsenicals.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"MD1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"3D-STRUCTURE MODELING\",\"MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H1",
  "excerpt": "ID   ARSI_BACX0              Reviewed;         161 AA.\nAC   A0A059WI14;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-SEP-2014, sequence version 1.\nDT   28-JAN-2026, entry version 22.\nDE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305|PubMed:24821808};\nDE            EC=1.13.11.- {ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};\nDE   AltName: Full=Arsenic inducible gene ArsI {ECO:0000303|PubMed:24821808};\nDE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24821808, ECO:0000303|PubMed:28936873};\nDE   AltName: Full=Methylarsonous acid demethylase {ECO:0000303|PubMed:24821808};\nDE            Short=MAs(III) demethylase {ECO:0000303|PubMed:24821808};\nGN   Name=arsI {ECO:0000303|PubMed:24821808, ECO:0000312|EMBL:AIA09488.1};\nOS   Bacillus sp. (strain MD1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus.\nOX   NCBI_TaxID=1501233;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=MD1;\nRX   PubMed=24821808; DOI=10.1073/pnas.1403057111;\nRA   Yoshinaga M., Rosen B.P.;\nRT   \"A C-As lyase for degradation of environmental organoarsenical herbicides\nRT   and animal husbandry growth promoters.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 111:7701-7706(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, 3D-STRUCTURE\nRP   MODELING, AND MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115.\nRC   STRAIN=MD1;\nRX   PubMed=28936873; DOI=10.1021/acs.est.7b03180;\nRA   Pawitwar S.S., Nadar V.S., Kandegedara A., Stemmler T.L., Rosen B.P.,\nRA   Yoshinaga M.;\nRT   \"Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation\nRT   of Environmental Organoarsenicals.\";\nRL   Environ. Sci. Technol. 51:11115-11125(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Nonheme iron-dependent dioxygenase that can break carbon-\nCC       arsenic bonds, playing a role in the detoxification of environmental\nCC       organoarsenical compounds. Catalyzes the oxygen-dependent demethylation\nCC       of highly toxic methylarsonous acid (MAs(III)) to arsenite, which can\nCC       then be exported out of the cell. Can also cleave the C-As bond in\nCC       several trivalent aromatic arsenicals, including roxarsone (III),\nCC       nitarsone (III) and (4-aminophenyl)arsonous acid. Organoarsenical\nCC       degradation by this enzyme is proposed to have a significant impact on\nCC       the arsenic biogeocycle that maintains a balance between organic and\nCC       inorganic species. {ECO:0000269|PubMed:24821808,\nCC       ECO:0000269|PubMed:28936873}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=methylarsonous acid + AH2 + O2 = arsenite + methanol + A +\nCC         H(+); Xref=Rhea:RHEA:82323, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:17499, ChEBI:CHEBI:17790,\nCC         ChEBI:CHEBI:17826, ChEBI:CHEBI:29242;\nCC         Evidence={ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82324;\nCC         Evidence={ECO:0000269|PubMed:24821808};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-\nCC         dien-1-one + arsenite + A + H(+); Xref=Rhea:RHEA:82363,\nCC         ChEBI:CHEBI:13193, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:17499, ChEBI:CHEBI:29242, ChEBI:CHEBI:231974,\nCC         ChEBI:CHEBI:231975; Evidence={ECO:0000269|PubMed:24821808,\nCC         ECO:0000269|PubMed:28936873};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82364;\nCC         Evidence={ECO:0000269|PubMed:24821808};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=nitarsone (III) + AH2 + O2 = 4-nitrocyclohexa-2,5-dien-1-one +\nCC         arsenite + A + H(+); Xref=Rhea:RHEA:82439, ChEBI:CHEBI:13193,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:17499,\nCC         ChEBI:CHEBI:29242, ChEBI:CHEBI:232329, ChEBI:CHEBI:232330;\nCC         Evidence={ECO:0000269|PubMed:24821808};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82440;\nCC         Evidence={ECO:0000305|PubMed:24821808};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-aminophenylarsonous acid + AH2 + O2 = 4-aminocyclohexa-2,5-\nCC         dien-1-one + arsenite + A; Xref=Rhea:RHEA:82443, ChEBI:CHEBI:13193,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:17499, ChEBI:CHEBI:29242,\nCC         ChEBI:CHEBI:50022, ChEBI:CHEBI:232331;\nCC         Evidence={ECO:0000269|PubMed:24821808};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82444;\nCC         Evidence={ECO:0000305|PubMed:24821808};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0051213; F:dioxygenase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004515\nname: nicotinate-nucleotide adenylyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: nicotinate beta-D-ribonucleotide + ATP + H+ = deamido-NAD+ + diphosphate.\" [RHEA:22860]\nsynonym: \"ATP:nicotinate-nucleotide adenylyltransferase activity\" EXACT []\nsynonym: \"ATP:nicotinate-ribonucleotide adenylyltransferase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD(+) diphosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD(+) pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD+ pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamidonicotinamide adenine dinucleotide pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"NaMN-ATase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"nicotinate mononucleotide adenylyltransferase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"nicotinic acid mononucleotide adenylyltransferase\" NARROW []\nxref: EC:2.7.7.18\nxref: MetaCyc:NICONUCADENYLYLTRAN-RXN\nxref: Reactome:R-HSA-197235 \"NMNAT2 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: Reactome:R-HSA-200474 \"NMNAT3 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: Reactome:R-HSA-200512 \"NMNAT1 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: RHEA:22860\nis_a: GO:0070566 ! adenylyltransferase activity\nproperty_value: skos:exactMatch EC:2.7.7.18\nproperty_value: skos:exactMatch MetaCyc:NICONUCADENYLYLTRAN-RXN\nproperty_value: skos:exactMatch RHEA:22860\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004515",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 43770-43794",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0008168\nname: methyltransferase activity\nnamespace: molecular_function\nalt_id: GO:0004480\ndef: \"Catalysis of the transfer of a methyl group to an acceptor molecule.\" [ISBN:0198506732]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"methylase\" BROAD []\nxref: EC:2.1.1.-\nxref: Reactome:R-HSA-212269 \"DNMT1,3A,3B:PRC2 methylates cytosine and histone H3\"\nxref: Reactome:R-HSA-379387 \"COMT transfers Met to DA to form 3MT\"\nxref: Reactome:R-HSA-379464 \"COMT transfers Met to DOPAC to form HVA\"\nxref: Reactome:R-HSA-5333608 \"GSSebGalNac is reduced and methylated to MeSebGalNac\"\nxref: Reactome:R-HSA-6800149 \"N6AMT1:TRMT112 transfers CH3 group from AdoMet to MMAIII\"\nxref: Reactome:R-HSA-71286 \"guanidinoacetate + S-adenosylmethionine => creatine + S-adenosylhomocysteine\"\nxref: Reactome:R-HSA-9710490 \"The GSDME gene promoter is hypermethylated\"\nis_a: GO:0016741 ! transferase activity, transferring one-carbon groups\nproperty_value: skos:exactMatch EC:2.1.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008168",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 80267-80287",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0106346\nname: snRNA methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group from a donor to a nucleoside residue in an snRNA molecule.\" [PMID:27573892]\nis_a: GO:0008173 ! RNA methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106346",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 429765-429771",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0140132\nname: iron-sulfur cluster chaperone activity\nnamespace: molecular_function\ndef: \"Binding to an iron-sulfur cluster and delivering it to an acceptor molecule.\" [PMID:22966982, PMID:29051382]\nsynonym: \"iron-sulfur cluster carrier activity\" EXACT []\nis_a: GO:0016530 ! metallochaperone activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140132",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 437539-437546",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
