# catalytic_activity_0153

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0153.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKYAHVGLNVTNLEKSIEFYSKLFGAEPVKVKPDYAKFLLESPGLNFTLNLRDEVNGNQVGHFGIQVESTEEVVAHKNRLAENGILSQYDEINTTCCYALQDKFWIHDPDGNEWEFFYTKTTVEENSTHPPTCCVNEPNVEKAECCSPTASSNKDTSNCCS

[Multiple Choices]
A. methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)
B. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
C. L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)
D. dUMP + ATP = dUDP + ADP
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

> The matched sequence has a catalytic-activity annotation for reaction A with experimental evidence codes citing two publications. This directly supports the keyed reaction for this protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short bacterial sequence has histidine/acidic-residue features compatible with a metalloenzyme, and its overall profile can support recognition as an ArsI-like organoarsenical-cleaving oxygenase. Transferable knowledge of that enzyme family favors oxidative C–As bond cleavage; among these choices, A is the only oxygen-dependent organoarsenical reaction. The sequence alone may not make the family identification certain, but it offers a meaningful distinction from the sugar redox, sugar phosphorylation, and nucleotide phosphorylation alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features and the sharply contrasting reaction choices provides a credible basis for selecting A without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A is consistent with the inferred organoarsenical-cleaving oxygenase activity among the listed choices.


### Important caveats

