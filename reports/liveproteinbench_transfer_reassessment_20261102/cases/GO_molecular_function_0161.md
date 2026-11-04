# GO_molecular_function_0161

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0161.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — 1-(5-phosphoribosyl)-5-&#91;(5-phosphoribosylamino)methylideneamino&#93;imidazole-4-carboxamide isomerase activity

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
A. 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity
B. NADP binding
C. zinc ion binding
D. O-methyltransferase activity
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

### Expected-answer support: supported

> The sequence-matched UniProt record reports the isomerase reaction and the corresponding GO molecular-function term; the annotation is linked to experimental evidence. This supports option A.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is consistent with a plastid-targeting peptide, followed by a globular enzyme core. A knowledgeable model could use sequence-family similarity to recognize a plant histidine-biosynthesis ProFAR-isomerase-like enzyme, favoring A. The sequence also lacks obvious hallmarks of a zinc-binding motif, a SAM-dependent O-methyltransferase, or a Rossmann-like NADP-binding enzyme, making C, D, and B less plausible, respectively.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and comparison with related enzyme sequences provide a meaningful route to A without needing the exact protein's database record. The localization and absence of those alternative motifs are supporting clues, not proof; the sequence alone may leave substantial uncertainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct functions, and the supplied evidence specifically supports the isomerase activity in A.


### Important caveats

