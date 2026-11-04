# pathway_0196

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0196.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Amino-acid biosynthesis

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
A. terpenoid biosynthesis.
B. Pigment biosynthesis. .
C. sterol biosynthesis. .
D. Amino-acid biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt pathway annotation places the protein in L-histidine biosynthesis, an amino-acid biosynthesis pathway. The annotation cites experimental evidence (ECO:0000269), though the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a likely plastid-targeting N-terminal region followed by a soluble enzyme domain whose family-level sequence pattern is consistent with a HisA/ProFAR-isomerase-type enzyme. Knowledge transferable from homologous enzymes links that family to histidine biosynthesis, distinguishing amino-acid biosynthesis (D) from the offered terpenoid, pigment, and sterol pathways.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition from the sequence provides a meaningful basis to choose D without needing the exact protein's recorded pathway annotation. The transit-peptide-like region is supportive context, but the enzyme-family inference is the main discriminator.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, amino-acid biosynthesis is the pathway indicated by the inferred enzyme family.


### Important caveats

- The sequence itself does not experimentally establish pathway function; the reviewer-only database annotation supports the key and cites experimental evidence.
- The family assignment is a transferable sequence-based inference, not a direct measurement from the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely plastid-targeting N-terminal region followed by a soluble enzyme domain whose family-level sequence pattern is consistent with a HisA/ProFAR-isomerase-type enzyme. Knowledge transferable from homologous enzymes links that family to histidine biosynthesis, distinguishing amino-acid biosynthesis (D) from the offered terpenoid, pigment, and sterol pathways.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence provides a meaningful basis to choose D without needing the exact protein's recorded pathway annotation. The transit-peptide-like region is supportive context, but the enzyme-family inference is the main discriminator."
  },
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation places the protein in L-histidine biosynthesis, an amino-acid biosynthesis pathway. The annotation cites experimental evidence (ECO:0000269), though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence itself does not experimentally establish pathway function; the reviewer-only database annotation supports the key and cites experimental evidence.",
    "The family assignment is a transferable sequence-based inference, not a direct measurement from the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, amino-acid biosynthesis is the pathway indicated by the inferred enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation places the protein in L-histidine biosynthesis, an amino-acid biosynthesis pathway. The annotation cites experimental evidence (ECO:0000269), though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a likely plastid-targeting N-terminal region followed by a soluble enzyme domain whose family-level sequence pattern is consistent with a HisA/ProFAR-isomerase-type enzyme. Knowledge transferable from homologous enzymes links that family to histidine biosynthesis, distinguishing amino-acid biosynthesis (D) from the offered terpenoid, pigment, and sterol pathways.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence provides a meaningful basis to choose D without needing the exact protein's recorded pathway annotation. The transit-peptide-like region is supportive context, but the enzyme-family inference is the main discriminator."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, amino-acid biosynthesis is the pathway indicated by the inferred enzyme family."
  },
  "important_caveats": [
    "The sequence itself does not experimentally establish pathway function; the reviewer-only database annotation supports the key and cites experimental evidence.",
    "The family assignment is a transferable sequence-based inference, not a direct measurement from the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) explicitly states the pathway as 'Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9' with experimental evidence (ECO:0000269, PubMed:39186852). The protein is HISN3 (5'-proFAR isomerase, EC 5.3.1.16), confirmed by X-ray crystallography and kinetic studies. Choice D (Amino-acid biosynthesis) is directly supported.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an N-terminal chloroplast transit peptide (rich in Ser, Pro, Arg in the first ~35 residues) followed by a core domain with diagnostic motifs of the HisA/HisF/HisN TIM-barrel isomerase superfamily: the 'GADP' motif (GADPFSK) and the 'DRWQ' motif (IVTDRWQKFSDVSLDAK). These motifs are well-characterized hallmarks of the histidine biosynthesis isomerase family (HisA/HisF in bacteria, HisN/HISN in plants and fungi). This entire family functions exclusively in L-histidine biosynthesis, which falls under amino-acid biosynthesis. The chloroplast targeting is consistent with plant histidine biosynthesis occurring in plastids. Among the offered choices: terpenoid biosynthesis uses terpene cyclases and prenyltransferases (different folds); sterol biosynthesis uses cytochrome P450s and reductases; pigment biosynthesis uses various enzymes but not HisA/HisF/HisN-like TIM-barrel isomerases. The specific combination of chloroplast targeting + TIM-barrel fold + GAD/DRWQ motifs uniquely identifies this as a histidine biosynthesis enzyme, making D the only viable choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HisA/HisF/HisN superfamily is extensively characterized across bacteria, fungi, and plants. The conserved TIM-barrel catalytic motifs (GAD, DRWQ) are transferable knowledge learned from many homologs. Recognizing these motifs and the chloroplast transit peptide allows a knowledgeable model to assign the protein to histidine biosynthesis (amino-acid biosynthesis) without needing to look up this specific Medicago truncatula entry. The other three pathway options involve mechanistically and structurally distinct enzyme families.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The HisA/HisF/HisN family is exclusively associated with histidine biosynthesis. The diagnostic motifs and chloroplast targeting unambiguously point to amino-acid biosynthesis among the four choices. Terpenoid, pigment, and sterol biosynthesis do not employ TIM-barrel isomerases of this family.


### Important caveats

- The reviewer-only evidence confirms the annotation with experimental support (X-ray crystallography, kinetics), but this was not available to the evaluated model.
- The entry was first publicly released in June 2025; if the benchmark was constructed before that date, the annotation may have been inferred computationally or from homolog transfer at construction time.
- The TIM-barrel fold is common across many enzyme families, but the specific GAD/DRWQ motif combination is diagnostic for HisA/HisF/HisN and not shared with enzymes in the other three pathway options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an N-terminal chloroplast transit peptide (rich in Ser, Pro, Arg in the first ~35 residues) followed by a core domain with diagnostic motifs of the HisA/HisF/HisN TIM-barrel isomerase superfamily: the 'GADP' motif (GADPFSK) and the 'DRWQ' motif (IVTDRWQKFSDVSLDAK). These motifs are well-characterized hallmarks of the histidine biosynthesis isomerase family (HisA/HisF in bacteria, HisN/HISN in plants and fungi). This entire family functions exclusively in L-histidine biosynthesis, which falls under amino-acid biosynthesis. The chloroplast targeting is consistent with plant histidine biosynthesis occurring in plastids. Among the offered choices: terpenoid biosynthesis uses terpene cyclases and prenyltransferases (different folds); sterol biosynthesis uses cytochrome P450s and reductases; pigment biosynthesis uses various enzymes but not HisA/HisF/HisN-like TIM-barrel isomerases. The specific combination of chloroplast targeting + TIM-barrel fold + GAD/DRWQ motifs uniquely identifies this as a histidine biosynthesis enzyme, making D the only viable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HisA/HisF/HisN superfamily is extensively characterized across bacteria, fungi, and plants. The conserved TIM-barrel catalytic motifs (GAD, DRWQ) are transferable knowledge learned from many homologs. Recognizing these motifs and the chloroplast transit peptide allows a knowledgeable model to assign the protein to histidine biosynthesis (amino-acid biosynthesis) without needing to look up this specific Medicago truncatula entry. The other three pathway options involve mechanistically and structurally distinct enzyme families."
  },
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly states the pathway as 'Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9' with experimental evidence (ECO:0000269, PubMed:39186852). The protein is HISN3 (5'-proFAR isomerase, EC 5.3.1.16), confirmed by X-ray crystallography and kinetic studies. Choice D (Amino-acid biosynthesis) is directly supported."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation with experimental support (X-ray crystallography, kinetics), but this was not available to the evaluated model.",
    "The entry was first publicly released in June 2025; if the benchmark was constructed before that date, the annotation may have been inferred computationally or from homolog transfer at construction time.",
    "The TIM-barrel fold is common across many enzyme families, but the specific GAD/DRWQ motif combination is diagnostic for HisA/HisF/HisN and not shared with enzymes in the other three pathway options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HisA/HisF/HisN family is exclusively associated with histidine biosynthesis. The diagnostic motifs and chloroplast targeting unambiguously point to amino-acid biosynthesis among the four choices. Terpenoid, pigment, and sterol biosynthesis do not employ TIM-barrel isomerases of this family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly states the pathway as 'Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9' with experimental evidence (ECO:0000269, PubMed:39186852). The protein is HISN3 (5'-proFAR isomerase, EC 5.3.1.16), confirmed by X-ray crystallography and kinetic studies. Choice D (Amino-acid biosynthesis) is directly supported.",
    "evidence_ids": ["C5", "C4", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an N-terminal chloroplast transit peptide (rich in Ser, Pro, Arg in the first ~35 residues) followed by a core domain with diagnostic motifs of the HisA/HisF/HisN TIM-barrel isomerase superfamily: the 'GADP' motif (GADPFSK) and the 'DRWQ' motif (IVTDRWQKFSDVSLDAK). These motifs are well-characterized hallmarks of the histidine biosynthesis isomerase family (HisA/HisF in bacteria, HisN/HISN in plants and fungi). This entire family functions exclusively in L-histidine biosynthesis, which falls under amino-acid biosynthesis. The chloroplast targeting is consistent with plant histidine biosynthesis occurring in plastids. Among the offered choices: terpenoid biosynthesis uses terpene cyclases and prenyltransferases (different folds); sterol biosynthesis uses cytochrome P450s and reductases; pigment biosynthesis uses various enzymes but not HisA/HisF/HisN-like TIM-barrel isomerases. The specific combination of chloroplast targeting + TIM-barrel fold + GAD/DRWQ motifs uniquely identifies this as a histidine biosynthesis enzyme, making D the only viable choice.",
    "missing_item_specific_fact": "",
    "reason": "The HisA/HisF/HisN superfamily is extensively characterized across bacteria, fungi, and plants. The conserved TIM-barrel catalytic motifs (GAD, DRWQ) are transferable knowledge learned from many homologs. Recognizing these motifs and the chloroplast transit peptide allows a knowledgeable model to assign the protein to histidine biosynthesis (amino-acid biosynthesis) without needing to look up this specific Medicago truncatula entry. The other three pathway options involve mechanistically and structurally distinct enzyme families."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HisA/HisF/HisN family is exclusively associated with histidine biosynthesis. The diagnostic motifs and chloroplast targeting unambiguously point to amino-acid biosynthesis among the four choices. Terpenoid, pigment, and sterol biosynthesis do not employ TIM-barrel isomerases of this family."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation with experimental support (X-ray crystallography, kinetics), but this was not available to the evaluated model.",
    "The entry was first publicly released in June 2025; if the benchmark was constructed before that date, the annotation may have been inferred computationally or from homolog transfer at construction time.",
    "The TIM-barrel fold is common across many enzyme families, but the specific GAD/DRWQ motif combination is diagnostic for HisA/HisF/HisN and not shared with enzymes in the other three pathway options."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine\nCC       from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9.\nCC       {ECO:0000269|PubMed:39186852}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 196. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
