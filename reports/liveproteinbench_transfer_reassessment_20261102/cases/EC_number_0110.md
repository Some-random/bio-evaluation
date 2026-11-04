# EC_number_0110

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0110.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.14.18.1

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTRQNVYELKDDTLSWYSRAVEEMKSRDINDPTSWWYQGAIHGYATYPSALTYWHDATGYPPSQQTVNSGFWNRCQHGTWYFLPWHRMYLFYFEEIVAKAIRDMGGPADWTLPYWNYCEAYNTSASPSNQQQALQIPPEFGSSQGPNADFASLWIKNRRNYVLNKNNVNPWPAMNEAEFTNSGGDISFGGGVTGFAHSGGQTGQLESLPHNVVHTDINGAMGNPDTAALDPIFWLHHANIDRLWQVWLAQAGRSNPVVNAWKDFRFKFHDANGQPVEIAVKDVETTQLLGYVYTPAFPLSSTTPARRSVPAMDVVGATSASFSVGDHMAPLDLTMVPQPARGARLLAARGGDEKRTILRISNVKGKGATSPIDLFITNRDNEEGNEENFVGCIGLFGLENASTPSVESDGSGLNFAIDISDTINKLRQRDDWDEDNIRVQLIPQSKQDSDVEINVGRVSLHSEID

[Multiple Choices]
A. 1.14.15.37
B. 2.3.1.31
C. 2.5.1.76
D. 1.14.18.1
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

> The sequence-matched UniProt record assigns EC 1.14.18.1 to tyrosinase HcTyr1 and records the tyrosine-to-L-dopaquinone reaction with experimental evidence cited to PubMed. This supports choice D, though the cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a histidine-rich, type-3 copper enzyme: it contains multiple histidines in motifs and regions characteristic of copper-binding sites in tyrosinase-family proteins. Family-level knowledge supports a tyrosinase function (EC 1.14.18.1), distinguishing D from the transferase choices B and C and the differently classified oxidoreductase A. This is a plausible family inference, not a sequence-only proof of the precise substrate reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family and its characteristic copper-binding features provides a meaningful transferable basis for selecting among these alternatives; the exact protein’s recorded annotation is not necessary for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices do not include another closely matching type-3 copper tyrosinase EC number; the family-level inference favors D among the listed options.


### Important caveats