- The sequence features do not independently prove the exact substrate or reaction; the family-level inference is probabilistic.
- The reviewer evidence supports the key for the matched sequence, but that evidence was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short bacterial sequence has histidine/acidic-residue features compatible with a metalloenzyme, and its overall profile can support recognition as an ArsI-like organoarsenical-cleaving oxygenase. Transferable knowledge of that enzyme family favors oxidative C–As bond cleavage; among these choices, A is the only oxygen-dependent organoarsenical reaction. The sequence alone may not make the family identification certain, but it offers a meaningful distinction from the sugar redox, sugar phosphorylation, and nucleotide phosphorylation alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features and the sharply contrasting reaction choices provides a credible basis for selecting A without needing the exact protein's recorded annotation."
  },
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a catalytic-activity annotation for reaction A with experimental evidence codes citing two publications. This directly supports the keyed reaction for this protein."
  },
  "important_caveats": [
    "The sequence features do not independently prove the exact substrate or reaction; the family-level inference is probabilistic.",
    "The reviewer evidence supports the key for the matched sequence, but that evidence was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is consistent with the inferred organoarsenical-cleaving oxygenase activity among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a catalytic-activity annotation for reaction A with experimental evidence codes citing two publications. This directly supports the keyed reaction for this protein.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short bacterial sequence has histidine/acidic-residue features compatible with a metalloenzyme, and its overall profile can support recognition as an ArsI-like organoarsenical-cleaving oxygenase. Transferable knowledge of that enzyme family favors oxidative C–As bond cleavage; among these choices, A is the only oxygen-dependent organoarsenical reaction. The sequence alone may not make the family identification certain, but it offers a meaningful distinction from the sugar redox, sugar phosphorylation, and nucleotide phosphorylation alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features and the sharply contrasting reaction choices provides a credible basis for selecting A without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is consistent with the inferred organoarsenical-cleaving oxygenase activity among the listed choices."
  },
  "important_caveats": [
    "The sequence features do not independently prove the exact substrate or reaction; the family-level inference is probabilistic.",
    "The reviewer evidence supports the key for the matched sequence, but that evidence was not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A059WI14 (sequence matched, 161 aa) annotates this protein as ArsI (Trivalent organoarsenical cleaving enzyme, EC 1.13.11.-), a C-As lyase / methylarsonous acid demethylase. The catalytic activity 'methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)' is supported by experimental evidence (ECO:0000269) from PubMed 24821808 (Yoshinaga & Rosen, PNAS 2014) and PubMed 28936873 (Pawitwar et al., ES&T 2017). The expected answer text matches the annotated reaction exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 161-aa protein lacks canonical nucleotide-binding motifs (no Walker A/B or P-loop for ATP, no Rossmann-fold GxGxxG for NAD). Choices B (fucose dehydrogenase) requires a Rossmann-fold NAD-binding domain typical of ~350-400 aa dehydrogenases; choices C and D (kinases) require ATP-binding motifs. The small size and absence of these motifs make B, C, D structurally implausible. The protein's clustered cysteines (CCYAL, CCVNEP, CCSPT, terminal CC) are consistent with metal (Fe(II)) coordination in a small oxygen-dependent enzyme. Choice A is the only option requiring O2 and a generic reductant (AH2) rather than a specific nucleotide cofactor, which aligns with a small metal-dependent oxygenase/lyase. Additionally, knowledge of the ArsI family (characterized 2014, C-As lyase with conserved Cys/His/Glu residues) supports positive identification of the arsenic demethylation reaction from the cysteine-rich pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of kinase (C, D) and dehydrogenase (B) options based on absence of nucleotide-binding motifs in a small protein is a legitimate structural/biochemical inference from general principles. The positive identification of the O2-dependent C-As lyase reaction benefits from family-level knowledge of ArsI (small, Cys-rich, metal-dependent oxygenase), which is transferable knowledge about this protein family learned from the literature. The combination of elimination and family recognition provides a meaningful basis for selecting A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span entirely different metabolic pathways (arsenic detoxification, fucose oxidation, fucose phosphorylation, nucleotide phosphorylation) with distinct cofactor requirements. No two choices are biochemically interchangeable or ambiguous given the sequence features.


### Important caveats

- The primary discriminating argument is elimination (absence of ATP/NAD motifs) rather than positive identification of the arsenic demethylation mechanism from sequence alone.
- Positive identification of ArsI specifically from the 161-aa sequence requires recognition of the cysteine-rich pattern as diagnostic of this recently characterized enzyme family, which is legitimate family-level knowledge but borders on specific protein recognition.
- The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 161-aa protein lacks canonical nucleotide-binding motifs (no Walker A/B or P-loop for ATP, no Rossmann-fold GxGxxG for NAD). Choices B (fucose dehydrogenase) requires a Rossmann-fold NAD-binding domain typical of ~350-400 aa dehydrogenases; choices C and D (kinases) require ATP-binding motifs. The small size and absence of these motifs make B, C, D structurally implausible. The protein's clustered cysteines (CCYAL, CCVNEP, CCSPT, terminal CC) are consistent with metal (Fe(II)) coordination in a small oxygen-dependent enzyme. Choice A is the only option requiring O2 and a generic reductant (AH2) rather than a specific nucleotide cofactor, which aligns with a small metal-dependent oxygenase/lyase. Additionally, knowledge of the ArsI family (characterized 2014, C-As lyase with conserved Cys/His/Glu residues) supports positive identification of the arsenic demethylation reaction from the cysteine-rich pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of kinase (C, D) and dehydrogenase (B) options based on absence of nucleotide-binding motifs in a small protein is a legitimate structural/biochemical inference from general principles. The positive identification of the O2-dependent C-As lyase reaction benefits from family-level knowledge of ArsI (small, Cys-rich, metal-dependent oxygenase), which is transferable knowledge about this protein family learned from the literature. The combination of elimination and family recognition provides a meaningful basis for selecting A."
  },
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A059WI14 (sequence matched, 161 aa) annotates this protein as ArsI (Trivalent organoarsenical cleaving enzyme, EC 1.13.11.-), a C-As lyase / methylarsonous acid demethylase. The catalytic activity 'methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)' is supported by experimental evidence (ECO:0000269) from PubMed 24821808 (Yoshinaga & Rosen, PNAS 2014) and PubMed 28936873 (Pawitwar et al., ES&T 2017). The expected answer text matches the annotated reaction exactly."
  },
  "important_caveats": [
    "The primary discriminating argument is elimination (absence of ATP/NAD motifs) rather than positive identification of the arsenic demethylation mechanism from sequence alone.",
    "Positive identification of ArsI specifically from the 161-aa sequence requires recognition of the cysteine-rich pattern as diagnostic of this recently characterized enzyme family, which is legitimate family-level knowledge but borders on specific protein recognition.",
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span entirely different metabolic pathways (arsenic detoxification, fucose oxidation, fucose phosphorylation, nucleotide phosphorylation) with distinct cofactor requirements. No two choices are biochemically interchangeable or ambiguous given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A059WI14 (sequence matched, 161 aa) annotates this protein as ArsI (Trivalent organoarsenical cleaving enzyme, EC 1.13.11.-), a C-As lyase / methylarsonous acid demethylase. The catalytic activity 'methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)' is supported by experimental evidence (ECO:0000269) from PubMed 24821808 (Yoshinaga & Rosen, PNAS 2014) and PubMed 28936873 (Pawitwar et al., ES&T 2017). The expected answer text matches the annotated reaction exactly.",
    "evidence_ids": ["C5", "C4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 161-aa protein lacks canonical nucleotide-binding motifs (no Walker A/B or P-loop for ATP, no Rossmann-fold GxGxxG for NAD). Choices B (fucose dehydrogenase) requires a Rossmann-fold NAD-binding domain typical of ~350-400 aa dehydrogenases; choices C and D (kinases) require ATP-binding motifs. The small size and absence of these motifs make B, C, D structurally implausible. The protein's clustered cysteines (CCYAL, CCVNEP, CCSPT, terminal CC) are consistent with metal (Fe(II)) coordination in a small oxygen-dependent enzyme. Choice A is the only option requiring O2 and a generic reductant (AH2) rather than a specific nucleotide cofactor, which aligns with a small metal-dependent oxygenase/lyase. Additionally, knowledge of the ArsI family (characterized 2014, C-As lyase with conserved Cys/His/Glu residues) supports positive identification of the arsenic demethylation reaction from the cysteine-rich pattern.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of kinase (C, D) and dehydrogenase (B) options based on absence of nucleotide-binding motifs in a small protein is a legitimate structural/biochemical inference from general principles. The positive identification of the O2-dependent C-As lyase reaction benefits from family-level knowledge of ArsI (small, Cys-rich, metal-dependent oxygenase), which is transferable knowledge about this protein family learned from the literature. The combination of elimination and family recognition provides a meaningful basis for selecting A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span entirely different metabolic pathways (arsenic detoxification, fucose oxidation, fucose phosphorylation, nucleotide phosphorylation) with distinct cofactor requirements. No two choices are biochemically interchangeable or ambiguous given the sequence features."
  },
  "important_caveats": [
    "The primary discriminating argument is elimination (absence of ATP/NAD motifs) rather than positive identification of the arsenic demethylation mechanism from sequence alone.",
    "Positive identification of ArsI specifically from the 161-aa sequence requires recognition of the cysteine-rich pattern as diagnostic of this recently characterized enzyme family, which is legitimate family-level knowledge but borders on specific protein recognition.",
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational prediction."
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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C6",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C7",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C8",
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

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C9",
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

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C10",
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
  "excerpt": "DE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305|PubMed:24821808};\nDE            EC=1.13.11.- {ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};\nDE   AltName: Full=Arsenic inducible gene ArsI {ECO:0000303|PubMed:24821808};\nDE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24821808, ECO:0000303|PubMed:28936873};\nDE   AltName: Full=Methylarsonous acid demethylase {ECO:0000303|PubMed:24821808};\nDE            Short=MAs(III) demethylase {ECO:0000303|PubMed:24821808};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H4",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