- Reviewer-only evidence confirms the annotation for the exact sequence; that evidence was not part of the original model input.
- The sequence clues are not uniquely diagnostic, so the transferable inference is probabilistic rather than conclusive.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is consistent with a plastid-targeting peptide, followed by a globular enzyme core. A knowledgeable model could use sequence-family similarity to recognize a plant histidine-biosynthesis ProFAR-isomerase-like enzyme, favoring A. The sequence also lacks obvious hallmarks of a zinc-binding motif, a SAM-dependent O-methyltransferase, or a Rossmann-like NADP-binding enzyme, making C, D, and B less plausible, respectively.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and comparison with related enzyme sequences provide a meaningful route to A without needing the exact protein's database record. The localization and absence of those alternative motifs are supporting clues, not proof; the sequence alone may leave substantial uncertainty."
  },
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports the isomerase reaction and the corresponding GO molecular-function term; the annotation is linked to experimental evidence. This supports option A."
  },
  "important_caveats": [
    "Reviewer-only evidence confirms the annotation for the exact sequence; that evidence was not part of the original model input.",
    "The sequence clues are not uniquely diagnostic, so the transferable inference is probabilistic rather than conclusive."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and the supplied evidence specifically supports the isomerase activity in A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports the isomerase reaction and the corresponding GO molecular-function term; the annotation is linked to experimental evidence. This supports option A.",
    "evidence_ids": ["H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is consistent with a plastid-targeting peptide, followed by a globular enzyme core. A knowledgeable model could use sequence-family similarity to recognize a plant histidine-biosynthesis ProFAR-isomerase-like enzyme, favoring A. The sequence also lacks obvious hallmarks of a zinc-binding motif, a SAM-dependent O-methyltransferase, or a Rossmann-like NADP-binding enzyme, making C, D, and B less plausible, respectively.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and comparison with related enzyme sequences provide a meaningful route to A without needing the exact protein's database record. The localization and absence of those alternative motifs are supporting clues, not proof; the sequence alone may leave substantial uncertainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and the supplied evidence specifically supports the isomerase activity in A."
  },
  "important_caveats": [
    "Reviewer-only evidence confirms the annotation for the exact sequence; that evidence was not part of the original model input.",
    "The sequence clues are not uniquely diagnostic, so the transferable inference is probabilistic rather than conclusive."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G7IFI7 (HISN3_MEDTR) is annotated with GO:0003949 (1-(5-phosphoribosyl)-5-&#91;(5-phosphoribosylamino)methylideneamino&#93;imidazole-4-carboxamide isomerase activity) with evidence code IDA (Inferred from Direct Assay), confirmed by X-ray crystallography at 1.54 Å in complex with 5'-ProFAR and PrFAR, kinetic characterization, and mutagenesis (PubMed:39186852). The EC number 5.3.1.16 is also experimentally assigned. The GO term name matches option A exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple TIM-barrel motifs characteristic of the HisA/HisI/HisF/HisN superfamily, most notably the conserved 'GADP' motif in 'IMLGADPFSKAASLEALHAYPGG' and the 'GGGINSDNCLSYIEEGASHVIVTSYVFNNGQ' segment, which are hallmark features of ProFAR isomerase (HisA/HisI/HisN) proteins. The N-terminal region rich in Ser, Pro, and Arg residues is consistent with a chloroplast transit peptide, fitting a plant HisN-type enzyme. Conversely, the sequence lacks a Rossmann-fold GxGxxG motif (ruling out NADP binding), lacks canonical zinc-finger Cys/His clusters such as CCHH or CCCH in the mature domain (ruling out zinc ion binding), and lacks the conserved β-sheet SAM-binding motifs of O-methyltransferases (ruling out O-methyltransferase activity). A model familiar with the HisA/HisI/HisF/HisN TIM-barrel superfamily and the distinctive GADP motif can confidently assign the isomerase activity of option A and exclude the mechanistically unrelated alternatives B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The TIM-barrel architecture with the GADP motif is a well-known, transferable feature of the HisA/HisI/HisN family learned from many characterized proteins (E. coli HisA, yeast HisI, etc.). The absence of motifs diagnostic of the three distractor functions (Rossmann fold, zinc finger, SAM-binding) further narrows the choice. This constitutes a concrete, family-level inference that meaningfully distinguishes option A from the offered alternatives without requiring the exact UniProt annotation of this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct molecular functions (aldose-ketose isomerase, nucleotide binding, metal binding, methyltransferase) with non-overlapping structural signatures. The GADP/TIM-barrel features point uniquely to A, and no other option is partially supported by the sequence.


### Important caveats

- The UniProt entry also carries a general GO:0046872 (metal ion binding) IEA annotation, but this is not the specific zinc ion binding (GO:0008270) listed in option C, and it is a broad keyword-derived annotation rather than a primary functional assignment.
- The exact GO term name in option A is unusually long and specific; a model might recognize the family but struggle to match the precise chemical name. However, among the four offered choices, only A corresponds to the HisA/HisI/HisN family function.
- The reviewer-only evidence confirms experimental (IDA) support for the answer; the evaluated model did not have access to this annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple TIM-barrel motifs characteristic of the HisA/HisI/HisF/HisN superfamily, most notably the conserved 'GADP' motif in 'IMLGADPFSKAASLEALHAYPGG' and the 'GGGINSDNCLSYIEEGASHVIVTSYVFNNGQ' segment, which are hallmark features of ProFAR isomerase (HisA/HisI/HisN) proteins. The N-terminal region rich in Ser, Pro, and Arg residues is consistent with a chloroplast transit peptide, fitting a plant HisN-type enzyme. Conversely, the sequence lacks a Rossmann-fold GxGxxG motif (ruling out NADP binding), lacks canonical zinc-finger Cys/His clusters such as CCHH or CCCH in the mature domain (ruling out zinc ion binding), and lacks the conserved β-sheet SAM-binding motifs of O-methyltransferases (ruling out O-methyltransferase activity). A model familiar with the HisA/HisI/HisF/HisN TIM-barrel superfamily and the distinctive GADP motif can confidently assign the isomerase activity of option A and exclude the mechanistically unrelated alternatives B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The TIM-barrel architecture with the GADP motif is a well-known, transferable feature of the HisA/HisI/HisN family learned from many characterized proteins (E. coli HisA, yeast HisI, etc.). The absence of motifs diagnostic of the three distractor functions (Rossmann fold, zinc finger, SAM-binding) further narrows the choice. This constitutes a concrete, family-level inference that meaningfully distinguishes option A from the offered alternatives without requiring the exact UniProt annotation of this specific protein."
  },
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G7IFI7 (HISN3_MEDTR) is annotated with GO:0003949 (1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity) with evidence code IDA (Inferred from Direct Assay), confirmed by X-ray crystallography at 1.54 Å in complex with 5'-ProFAR and PrFAR, kinetic characterization, and mutagenesis (PubMed:39186852). The EC number 5.3.1.16 is also experimentally assigned. The GO term name matches option A exactly."
  },
  "important_caveats": [
    "The UniProt entry also carries a general GO:0046872 (metal ion binding) IEA annotation, but this is not the specific zinc ion binding (GO:0008270) listed in option C, and it is a broad keyword-derived annotation rather than a primary functional assignment.",
    "The exact GO term name in option A is unusually long and specific; a model might recognize the family but struggle to match the precise chemical name. However, among the four offered choices, only A corresponds to the HisA/HisI/HisN family function.",
    "The reviewer-only evidence confirms experimental (IDA) support for the answer; the evaluated model did not have access to this annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct molecular functions (aldose-ketose isomerase, nucleotide binding, metal binding, methyltransferase) with non-overlapping structural signatures. The GADP/TIM-barrel features point uniquely to A, and no other option is partially supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G7IFI7 (HISN3_MEDTR) is annotated with GO:0003949 (1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity) with evidence code IDA (Inferred from Direct Assay), confirmed by X-ray crystallography at 1.54 Å in complex with 5'-ProFAR and PrFAR, kinetic characterization, and mutagenesis (PubMed:39186852). The EC number 5.3.1.16 is also experimentally assigned. The GO term name matches option A exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple TIM-barrel motifs characteristic of the HisA/HisI/HisF/HisN superfamily, most notably the conserved 'GADP' motif in 'IMLGADPFSKAASLEALHAYPGG' and the 'GGGINSDNCLSYIEEGASHVIVTSYVFNNGQ' segment, which are hallmark features of ProFAR isomerase (HisA/HisI/HisN) proteins. The N-terminal region rich in Ser, Pro, and Arg residues is consistent with a chloroplast transit peptide, fitting a plant HisN-type enzyme. Conversely, the sequence lacks a Rossmann-fold GxGxxG motif (ruling out NADP binding), lacks canonical zinc-finger Cys/His clusters such as CCHH or CCCH in the mature domain (ruling out zinc ion binding), and lacks the conserved β-sheet SAM-binding motifs of O-methyltransferases (ruling out O-methyltransferase activity). A model familiar with the HisA/HisI/HisF/HisN TIM-barrel superfamily and the distinctive GADP motif can confidently assign the isomerase activity of option A and exclude the mechanistically unrelated alternatives B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The TIM-barrel architecture with the GADP motif is a well-known, transferable feature of the HisA/HisI/HisN family learned from many characterized proteins (E. coli HisA, yeast HisI, etc.). The absence of motifs diagnostic of the three distractor functions (Rossmann fold, zinc finger, SAM-binding) further narrows the choice. This constitutes a concrete, family-level inference that meaningfully distinguishes option A from the offered alternatives without requiring the exact UniProt annotation of this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct molecular functions (aldose-ketose isomerase, nucleotide binding, metal binding, methyltransferase) with non-overlapping structural signatures. The GADP/TIM-barrel features point uniquely to A, and no other option is partially supported by the sequence."
  },
  "important_caveats": [
    "The UniProt entry also carries a general GO:0046872 (metal ion binding) IEA annotation, but this is not the specific zinc ion binding (GO:0008270) listed in option C, and it is a broad keyword-derived annotation rather than a primary functional assignment.",
    "The exact GO term name in option A is unusually long and specific; a model might recognize the family but struggle to match the precise chemical name. However, among the four offered choices, only A corresponds to the HisA/HisI/HisN family function.",
    "The reviewer-only evidence confirms experimental (IDA) support for the answer; the evaluated model did not have access to this annotation."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"value\":\"Component of the histidine biosynthesis pathway that catalyzes the isomerization of 5'-ProFAR (pro-phosphoribosyl formimino-5-aminoimidazole-4-carboxamide ribonucleotide, referred as 1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide) to PrFAR (phosphoribulosyl formimino-5-aminoimidazole-4-carboxamide ribonucleotide, referred as 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide) (PubMed:39186852)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39186852\",\"source\":\"PubMed\"}],\"id\":\"GO:0003949\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "retrieved_utc": "2026-11-02T04:28:47.235961+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad",
  "url": "https://rest.uniprot.org/uniprotkb/G7IFI7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)

```json
{
  "evidence_id": "C8",
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
  "excerpt": "CC   -!- FUNCTION: Component of the histidine biosynthesis pathway that\nCC       catalyzes the isomerization of 5'-ProFAR (pro-phosphoribosyl formimino-\nCC       5-aminoimidazole-4-carboxamide ribonucleotide, referred as 1-(5-\nCC       phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-\nCC       ribosylamino)methylideneamino]imidazole-4-carboxamide) to PrFAR\nCC       (phosphoribulosyl formimino-5-aminoimidazole-4-carboxamide\nCC       ribonucleotide, referred as 5-[(5-phospho-1-deoxy-D-ribulos-1-\nCC       ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-\nCC       carboxamide) (PubMed:39186852). {ECO:0000269|PubMed:39186852}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-95",
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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0003949; F:1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 147-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:50.784174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8",
  "url": "https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003949\nname: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide.\" [EC:5.3.1.16, RHEA:15469]\nsynonym: \"1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide aldose-ketose-isomerase activity\" RELATED [EC:5.3.1.16]\nsynonym: \"1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide ketol-isomerase activity\" RELATED [EC:5.3.1.16]\nsynonym: \"N-(5'-phospho-D-ribosylformimino)-5-amino-1-(5''-phosphoribosyl)-4-imidazolecarboxamide isomerase activity\" RELATED [EC:5.3.1.16]\nsynonym: \"N-(phosphoribosylformimino) aminophosphoribosylimidazolecarboxamide isomerase activity\" RELATED [EC:5.3.1.16]\nsynonym: \"phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase activity\" RELATED [EC:5.3.1.16]\nsynonym: \"phosphoribosylformiminoaminophosphoribosylimidazolecarboxamide isomerase activity\" RELATED [EC:5.3.1.16]\nxref: EC:5.3.1.16\nxref: KEGG_REACTION:R04640\nxref: MetaCyc:PRIBFAICARPISOM-RXN\nxref: RHEA:15469\nis_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses\nproperty_value: skos:exactMatch EC:5.3.1.16\nproperty_value: skos:exactMatch RHEA:15469\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003949",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 31924-31942",
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
  "excerpt": "[Term]\nid: GO:0008171\nname: O-methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group to the oxygen atom of an acceptor molecule.\" [GOC:ai]\nxref: Reactome:R-HSA-5578717 \"BCDIN3D dimethylates 5' phosphate of pre-miR-145\"\nxref: Reactome:R-HSA-5629203 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in 4xMeR-PIWIL1:piRNA:TDRD6:TDRKH\"\nxref: Reactome:R-HSA-5629218 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in 6xMeR-PIWIL2:piRNA:TDRD1:TDRD12:DDX4:ASZ:MOV10L1\"\nxref: Reactome:R-HSA-5629237 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in MeR-PIWIL4:piRNA:TDRD9:MAEL:TDRKH\"\nxref: Reactome:R-HSA-6790907 \"Box C/D snoRNP methylates ribonucleotides in pre-rRNA yielding 2'-O-methylribonucleotides\"\nis_a: GO:0008168 ! methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008171",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 80302-80313",
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
  "excerpt": "[Term]\nid: GO:0008270\nname: zinc ion binding\nnamespace: molecular_function\ndef: \"Binding to a zinc ion (Zn).\" [GOC:ai]\nsynonym: \"zinc binding\" EXACT []\nsynonym: \"Zn binding\" EXACT []\nis_a: GO:0046914 ! transition metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008270",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81431-81439",
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
  "excerpt": "[Term]\nid: GO:0050661\nname: NADP binding\nnamespace: molecular_function\ndef: \"Binding to nicotinamide-adenine dinucleotide phosphate, a coenzyme involved in many redox and biosynthetic reactions; binding may be to either the oxidized form, NADP+, or the reduced form, NADPH.\" [GOC:ai]\nsynonym: \"NADP or NADPH binding\" RELATED [GOC:mah]\nsynonym: \"NADP+ or NADPH binding\" RELATED []\nsynonym: \"nicotinamide adenine dinucleotide phosphate binding\" EXACT []\nis_a: GO:0030554 ! adenyl nucleotide binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050661",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 318403-318412",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