- The reviewer-only record is sequence-matched and cites experimental evidence, but the primary study was not independently validated.
- Sequence motifs support family recognition probabilistically and do not alone establish every catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a histidine-rich, type-3 copper enzyme: it contains multiple histidines in motifs and regions characteristic of copper-binding sites in tyrosinase-family proteins. Family-level knowledge supports a tyrosinase function (EC 1.14.18.1), distinguishing D from the transferase choices B and C and the differently classified oxidoreductase A. This is a plausible family inference, not a sequence-only proof of the precise substrate reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family and its characteristic copper-binding features provides a meaningful transferable basis for selecting among these alternatives; the exact protein’s recorded annotation is not necessary for that distinction."
  },
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.18.1 to tyrosinase HcTyr1 and records the tyrosine-to-L-dopaquinone reaction with experimental evidence cited to PubMed. This supports choice D, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only record is sequence-matched and cites experimental evidence, but the primary study was not independently validated.",
    "Sequence motifs support family recognition probabilistically and do not alone establish every catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices do not include another closely matching type-3 copper tyrosinase EC number; the family-level inference favors D among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.18.1 to tyrosinase HcTyr1 and records the tyrosine-to-L-dopaquinone reaction with experimental evidence cited to PubMed. This supports choice D, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a histidine-rich, type-3 copper enzyme: it contains multiple histidines in motifs and regions characteristic of copper-binding sites in tyrosinase-family proteins. Family-level knowledge supports a tyrosinase function (EC 1.14.18.1), distinguishing D from the transferase choices B and C and the differently classified oxidoreductase A. This is a plausible family inference, not a sequence-only proof of the precise substrate reaction.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family and its characteristic copper-binding features provides a meaningful transferable basis for selecting among these alternatives; the exact protein’s recorded annotation is not necessary for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices do not include another closely matching type-3 copper tyrosinase EC number; the family-level inference favors D among the listed options."
  },
  "important_caveats": [
    "The reviewer-only record is sequence-matched and cites experimental evidence, but the primary study was not independently validated.",
    "Sequence motifs support family recognition probabilistically and do not alone establish every catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A261GRE4 (sequence matched) annotates this protein as Tyrosinase HcTyr1 with EC 1.14.18.1. The annotation is experimentally supported (ECO:0000269, PubMed:39382070) with X-ray crystallography at 1.97 Å (PDB 8B74). The catalytic activity L-tyrosine + O2 = L-dopaquinone + H2O (EC 1.14.18.1) is confirmed by both monooxygenase and oxidase activities. The evidence is robust and directly applicable to the supplied sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the well-known 'GYATY' motif (visible as 'GAIHGYATYPS' and 'HGYATY' in the N-terminal region), which is a hallmark conserved signature of the tyrosinase/polyphenol oxidase family found across mushroom tyrosinases, plant PPOs, and bacterial tyrosinases. This motif is part of the CuA copper-binding site and is a textbook family-level identifier. Additionally, multiple histidine residues in patterns consistent with binuclear copper coordination support a copper-dependent oxidase. Among the choices: EC 2.3.1.31 (arylamine N-acetyltransferase) and EC 2.5.1.76 (sulfurtransferase) are non-copper enzymes with entirely different folds and no GYATY motif; EC 1.14.15.37 (dopamine β-monooxygenase) belongs to the PHM/DBM copper enzyme family with different structural motifs (HxxxH patterns but not the GYATY signature). The GYATY motif thus meaningfully distinguishes EC 1.14.18.1 (tyrosinase) from all three distractors using family-level knowledge transferable from other tyrosinases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GYATY motif is a widely recognized, transferable sequence signature of the tyrosinase family. A model with knowledge of tyrosinases from other organisms (mushroom, plant, other bacterial tyrosinases) would recognize this motif and the copper-coordinating histidine pattern, enabling it to select EC 1.14.18.1 over the other three options without needing to recall this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GYATY motif and copper-binding histidine pattern clearly point to the tyrosinase family (EC 1.14.18.1) and are absent from the structural families of the other three options. No other option is defensible given these sequence features.


### Important caveats

- The GYATY motif is a strong but not absolutely exclusive tyrosinase-family indicator; however, among the four offered choices, it uniquely supports EC 1.14.18.1.
- The annotation is experimentally verified (X-ray crystallography, PubMed 39382070), not merely computational.
- The reviewer-only evidence confirms sequence match and current annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the well-known 'GYATY' motif (visible as 'GAIHGYATYPS' and 'HGYATY' in the N-terminal region), which is a hallmark conserved signature of the tyrosinase/polyphenol oxidase family found across mushroom tyrosinases, plant PPOs, and bacterial tyrosinases. This motif is part of the CuA copper-binding site and is a textbook family-level identifier. Additionally, multiple histidine residues in patterns consistent with binuclear copper coordination support a copper-dependent oxidase. Among the choices: EC 2.3.1.31 (arylamine N-acetyltransferase) and EC 2.5.1.76 (sulfurtransferase) are non-copper enzymes with entirely different folds and no GYATY motif; EC 1.14.15.37 (dopamine β-monooxygenase) belongs to the PHM/DBM copper enzyme family with different structural motifs (HxxxH patterns but not the GYATY signature). The GYATY motif thus meaningfully distinguishes EC 1.14.18.1 (tyrosinase) from all three distractors using family-level knowledge transferable from other tyrosinases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GYATY motif is a widely recognized, transferable sequence signature of the tyrosinase family. A model with knowledge of tyrosinases from other organisms (mushroom, plant, other bacterial tyrosinases) would recognize this motif and the copper-coordinating histidine pattern, enabling it to select EC 1.14.18.1 over the other three options without needing to recall this specific protein's database entry."
  },
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A261GRE4 (sequence matched) annotates this protein as Tyrosinase HcTyr1 with EC 1.14.18.1. The annotation is experimentally supported (ECO:0000269, PubMed:39382070) with X-ray crystallography at 1.97 Å (PDB 8B74). The catalytic activity L-tyrosine + O2 = L-dopaquinone + H2O (EC 1.14.18.1) is confirmed by both monooxygenase and oxidase activities. The evidence is robust and directly applicable to the supplied sequence."
  },
  "important_caveats": [
    "The GYATY motif is a strong but not absolutely exclusive tyrosinase-family indicator; however, among the four offered choices, it uniquely supports EC 1.14.18.1.",
    "The annotation is experimentally verified (X-ray crystallography, PubMed 39382070), not merely computational.",
    "The reviewer-only evidence confirms sequence match and current annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GYATY motif and copper-binding histidine pattern clearly point to the tyrosinase family (EC 1.14.18.1) and are absent from the structural families of the other three options. No other option is defensible given these sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A261GRE4 (sequence matched) annotates this protein as Tyrosinase HcTyr1 with EC 1.14.18.1. The annotation is experimentally supported (ECO:0000269, PubMed:39382070) with X-ray crystallography at 1.97 Å (PDB 8B74). The catalytic activity L-tyrosine + O2 = L-dopaquinone + H2O (EC 1.14.18.1) is confirmed by both monooxygenase and oxidase activities. The evidence is robust and directly applicable to the supplied sequence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the well-known 'GYATY' motif (visible as 'GAIHGYATYPS' and 'HGYATY' in the N-terminal region), which is a hallmark conserved signature of the tyrosinase/polyphenol oxidase family found across mushroom tyrosinases, plant PPOs, and bacterial tyrosinases. This motif is part of the CuA copper-binding site and is a textbook family-level identifier. Additionally, multiple histidine residues in patterns consistent with binuclear copper coordination support a copper-dependent oxidase. Among the choices: EC 2.3.1.31 (arylamine N-acetyltransferase) and EC 2.5.1.76 (sulfurtransferase) are non-copper enzymes with entirely different folds and no GYATY motif; EC 1.14.15.37 (dopamine β-monooxygenase) belongs to the PHM/DBM copper enzyme family with different structural motifs (HxxxH patterns but not the GYATY signature). The GYATY motif thus meaningfully distinguishes EC 1.14.18.1 (tyrosinase) from all three distractors using family-level knowledge transferable from other tyrosinases.",
    "missing_item_specific_fact": "",
    "reason": "The GYATY motif is a widely recognized, transferable sequence signature of the tyrosinase family. A model with knowledge of tyrosinases from other organisms (mushroom, plant, other bacterial tyrosinases) would recognize this motif and the copper-coordinating histidine pattern, enabling it to select EC 1.14.18.1 over the other three options without needing to recall this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GYATY motif and copper-binding histidine pattern clearly point to the tyrosinase family (EC 1.14.18.1) and are absent from the structural families of the other three options. No other option is defensible given these sequence features."
  },
  "important_caveats": [
    "The GYATY motif is a strong but not absolutely exclusive tyrosinase-family indicator; however, among the four offered choices, it uniquely supports EC 1.14.18.1.",
    "The annotation is experimentally verified (X-ray crystallography, PubMed 39382070), not merely computational.",
    "The reviewer-only evidence confirms sequence match and current annotation but was not available to the evaluated model."
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
  "benchmark_sequence_length": 466,
  "benchmark_sequence_sha256": "9995b12ae04ed7d37120f23f1e35c673a361e1e8e6a50c25ae994ce0fdc4f509",
  "current_entry_audit": {
    "entryVersion": 26,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-12-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 466,
  "current_source_sequence_sha256": "9995b12ae04ed7d37120f23f1e35c673a361e1e8e6a50c25ae994ce0fdc4f509",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 24,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A261GRE4",
  "selected_historical_entry_version": 24,
  "selected_historical_record_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "selected_historical_source_sequence_length": 466,
  "selected_historical_source_sequence_sha256": "9995b12ae04ed7d37120f23f1e35c673a361e1e8e6a50c25ae994ce0fdc4f509",
  "selected_historical_version": {
    "accession": "A0A261GRE4",
    "database": "Swiss-Prot",
    "entryVersion": 24,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TYR1_HAHS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A261GRE4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":26,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-12-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Oceanospirillales\",\"Hahellaceae\",\"Hahella\"],\"scientificName\":\"Hahella sp. (strain CCB-MM4)\",\"taxonId\":1926491}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"value\":\"1.14.18.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"value\":\"Tyrosinase HcTyr1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.14.18.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"name\":\"L-tyrosine + O2 = L-dopaquinone + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:18117\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57924\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58315\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"name\":\"2 L-tyrosine + O2 = 2 L-dopa\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:34283\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57504\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58315\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.14.18.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"name\":\"2 L-dopa + O2 = 2 L-dopaquinone + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:34287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57504\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57924\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"de Almeida Santos G.\",\"Englund A.N.B.\",\"Dalleywater E.L.\",\"Roehr A.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39382070\"},{\"database\":\"DOI\",\"id\":\"10.1002/2211-5463.13906\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39382070\",\"journal\":\"FEBS Open Bio\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Characterization of two bacterial tyrosinases from the halophilic bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in wetlands.\",\"volume\":\"0\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8B74\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CCB-MM4\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\",\"AUTO-CLEAVAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H1",
  "excerpt": "ID   TYR1_HAHS4              Reviewed;         466 AA.\nAC   A0A261GRE4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-DEC-2017, sequence version 1.\nDT   28-JAN-2026, entry version 24.\nDE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};\nDE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};\nGN   ORFNames=BTA51_09820 {ECO:0000312|EMBL:OZG74058.1};\nOS   Hahella sp. (strain CCB-MM4).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Oceanospirillales; Hahellaceae; Hahella.\nOX   NCBI_TaxID=1926491;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};\nDE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8B74}\nRP   X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   COFACTOR, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,\nRP   DOMAIN, AND AUTO-CLEAVAGE.\nRC   STRAIN=CCB-MM4;\nRX   PubMed=39382070; DOI=10.1002/2211-5463.13906;\nRA   de Almeida Santos G., Englund A.N.B., Dalleywater E.L., Roehr A.K.;\nRT   \"Characterization of two bacterial tyrosinases from the halophilic\nRT   bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in\nRT   wetlands.\";\nRL   FEBS Open Bio 0:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-tyrosine + O2 = L-dopaquinone + H2O; Xref=Rhea:RHEA:18117,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15379, ChEBI:CHEBI:57924,\nCC         ChEBI:CHEBI:58315; EC=1.14.18.1;\nCC         Evidence={ECO:0000269|PubMed:39382070};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 L-tyrosine + O2 = 2 L-dopa; Xref=Rhea:RHEA:34283,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:57504, ChEBI:CHEBI:58315;\nCC         Evidence={ECO:0000269|PubMed:39382070};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 L-dopa + O2 = 2 L-dopaquinone + 2 H2O; Xref=Rhea:RHEA:34287,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15379, ChEBI:CHEBI:57504,\nCC         ChEBI:CHEBI:57924; EC=1.14.18.1;\nCC         Evidence={ECO:0000269|PubMed:39382070};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
