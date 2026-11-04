# catalytic_activity_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0064.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKQVQMPEVELNSDHKMPLVGFGTCIPDPIPPLEELATIFLEVIKVGYRHFDTASCYGTEEALGKAVAQAIESGLVNGREEFFITSKLWVEDADQDLILPALKKTLGNLGLDYLDLYLIHMPLRLRQGAEMFKYTKEDFLPFDIKGTWKAMEECSKLGLCKSIGVSNYSCEKLSKLLENATILPAVNQVEMNVVWKQSKLLPFCKEKNIHVSAWSPLLSYGSIWSQNAVMENTVLVDIAASKSKTVAQVALRWIYEQGASFIMRTFNKERMYQNVQIFDWELTQEELDQIQQIPQRRSNLAEAFVHPEGPIKSVEELWDGDL

[Multiple Choices]
A. rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)
B. N-methylmescaline + S-adenosyl-L-methionine = N,N-dimethylmescaline + S-adenosyl-L-homocysteine + H(+)
C. 12-deshydroxyl okaramine E + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = 3-desmethyl okaramine B + 2 oxidized [NADPH--hemoprotein reductase] + 2 H2O + 2 H(+)
D. deacetylisoipecoside + S-adenosyl-L-methionine = 7-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)
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

> The sequence-matched UniProt record annotates this catalytic activity with evidence code ECO:0000269 linked to a publication, and gives the same reaction as choice A. This supports the key, although the evidence here is an annotation citing experimental evidence rather than an independent review of the experiment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 323-residue sequence is compatible with a soluble NAD(P)-dependent oxidoreductase, rather than the P450-type oxygenation in C or the SAM-dependent methyl transfers in B and D. Family-level recognition of an aldo-keto-reductase-like enzyme would favor an alcohol/aldehyde redox reaction, making A the meaningful choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable enzyme-family knowledge provide a credible basis for distinguishing the redox option from the methylation and P450 options. They do not independently establish rhazimol as the substrate or prove the exact reaction equation, but that finer target-specific detail is not needed to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and the sequence-based oxidoreductase inference favors A over the methyltransferase and P450 alternatives.


### Important caveats

