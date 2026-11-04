# EC_number_0085

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0085.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.1.1.25

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSLDIKQESSPLMTNPLDSEEFRRQGYMVIDFLAEYYKNIQKFPVRSQVEPGYLRKRLPESAPYEPESIETILKDVHDDIVPGLTHWQSPNYYAYFPSSGSTAGLLGETLAAGFNVVGFNWISSPASTELESIVMDWLAEMLNLPKSFTFSGDGGGVMMGTTCEAILTTITAARDRILDRIGREHINKLVVYGSDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC

[Multiple Choices]
A. 4.1.1.36
B. 3.1.3.2
C. 4.1.1.25
D. 2.7.4.9
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

> The sequence-matched UniProt entry reports EC 4.1.1.25 for L-tyrosine decarboxylation and cites experimental evidence (ECO:0000269). This supports choice C. The same entry also reports EC 4.1.1.28 for L-DOPA decarboxylation, which is not among the options.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 522-residue sequence is consistent with a PLP-dependent aromatic amino-acid decarboxylase, a family-level inference that distinguishes it from the phosphatase and nucleotide kinase choices. Among the offered options, EC 4.1.1.25 is the tyrosine-decarboxylase option and is a credible choice for this family. The sequence alone may not establish which aromatic substrate activity is physiologically relevant, but EC 4.1.1.25 is meaningfully distinguished from the unrelated alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable enzyme-family knowledge provides a credible basis for selecting the tyrosine decarboxylase option over the alternatives. The target-specific experimental annotation supports the key but is not necessary to establish that this is answerable by biological inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source reports a second activity, EC 4.1.1.28, but that number is not offered. Among the listed choices, only C is supported by the reported tyrosine-decarboxylase activity.


### Important caveats

