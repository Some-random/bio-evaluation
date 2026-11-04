# EC_number_0169

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0169.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAVVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPLVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTSAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. 3.2.1.8
B. 3.2.1.18
C. 1.1.1.336
D. 3.1.3.112
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

> The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-xylosidic linkages in xylans. The EC assignment is attributed to a PROSITE-ProRule computational annotation, so this supports the key as a database annotation but is not, by itself, direct experimental confirmation of catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a likely N-terminal secretion signal followed by a compact, aromatic-rich fungal glycoside-hydrolase domain of the sort associated with secreted endo-xylanases. Recognizing the transferable sequence/family pattern favors xylanase EC 3.2.1.8 over cellulase EC 3.2.1.18; the dehydrogenase and phosphatase options are still less compatible with this secreted glycosidase-like sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition provides a meaningful basis for distinguishing the xylanase choice from the offered alternatives without recalling this exact protein's database entry. The sequence alone may not establish the precise substrate specificity with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence-level family inference, although distinguishing closely related glycosidase activities from sequence alone has some uncertainty.


### Important caveats

- The supplied source evidence identifies the EC assignment as computationally inferred; it does not establish direct experimental verification of the reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely N-terminal secretion signal followed by a compact, aromatic-rich fungal glycoside-hydrolase domain of the sort associated with secreted endo-xylanases. Recognizing the transferable sequence/family pattern favors xylanase EC 3.2.1.8 over cellulase EC 3.2.1.18; the dehydrogenase and phosphatase options are still less compatible with this secreted glycosidase-like sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful basis for distinguishing the xylanase choice from the offered alternatives without recalling this exact protein's database entry. The sequence alone may not establish the precise substrate specificity with certainty."
  },
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-xylosidic linkages in xylans. The EC assignment is attributed to a PROSITE-ProRule computational annotation, so this supports the key as a database annotation but is not, by itself, direct experimental confirmation of catalytic activity."
  },
  "important_caveats": [
    "The supplied source evidence identifies the EC assignment as computationally inferred; it does not establish direct experimental verification of the reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level family inference, although distinguishing closely related glycosidase activities from sequence alone has some uncertainty."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-xylosidic linkages in xylans. The EC assignment is attributed to a PROSITE-ProRule computational annotation, so this supports the key as a database annotation but is not, by itself, direct experimental confirmation of catalytic activity.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a likely N-terminal secretion signal followed by a compact, aromatic-rich fungal glycoside-hydrolase domain of the sort associated with secreted endo-xylanases. Recognizing the transferable sequence/family pattern favors xylanase EC 3.2.1.8 over cellulase EC 3.2.1.18; the dehydrogenase and phosphatase options are still less compatible with this secreted glycosidase-like sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful basis for distinguishing the xylanase choice from the offered alternatives without recalling this exact protein's database entry. The sequence alone may not establish the precise substrate specificity with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level family inference, although distinguishing closely related glycosidase activities from sequence alone has some uncertainty."
  },
  "important_caveats": [
    "The supplied source evidence identifies the EC assignment as computationally inferred; it does not establish direct experimental verification of the reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0G4KL96 annotates EC 3.2.1.8 (endo-1,4-beta-xylanase) with evidence code ECO:0000255 (PROSITE-ProRule PRU01097), and the alternative name is 'Endo-1,4-beta-xylanase EIX3.' The catalytic activity comment confirms 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The PubMed reference (33205907) describes the protein as an EIX-like protein from Verticillium dahliae. The EC assignment is based on PROSITE-ProRule pattern matching (computational/curatorial), not direct enzymatic assay, but the sequence features are consistent with GH10 xylanase activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-known GH10 (glycoside hydrolase family 10) xylanase motifs: the 'TDGG' catalytic motif (acid/base region), 'GWNPG' motif, 'TYNP'/'NYNP' motifs, 'WTRNP' motif, and 'VVENFG' motif. These are diagnostic family-level signatures of GH10 endo-1,4-beta-xylanases (EC 3.2.1.8) found across many fungal and bacterial xylanases. EC 3.2.1.18 (arabinofuranosidase, GH43/GH51) has entirely different catalytic motifs (e.g., D-E-W catalytic triad in GH43, not TDGG). EC 1.1.1.336 (oxidoreductase) and EC 3.1.3.112 (phosphatase) belong to completely different enzyme classes with no glycoside hydrolase motifs. The N-terminal signal peptide (MVCFSSLFVAASAIAVVFASPVDHEQ) is consistent with a secreted fungal enzyme. The C-terminal region with 'GGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL' resembles a fungal cell-wall-binding or linker region common in secreted fungal hydrolases. A knowledgeable model recognizing the TDGG and other GH10 motifs can confidently assign EC 3.2.1.8 over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH10 xylanase family motifs (TDGG, GWNPG, TYNP, WTRNP, VVENFG) are extensively documented across hundreds of characterized xylanases in fungi and bacteria. Recognizing these motifs is standard transferable knowledge in enzymology. The four options span three different EC classes (3.2.1.x hydrolases, 1.1.x.x oxidoreductase, 3.1.3.x phosphatase), and the hydrolase sub-class distinction (GH10 vs GH43) is made by the specific motif pattern. No target-specific annotation is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GH10-specific motifs clearly distinguish option A (3.2.1.8) from B (3.2.1.18, GH43 arabinofuranosidase), C (1.1.1.336, oxidoreductase), and D (3.1.3.112, phosphatase). No other option is defensible given the sequence features.


### Important caveats

- The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct enzymatic assay. However, the sequence motifs are unambiguous for GH10 family membership.
- The 'ethylene-inducing' activity of EIX proteins is a biological elicitor function separate from the xylanase catalytic activity; the EC number refers to the catalytic reaction.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the sequence-based reasoning stands independently.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-known GH10 (glycoside hydrolase family 10) xylanase motifs: the 'TDGG' catalytic motif (acid/base region), 'GWNPG' motif, 'TYNP'/'NYNP' motifs, 'WTRNP' motif, and 'VVENFG' motif. These are diagnostic family-level signatures of GH10 endo-1,4-beta-xylanases (EC 3.2.1.8) found across many fungal and bacterial xylanases. EC 3.2.1.18 (arabinofuranosidase, GH43/GH51) has entirely different catalytic motifs (e.g., D-E-W catalytic triad in GH43, not TDGG). EC 1.1.1.336 (oxidoreductase) and EC 3.1.3.112 (phosphatase) belong to completely different enzyme classes with no glycoside hydrolase motifs. The N-terminal signal peptide (MVCFSSLFVAASAIAVVFASPVDHEQ) is consistent with a secreted fungal enzyme. The C-terminal region with 'GGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL' resembles a fungal cell-wall-binding or linker region common in secreted fungal hydrolases. A knowledgeable model recognizing the TDGG and other GH10 motifs can confidently assign EC 3.2.1.8 over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase family motifs (TDGG, GWNPG, TYNP, WTRNP, VVENFG) are extensively documented across hundreds of characterized xylanases in fungi and bacteria. Recognizing these motifs is standard transferable knowledge in enzymology. The four options span three different EC classes (3.2.1.x hydrolases, 1.1.x.x oxidoreductase, 3.1.3.x phosphatase), and the hydrolase sub-class distinction (GH10 vs GH43) is made by the specific motif pattern. No target-specific annotation is needed."
  },
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0G4KL96 annotates EC 3.2.1.8 (endo-1,4-beta-xylanase) with evidence code ECO:0000255 (PROSITE-ProRule PRU01097), and the alternative name is 'Endo-1,4-beta-xylanase EIX3.' The catalytic activity comment confirms 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The PubMed reference (33205907) describes the protein as an EIX-like protein from Verticillium dahliae. The EC assignment is based on PROSITE-ProRule pattern matching (computational/curatorial), not direct enzymatic assay, but the sequence features are consistent with GH10 xylanase activity."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct enzymatic assay. However, the sequence motifs are unambiguous for GH10 family membership.",
    "The 'ethylene-inducing' activity of EIX proteins is a biological elicitor function separate from the xylanase catalytic activity; the EC number refers to the catalytic reaction.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the sequence-based reasoning stands independently."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH10-specific motifs clearly distinguish option A (3.2.1.8) from B (3.2.1.18, GH43 arabinofuranosidase), C (1.1.1.336, oxidoreductase), and D (3.1.3.112, phosphatase). No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0G4KL96 annotates EC 3.2.1.8 (endo-1,4-beta-xylanase) with evidence code ECO:0000255 (PROSITE-ProRule PRU01097), and the alternative name is 'Endo-1,4-beta-xylanase EIX3.' The catalytic activity comment confirms 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The PubMed reference (33205907) describes the protein as an EIX-like protein from Verticillium dahliae. The EC assignment is based on PROSITE-ProRule pattern matching (computational/curatorial), not direct enzymatic assay, but the sequence features are consistent with GH10 xylanase activity.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-known GH10 (glycoside hydrolase family 10) xylanase motifs: the 'TDGG' catalytic motif (acid/base region), 'GWNPG' motif, 'TYNP'/'NYNP' motifs, 'WTRNP' motif, and 'VVENFG' motif. These are diagnostic family-level signatures of GH10 endo-1,4-beta-xylanases (EC 3.2.1.8) found across many fungal and bacterial xylanases. EC 3.2.1.18 (arabinofuranosidase, GH43/GH51) has entirely different catalytic motifs (e.g., D-E-W catalytic triad in GH43, not TDGG). EC 1.1.1.336 (oxidoreductase) and EC 3.1.3.112 (phosphatase) belong to completely different enzyme classes with no glycoside hydrolase motifs. The N-terminal signal peptide (MVCFSSLFVAASAIAVVFASPVDHEQ) is consistent with a secreted fungal enzyme. The C-terminal region with 'GGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL' resembles a fungal cell-wall-binding or linker region common in secreted fungal hydrolases. A knowledgeable model recognizing the TDGG and other GH10 motifs can confidently assign EC 3.2.1.8 over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase family motifs (TDGG, GWNPG, TYNP, WTRNP, VVENFG) are extensively documented across hundreds of characterized xylanases in fungi and bacteria. Recognizing these motifs is standard transferable knowledge in enzymology. The four options span three different EC classes (3.2.1.x hydrolases, 1.1.x.x oxidoreductase, 3.1.3.x phosphatase), and the hydrolase sub-class distinction (GH10 vs GH43) is made by the specific motif pattern. No target-specific annotation is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH10-specific motifs clearly distinguish option A (3.2.1.8) from B (3.2.1.18, GH43 arabinofuranosidase), C (1.1.1.336, oxidoreductase), and D (3.1.3.112, phosphatase). No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct enzymatic assay. However, the sequence motifs are unambiguous for GH10 family membership.",
    "The 'ethylene-inducing' activity of EIX proteins is a biological elicitor function separate from the xylanase catalytic activity; the EC number refers to the catalytic reaction.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the sequence-based reasoning stands independently."
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
  "benchmark_sequence_length": 287,
  "benchmark_sequence_sha256": "15441327e40b4a507f2d749497c8c4cbcbed343d618fb80e7789fe007d17270c",
  "current_entry_audit": {
    "entryVersion": 37,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 287,
  "current_source_sequence_sha256": "15441327e40b4a507f2d749497c8c4cbcbed343d618fb80e7789fe007d17270c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0G4KL96",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "selected_historical_source_sequence_length": 287,
  "selected_historical_source_sequence_sha256": "15441327e40b4a507f2d749497c8c4cbcbed343d618fb80e7789fe007d17270c",
  "selected_historical_version": {
    "accession": "A0A0G4KL96",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX3_VERLO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0G4KL96\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":37,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium dahliae var. longisporum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium longisporum\",\"taxonId\":100787}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX3\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   EIX3_VERLO              Reviewed;         287 AA.\nAC   A0A0G4KL96;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=BN1708_002170;\nOS   Verticillium longisporum (Verticillium dahliae var. longisporum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=100787;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