- The exact substrate specificity and reaction equation are supported here by reviewer-only, sequence-matched annotation, not established from the original sequence alone.
- The cited UniProt annotation reports physiological direction as right-to-left; choice A gives the reversible reaction equation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 323-residue sequence is compatible with a soluble NAD(P)-dependent oxidoreductase, rather than the P450-type oxygenation in C or the SAM-dependent methyl transfers in B and D. Family-level recognition of an aldo-keto-reductase-like enzyme would favor an alcohol/aldehyde redox reaction, making A the meaningful choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable enzyme-family knowledge provide a credible basis for distinguishing the redox option from the methylation and P450 options. They do not independently establish rhazimol as the substrate or prove the exact reaction equation, but that finer target-specific detail is not needed to distinguish the offered choices."
  },
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this catalytic activity with evidence code ECO:0000269 linked to a publication, and gives the same reaction as choice A. This supports the key, although the evidence here is an annotation citing experimental evidence rather than an independent review of the experiment."
  },
  "important_caveats": [
    "The exact substrate specificity and reaction equation are supported here by reviewer-only, sequence-matched annotation, not established from the original sequence alone.",
    "The cited UniProt annotation reports physiological direction as right-to-left; choice A gives the reversible reaction equation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence-based oxidoreductase inference favors A over the methyltransferase and P450 alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this catalytic activity with evidence code ECO:0000269 linked to a publication, and gives the same reaction as choice A. This supports the key, although the evidence here is an annotation citing experimental evidence rather than an independent review of the experiment.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 323-residue sequence is compatible with a soluble NAD(P)-dependent oxidoreductase, rather than the P450-type oxygenation in C or the SAM-dependent methyl transfers in B and D. Family-level recognition of an aldo-keto-reductase-like enzyme would favor an alcohol/aldehyde redox reaction, making A the meaningful choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable enzyme-family knowledge provide a credible basis for distinguishing the redox option from the methylation and P450 options. They do not independently establish rhazimol as the substrate or prove the exact reaction equation, but that finer target-specific detail is not needed to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence-based oxidoreductase inference favors A over the methyltransferase and P450 alternatives."
  },
  "important_caveats": [
    "The exact substrate specificity and reaction equation are supported here by reviewer-only, sequence-matched annotation, not established from the original sequence alone.",
    "The cited UniProt annotation reports physiological direction as right-to-left; choice A gives the reversible reaction equation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A9E7S5B9 (RHR2_ALSSC, Rhazimal reductase 2, EC 1.1.1.440) with exact SHA256 match. The catalytic activity 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' is annotated with experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022 Chem. Sci.). The sequence length (323 aa) and all annotation fields are consistent.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark features of the Short-chain Dehydrogenase/Reductase (SDR) family: (1) a Rossmann-fold NAD(P)-binding motif 'GFGTCIPDP' near the N-terminus matching the GxGxxG consensus; (2) the diagnostic 'GDL' tripeptide at the C-terminus, a well-known SDR signature; (3) overall length (~323 aa) consistent with SDR enzymes; (4) putative catalytic tetrad residues (Ser in 'GASF', Tyr in 'MYQ', Lys in 'KER') distributed in the expected SDR spatial arrangement. SDR enzymes catalyze NAD(P)-dependent oxidation/reduction of alcohols. Among the four choices, only A describes an NADP+-dependent dehydrogenase/reductase reaction. Choices B and D are SAM-dependent methyltransferase reactions (requiring a completely different fold and SAM-binding motifs absent here), and Choice C is a cytochrome P450 monooxygenase reaction (requiring a heme-binding FxxGxxxCxG motif and typically 400-600+ residues, neither present). The SDR family recognition from sequence motifs is well-established transferable knowledge that meaningfully eliminates B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR family motifs (Rossmann GxGxxG, C-terminal GDL, catalytic tetrad architecture, appropriate length) are directly observable in the supplied sequence and are textbook transferable knowledge. These features unambiguously classify the enzyme as a short-chain dehydrogenase/reductase, which is mechanistically incompatible with SAM-dependent methyltransferases (B, D) or cytochrome P450 monooxygenases (C). Only Choice A describes an NADP+-dependent alcohol dehydrogenase reaction, matching the SDR catalytic mechanism. The specific substrate name 'rhazimol' is unusual, but the reaction type alone distinguishes A from the other three.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent three distinct enzyme classes (SDR/dehydrogenase for A, SAM-methyltransferase for B and D, P450 for C). The sequence motifs clearly indicate an SDR enzyme, leaving only A as mechanistically consistent. No ambiguity among the offered alternatives.


### Important caveats

- The specific substrate 'rhazimol' is a specialized indole alkaloid; a model recognizing the SDR fold would infer the reaction class but not necessarily the exact substrate name from sequence alone. However, since only one choice (A) is a dehydrogenase/reductase reaction, the family-level inference suffices to select the correct option.
- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2022 publication, confirming the catalytic activity was experimentally characterized rather than purely inferred by similarity.
- The entry was first publicly released in June 2025; depending on the benchmark construction date, this annotation may or may not have been available in training data, but the sequence-based SDR recognition is independent of the specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark features of the Short-chain Dehydrogenase/Reductase (SDR) family: (1) a Rossmann-fold NAD(P)-binding motif 'GFGTCIPDP' near the N-terminus matching the GxGxxG consensus; (2) the diagnostic 'GDL' tripeptide at the C-terminus, a well-known SDR signature; (3) overall length (~323 aa) consistent with SDR enzymes; (4) putative catalytic tetrad residues (Ser in 'GASF', Tyr in 'MYQ', Lys in 'KER') distributed in the expected SDR spatial arrangement. SDR enzymes catalyze NAD(P)-dependent oxidation/reduction of alcohols. Among the four choices, only A describes an NADP+-dependent dehydrogenase/reductase reaction. Choices B and D are SAM-dependent methyltransferase reactions (requiring a completely different fold and SAM-binding motifs absent here), and Choice C is a cytochrome P450 monooxygenase reaction (requiring a heme-binding FxxGxxxCxG motif and typically 400-600+ residues, neither present). The SDR family recognition from sequence motifs is well-established transferable knowledge that meaningfully eliminates B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR family motifs (Rossmann GxGxxG, C-terminal GDL, catalytic tetrad architecture, appropriate length) are directly observable in the supplied sequence and are textbook transferable knowledge. These features unambiguously classify the enzyme as a short-chain dehydrogenase/reductase, which is mechanistically incompatible with SAM-dependent methyltransferases (B, D) or cytochrome P450 monooxygenases (C). Only Choice A describes an NADP+-dependent alcohol dehydrogenase reaction, matching the SDR catalytic mechanism. The specific substrate name 'rhazimol' is unusual, but the reaction type alone distinguishes A from the other three."
  },
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A9E7S5B9 (RHR2_ALSSC, Rhazimal reductase 2, EC 1.1.1.440) with exact SHA256 match. The catalytic activity 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' is annotated with experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022 Chem. Sci.). The sequence length (323 aa) and all annotation fields are consistent."
  },
  "important_caveats": [
    "The specific substrate 'rhazimol' is a specialized indole alkaloid; a model recognizing the SDR fold would infer the reaction class but not necessarily the exact substrate name from sequence alone. However, since only one choice (A) is a dehydrogenase/reductase reaction, the family-level inference suffices to select the correct option.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2022 publication, confirming the catalytic activity was experimentally characterized rather than purely inferred by similarity.",
    "The entry was first publicly released in June 2025; depending on the benchmark construction date, this annotation may or may not have been available in training data, but the sequence-based SDR recognition is independent of the specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent three distinct enzyme classes (SDR/dehydrogenase for A, SAM-methyltransferase for B and D, P450 for C). The sequence motifs clearly indicate an SDR enzyme, leaving only A as mechanistically consistent. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A9E7S5B9 (RHR2_ALSSC, Rhazimal reductase 2, EC 1.1.1.440) with exact SHA256 match. The catalytic activity 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' is annotated with experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022 Chem. Sci.). The sequence length (323 aa) and all annotation fields are consistent.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark features of the Short-chain Dehydrogenase/Reductase (SDR) family: (1) a Rossmann-fold NAD(P)-binding motif 'GFGTCIPDP' near the N-terminus matching the GxGxxG consensus; (2) the diagnostic 'GDL' tripeptide at the C-terminus, a well-known SDR signature; (3) overall length (~323 aa) consistent with SDR enzymes; (4) putative catalytic tetrad residues (Ser in 'GASF', Tyr in 'MYQ', Lys in 'KER') distributed in the expected SDR spatial arrangement. SDR enzymes catalyze NAD(P)-dependent oxidation/reduction of alcohols. Among the four choices, only A describes an NADP+-dependent dehydrogenase/reductase reaction. Choices B and D are SAM-dependent methyltransferase reactions (requiring a completely different fold and SAM-binding motifs absent here), and Choice C is a cytochrome P450 monooxygenase reaction (requiring a heme-binding FxxGxxxCxG motif and typically 400-600+ residues, neither present). The SDR family recognition from sequence motifs is well-established transferable knowledge that meaningfully eliminates B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The SDR family motifs (Rossmann GxGxxG, C-terminal GDL, catalytic tetrad architecture, appropriate length) are directly observable in the supplied sequence and are textbook transferable knowledge. These features unambiguously classify the enzyme as a short-chain dehydrogenase/reductase, which is mechanistically incompatible with SAM-dependent methyltransferases (B, D) or cytochrome P450 monooxygenases (C). Only Choice A describes an NADP+-dependent alcohol dehydrogenase reaction, matching the SDR catalytic mechanism. The specific substrate name 'rhazimol' is unusual, but the reaction type alone distinguishes A from the other three."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent three distinct enzyme classes (SDR/dehydrogenase for A, SAM-methyltransferase for B and D, P450 for C). The sequence motifs clearly indicate an SDR enzyme, leaving only A as mechanistically consistent. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The specific substrate 'rhazimol' is a specialized indole alkaloid; a model recognizing the SDR fold would infer the reaction class but not necessarily the exact substrate name from sequence alone. However, since only one choice (A) is a dehydrogenase/reductase reaction, the family-level inference suffices to select the correct option.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2022 publication, confirming the catalytic activity was experimentally characterized rather than purely inferred by similarity.",
    "The entry was first publicly released in June 2025; depending on the benchmark construction date, this annotation may or may not have been available in training data, but the sequence-based SDR recognition is independent of the specific annotation."
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
  "benchmark_sequence_length": 323,
  "benchmark_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 323,
  "current_source_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S5B9",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "selected_historical_source_sequence_length": 323,
  "selected_historical_source_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "selected_historical_version": {
    "accession": "A0A9E7S5B9",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RHR2_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S5B9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.440\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Rhazimal reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsRHR2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79617\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.440\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79615\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230473\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230474\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65386.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   RHR2_ALSSC              Reviewed;         323 AA.\nAC   A0A9E7S5B9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Rhazimal reductase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR2 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\nGN   Name=RHR2 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Rhazimal reductase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR2 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65386.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+);\nCC         Xref=Rhea:RHEA:79615, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:230473, ChEBI:CHEBI:230474;\nCC         EC=1.1.1.440; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79617;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
