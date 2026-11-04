# catalytic_activity_0082

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0082.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSIALALAAAPAVLAQSQLWGQCGGIGWNGPTTCVSGATCTKINDWYHQCLPGGNNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGGNTLHEKFKARGKQYFGTEIDHYHLNNNQLMEIARREFGQITHENSMKWDATEPSRGSFSFGNADRVVDWATSNGKLIRGHTLLWHSQLPQWVQNINDRNTLTQVIENHVKTIMTRYKGKIFHYDVVNEILDENGGLRNSVFSRVLGEDFVGIAFRAARATDPDAKLYINDYNLDSANYAKTRGMINLVNKWVSQGVPIDGIGTQAHLAGPGGWNPASGVPAALQALAGANVKEVAITELDIQGAGANDYVTVANACLNVQKCVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL

[Multiple Choices]
A. cytidine(in) = cytidine(out)
B. tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
C. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
D. FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate
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

> The sequence-matched UniProt annotation identifies the protein as endo-1,4-beta-xylanase C and records the exact reaction in choice C. The catalytic-activity annotation carries an experimental evidence code linked to a publication, though the evidence here is the database record rather than an independent review of that study.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a hydrophobic signal-peptide-like segment, and the sequence lacks the features expected of a membrane transporter. A secreted, soluble fungal enzyme is consistent with extracellular carbohydrate breakdown; fungal xylanases are a common example. That provides a meaningful family-level basis for preferring the xylan-hydrolysis option C over the transport and intracellular redox/ATP-dependent reactions in the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge about secreted fungal carbohydrate-degrading enzymes give a credible, though not definitive, basis for distinguishing C among these alternatives. This inference does not require knowing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe substantially different activities, and the secreted-enzyme context favors the xylan-hydrolysis reaction.


### Important caveats

