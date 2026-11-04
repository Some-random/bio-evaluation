# EC_number_0072

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0072.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 5.3.1.16

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQCSVQFRPCIDIHKGKVKQIVGSTLKDLKDDDGSDPITNFESDKSAAEYATLYKQDGLKGGHVIMLGADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA

[Multiple Choices]
A. 5.3.1.16
B. 5.3.1.8
C. 2.7.4.9
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

> The supplied sequence matches the annotated protein. Its UniProt catalytic-activity annotation assigns EC 5.3.1.16 to the isomerization reaction and cites experimental evidence (ECO:0000269); the protein description gives the same EC number with that evidence code.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A transferable sequence-family inference is plausible: the N-terminal Ser/Thr- and Pro-rich segment is consistent with a plastid-targeting transit peptide, followed by a roughly 270-residue enzyme core with the sequence pattern of a plant HISN3/5'-ProFAR-isomerase family protein. Knowledge of that enzyme family connects the catalytic core to EC 5.3.1.16 (A), distinguishing it from the other isomerase in B and the kinase and methyltransferase choices. The targeting segment alone would not establish the EC number; the family-level inference does the discriminating work.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices include unrelated reaction classes as well as another isomerase, and transferable recognition of the catalytic protein family provides a meaningful, if probabilistic, basis for choosing A. This does not require recall of this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives specify different EC activities, and the family-level inference supports A over the listed alternatives.


### Important caveats

- The reviewer-only annotations support the key but were not available as original inputs.
- The inference from sequence to enzyme family is probabilistic; the transit-peptide-like N-terminus by itself is not diagnostic of catalytic function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A transferable sequence-family inference is plausible: the N-terminal Ser/Thr- and Pro-rich segment is consistent with a plastid-targeting transit peptide, followed by a roughly 270-residue enzyme core with the sequence pattern of a plant HISN3/5'-ProFAR-isomerase family protein. Knowledge of that enzyme family connects the catalytic core to EC 5.3.1.16 (A), distinguishing it from the other isomerase in B and the kinase and methyltransferase choices. The targeting segment alone would not establish the EC number; the family-level inference does the discriminating work.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices include unrelated reaction classes as well as another isomerase, and transferable recognition of the catalytic protein family provides a meaningful, if probabilistic, basis for choosing A. This does not require recall of this exact protein's database entry."
  },
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. Its UniProt catalytic-activity annotation assigns EC 5.3.1.16 to the isomerization reaction and cites experimental evidence (ECO:0000269); the protein description gives the same EC number with that evidence code."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but were not available as original inputs.",
    "The inference from sequence to enzyme family is probabilistic; the transit-peptide-like N-terminus by itself is not diagnostic of catalytic function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives specify different EC activities, and the family-level inference supports A over the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. Its UniProt catalytic-activity annotation assigns EC 5.3.1.16 to the isomerization reaction and cites experimental evidence (ECO:0000269); the protein description gives the same EC number with that evidence code.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A transferable sequence-family inference is plausible: the N-terminal Ser/Thr- and Pro-rich segment is consistent with a plastid-targeting transit peptide, followed by a roughly 270-residue enzyme core with the sequence pattern of a plant HISN3/5'-ProFAR-isomerase family protein. Knowledge of that enzyme family connects the catalytic core to EC 5.3.1.16 (A), distinguishing it from the other isomerase in B and the kinase and methyltransferase choices. The targeting segment alone would not establish the EC number; the family-level inference does the discriminating work.",
    "missing_item_specific_fact": "",
    "reason": "The choices include unrelated reaction classes as well as another isomerase, and transferable recognition of the catalytic protein family provides a meaningful, if probabilistic, basis for choosing A. This does not require recall of this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives specify different EC activities, and the family-level inference supports A over the listed alternatives."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but were not available as original inputs.",
    "The inference from sequence to enzyme family is probabilistic; the transit-peptide-like N-terminus by itself is not diagnostic of catalytic function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G7IFI7 (HISN3_MEDTR) is annotated with EC 5.3.1.16 (5'-proFAR isomerase) supported by experimental evidence (ECO:0000269, PubMed:39186852) including X-ray crystallography at 1.54 Å in complex with substrate and product, catalytic activity assays, and biophysical characterization. The sequence in the question matches the UniProt entry exactly (312 aa, SHA-256 confirmed). The EC number is well-established with direct experimental support.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish the options. (1) SIZE: The full sequence is 312 aa. Phosphoglucose isomerase (EC 5.3.1.8, option B) is a dimeric eukaryotic enzyme of ~550-570 aa; a 312-aa protein is far too short for PGI but fits the HisA/HisP family of 5'-proFAR isomerases (~240-260 aa mature + transit peptide). (2) TRANSFERASE EXCLUSION: Options C (2.7.4.9, adenylate kinase) and D (2.1.1.348, methyltransferase) belong to the transferase class (EC 2) and require entirely different folds (P-loop for adenylate kinase ~200 aa; Rossmann-like for methyltransferases) and catalytic mechanisms (phosphoryl or methyl transfer). The sequence shows no P-loop Walker A motif, no methyltransferase catalytic triad, and its TIM-barrel architecture is inconsistent with transferase folds. (3) FAMILY RECOGNITION: The N-terminal ~40 residues (MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQ...) form a chloroplast transit peptide, consistent with plant histidine-biosynthesis enzymes (HISN1/2/3 family). The mature region contains a TIM-barrel scaffold with conserved loop motifs (e.g., the 'GAD' motif in 'GADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEG', and 'DVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA') characteristic of the HisA/HisP/HisD superfamily. These features collectively point to a histidine-pathway isomerase (EC 5.3.1.16) rather than a sugar isomerase (5.3.1.8) or any transferase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use protein size (312 aa excludes PGI at ~550+ aa), fold architecture (TIM barrel excludes transferase options C and D), chloroplast transit peptide (consistent with plant HisA/HISN family), and conserved HisA-family sequence motifs to meaningfully distinguish option A from B, C, and D. This is legitimate family-level and structural-knowledge transfer, not memorization of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size constraint (312 aa vs ~550 aa for PGI), the transferase-vs-isomerase fold distinction, and the HisA-family sequence motifs together clearly favor A over B, C, and D. No other option is defensible given the sequence features.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269) from X-ray crystallography and kinetic assays (PubMed:39186852, 2024), so the EC assignment is not merely computational.