- The protein is reported to catalyze both L-tyrosine and L-DOPA decarboxylation; the question offers only the EC number for the former.
- A family-level sequence inference does not by itself prove the exact substrate activities of this particular protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 522-residue sequence is consistent with a PLP-dependent aromatic amino-acid decarboxylase, a family-level inference that distinguishes it from the phosphatase and nucleotide kinase choices. Among the offered options, EC 4.1.1.25 is the tyrosine-decarboxylase option and is a credible choice for this family. The sequence alone may not establish which aromatic substrate activity is physiologically relevant, but EC 4.1.1.25 is meaningfully distinguished from the unrelated alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family knowledge provides a credible basis for selecting the tyrosine decarboxylase option over the alternatives. The target-specific experimental annotation supports the key but is not necessary to establish that this is answerable by biological inference."
  },
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports EC 4.1.1.25 for L-tyrosine decarboxylation and cites experimental evidence (ECO:0000269). This supports choice C. The same entry also reports EC 4.1.1.28 for L-DOPA decarboxylation, which is not among the options."
  },
  "important_caveats": [
    "The protein is reported to catalyze both L-tyrosine and L-DOPA decarboxylation; the question offers only the EC number for the former.",
    "A family-level sequence inference does not by itself prove the exact substrate activities of this particular protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source reports a second activity, EC 4.1.1.28, but that number is not offered. Among the listed choices, only C is supported by the reported tyrosine-decarboxylase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports EC 4.1.1.25 for L-tyrosine decarboxylation and cites experimental evidence (ECO:0000269). This supports choice C. The same entry also reports EC 4.1.1.28 for L-DOPA decarboxylation, which is not among the options.",
    "evidence_ids": ["C5", "H5", "C6", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 522-residue sequence is consistent with a PLP-dependent aromatic amino-acid decarboxylase, a family-level inference that distinguishes it from the phosphatase and nucleotide kinase choices. Among the offered options, EC 4.1.1.25 is the tyrosine-decarboxylase option and is a credible choice for this family. The sequence alone may not establish which aromatic substrate activity is physiologically relevant, but EC 4.1.1.25 is meaningfully distinguished from the unrelated alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family knowledge provides a credible basis for selecting the tyrosine decarboxylase option over the alternatives. The target-specific experimental annotation supports the key but is not necessary to establish that this is answerable by biological inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source reports a second activity, EC 4.1.1.28, but that number is not offered. Among the listed choices, only C is supported by the reported tyrosine-decarboxylase activity."
  },
  "important_caveats": [
    "The protein is reported to catalyze both L-tyrosine and L-DOPA decarboxylation; the question offers only the EC number for the former.",
    "A family-level sequence inference does not by itself prove the exact substrate activities of this particular protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms that this protein (UniProt A0AA51Z3J4, L-tyrosine/L-DOPA decarboxylase 2 from Lophophora williamsii) has experimentally verified EC 4.1.1.25 activity (L-tyrosine + H+ = tyramine + CO2, ECO:0000269 from two independent PubMed sources). The protein also has EC 4.1.1.28 activity, but that EC number is not among the answer choices, so C (4.1.1.25) is the only correct option.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'SGDGGGVMMG' motif, which is a hallmark PLP-binding signature of the aromatic amino acid decarboxylase (AADC) family (EC 4.1.1.25/4.1.1.28). This motif is well-characterized across homologs from DOPA decarboxylase in humans, tyrosine decarboxylases in plants, and bacterial AADCs. The ~522-aa length is consistent with plant AADCs. This family-level motif immediately excludes phosphatases (B: 3.1.3.2, which use Ser/His/Asp catalytic triads or metal-dependent mechanisms with entirely different folds) and kinases (D: 2.7.4.9, which require Walker A/B nucleotide-binding motifs). Between the two 4.1.1 options, the specific 'SGDGGGVMMG' pattern and overall sequence architecture match the well-studied AADC fold (4.1.1.25) rather than the more obscure 4.1.1.36. A knowledgeable model recognizing PLP-dependent enzyme motifs from homologs can meaningfully distinguish C from the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SGDGGGVMMG PLP-binding motif is a transferable family-level feature recognized across many AADC homologs. Combined with sequence length and overall architecture, this provides a concrete inference pathway from the raw sequence to the AADC family, distinguishing it from phosphatases, kinases, and other decarboxylases among the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein has dual EC activity (4.1.1.25 and 4.1.1.28), only 4.1.1.25 appears among the choices. The other options (phosphatase, kinase, and an unrelated decarboxylase) are clearly excluded by the PLP-binding motif and sequence architecture.


### Important caveats

- The protein also catalyzes EC 4.1.1.28 (L-DOPA decarboxylase), but this EC number is not offered as a choice, so no ambiguity arises among the given options.
- The SGDGGGVMMG motif is a strong family-level indicator but does not by itself prove the exact substrate specificity (tyrosine vs. DOPA vs. other aromatic amino acids); however, since only 4.1.1.25 is offered, this does not affect the answer choice.
- EC 4.1.1.36 is a relatively obscure/rare EC number; a model unfamiliar with it would likely treat it as a distractor, and the AADC-specific motifs favor 4.1.1.25.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'SGDGGGVMMG' motif, which is a hallmark PLP-binding signature of the aromatic amino acid decarboxylase (AADC) family (EC 4.1.1.25/4.1.1.28). This motif is well-characterized across homologs from DOPA decarboxylase in humans, tyrosine decarboxylases in plants, and bacterial AADCs. The ~522-aa length is consistent with plant AADCs. This family-level motif immediately excludes phosphatases (B: 3.1.3.2, which use Ser/His/Asp catalytic triads or metal-dependent mechanisms with entirely different folds) and kinases (D: 2.7.4.9, which require Walker A/B nucleotide-binding motifs). Between the two 4.1.1 options, the specific 'SGDGGGVMMG' pattern and overall sequence architecture match the well-studied AADC fold (4.1.1.25) rather than the more obscure 4.1.1.36. A knowledgeable model recognizing PLP-dependent enzyme motifs from homologs can meaningfully distinguish C from the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SGDGGGVMMG PLP-binding motif is a transferable family-level feature recognized across many AADC homologs. Combined with sequence length and overall architecture, this provides a concrete inference pathway from the raw sequence to the AADC family, distinguishing it from phosphatases, kinases, and other decarboxylases among the offered choices."
  },
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms that this protein (UniProt A0AA51Z3J4, L-tyrosine/L-DOPA decarboxylase 2 from Lophophora williamsii) has experimentally verified EC 4.1.1.25 activity (L-tyrosine + H+ = tyramine + CO2, ECO:0000269 from two independent PubMed sources). The protein also has EC 4.1.1.28 activity, but that EC number is not among the answer choices, so C (4.1.1.25) is the only correct option."
  },
  "important_caveats": [
    "The protein also catalyzes EC 4.1.1.28 (L-DOPA decarboxylase), but this EC number is not offered as a choice, so no ambiguity arises among the given options.",
    "The SGDGGGVMMG motif is a strong family-level indicator but does not by itself prove the exact substrate specificity (tyrosine vs. DOPA vs. other aromatic amino acids); however, since only 4.1.1.25 is offered, this does not affect the answer choice.",
    "EC 4.1.1.36 is a relatively obscure/rare EC number; a model unfamiliar with it would likely treat it as a distractor, and the AADC-specific motifs favor 4.1.1.25."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual EC activity (4.1.1.25 and 4.1.1.28), only 4.1.1.25 appears among the choices. The other options (phosphatase, kinase, and an unrelated decarboxylase) are clearly excluded by the PLP-binding motif and sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms that this protein (UniProt A0AA51Z3J4, L-tyrosine/L-DOPA decarboxylase 2 from Lophophora williamsii) has experimentally verified EC 4.1.1.25 activity (L-tyrosine + H+ = tyramine + CO2, ECO:0000269 from two independent PubMed sources). The protein also has EC 4.1.1.28 activity, but that EC number is not among the answer choices, so C (4.1.1.25) is the only correct option.",
    "evidence_ids": ["C4", "C5", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'SGDGGGVMMG' motif, which is a hallmark PLP-binding signature of the aromatic amino acid decarboxylase (AADC) family (EC 4.1.1.25/4.1.1.28). This motif is well-characterized across homologs from DOPA decarboxylase in humans, tyrosine decarboxylases in plants, and bacterial AADCs. The ~522-aa length is consistent with plant AADCs. This family-level motif immediately excludes phosphatases (B: 3.1.3.2, which use Ser/His/Asp catalytic triads or metal-dependent mechanisms with entirely different folds) and kinases (D: 2.7.4.9, which require Walker A/B nucleotide-binding motifs). Between the two 4.1.1 options, the specific 'SGDGGGVMMG' pattern and overall sequence architecture match the well-studied AADC fold (4.1.1.25) rather than the more obscure 4.1.1.36. A knowledgeable model recognizing PLP-dependent enzyme motifs from homologs can meaningfully distinguish C from the other choices.",
    "missing_item_specific_fact": "",
    "reason": "The SGDGGGVMMG PLP-binding motif is a transferable family-level feature recognized across many AADC homologs. Combined with sequence length and overall architecture, this provides a concrete inference pathway from the raw sequence to the AADC family, distinguishing it from phosphatases, kinases, and other decarboxylases among the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual EC activity (4.1.1.25 and 4.1.1.28), only 4.1.1.25 appears among the choices. The other options (phosphatase, kinase, and an unrelated decarboxylase) are clearly excluded by the PLP-binding motif and sequence architecture."
  },
  "important_caveats": [
    "The protein also catalyzes EC 4.1.1.28 (L-DOPA decarboxylase), but this EC number is not offered as a choice, so no ambiguity arises among the given options.",
    "The SGDGGGVMMG motif is a strong family-level indicator but does not by itself prove the exact substrate specificity (tyrosine vs. DOPA vs. other aromatic amino acids); however, since only 4.1.1.25 is offered, this does not affect the answer choice.",
    "EC 4.1.1.36 is a relatively obscure/rare EC number; a model unfamiliar with it would likely treat it as a distractor, and the AADC-specific motifs favor 4.1.1.25."
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
  "benchmark_sequence_length": 522,
  "benchmark_sequence_sha256": "39ec61a6d8642a0a7790dd9cb740bee54c5dd090de950c5c89bb7477e43c264e",
  "current_entry_audit": {
    "entryVersion": 11,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 522,
  "current_source_sequence_sha256": "39ec61a6d8642a0a7790dd9cb740bee54c5dd090de950c5c89bb7477e43c264e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 9,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AA51Z3J4",
  "selected_historical_entry_version": 9,
  "selected_historical_record_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "selected_historical_source_sequence_length": 522,
  "selected_historical_source_sequence_sha256": "39ec61a6d8642a0a7790dd9cb740bee54c5dd090de950c5c89bb7477e43c264e",
  "selected_historical_version": {
    "accession": "A0AA51Z3J4",
    "database": "Swiss-Prot",
    "entryVersion": 9,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TYDC2_LOPWI",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AA51Z3J4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":11,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"Aromatic amino acid decarboxylase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwTyDC1\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.25\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.28\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"L-tyrosine/L-DOPA decarboxylase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"LwTyDC2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14346\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.25\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"L-tyrosine + H(+) = tyramine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14345\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:327995\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:12273\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.28\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"L-dopa + H(+) = dopamine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12272\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57504\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59905\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25288.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Berman P.\",\"de Haro L.A.\",\"Cavaco A.-R.\",\"Panda S.\",\"Dong Y.\",\"Kuzmich N.\",\"Lichtenstein G.\",\"Peleg Y.\",\"Harat H.\",\"Jozwiak A.\",\"Cai J.\",\"Heinig U.\",\"Meir S.\",\"Rogachev I.\",\"Aharoni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38835170\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molp.2024.05.012\"}],\"citationType\":\"journal article\",\"firstPage\":\"1129\",\"id\":\"38835170\",\"journal\":\"Mol. Plant\",\"lastPage\":\"1150\",\"publicationDate\":\"2024\",\"title\":\"The biosynthetic pathway of the hallucinogen mescaline and its heterologous reconstruction.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Rehovot 7\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H1",
  "excerpt": "ID   TYDC2_LOPWI             Reviewed;         522 AA.\nAC   A0AA51Z3J4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 9.\nDE   RecName: Full=L-tyrosine/L-DOPA decarboxylase 2 {ECO:0000303|PubMed:38835170};\nDE            Short=LwTyDC2 {ECO:0000303|PubMed:38835170};\nDE            EC=4.1.1.25 {ECO:0000269|PubMed:38835170};\nDE            EC=4.1.1.28 {ECO:0000269|PubMed:38835170};\nDE   AltName: Full=Aromatic amino acid decarboxylase 1 {ECO:0000303|PubMed:37675639};\nDE            Short=LwTyDC1 {ECO:0000303|PubMed:37675639};\nGN   Name=TyDC2 {ECO:0000303|PubMed:38835170};\nGN   Synonyms=TyDC1 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-tyrosine/L-DOPA decarboxylase 2 {ECO:0000303|PubMed:38835170};\nDE            Short=LwTyDC2 {ECO:0000303|PubMed:38835170};\nDE            EC=4.1.1.25 {ECO:0000269|PubMed:38835170};\nDE            EC=4.1.1.28 {ECO:0000269|PubMed:38835170};\nDE   AltName: Full=Aromatic amino acid decarboxylase 1 {ECO:0000303|PubMed:37675639};\nDE            Short=LwTyDC1 {ECO:0000303|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25288.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,\nRP   BIOTECHNOLOGY, BIOPHYSICOCHEMICAL PROPERTIES, AND TISSUE SPECIFICITY.\nRC   STRAIN=cv. Rehovot 7;\nRX   PubMed=38835170; DOI=10.1016/j.molp.2024.05.012;\nRA   Berman P., de Haro L.A., Cavaco A.-R., Panda S., Dong Y., Kuzmich N.,\nRA   Lichtenstein G., Peleg Y., Harat H., Jozwiak A., Cai J., Heinig U.,\nRA   Meir S., Rogachev I., Aharoni A.;\nRT   \"The biosynthetic pathway of the hallucinogen mescaline and its\nRT   heterologous reconstruction.\";\nRL   Mol. Plant 17:1129-1150(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-tyrosine + H(+) = tyramine + CO2; Xref=Rhea:RHEA:14345,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:58315,\nCC         ChEBI:CHEBI:327995; EC=4.1.1.25;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14346;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-dopa + H(+) = dopamine + CO2; Xref=Rhea:RHEA:12272,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57504,\nCC         ChEBI:CHEBI:59905; EC=4.1.1.28;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:12273;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