- A signal peptide and fungal context alone do not prove xylanase activity; the transferable inference is probabilistic.
- The sequence-matched source record supports the key, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, and the sequence lacks the features expected of a membrane transporter. A secreted, soluble fungal enzyme is consistent with extracellular carbohydrate breakdown; fungal xylanases are a common example. That provides a meaningful family-level basis for preferring the xylan-hydrolysis option C over the transport and intracellular redox/ATP-dependent reactions in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge about secreted fungal carbohydrate-degrading enzymes give a credible, though not definitive, basis for distinguishing C among these alternatives. This inference does not require knowing the exact protein's recorded annotation."
  },
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as endo-1,4-beta-xylanase C and records the exact reaction in choice C. The catalytic-activity annotation carries an experimental evidence code linked to a publication, though the evidence here is the database record rather than an independent review of that study."
  },
  "important_caveats": [
    "A signal peptide and fungal context alone do not prove xylanase activity; the transferable inference is probabilistic.",
    "The sequence-matched source record supports the key, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different activities, and the secreted-enzyme context favors the xylan-hydrolysis reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as endo-1,4-beta-xylanase C and records the exact reaction in choice C. The catalytic-activity annotation carries an experimental evidence code linked to a publication, though the evidence here is the database record rather than an independent review of that study.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, and the sequence lacks the features expected of a membrane transporter. A secreted, soluble fungal enzyme is consistent with extracellular carbohydrate breakdown; fungal xylanases are a common example. That provides a meaningful family-level basis for preferring the xylan-hydrolysis option C over the transport and intracellular redox/ATP-dependent reactions in the other choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge about secreted fungal carbohydrate-degrading enzymes give a credible, though not definitive, basis for distinguishing C among these alternatives. This inference does not require knowing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different activities, and the secreted-enzyme context favors the xylan-hydrolysis reaction."
  },
  "important_caveats": [
    "A signal peptide and fungal context alone do not prove xylanase activity; the transferable inference is probabilistic.",
    "The sequence-matched source record supports the key, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MEY9 (XYNC_HUMIN) is annotated as Endo-1,4-beta-xylanase C (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' matching choice C exactly. The annotation carries evidence code ECO:0000269 (experimental) from PubMed:23306124. The benchmark sequence SHA256 matches the source entry sequence in both current and historical snapshots.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish the four choices through a combination of positive identification and elimination. (1) The N-terminal hydrophobic stretch (MRSIALALAAAPAVLAQSQLW) is a classic fungal signal peptide, indicating a secreted protein. (2) The sequence lacks any transmembrane helices, ruling out choice A (cytidine transporter, which requires multiple TM segments). (3) The sequence lacks heme-binding motifs (CXXCH/FxxGxxG), FAD-binding Rossmann folds, or NADPH-cytochrome reductase domains, ruling out choice B (a P450/monooxygenase system typically >400 AA with specific cofactor-binding signatures). (4) The sequence lacks FMN-binding motifs (e.g., 'GxGxxG' in a flavin context), ruling out choice D. (5) Positively, the mature protein (~370 AA) contains motifs consistent with GH11 xylanases: the 'GKQYFGTEIDHYHL' segment matches the conserved catalytic-nucleophile region of GH11 (the 'GTE' context for the catalytic Glu), and the overall composition (Gly-rich, Asn/Ser/Thr-rich, with beta-sandwich-compatible patterns like 'GITVWGVSD') is characteristic of glycoside hydrolases acting on polysaccharides. The size, secretion signal, and absence of cofactor requirements are consistent with a secreted fungal xylanase. Among the four very different enzyme classes offered, these features meaningfully favor C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four choices represent fundamentally different enzyme classes (transporter, P450 monooxygenase, glycoside hydrolase, flavoenzyme), each requiring distinct structural/cofactor features. Elimination of A, B, and D relies on general structural biology (absence of TM helices, heme motifs, FMN motifs). Positive identification of C is supported by recognition of GH11-family sequence motifs (GKQYFG, GTE catalytic context), appropriate size for a secreted fungal GH, and composition typical of carbohydrate-active enzymes. This is transferable family-level knowledge, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct enzyme classes with mutually exclusive structural requirements. The sequence clearly lacks features for A (no TM domains), B (no heme/FAD/NADPH motifs), and D (no FMN-binding), while containing GH11-consistent motifs. No ambiguity among the offered alternatives.


### Important caveats

- The mature protein (~370 AA) is somewhat larger than canonical GH11 xylanases (typically 200-250 mature residues), but thermophilic fungal GH11 enzymes with extended regions or low-complexity linkers (the NNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGG segment) are documented.
- Precise GH family assignment (GH11 vs GH10 vs other) from sequence alone carries some uncertainty, but the question only requires distinguishing among four very different enzyme classes, for which the elimination argument is robust.
- The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269), but this was not available to the evaluated model; the model must rely on sequence-based inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish the four choices through a combination of positive identification and elimination. (1) The N-terminal hydrophobic stretch (MRSIALALAAAPAVLAQSQLW) is a classic fungal signal peptide, indicating a secreted protein. (2) The sequence lacks any transmembrane helices, ruling out choice A (cytidine transporter, which requires multiple TM segments). (3) The sequence lacks heme-binding motifs (CXXCH/FxxGxxG), FAD-binding Rossmann folds, or NADPH-cytochrome reductase domains, ruling out choice B (a P450/monooxygenase system typically >400 AA with specific cofactor-binding signatures). (4) The sequence lacks FMN-binding motifs (e.g., 'GxGxxG' in a flavin context), ruling out choice D. (5) Positively, the mature protein (~370 AA) contains motifs consistent with GH11 xylanases: the 'GKQYFGTEIDHYHL' segment matches the conserved catalytic-nucleophile region of GH11 (the 'GTE' context for the catalytic Glu), and the overall composition (Gly-rich, Asn/Ser/Thr-rich, with beta-sandwich-compatible patterns like 'GITVWGVSD') is characteristic of glycoside hydrolases acting on polysaccharides. The size, secretion signal, and absence of cofactor requirements are consistent with a secreted fungal xylanase. Among the four very different enzyme classes offered, these features meaningfully favor C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four choices represent fundamentally different enzyme classes (transporter, P450 monooxygenase, glycoside hydrolase, flavoenzyme), each requiring distinct structural/cofactor features. Elimination of A, B, and D relies on general structural biology (absence of TM helices, heme motifs, FMN motifs). Positive identification of C is supported by recognition of GH11-family sequence motifs (GKQYFG, GTE catalytic context), appropriate size for a secreted fungal GH, and composition typical of carbohydrate-active enzymes. This is transferable family-level knowledge, not a lookup of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MEY9 (XYNC_HUMIN) is annotated as Endo-1,4-beta-xylanase C (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' matching choice C exactly. The annotation carries evidence code ECO:0000269 (experimental) from PubMed:23306124. The benchmark sequence SHA256 matches the source entry sequence in both current and historical snapshots."
  },
  "important_caveats": [
    "The mature protein (~370 AA) is somewhat larger than canonical GH11 xylanases (typically 200-250 mature residues), but thermophilic fungal GH11 enzymes with extended regions or low-complexity linkers (the NNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGG segment) are documented.",
    "Precise GH family assignment (GH11 vs GH10 vs other) from sequence alone carries some uncertainty, but the question only requires distinguishing among four very different enzyme classes, for which the elimination argument is robust.",
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269), but this was not available to the evaluated model; the model must rely on sequence-based inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes with mutually exclusive structural requirements. The sequence clearly lacks features for A (no TM domains), B (no heme/FAD/NADPH motifs), and D (no FMN-binding), while containing GH11-consistent motifs. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MEY9 (XYNC_HUMIN) is annotated as Endo-1,4-beta-xylanase C (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' matching choice C exactly. The annotation carries evidence code ECO:0000269 (experimental) from PubMed:23306124. The benchmark sequence SHA256 matches the source entry sequence in both current and historical snapshots.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish the four choices through a combination of positive identification and elimination. (1) The N-terminal hydrophobic stretch (MRSIALALAAAPAVLAQSQLW) is a classic fungal signal peptide, indicating a secreted protein. (2) The sequence lacks any transmembrane helices, ruling out choice A (cytidine transporter, which requires multiple TM segments). (3) The sequence lacks heme-binding motifs (CXXCH/FxxGxxG), FAD-binding Rossmann folds, or NADPH-cytochrome reductase domains, ruling out choice B (a P450/monooxygenase system typically >400 AA with specific cofactor-binding signatures). (4) The sequence lacks FMN-binding motifs (e.g., 'GxGxxG' in a flavin context), ruling out choice D. (5) Positively, the mature protein (~370 AA) contains motifs consistent with GH11 xylanases: the 'GKQYFGTEIDHYHL' segment matches the conserved catalytic-nucleophile region of GH11 (the 'GTE' context for the catalytic Glu), and the overall composition (Gly-rich, Asn/Ser/Thr-rich, with beta-sandwich-compatible patterns like 'GITVWGVSD') is characteristic of glycoside hydrolases acting on polysaccharides. The size, secretion signal, and absence of cofactor requirements are consistent with a secreted fungal xylanase. Among the four very different enzyme classes offered, these features meaningfully favor C.",
    "missing_item_specific_fact": "",
    "reason": "The four choices represent fundamentally different enzyme classes (transporter, P450 monooxygenase, glycoside hydrolase, flavoenzyme), each requiring distinct structural/cofactor features. Elimination of A, B, and D relies on general structural biology (absence of TM helices, heme motifs, FMN motifs). Positive identification of C is supported by recognition of GH11-family sequence motifs (GKQYFG, GTE catalytic context), appropriate size for a secreted fungal GH, and composition typical of carbohydrate-active enzymes. This is transferable family-level knowledge, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes with mutually exclusive structural requirements. The sequence clearly lacks features for A (no TM domains), B (no heme/FAD/NADPH motifs), and D (no FMN-binding), while containing GH11-consistent motifs. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The mature protein (~370 AA) is somewhat larger than canonical GH11 xylanases (typically 200-250 mature residues), but thermophilic fungal GH11 enzymes with extended regions or low-complexity linkers (the NNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGG segment) are documented.",
    "Precise GH family assignment (GH11 vs GH10 vs other) from sequence alone carries some uncertainty, but the question only requires distinguishing among four very different enzyme classes, for which the elimination argument is robust.",
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269), but this was not available to the evaluated model; the model must rely on sequence-based inference."
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
  "benchmark_sequence_length": 390,
  "benchmark_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 390,
  "current_source_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MEY9",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "selected_historical_source_sequence_length": 390,
  "selected_historical_source_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "selected_historical_version": {
    "accession": "M4MEY9",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNC_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MEY9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase C\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase C\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   XYNC_HUMIN              Reviewed;         390 AA.\nAC   M4MEY9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynC {ECO:0000303|PubMed:23306124};\nGN   Synonyms=Xyl3 {ECO:0000303|PubMed:8190078},\nGN   XynW {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION.\nRX   PubMed=8190078; DOI=10.1007/bf00301060;\nRA   Dalboege H., Hansen H.P.H.;\nRT   \"A novel method for efficient expression cloning of fungal enzyme genes.\";\nRL   Mol. Gen. Genet. 243:253-260(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
