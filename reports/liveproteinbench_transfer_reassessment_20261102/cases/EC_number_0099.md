# EC_number_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0099.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 5.4.99.39

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWRLKIAEGGNDPYLYSTNNFVGRQTWEFDSEYGTPEAIKEVEEARQIFYKNRFQVKPCGDLLWRFQFLREKNFKQTIPQVKVGDGEEVTYEAASTTLKRSVNLLTALQADDGHWPAEIAGPQFFLPPLVFCLYITGHLNVVFNVHHREEILRSIYYHQNEDGGWGLHIEGHSTMFCTALNYICLRMLGVGPDEGDDNACPRARKWILDHGSVTHIPSWGKTWLSILGLFDWSGSNPMPPEFWILPTFMPMYPAKMWCYCRMVYMPMSYLYGKRFVGPITPLIKQLREELFSEPFEEIKWKKVRHLCAPEDLYYPHPLIQDLMWDSLYLFTEPLLTRWPFNNLIRQKALQVTMDHIHYEDENSRYITIGCVEKVLCMLACWVEDPNGVCYKKHLARVPDYIWIAEDGLKMQSFGSQQWDCGFAVQALLASNMSLDEIGPALKKGHFFIKESQVKDNPSGDFKSMHRHISKGSWTFSDQDHGWQVSDCTAEGLKCCLILSTMPPEIVGEKMDPERLYDSVNVLLSLQSENGGLSAWEPAGAQAWLELLNPTEFFADIVIEHEYVECTGASIQALVLFKKMYPGHRKKEIENFIAKAAKYLEDTQYPNGSWYGNWGVCFTYGTWFALGGLAAAGKTYANCAAMRKGVEFLLKSQKEDGGWGESYVSCPKKDFVPLEGPSNLTQTAWALMGLIYARQMERDPTPLHQAAKLLINSQLENGDFPQQEITGVFMKNCMLHYPMYRTIYPLWAIAEYRTHVPLRLS

[Multiple Choices]
A. 5.4.99.14
B. 1.14.18.1
C. 3.2.1.18
D. 5.4.99.39
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

> The sequence-matched UniProt entry assigns EC 5.4.99.39 and records the reaction (S)-2,3-epoxysqualene → beta-amyrin with ECO:0000269 evidence linked to a publication. This supports the key, although the excerpts provide the database's evidence attribution rather than an independent review of the experiment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence has features characteristic of oxidosqualene cyclases, including QW-rich regions and the catalytic DCTAE motif. Transferable family knowledge supports an oxidosqualene-cyclase/isomerase interpretation and distinguishes it from the unrelated enzyme classes in B and C. But that family recognition does not meaningfully distinguish the closely related 5.4.99 choices: product specificity among oxidosqualene cyclases cannot be read from those shared hallmarks alone.


**Missing item-specific fact**

> Whether this particular enzyme produces beta-amyrin rather than the product associated with the other 5.4.99 option; a target-specific product measurement or sufficiently close, functionally characterized homolog would resolve that distinction.


**Reason**

> The sequence supports a broad enzyme-family inference, but the offered choices include a closely related alternative within that family. No concrete transferable feature in the supplied input establishes the exact product specificity needed for the final EC digits.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports the keyed beta-amyrin reaction; lack of a sequence-only way to distinguish the close alternatives does not establish that multiple options are catalytically correct.


### Important caveats

