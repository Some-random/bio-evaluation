# GO_molecular_function_0152

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0152.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — S-adenosylmethionine-dependent methyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. 2-oxoglutarate-dependent dioxygenase activity
B. phosphopantothenoylcysteine decarboxylase activity
C. S-adenosylmethionine-dependent methyltransferase activity
D. tRNA (guanine(18)-2'-O)-methyltransferase activity
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

> The sequence-matched record reports experimentally supported N-methylation of ajmaline using S-adenosyl-L-methionine, which directly supports the broader SAM-dependent methyltransferase activity in C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 291-aa sequence is consistent with a plant small-molecule methyltransferase: its methyltransferase-like sequence features and compact enzyme length support a SAM-dependent methyltransferase rather than an Fe/2-oxoglutarate-dependent dioxygenase or phosphopantothenoylcysteine decarboxylase. Family-level knowledge that plant gamma-tocopherol-methyltransferase-like enzymes are SAM-dependent methyltransferases favors C; the sequence does not suggest the specific tRNA substrate and RNA-methyltransferase class required by D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable methyltransferase-family and sequence-pattern knowledge gives a meaningful basis for selecting the broad SAM-dependent methyltransferase option over these alternatives. Exact substrate specificity would require further evidence, but is not needed to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is a more specific tRNA methyltransferase activity, not an equivalent alternative supported by the sequence-level family inference; C is the broad activity indicated.


### Important caveats

- The experimental functional annotation is reviewer-only evidence and was not available as an input to the evaluated model.
- The sequence-based family inference supports the broad methyltransferase choice but does not independently establish the exact ajmaline substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 291-aa sequence is consistent with a plant small-molecule methyltransferase: its methyltransferase-like sequence features and compact enzyme length support a SAM-dependent methyltransferase rather than an Fe/2-oxoglutarate-dependent dioxygenase or phosphopantothenoylcysteine decarboxylase. Family-level knowledge that plant gamma-tocopherol-methyltransferase-like enzymes are SAM-dependent methyltransferases favors C; the sequence does not suggest the specific tRNA substrate and RNA-methyltransferase class required by D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable methyltransferase-family and sequence-pattern knowledge gives a meaningful basis for selecting the broad SAM-dependent methyltransferase option over these alternatives. Exact substrate specificity would require further evidence, but is not needed to distinguish the offered choices."
  },
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports experimentally supported N-methylation of ajmaline using S-adenosyl-L-methionine, which directly supports the broader SAM-dependent methyltransferase activity in C."
  },
  "important_caveats": [
    "The experimental functional annotation is reviewer-only evidence and was not available as an input to the evaluated model.",
    "The sequence-based family inference supports the broad methyltransferase choice but does not independently establish the exact ajmaline substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is a more specific tRNA methyltransferase activity, not an equivalent alternative supported by the sequence-level family inference; C is the broad activity indicated."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports experimentally supported N-methylation of ajmaline using S-adenosyl-L-methionine, which directly supports the broader SAM-dependent methyltransferase activity in C.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 291-aa sequence is consistent with a plant small-molecule methyltransferase: its methyltransferase-like sequence features and compact enzyme length support a SAM-dependent methyltransferase rather than an Fe/2-oxoglutarate-dependent dioxygenase or phosphopantothenoylcysteine decarboxylase. Family-level knowledge that plant gamma-tocopherol-methyltransferase-like enzymes are SAM-dependent methyltransferases favors C; the sequence does not suggest the specific tRNA substrate and RNA-methyltransferase class required by D.",
    "missing_item_specific_fact": "",
    "reason": "Transferable methyltransferase-family and sequence-pattern knowledge gives a meaningful basis for selecting the broad SAM-dependent methyltransferase option over these alternatives. Exact substrate specificity would require further evidence, but is not needed to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is a more specific tRNA methyltransferase activity, not an equivalent alternative supported by the sequence-level family inference; C is the broad activity indicated."
  },
  "important_caveats": [
    "The experimental functional annotation is reviewer-only evidence and was not available as an input to the evaluated model.",
    "The sequence-based family inference supports the broad methyltransferase choice but does not independently establish the exact ajmaline substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0A075D654, Ajmaline N-methyltransferase, EC 2.1.1.393) explicitly annotates GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) via IEA:InterPro. The catalytic activity is experimentally verified (ECO:0000269, PubMed:27122470): ajmaline + SAM → 4-methylajmaline + SAH + H⁺. The protein is a SAM-dependent N-methyltransferase, fully consistent with option C. The GO assignment itself is computational (IEA:InterPro), but the underlying SAM-dependent methyltransferase activity is experimentally confirmed.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several well-known, transferable motifs diagnostic of Class I SAM-dependent methyltransferases: (1) The 'ADWS' motif (~residues 225-228, 'ADWSRN') is a hallmark of the SAM-binding pocket in Class I methyltransferases, found across hundreds of characterized SAM-dependent methyltransferases. (2) The glycine-rich 'GCGIGGT' segment (~residues 73-79) resembles the glycine-rich loop used for SAM cofactor binding in the Rossmann-like methyltransferase fold. (3) The 'VLSIHC' region and overall secondary-structure propensity (alternating β-strand/α-helix segments) are consistent with the β-sheet core of the Class I methyltransferase fold. These features collectively indicate SAM-dependent methyltransferase activity. Against the alternatives: (A) 2-oxoglutarate-dependent dioxygenases require an HxD/E…H facial triad for Fe(II) coordination and a double-stranded β-helix fold; no such motifs are present. (B) Phosphopantothenoylcysteine decarboxylase is a flavin-dependent decarboxylase (EC 4.1.1.36) with FMN-binding motifs absent here. (D) TRM11 (tRNA guanine-18 2'-O-methyltransferase) belongs to a distinct methyltransferase subclass with specific tRNA-recognition elements and a different active-site architecture; the plant-alkaloid-biosynthesis context and the ADWS motif pattern here do not match TRM11 family signatures. Thus transferable knowledge of the ADWS SAM-binding motif and methyltransferase superfamily architecture meaningfully selects C over A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ADWS motif and glycine-rich SAM-binding region are widely recognized, transferable sequence features of SAM-dependent methyltransferases learned from many characterized enzymes. A knowledgeable model can use these to infer option C and exclude the non-methyltransferase options (A, B) and the specific tRNA methyltransferase option (D) based on the absence of TRM11-specific features and the presence of plant alkaloid-biosynthesis methyltransferase hallmarks.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The ADWS SAM-binding motif and overall Class I methyltransferase fold features clearly point to SAM-dependent methyltransferase activity (C). Option D (TRM11) is a specific tRNA-modifying methyltransferase with a different family signature not present here. Options A and B lack any relevant catalytic motifs. Only C is well-supported by the sequence features.


### Important caveats

- The GO:0008757 annotation in UniProt is assigned via IEA:InterPro (computational family inference), but the SAM-dependent methyltransferase activity is experimentally confirmed by PubMed:27122470.
- The protein is an N-methyltransferase (transfers methyl to nitrogen of ajmaline), which falls under the broad GO:0008757 umbrella; the more specific EC 2.1.1.393 is not among the options.
- The sequence is 291 aa from Rauvolfia serpentina; the plant origin and derivation from gamma-tocopherol C-methyltransferase family (per the 2016 paper title) are consistent with the SAM-dependent methyltransferase assignment but were not provided to the evaluated model.
- The reviewer-only evidence confirms the sequence matches the UniProt entry (SHA-256 match, 291 aa), but the model only sees the raw sequence and the four options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several well-known, transferable motifs diagnostic of Class I SAM-dependent methyltransferases: (1) The 'ADWS' motif (~residues 225-228, 'ADWSRN') is a hallmark of the SAM-binding pocket in Class I methyltransferases, found across hundreds of characterized SAM-dependent methyltransferases. (2) The glycine-rich 'GCGIGGT' segment (~residues 73-79) resembles the glycine-rich loop used for SAM cofactor binding in the Rossmann-like methyltransferase fold. (3) The 'VLSIHC' region and overall secondary-structure propensity (alternating β-strand/α-helix segments) are consistent with the β-sheet core of the Class I methyltransferase fold. These features collectively indicate SAM-dependent methyltransferase activity. Against the alternatives: (A) 2-oxoglutarate-dependent dioxygenases require an HxD/E…H facial triad for Fe(II) coordination and a double-stranded β-helix fold; no such motifs are present. (B) Phosphopantothenoylcysteine decarboxylase is a flavin-dependent decarboxylase (EC 4.1.1.36) with FMN-binding motifs absent here. (D) TRM11 (tRNA guanine-18 2'-O-methyltransferase) belongs to a distinct methyltransferase subclass with specific tRNA-recognition elements and a different active-site architecture; the plant-alkaloid-biosynthesis context and the ADWS motif pattern here do not match TRM11 family signatures. Thus transferable knowledge of the ADWS SAM-binding motif and methyltransferase superfamily architecture meaningfully selects C over A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ADWS motif and glycine-rich SAM-binding region are widely recognized, transferable sequence features of SAM-dependent methyltransferases learned from many characterized enzymes. A knowledgeable model can use these to infer option C and exclude the non-methyltransferase options (A, B) and the specific tRNA methyltransferase option (D) based on the absence of TRM11-specific features and the presence of plant alkaloid-biosynthesis methyltransferase hallmarks."
  },
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A075D654, Ajmaline N-methyltransferase, EC 2.1.1.393) explicitly annotates GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) via IEA:InterPro. The catalytic activity is experimentally verified (ECO:0000269, PubMed:27122470): ajmaline + SAM → 4-methylajmaline + SAH + H⁺. The protein is a SAM-dependent N-methyltransferase, fully consistent with option C. The GO assignment itself is computational (IEA:InterPro), but the underlying SAM-dependent methyltransferase activity is experimentally confirmed."
  },
  "important_caveats": [
    "The GO:0008757 annotation in UniProt is assigned via IEA:InterPro (computational family inference), but the SAM-dependent methyltransferase activity is experimentally confirmed by PubMed:27122470.",
    "The protein is an N-methyltransferase (transfers methyl to nitrogen of ajmaline), which falls under the broad GO:0008757 umbrella; the more specific EC 2.1.1.393 is not among the options.",
    "The sequence is 291 aa from Rauvolfia serpentina; the plant origin and derivation from gamma-tocopherol C-methyltransferase family (per the 2016 paper title) are consistent with the SAM-dependent methyltransferase assignment but were not provided to the evaluated model.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry (SHA-256 match, 291 aa), but the model only sees the raw sequence and the four options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ADWS SAM-binding motif and overall Class I methyltransferase fold features clearly point to SAM-dependent methyltransferase activity (C). Option D (TRM11) is a specific tRNA-modifying methyltransferase with a different family signature not present here. Options A and B lack any relevant catalytic motifs. Only C is well-supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A075D654, Ajmaline N-methyltransferase, EC 2.1.1.393) explicitly annotates GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) via IEA:InterPro. The catalytic activity is experimentally verified (ECO:0000269, PubMed:27122470): ajmaline + SAM → 4-methylajmaline + SAH + H⁺. The protein is a SAM-dependent N-methyltransferase, fully consistent with option C. The GO assignment itself is computational (IEA:InterPro), but the underlying SAM-dependent methyltransferase activity is experimentally confirmed.",
    "evidence_ids": ["C6", "C7", "C8", "H4", "H5", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several well-known, transferable motifs diagnostic of Class I SAM-dependent methyltransferases: (1) The 'ADWS' motif (~residues 225-228, 'ADWSRN') is a hallmark of the SAM-binding pocket in Class I methyltransferases, found across hundreds of characterized SAM-dependent methyltransferases. (2) The glycine-rich 'GCGIGGT' segment (~residues 73-79) resembles the glycine-rich loop used for SAM cofactor binding in the Rossmann-like methyltransferase fold. (3) The 'VLSIHC' region and overall secondary-structure propensity (alternating β-strand/α-helix segments) are consistent with the β-sheet core of the Class I methyltransferase fold. These features collectively indicate SAM-dependent methyltransferase activity. Against the alternatives: (A) 2-oxoglutarate-dependent dioxygenases require an HxD/E…H facial triad for Fe(II) coordination and a double-stranded β-helix fold; no such motifs are present. (B) Phosphopantothenoylcysteine decarboxylase is a flavin-dependent decarboxylase (EC 4.1.1.36) with FMN-binding motifs absent here. (D) TRM11 (tRNA guanine-18 2'-O-methyltransferase) belongs to a distinct methyltransferase subclass with specific tRNA-recognition elements and a different active-site architecture; the plant-alkaloid-biosynthesis context and the ADWS motif pattern here do not match TRM11 family signatures. Thus transferable knowledge of the ADWS SAM-binding motif and methyltransferase superfamily architecture meaningfully selects C over A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "The ADWS motif and glycine-rich SAM-binding region are widely recognized, transferable sequence features of SAM-dependent methyltransferases learned from many characterized enzymes. A knowledgeable model can use these to infer option C and exclude the non-methyltransferase options (A, B) and the specific tRNA methyltransferase option (D) based on the absence of TRM11-specific features and the presence of plant alkaloid-biosynthesis methyltransferase hallmarks."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ADWS SAM-binding motif and overall Class I methyltransferase fold features clearly point to SAM-dependent methyltransferase activity (C). Option D (TRM11) is a specific tRNA-modifying methyltransferase with a different family signature not present here. Options A and B lack any relevant catalytic motifs. Only C is well-supported by the sequence features."
  },
  "important_caveats": [
    "The GO:0008757 annotation in UniProt is assigned via IEA:InterPro (computational family inference), but the SAM-dependent methyltransferase activity is experimentally confirmed by PubMed:27122470.",
    "The protein is an N-methyltransferase (transfers methyl to nitrogen of ajmaline), which falls under the broad GO:0008757 umbrella; the more specific EC 2.1.1.393 is not among the options.",
    "The sequence is 291 aa from Rauvolfia serpentina; the plant origin and derivation from gamma-tocopherol C-methyltransferase family (per the 2016 paper title) are consistent with the SAM-dependent methyltransferase assignment but were not provided to the evaluated model.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry (SHA-256 match, 291 aa), but the model only sees the raw sequence and the four options."
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
  "benchmark_sequence_length": 291,
  "benchmark_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 291,
  "current_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A075D654",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "selected_historical_source_sequence_length": 291,
  "selected_historical_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "selected_historical_version": {
    "accession": "A0A075D654",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ANMT_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A075D654\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHH02777.1\",\"source\":\"EMBL\"}],\"value\":\"Gamma-tocopherol-like methyltransferase ANMT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.393\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Ajmaline N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"RsANMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"N-methyltransferase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:27122470). Catalyzes the indole N-methylation of ajmaline to produce 4-methylajmaline (PubMed:27122470). Also able, with a lower efficiency, to mediate the conversion of norajmaline to 4-methylnorajmaline (PubMed:27122470)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79632\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.393\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"name\":\"ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79631\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230509\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79628\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.393\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"name\":\"norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79627\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230510\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008757\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:S-adenosylmethionine-dependent methyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Cazares-Flores P.\",\"Levac D.\",\"De Luca V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27122470\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.13186\"}],\"citationType\":\"journal article\",\"firstPage\":\"335\",\"id\":\"27122470\",\"journal\":\"Plant J.\",\"lastPage\":\"342\",\"publicationDate\":\"2016\",\"title\":\"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.\",\"volume\":\"87\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   ANMT_RAUSE              Reviewed;         291 AA.\nAC   A0A075D654;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};\nDE            Short=RsANMT {ECO:0000303|PubMed:27122470};\nDE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};\nGN   Name=ANMT {ECO:0000303|PubMed:27122470};\nGN   Synonyms=Rs820 {ECO:0000312|EMBL:AHH02777.1};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRX   PubMed=27122470; DOI=10.1111/tpj.13186;\nRA   Cazares-Flores P., Levac D., De Luca V.;\nRT   \"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta\nRT   -methylajmaline biosynthesis belong to a gene family derived from gamma-\nRT   tocopherol C-methyltransferase.\";\nRL   Plant J. 87:335-342(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: N-methyltransferase involved in the biosynthesis of ajmaline-\nCC       type monoterpenoid indole alkaloids (MIAs) natural products, important\nCC       plant-derived pharmaceuticals used in the therapy of heart disorders\nCC       (PubMed:27122470). Catalyzes the indole N-methylation of ajmaline to\nCC       produce 4-methylajmaline (PubMed:27122470). Also able, with a lower\nCC       efficiency, to mediate the conversion of norajmaline to 4-\nCC       methylnorajmaline (PubMed:27122470). {ECO:0000269|PubMed:27122470}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79631,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58567,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509; EC=2.1.1.393;\nCC         Evidence={ECO:0000269|PubMed:27122470};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79632;\nCC         Evidence={ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline +\nCC         S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79627,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:77618, ChEBI:CHEBI:230510; EC=2.1.1.393;\nCC         Evidence={ECO:0000269|PubMed:27122470};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79628;\nCC         Evidence={ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008757; F:S-adenosylmethionine-dependent methyltransferase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004633\nname: phosphopantothenoylcysteine decarboxylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: N-[(R)-4-phosphonatopantothenoyl]-L-cysteinate + H+ = CO2 + pantetheine 4'-phosphate.\" [EC:4.1.1.36, RHEA:16793]\nsynonym: \"4-phosphopantothenoyl-L-cysteine decarboxylase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"4-phosphopantotheoylcysteine decarboxylase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"N-((R)-4'-phosphopantothenoyl)-L-cysteine carboxy-lyase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase (pantotheine-4'-phosphate-forming)\" RELATED [EC:4.1.1.36]\nsynonym: \"N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"PPC-decarboxylase activity\" RELATED [EC:4.1.1.36]\nxref: EC:4.1.1.36\nxref: KEGG_REACTION:R03269\nxref: MetaCyc:P-PANTOCYSDECARB-RXN\nxref: Reactome:R-HSA-196840 \"3xPPCDC:3FMN decarboxylates PPC\"\nxref: RHEA:16793\nis_a: GO:0016831 ! carboxy-lyase activity\nproperty_value: skos:exactMatch EC:4.1.1.36\nproperty_value: skos:exactMatch RHEA:16793\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004633",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 45927-45946",
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
  "excerpt": "[Term]\nid: GO:0008757\nname: S-adenosylmethionine-dependent methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group from S-adenosyl-L-methionine to a substrate.\" [GOC:mah]\nsynonym: \"S-adenosyl methionine-dependent methyltransferase activity\" EXACT []\nsynonym: \"SAM-dependent methyltransferase activity\" EXACT []\nis_a: GO:0008168 ! methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008757",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 87421-87429",
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
  "excerpt": "[Term]\nid: GO:0016706\nname: 2-oxoglutarate-dependent dioxygenase activity\nnamespace: molecular_function\nalt_id: GO:0010302\ndef: \"Catalysis of the reaction: A + 2-oxoglutarate + O2 = B + succinate + CO2. This is an oxidation-reduction (redox) reaction in which hydrogen or electrons are transferred from 2-oxoglutarate and one other donor, and one atom of oxygen is incorporated into each donor.\" [GOC:mah]\nsynonym: \"2-oxoglutarate dioxygenase activity\" EXACT []\nsynonym: \"oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor, and incorporation of one atom each of oxygen into both donors\" EXACT []\nxref: EC:1.14.11.-\nxref: Reactome:R-HSA-1234164 \"Cytosolic HIF1AN (FIH1) hydroxylates asparagine residues of Hypoxia-inducible Factor Alpha (HIF1A,HIF2A)\"\nxref: Reactome:R-HSA-6783455 \"TYW5 hydroxylates yW-72 yielding OHyW-72 at nucleotide 37 of tRNA(Phe)\"\nis_a: GO:0016705 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen\nis_a: GO:0051213 ! dioxygenase activity\nproperty_value: skos:exactMatch EC:1.14.11.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016706",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129228-129242",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