- The entry was first publicly released in June 2025; the author's exact source snapshot is unknown, but the sequence matches both current and archived (entry version 82) records.
- Distinguishing 5.3.1.16 from 5.3.1.8 relies partly on size and family motifs; a model with very limited training data on HisA-family sequences might find this distinction challenging, though the size argument is quite strong.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish the options. (1) SIZE: The full sequence is 312 aa. Phosphoglucose isomerase (EC 5.3.1.8, option B) is a dimeric eukaryotic enzyme of ~550-570 aa; a 312-aa protein is far too short for PGI but fits the HisA/HisP family of 5'-proFAR isomerases (~240-260 aa mature + transit peptide). (2) TRANSFERASE EXCLUSION: Options C (2.7.4.9, adenylate kinase) and D (2.1.1.348, methyltransferase) belong to the transferase class (EC 2) and require entirely different folds (P-loop for adenylate kinase ~200 aa; Rossmann-like for methyltransferases) and catalytic mechanisms (phosphoryl or methyl transfer). The sequence shows no P-loop Walker A motif, no methyltransferase catalytic triad, and its TIM-barrel architecture is inconsistent with transferase folds. (3) FAMILY RECOGNITION: The N-terminal ~40 residues (MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQ...) form a chloroplast transit peptide, consistent with plant histidine-biosynthesis enzymes (HISN1/2/3 family). The mature region contains a TIM-barrel scaffold with conserved loop motifs (e.g., the 'GAD' motif in 'GADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEG', and 'DVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA') characteristic of the HisA/HisP/HisD superfamily. These features collectively point to a histidine-pathway isomerase (EC 5.3.1.16) rather than a sugar isomerase (5.3.1.8) or any transferase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein size (312 aa excludes PGI at ~550+ aa), fold architecture (TIM barrel excludes transferase options C and D), chloroplast transit peptide (consistent with plant HisA/HISN family), and conserved HisA-family sequence motifs to meaningfully distinguish option A from B, C, and D. This is legitimate family-level and structural-knowledge transfer, not memorization of this specific entry's annotation."
  },
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G7IFI7 (HISN3_MEDTR) is annotated with EC 5.3.1.16 (5'-proFAR isomerase) supported by experimental evidence (ECO:0000269, PubMed:39186852) including X-ray crystallography at 1.54 Å in complex with substrate and product, catalytic activity assays, and biophysical characterization. The sequence in the question matches the UniProt entry exactly (312 aa, SHA-256 confirmed). The EC number is well-established with direct experimental support."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from X-ray crystallography and kinetic assays (PubMed:39186852, 2024), so the EC assignment is not merely computational.",
    "The entry was first publicly released in June 2025; the author's exact source snapshot is unknown, but the sequence matches both current and archived (entry version 82) records.",
    "Distinguishing 5.3.1.16 from 5.3.1.8 relies partly on size and family motifs; a model with very limited training data on HisA-family sequences might find this distinction challenging, though the size argument is quite strong."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size constraint (312 aa vs ~550 aa for PGI), the transferase-vs-isomerase fold distinction, and the HisA-family sequence motifs together clearly favor A over B, C, and D. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G7IFI7 (HISN3_MEDTR) is annotated with EC 5.3.1.16 (5'-proFAR isomerase) supported by experimental evidence (ECO:0000269, PubMed:39186852) including X-ray crystallography at 1.54 Å in complex with substrate and product, catalytic activity assays, and biophysical characterization. The sequence in the question matches the UniProt entry exactly (312 aa, SHA-256 confirmed). The EC number is well-established with direct experimental support.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish the options. (1) SIZE: The full sequence is 312 aa. Phosphoglucose isomerase (EC 5.3.1.8, option B) is a dimeric eukaryotic enzyme of ~550-570 aa; a 312-aa protein is far too short for PGI but fits the HisA/HisP family of 5'-proFAR isomerases (~240-260 aa mature + transit peptide). (2) TRANSFERASE EXCLUSION: Options C (2.7.4.9, adenylate kinase) and D (2.1.1.348, methyltransferase) belong to the transferase class (EC 2) and require entirely different folds (P-loop for adenylate kinase ~200 aa; Rossmann-like for methyltransferases) and catalytic mechanisms (phosphoryl or methyl transfer). The sequence shows no P-loop Walker A motif, no methyltransferase catalytic triad, and its TIM-barrel architecture is inconsistent with transferase folds. (3) FAMILY RECOGNITION: The N-terminal ~40 residues (MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQ...) form a chloroplast transit peptide, consistent with plant histidine-biosynthesis enzymes (HISN1/2/3 family). The mature region contains a TIM-barrel scaffold with conserved loop motifs (e.g., the 'GAD' motif in 'GADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEG', and 'DVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA') characteristic of the HisA/HisP/HisD superfamily. These features collectively point to a histidine-pathway isomerase (EC 5.3.1.16) rather than a sugar isomerase (5.3.1.8) or any transferase.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein size (312 aa excludes PGI at ~550+ aa), fold architecture (TIM barrel excludes transferase options C and D), chloroplast transit peptide (consistent with plant HisA/HISN family), and conserved HisA-family sequence motifs to meaningfully distinguish option A from B, C, and D. This is legitimate family-level and structural-knowledge transfer, not memorization of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size constraint (312 aa vs ~550 aa for PGI), the transferase-vs-isomerase fold distinction, and the HisA-family sequence motifs together clearly favor A over B, C, and D. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from X-ray crystallography and kinetic assays (PubMed:39186852, 2024), so the EC assignment is not merely computational.",
    "The entry was first publicly released in June 2025; the author's exact source snapshot is unknown, but the sequence matches both current and archived (entry version 82) records.",
    "Distinguishing 5.3.1.16 from 5.3.1.8 relies partly on size and family motifs; a model with very limited training data on HisA-family sequences might find this distinction challenging, though the size argument is quite strong."
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
  "benchmark_sequence_length": 312,
  "benchmark_sequence_sha256": "5cc38259edb8e6a0c05d63b5b309a07322d6beb3042fe4fc48cb46b256ebf155",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-01-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 312,
  "current_source_sequence_sha256": "5cc38259edb8e6a0c05d63b5b309a07322d6beb3042fe4fc48cb46b256ebf155",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 82,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G7IFI7",
  "selected_historical_entry_version": 82,
  "selected_historical_record_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "selected_historical_source_sequence_length": 312,
  "selected_historical_source_sequence_sha256": "5cc38259edb8e6a0c05d63b5b309a07322d6beb3042fe4fc48cb46b256ebf155",
  "selected_historical_version": {
    "accession": "G7IFI7",
    "database": "Swiss-Prot",
    "entryVersion": 82,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISN3_MEDTR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G7IFI7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-01-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Barrel medic\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"Hologalegina\",\"IRL clade\",\"Trifolieae\",\"Medicago\"],\"scientificName\":\"Medicago truncatula\",\"synonyms\":[\"Medicago tribuloides\"],\"taxonId\":3880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"5'-proFAR isomerase 3\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Protein HISTIDINE BIOSYNTHESIS 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"MtHISN3\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:15470\"}}],\"reaction\":{\"ecNumber\":\"5.3.1.16\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"name\":\"1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15469\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58435\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58525\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Witek W.\",\"Imiolczyk B.\",\"Ruszkowski M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39186852\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.plaphy.2024.109065\"}],\"citationType\":\"journal article\",\"firstPage\":\"109065\",\"id\":\"39186852\",\"journal\":\"Plant Physiol. Biochem.\",\"lastPage\":\"109065\",\"publicationDate\":\"2024\",\"title\":\"Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-ProFAR isomerase.\",\"volume\":\"215\"},\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM ION; 5'-PROFAR AND PRFAR\",\"FUNCTION\",\"MUTAGENESIS OF ASP-57 AND 74-LEU--SER-80\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"COFACTOR\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H1",
  "excerpt": "ID   HISN3_MEDTR             Reviewed;         312 AA.\nAC   G7IFI7; A0A396J617; B7FHU9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-JAN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 82.\nDE   RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic {ECO:0000303|PubMed:39186852};\nDE            EC=5.3.1.16 {ECO:0000269|PubMed:39186852};\nDE   AltName: Full=5'-proFAR isomerase 3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Protein HISTIDINE BIOSYNTHESIS 3 {ECO:0000303|PubMed:39186852};\nDE            Short=MtHISN3 {ECO:0000303|PubMed:39186852};\nDE   Flags: Precursor;\nGN   Name=HISN3 {ECO:0000303|PubMed:39186852};\nGN   OrderedLocusNames=MTR_2g015010 {ECO:0000312|EMBL:AES63938.1},\nGN   MtrunA17_Chr2g0283151 {ECO:0000312|EMBL:RHN72021.1};\nOS   Medicago truncatula (Barrel medic) (Medicago tribuloides).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; Hologalegina; IRL clade; Trifolieae; Medicago.\nOX   NCBI_TaxID=3880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic {ECO:0000303|PubMed:39186852};\nDE            EC=5.3.1.16 {ECO:0000269|PubMed:39186852};\nDE   AltName: Full=5'-proFAR isomerase 3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3 {ECO:0000303|PubMed:39186852};\nDE   AltName: Full=Protein HISTIDINE BIOSYNTHESIS 3 {ECO:0000303|PubMed:39186852};\nDE            Short=MtHISN3 {ECO:0000303|PubMed:39186852};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H3",
  "excerpt": "RN   [5]\nRP   X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM\nRP   ION; 5'-PROFAR AND PRFAR, FUNCTION, MUTAGENESIS OF ASP-57 AND\nRP   74-LEU--SER-80, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES,\nRP   COFACTOR, AND PATHWAY.\nRX   PubMed=39186852; DOI=10.1016/j.plaphy.2024.109065;\nRA   Witek W., Imiolczyk B., Ruszkowski M.;\nRT   \"Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-\nRT   ProFAR isomerase.\";\nRL   Plant Physiol. Biochem. 215:109065-109065(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-\nCC         ribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-\nCC         phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-\nCC         ribosyl)imidazole-4-carboxamide; Xref=Rhea:RHEA:15469,\nCC         ChEBI:CHEBI:58435, ChEBI:CHEBI:58525; EC=5.3.1.16;\nCC         Evidence={ECO:0000269|PubMed:39186852};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:15470;\nCC         Evidence={ECO:0000269|PubMed:39186852};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