- The reviewer-only database annotation is sequence-matched and cites experimental evidence, but the underlying publication was not independently assessed here.
- The exact target identity and its database annotation were not part of the original input and are not used as transferable evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has features characteristic of oxidosqualene cyclases, including QW-rich regions and the catalytic DCTAE motif. Transferable family knowledge supports an oxidosqualene-cyclase/isomerase interpretation and distinguishes it from the unrelated enzyme classes in B and C. But that family recognition does not meaningfully distinguish the closely related 5.4.99 choices: product specificity among oxidosqualene cyclases cannot be read from those shared hallmarks alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular enzyme produces beta-amyrin rather than the product associated with the other 5.4.99 option; a target-specific product measurement or sufficiently close, functionally characterized homolog would resolve that distinction.",
    "reason": "The sequence supports a broad enzyme-family inference, but the offered choices include a closely related alternative within that family. No concrete transferable feature in the supplied input establishes the exact product specificity needed for the final EC digits."
  },
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 5.4.99.39 and records the reaction (S)-2,3-epoxysqualene → beta-amyrin with ECO:0000269 evidence linked to a publication. This supports the key, although the excerpts provide the database's evidence attribution rather than an independent review of the experiment."
  },
  "important_caveats": [
    "The reviewer-only database annotation is sequence-matched and cites experimental evidence, but the underlying publication was not independently assessed here.",
    "The exact target identity and its database annotation were not part of the original input and are not used as transferable evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports the keyed beta-amyrin reaction; lack of a sequence-only way to distinguish the close alternatives does not establish that multiple options are catalytically correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 5.4.99.39 and records the reaction (S)-2,3-epoxysqualene → beta-amyrin with ECO:0000269 evidence linked to a publication. This supports the key, although the excerpts provide the database's evidence attribution rather than an independent review of the experiment.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence has features characteristic of oxidosqualene cyclases, including QW-rich regions and the catalytic DCTAE motif. Transferable family knowledge supports an oxidosqualene-cyclase/isomerase interpretation and distinguishes it from the unrelated enzyme classes in B and C. But that family recognition does not meaningfully distinguish the closely related 5.4.99 choices: product specificity among oxidosqualene cyclases cannot be read from those shared hallmarks alone.",
    "missing_item_specific_fact": "Whether this particular enzyme produces beta-amyrin rather than the product associated with the other 5.4.99 option; a target-specific product measurement or sufficiently close, functionally characterized homolog would resolve that distinction.",
    "reason": "The sequence supports a broad enzyme-family inference, but the offered choices include a closely related alternative within that family. No concrete transferable feature in the supplied input establishes the exact product specificity needed for the final EC digits."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports the keyed beta-amyrin reaction; lack of a sequence-only way to distinguish the close alternatives does not establish that multiple options are catalytically correct."
  },
  "important_caveats": [
    "The reviewer-only database annotation is sequence-matched and cites experimental evidence, but the underlying publication was not independently assessed here.",
    "The exact target identity and its database annotation were not part of the original input and are not used as transferable evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1L0L7 (Beta-amyrin synthase 1, SobAS1, from Saponaria officinalis) is annotated with EC 5.4.99.39, supported by experimental evidence (ECO:0000269, PubMed:39043959). The catalytic activity is documented as (S)-2,3-epoxysqualene → beta-amyrin (Rhea:RHEA:31007). The sequence in the benchmark matches the UniProt sequence (SHA-256 identical, 760 AA). The author key D (5.4.99.39) is experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two hallmark motifs of the oxidosqualene cyclase (OSC) family: the DCTAE motif (visible as 'SDCTAEGL' near residue ~530) and the QW motif (visible as 'QWDCGFAV' near residue ~490). These motifs are universally conserved across all known OSCs and are absent from monooxygenases (EC 1.14.x.x, option B) and glycosidases (EC 3.2.1.x, option C), definitively eliminating those two choices. The ~760-residue length, highly hydrophobic character, and overall architecture are consistent with plant triterpene cyclases. Between the two remaining 5.4.99.x cyclase options (A: 5.4.99.14, D: 5.4.99.39), both belong to the OSC superfamily. However, 5.4.99.39 (beta-amyrin synthase) is the canonical EC number for plant triterpene cyclases of the β-amyrin type, which are the most widely studied and annotated OSCs in plant natural-product chemistry. A knowledgeable model familiar with the OSC family and plant triterpene biosynthesis would recognize that 5.4.99.39 is the standard EC assignment for plant β-amyrin synthases, while 5.4.99.14 is a less commonly encountered cyclase EC number. The combination of OSC-family motifs, plant-like sequence features, and the well-known association of β-amyrin synthase with EC 5.4.99.39 provides a transferable, family-level inference that meaningfully favors D over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DCTAE and QW motifs are well-known, transferable sequence signatures of the oxidosqualene cyclase family learned from multiple characterized OSCs (lanosterol synthase, cycloartenol synthase, lupeol synthase, β-amyrin synthase, etc.). These motifs eliminate options B and C with high confidence. The distinction between the two remaining 5.4.99.x options relies on family-level knowledge: 5.4.99.39 is the standard, well-annotated EC number for plant β-amyrin synthases, a heavily studied class of plant triterpene cyclases. While pinpointing the exact triterpene product from sequence alone is inherently difficult, the offered alternatives make the reasoning tractable: one is the canonical plant triterpene cyclase EC number and the other is a less standard alternative. A model with broad OSC-family knowledge can meaningfully favor D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (EC 1.14.18.1, a monooxygenase) and C (EC 3.2.1.18, a glycosidase) are clearly incompatible with the DCTAE/QW OSC motifs and can be eliminated. Between A and D, both are 5.4.99.x cyclases, but 5.4.99.39 is the canonical EC for plant β-amyrin synthase, while 5.4.99.14 does not correspond to a well-characterized plant triterpene cyclase product. The DCTAE/QW evidence plus plant OSC family knowledge provides a meaningful preference for D without requiring exact memorization of this protein's record.


### Important caveats

- The DCTAE and QW motifs confirm OSC family membership but do not, by themselves, specify which triterpene product is formed. Distinguishing β-amyrin synthase from other plant triterpene cyclases (α-amyrin, lupeol, taraxasterol synthases) from sequence alone is genuinely difficult.
- The distinction between 5.4.99.14 (option A) and 5.4.99.39 (option D) is the hardest part of this question. If 5.4.99.14 were also a well-known plant triterpene cyclase EC number, the A-vs-D distinction would be substantially weaker and more lookup-dependent.
- The experimental evidence (PubMed:39043959) for the β-amyrin synthase activity is recent (2025), meaning the specific product assignment for this exact protein was established by heterologous expression and GC-MS analysis, not by sequence motifs alone.
- The UniProt entry was first publicly released in June 2025 and reviewed in January 2026; the author's source snapshot date is unknown, so the annotation may not have been available at the time the benchmark was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two hallmark motifs of the oxidosqualene cyclase (OSC) family: the DCTAE motif (visible as 'SDCTAEGL' near residue ~530) and the QW motif (visible as 'QWDCGFAV' near residue ~490). These motifs are universally conserved across all known OSCs and are absent from monooxygenases (EC 1.14.x.x, option B) and glycosidases (EC 3.2.1.x, option C), definitively eliminating those two choices. The ~760-residue length, highly hydrophobic character, and overall architecture are consistent with plant triterpene cyclases. Between the two remaining 5.4.99.x cyclase options (A: 5.4.99.14, D: 5.4.99.39), both belong to the OSC superfamily. However, 5.4.99.39 (beta-amyrin synthase) is the canonical EC number for plant triterpene cyclases of the β-amyrin type, which are the most widely studied and annotated OSCs in plant natural-product chemistry. A knowledgeable model familiar with the OSC family and plant triterpene biosynthesis would recognize that 5.4.99.39 is the standard EC assignment for plant β-amyrin synthases, while 5.4.99.14 is a less commonly encountered cyclase EC number. The combination of OSC-family motifs, plant-like sequence features, and the well-known association of β-amyrin synthase with EC 5.4.99.39 provides a transferable, family-level inference that meaningfully favors D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DCTAE and QW motifs are well-known, transferable sequence signatures of the oxidosqualene cyclase family learned from multiple characterized OSCs (lanosterol synthase, cycloartenol synthase, lupeol synthase, β-amyrin synthase, etc.). These motifs eliminate options B and C with high confidence. The distinction between the two remaining 5.4.99.x options relies on family-level knowledge: 5.4.99.39 is the standard, well-annotated EC number for plant β-amyrin synthases, a heavily studied class of plant triterpene cyclases. While pinpointing the exact triterpene product from sequence alone is inherently difficult, the offered alternatives make the reasoning tractable: one is the canonical plant triterpene cyclase EC number and the other is a less standard alternative. A model with broad OSC-family knowledge can meaningfully favor D."
  },
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1L0L7 (Beta-amyrin synthase 1, SobAS1, from Saponaria officinalis) is annotated with EC 5.4.99.39, supported by experimental evidence (ECO:0000269, PubMed:39043959). The catalytic activity is documented as (S)-2,3-epoxysqualene → beta-amyrin (Rhea:RHEA:31007). The sequence in the benchmark matches the UniProt sequence (SHA-256 identical, 760 AA). The author key D (5.4.99.39) is experimentally supported."
  },
  "important_caveats": [
    "The DCTAE and QW motifs confirm OSC family membership but do not, by themselves, specify which triterpene product is formed. Distinguishing β-amyrin synthase from other plant triterpene cyclases (α-amyrin, lupeol, taraxasterol synthases) from sequence alone is genuinely difficult.",
    "The distinction between 5.4.99.14 (option A) and 5.4.99.39 (option D) is the hardest part of this question. If 5.4.99.14 were also a well-known plant triterpene cyclase EC number, the A-vs-D distinction would be substantially weaker and more lookup-dependent.",
    "The experimental evidence (PubMed:39043959) for the β-amyrin synthase activity is recent (2025), meaning the specific product assignment for this exact protein was established by heterologous expression and GC-MS analysis, not by sequence motifs alone.",
    "The UniProt entry was first publicly released in June 2025 and reviewed in January 2026; the author's source snapshot date is unknown, so the annotation may not have been available at the time the benchmark was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (EC 1.14.18.1, a monooxygenase) and C (EC 3.2.1.18, a glycosidase) are clearly incompatible with the DCTAE/QW OSC motifs and can be eliminated. Between A and D, both are 5.4.99.x cyclases, but 5.4.99.39 is the canonical EC for plant β-amyrin synthase, while 5.4.99.14 does not correspond to a well-characterized plant triterpene cyclase product. The DCTAE/QW evidence plus plant OSC family knowledge provides a meaningful preference for D without requiring exact memorization of this protein's record."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1L0L7 (Beta-amyrin synthase 1, SobAS1, from Saponaria officinalis) is annotated with EC 5.4.99.39, supported by experimental evidence (ECO:0000269, PubMed:39043959). The catalytic activity is documented as (S)-2,3-epoxysqualene → beta-amyrin (Rhea:RHEA:31007). The sequence in the benchmark matches the UniProt sequence (SHA-256 identical, 760 AA). The author key D (5.4.99.39) is experimentally supported.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two hallmark motifs of the oxidosqualene cyclase (OSC) family: the DCTAE motif (visible as 'SDCTAEGL' near residue ~530) and the QW motif (visible as 'QWDCGFAV' near residue ~490). These motifs are universally conserved across all known OSCs and are absent from monooxygenases (EC 1.14.x.x, option B) and glycosidases (EC 3.2.1.x, option C), definitively eliminating those two choices. The ~760-residue length, highly hydrophobic character, and overall architecture are consistent with plant triterpene cyclases. Between the two remaining 5.4.99.x cyclase options (A: 5.4.99.14, D: 5.4.99.39), both belong to the OSC superfamily. However, 5.4.99.39 (beta-amyrin synthase) is the canonical EC number for plant triterpene cyclases of the β-amyrin type, which are the most widely studied and annotated OSCs in plant natural-product chemistry. A knowledgeable model familiar with the OSC family and plant triterpene biosynthesis would recognize that 5.4.99.39 is the standard EC assignment for plant β-amyrin synthases, while 5.4.99.14 is a less commonly encountered cyclase EC number. The combination of OSC-family motifs, plant-like sequence features, and the well-known association of β-amyrin synthase with EC 5.4.99.39 provides a transferable, family-level inference that meaningfully favors D over A.",
    "missing_item_specific_fact": "",
    "reason": "The DCTAE and QW motifs are well-known, transferable sequence signatures of the oxidosqualene cyclase family learned from multiple characterized OSCs (lanosterol synthase, cycloartenol synthase, lupeol synthase, β-amyrin synthase, etc.). These motifs eliminate options B and C with high confidence. The distinction between the two remaining 5.4.99.x options relies on family-level knowledge: 5.4.99.39 is the standard, well-annotated EC number for plant β-amyrin synthases, a heavily studied class of plant triterpene cyclases. While pinpointing the exact triterpene product from sequence alone is inherently difficult, the offered alternatives make the reasoning tractable: one is the canonical plant triterpene cyclase EC number and the other is a less standard alternative. A model with broad OSC-family knowledge can meaningfully favor D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (EC 1.14.18.1, a monooxygenase) and C (EC 3.2.1.18, a glycosidase) are clearly incompatible with the DCTAE/QW OSC motifs and can be eliminated. Between A and D, both are 5.4.99.x cyclases, but 5.4.99.39 is the canonical EC for plant β-amyrin synthase, while 5.4.99.14 does not correspond to a well-characterized plant triterpene cyclase product. The DCTAE/QW evidence plus plant OSC family knowledge provides a meaningful preference for D without requiring exact memorization of this protein's record."
  },
  "important_caveats": [
    "The DCTAE and QW motifs confirm OSC family membership but do not, by themselves, specify which triterpene product is formed. Distinguishing β-amyrin synthase from other plant triterpene cyclases (α-amyrin, lupeol, taraxasterol synthases) from sequence alone is genuinely difficult.",
    "The distinction between 5.4.99.14 (option A) and 5.4.99.39 (option D) is the hardest part of this question. If 5.4.99.14 were also a well-known plant triterpene cyclase EC number, the A-vs-D distinction would be substantially weaker and more lookup-dependent.",
    "The experimental evidence (PubMed:39043959) for the β-amyrin synthase activity is recent (2025), meaning the specific product assignment for this exact protein was established by heterologous expression and GC-MS analysis, not by sequence motifs alone.",
    "The UniProt entry was first publicly released in June 2025 and reviewed in January 2026; the author's source snapshot date is unknown, so the annotation may not have been available at the time the benchmark was constructed."
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
  "benchmark_sequence_length": 760,
  "benchmark_sequence_sha256": "f45cb32ac82bac07fe18a4c04087fada3e3b643744290cb71a5355e4210f1f86",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 760,
  "current_source_sequence_sha256": "f45cb32ac82bac07fe18a4c04087fada3e3b643744290cb71a5355e4210f1f86",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1L0L7",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742",
  "selected_historical_source_sequence_length": 760,
  "selected_historical_source_sequence_sha256": "f45cb32ac82bac07fe18a4c04087fada3e3b643744290cb71a5355e4210f1f86",
  "selected_historical_version": {
    "accession": "A0AAW1L0L7",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BAMS1_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1L0L7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:39.404038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:39.404038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:39.404038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.39\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Beta-amyrin synthase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SobAS1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:39.404038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:31008\"}}],\"reaction\":{\"ecNumber\":\"5.4.99.39\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"name\":\"(S)-2,3-epoxysqualene = beta-amyrin\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:31007\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:10352\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15441\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:39.404038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48160.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:39.404038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   BAMS1_SAPOF             Reviewed;         760 AA.\nAC   A0AAW1L0L7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Beta-amyrin synthase 1 {ECO:0000303|PubMed:39043959};\nDE            Short=SobAS1 {ECO:0000303|PubMed:39043959};\nDE            EC=5.4.99.39 {ECO:0000269|PubMed:39043959};\nGN   Name=bAS1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11027757m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_05G236200 {ECO:0000312|EMBL:KAK9726778.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.045167+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742",
  "url": "https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Beta-amyrin synthase 1 {ECO:0000303|PubMed:39043959};\nDE            Short=SobAS1 {ECO:0000303|PubMed:39043959};\nDE            EC=5.4.99.39 {ECO:0000269|PubMed:39043959};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.045167+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742",
  "url": "https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48160.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.045167+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742",
  "url": "https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(S)-2,3-epoxysqualene = beta-amyrin; Xref=Rhea:RHEA:31007,\nCC         ChEBI:CHEBI:10352, ChEBI:CHEBI:15441; EC=5.4.99.39;\nCC         Evidence={ECO:0000269|PubMed:39043959};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:31008;\nCC         Evidence={ECO:0000269|PubMed:39043959};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.045167+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742",
  "url": "https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
