# GO_molecular_function_0109

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0109.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — delta(3)-delta(2)-enoyl-CoA isomerase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. histone deacetylase binding
B. methyltransferase activity
C. peptide binding
D. delta(3)-delta(2)-enoyl-CoA isomerase activity
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

> The sequence-matched historical UniProt entry assigns the exact GO activity in D, but as an IEA computational annotation, not direct experimental confirmation of that precise activity. The cited experimental function is a related dienoyl-CoA isomerase reaction, so the evidence supports D while leaving some substrate-specificity nuance.

Citations as saved: [H5](#evidence-h5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A sequence-profile or homology-level recognition of the compact enzyme as belonging to the CoA-dependent enoyl/dienoyl-CoA isomerase family would favor D: related enzymes catalyze double-bond rearrangements in fatty-acid metabolism. That family-level inference meaningfully separates D from methyltransferase activity and the two binding options, without requiring knowledge of this exact protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence permits a transferable enzyme-family inference toward CoA isomerization. It may not establish the exact substrate range or the precise GO term experimentally, but the alternatives do not require that finer distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered choice in the relevant metabolic-enzyme family; the annotation's distinction between enoyl-CoA and dienoyl-CoA isomerization is a caveat, not support for another listed option.


### Important caveats

- The exact D GO assignment is computational (IEA); the cited experimental evidence describes a related dienoyl-CoA isomerase activity.
- The historical source sequence matches the input, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A sequence-profile or homology-level recognition of the compact enzyme as belonging to the CoA-dependent enoyl/dienoyl-CoA isomerase family would favor D: related enzymes catalyze double-bond rearrangements in fatty-acid metabolism. That family-level inference meaningfully separates D from methyltransferase activity and the two binding options, without requiring knowledge of this exact protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence permits a transferable enzyme-family inference toward CoA isomerization. It may not establish the exact substrate range or the precise GO term experimentally, but the alternatives do not require that finer distinction."
  },
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry assigns the exact GO activity in D, but as an IEA computational annotation, not direct experimental confirmation of that precise activity. The cited experimental function is a related dienoyl-CoA isomerase reaction, so the evidence supports D while leaving some substrate-specificity nuance."
  },
  "important_caveats": [
    "The exact D GO assignment is computational (IEA); the cited experimental evidence describes a related dienoyl-CoA isomerase activity.",
    "The historical source sequence matches the input, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice in the relevant metabolic-enzyme family; the annotation's distinction between enoyl-CoA and dienoyl-CoA isomerization is a caveat, not support for another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry assigns the exact GO activity in D, but as an IEA computational annotation, not direct experimental confirmation of that precise activity. The cited experimental function is a related dienoyl-CoA isomerase reaction, so the evidence supports D while leaving some substrate-specificity nuance.",
    "evidence_ids": ["H5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A sequence-profile or homology-level recognition of the compact enzyme as belonging to the CoA-dependent enoyl/dienoyl-CoA isomerase family would favor D: related enzymes catalyze double-bond rearrangements in fatty-acid metabolism. That family-level inference meaningfully separates D from methyltransferase activity and the two binding options, without requiring knowledge of this exact protein's record.",
    "missing_item_specific_fact": "",
    "reason": "The sequence permits a transferable enzyme-family inference toward CoA isomerization. It may not establish the exact substrate range or the precise GO term experimentally, but the alternatives do not require that finer distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice in the relevant metabolic-enzyme family; the annotation's distinction between enoyl-CoA and dienoyl-CoA isomerization is a caveat, not support for another listed option."
  },
  "important_caveats": [
    "The exact D GO assignment is computational (IEA); the cited experimental evidence describes a related dienoyl-CoA isomerase activity.",
    "The historical source sequence matches the input, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4NCP4 carries GO:0004165 (delta(3)-delta(2)-enoyl-CoA isomerase activity) as an annotation with evidence code IEA:UniProtKB-ARBA (C7/H5). The protein is also annotated with the closely related GO:0051750 (delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity, ISS:UniProtKB, C8/H6), and its experimentally validated activity (PubMed:36774535, ECO:0000269) is dienoyl-CoA isomerase (EC 5.3.3.21). The expected answer D corresponds to GO:0004165, which is present in the annotation, though only by automatic rule-based assignment. The ARBA annotation places this protein in the enoyl-CoA isomerase superfamily (referencing human ECI1 Q08558). The annotation is database-supported, though the experimentally characterized activity is the more specific dienoyl variant not offered as a choice.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [C5](#evidence-c5), [C4](#evidence-c4), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use several transferable features to favor D over A, B, and C: (1) The protein is small (~280 aa), consistent with the enoyl-CoA isomerase/dienoyl-CoA isomerase superfamily (e.g., human ECI1 is ~280 aa). (2) The sequence contains extended hydrophobic stretches (e.g., 'VVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGG') characteristic of the hydrophobic CoA-binding active site in this family. (3) The C-terminus ends in 'HKL', resembling a peroxisomal targeting signal PTS1 (SKL-like tripeptide), consistent with peroxisomal fatty acid oxidation enzymes in the ECI/dienoyl-CoA isomerase family. (4) There are no recognizable SAM-binding motifs (e.g., VIGXG, DPPX) to support methyltransferase (B). (5) There are no protein-protein interaction domains (e.g., HDAC-interaction motifs, SH3, PDZ) to support histone deacetylase binding (A). (6) There are no peptide-binding groove features (MHC-like folds, chaperone motifs) to support peptide binding (C). The combination of small size, hydrophobic active-site region, PTS1-like C-terminus, and absence of motifs for the other three functions provides a credible family-level inference pointing to an enoyl/dienoyl-CoA isomerase, which among the offered choices is D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on recognizing family-level sequence features (small size, hydrophobic CoA-binding region, PTS1-like signal) shared with known ECI/dienoyl-CoA isomerase family members, and on the absence of motifs required for the other three options. This is transferable knowledge from the ECI/dienoyl-CoA isomerase superfamily and general protein-structure-function relationships, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only D falls within the enoyl/dienoyl-CoA isomerase superfamily. The experimentally validated activity (GO:0051750, dienoyl-CoA isomerase) is not offered as a choice, so no ambiguity arises between D and another option. A, B, and C lack any supporting sequence features.


### Important caveats

- The expected answer GO:0004165 is annotated only by IEA:UniProtKB-ARBA (automatic rule-based assignment), not by direct experimental evidence for this protein.
- The experimentally validated activity (PubMed:36774535) is EC 5.3.3.21 / GO:0051750 (dienoyl-CoA isomerase), a closely related but distinct activity from EC 5.3.3.8 / GO:0004165 (enoyl-CoA isomerase). The distinction between these two isomerase activities is subtle and not resolvable from sequence alone.
- The ARBA annotation references human ECI1 (Q08558) as the similarity source, indicating the protein is recognized as a family member rather than having independently demonstrated enoyl-CoA isomerase activity.
- The PTS1-like C-terminal signal ('HKL') is suggestive but not definitively confirmed as a peroxisomal targeting signal without experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use several transferable features to favor D over A, B, and C: (1) The protein is small (~280 aa), consistent with the enoyl-CoA isomerase/dienoyl-CoA isomerase superfamily (e.g., human ECI1 is ~280 aa). (2) The sequence contains extended hydrophobic stretches (e.g., 'VVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGG') characteristic of the hydrophobic CoA-binding active site in this family. (3) The C-terminus ends in 'HKL', resembling a peroxisomal targeting signal PTS1 (SKL-like tripeptide), consistent with peroxisomal fatty acid oxidation enzymes in the ECI/dienoyl-CoA isomerase family. (4) There are no recognizable SAM-binding motifs (e.g., VIGXG, DPPX) to support methyltransferase (B). (5) There are no protein-protein interaction domains (e.g., HDAC-interaction motifs, SH3, PDZ) to support histone deacetylase binding (A). (6) There are no peptide-binding groove features (MHC-like folds, chaperone motifs) to support peptide binding (C). The combination of small size, hydrophobic active-site region, PTS1-like C-terminus, and absence of motifs for the other three functions provides a credible family-level inference pointing to an enoyl/dienoyl-CoA isomerase, which among the offered choices is D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on recognizing family-level sequence features (small size, hydrophobic CoA-binding region, PTS1-like signal) shared with known ECI/dienoyl-CoA isomerase family members, and on the absence of motifs required for the other three options. This is transferable knowledge from the ECI/dienoyl-CoA isomerase superfamily and general protein-structure-function relationships, not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "C5",
      "C4",
      "H5",
      "H6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 carries GO:0004165 (delta(3)-delta(2)-enoyl-CoA isomerase activity) as an annotation with evidence code IEA:UniProtKB-ARBA (C7/H5). The protein is also annotated with the closely related GO:0051750 (delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity, ISS:UniProtKB, C8/H6), and its experimentally validated activity (PubMed:36774535, ECO:0000269) is dienoyl-CoA isomerase (EC 5.3.3.21). The expected answer D corresponds to GO:0004165, which is present in the annotation, though only by automatic rule-based assignment. The ARBA annotation places this protein in the enoyl-CoA isomerase superfamily (referencing human ECI1 Q08558). The annotation is database-supported, though the experimentally characterized activity is the more specific dienoyl variant not offered as a choice."
  },
  "important_caveats": [
    "The expected answer GO:0004165 is annotated only by IEA:UniProtKB-ARBA (automatic rule-based assignment), not by direct experimental evidence for this protein.",
    "The experimentally validated activity (PubMed:36774535) is EC 5.3.3.21 / GO:0051750 (dienoyl-CoA isomerase), a closely related but distinct activity from EC 5.3.3.8 / GO:0004165 (enoyl-CoA isomerase). The distinction between these two isomerase activities is subtle and not resolvable from sequence alone.",
    "The ARBA annotation references human ECI1 (Q08558) as the similarity source, indicating the protein is recognized as a family member rather than having independently demonstrated enoyl-CoA isomerase activity.",
    "The PTS1-like C-terminal signal ('HKL') is suggestive but not definitively confirmed as a peroxisomal targeting signal without experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D falls within the enoyl/dienoyl-CoA isomerase superfamily. The experimentally validated activity (GO:0051750, dienoyl-CoA isomerase) is not offered as a choice, so no ambiguity arises between D and another option. A, B, and C lack any supporting sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 carries GO:0004165 (delta(3)-delta(2)-enoyl-CoA isomerase activity) as an annotation with evidence code IEA:UniProtKB-ARBA (C7/H5). The protein is also annotated with the closely related GO:0051750 (delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity, ISS:UniProtKB, C8/H6), and its experimentally validated activity (PubMed:36774535, ECO:0000269) is dienoyl-CoA isomerase (EC 5.3.3.21). The expected answer D corresponds to GO:0004165, which is present in the annotation, though only by automatic rule-based assignment. The ARBA annotation places this protein in the enoyl-CoA isomerase superfamily (referencing human ECI1 Q08558). The annotation is database-supported, though the experimentally characterized activity is the more specific dienoyl variant not offered as a choice.",
    "evidence_ids": ["C7", "C8", "C5", "C4", "H5", "H6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use several transferable features to favor D over A, B, and C: (1) The protein is small (~280 aa), consistent with the enoyl-CoA isomerase/dienoyl-CoA isomerase superfamily (e.g., human ECI1 is ~280 aa). (2) The sequence contains extended hydrophobic stretches (e.g., 'VVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGG') characteristic of the hydrophobic CoA-binding active site in this family. (3) The C-terminus ends in 'HKL', resembling a peroxisomal targeting signal PTS1 (SKL-like tripeptide), consistent with peroxisomal fatty acid oxidation enzymes in the ECI/dienoyl-CoA isomerase family. (4) There are no recognizable SAM-binding motifs (e.g., VIGXG, DPPX) to support methyltransferase (B). (5) There are no protein-protein interaction domains (e.g., HDAC-interaction motifs, SH3, PDZ) to support histone deacetylase binding (A). (6) There are no peptide-binding groove features (MHC-like folds, chaperone motifs) to support peptide binding (C). The combination of small size, hydrophobic active-site region, PTS1-like C-terminus, and absence of motifs for the other three functions provides a credible family-level inference pointing to an enoyl/dienoyl-CoA isomerase, which among the offered choices is D.",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on recognizing family-level sequence features (small size, hydrophobic CoA-binding region, PTS1-like signal) shared with known ECI/dienoyl-CoA isomerase family members, and on the absence of motifs required for the other three options. This is transferable knowledge from the ECI/dienoyl-CoA isomerase superfamily and general protein-structure-function relationships, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D falls within the enoyl/dienoyl-CoA isomerase superfamily. The experimentally validated activity (GO:0051750, dienoyl-CoA isomerase) is not offered as a choice, so no ambiguity arises between D and another option. A, B, and C lack any supporting sequence features."
  },
  "important_caveats": [
    "The expected answer GO:0004165 is annotated only by IEA:UniProtKB-ARBA (automatic rule-based assignment), not by direct experimental evidence for this protein.",
    "The experimentally validated activity (PubMed:36774535) is EC 5.3.3.21 / GO:0051750 (dienoyl-CoA isomerase), a closely related but distinct activity from EC 5.3.3.8 / GO:0004165 (enoyl-CoA isomerase). The distinction between these two isomerase activities is subtle and not resolvable from sequence alone.",
    "The ARBA annotation references human ECI1 (Q08558) as the similarity source, indicating the protein is recognized as a family member rather than having independently demonstrated enoyl-CoA isomerase activity.",
    "The PTS1-like C-terminal signal ('HKL') is suggestive but not definitively confirmed as a peroxisomal targeting signal without experimental validation."
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
  "benchmark_sequence_length": 280,
  "benchmark_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "current_entry_audit": {
    "entryVersion": 51,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 280,
  "current_source_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 50,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4NCP4",
  "selected_historical_entry_version": 50,
  "selected_historical_record_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "selected_historical_source_sequence_length": 280,
  "selected_historical_source_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "selected_historical_version": {
    "accession": "G4NCP4",
    "database": "Swiss-Prot",
    "entryVersion": 50,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "DCI1_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4NCP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":51,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"value\":\"Peroxisomal di-isomerase DCI1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"5.3.3.21\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"Peroxisomal di-isomerase that is involved in fatty acid metabolism enzyme by converting 3,5-dienoyl-CoAs to the corresponding 2,4-dienoyl-CoAs (PubMed:36774535). Involved in fatty acid beta-oxidation, which is important for lipid droplets degradation and infectious growth (PubMed:36774535)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:45241\"}}],\"reaction\":{\"ecNumber\":\"5.3.3.21\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"name\":\"a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:45240\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:85110\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:85111\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004165\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:delta(3)-delta(2)-enoyl-CoA isomerase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051750\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/21",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang T.\",\"Wang X.\",\"Li X.\",\"Li Y.N.\",\"Li Y.\",\"Wu S.\",\"Xu L.\",\"Zhou R.\",\"Yang J.\",\"Li G.\",\"Liu X.\",\"Zheng X.\",\"Zhang Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36774535\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.xplc.2023.100561\"}],\"citationType\":\"journal article\",\"firstPage\":\"100561\",\"id\":\"36774535\",\"journal\":\"Plant Commun.\",\"lastPage\":\"100561\",\"publicationDate\":\"2023\",\"title\":\"MoLrp1-mediated signaling induces nuclear accumulation of MoMsn2 to facilitate fatty acid oxidation for infectious growth of the rice blast fungus.\",\"volume\":\"4\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H1",
  "excerpt": "ID   DCI1_PYRO7              Reviewed;         280 AA.\nAC   G4NCP4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 50.\nDE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};\nDE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};\nDE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};\nGN   Name=DCI1 {ECO:0000303|PubMed:36774535}; ORFNames=MGG_00359;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, INDUCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=36774535; DOI=10.1016/j.xplc.2023.100561;\nRA   Zhang T., Wang X., Li X., Li Y.N., Li Y., Wu S., Xu L., Zhou R., Yang J.,\nRA   Li G., Liu X., Zheng X., Zhang Z., Zhang H.;\nRT   \"MoLrp1-mediated signaling induces nuclear accumulation of MoMsn2 to\nRT   facilitate fatty acid oxidation for infectious growth of the rice blast\nRT   fungus.\";\nRL   Plant Commun. 4:100561-100561(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Peroxisomal di-isomerase that is involved in fatty acid\nCC       metabolism enzyme by converting 3,5-dienoyl-CoAs to the corresponding\nCC       2,4-dienoyl-CoAs (PubMed:36774535). Involved in fatty acid beta-\nCC       oxidation, which is important for lipid droplets degradation and\nCC       infectious growth (PubMed:36774535). {ECO:0000269|PubMed:36774535}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA;\nCC         Xref=Rhea:RHEA:45240, ChEBI:CHEBI:85110, ChEBI:CHEBI:85111;\nCC         EC=5.3.3.21; Evidence={ECO:0000250|UniProtKB:Q08558};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45241;\nCC         Evidence={ECO:0000250|UniProtKB:Q08558};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004165; F:delta(3)-delta(2)-enoyl-CoA isomerase activity; IEA:UniProtKB-ARBA.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0051750; F:delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004165\nname: delta(3)-delta(2)-enoyl-CoA isomerase activity\nnamespace: molecular_function\nalt_id: GO:0008461\ndef: \"Catalysis of the reactions: a (3Z)-enoyl-CoA = a 4-saturated (2E)-enoyl-CoA or a (3E)-enoyl-CoA = a 4-saturated (2E)-enoyl-CoA.\" [RHEA:45900]\nsynonym: \"3,2-trans-enoyl-CoA isomerase activity\" RELATED [EC:5.3.3.8]\nsynonym: \"acetylene-allene isomerase activity\" RELATED [EC:5.3.3.8]\nsynonym: \"delta(3),delta(2)-enoyl-CoA isomerase activity\" RELATED [EC:5.3.3.8]\nsynonym: \"delta(3)-cis-delta(2)-trans-enoyl-CoA isomerase activity\" RELATED [EC:5.3.3.8]\nsynonym: \"delta3,delta2-enoyl-CoA isomerase activity\" RELATED [EC:5.3.3.8]\nsynonym: \"delta3-cis-delta2-trans-enoyl-CoA isomerase\" EXACT [EC:5.3.3.8]\nsynonym: \"delta3-delta2 enoyl-CoA isomerase activity\" EXACT []\nsynonym: \"dodecenoyl-CoA (3Z)-(2E)-isomerase activity\" NARROW [EC:5.3.3.8]\nsynonym: \"dodecenoyl-CoA D-isomerase activity\" NARROW []\nsynonym: \"dodecenoyl-CoA delta-isomerase activity\" NARROW []\nsynonym: \"dodecenoyl-CoA delta3-cis-delta2-trans-isomerase activity\" NARROW [EC:5.3.3.8]\nsynonym: \"dodecenoyl-CoA isomerase activity\" RELATED [EC:5.3.3.8]\nxref: EC:5.3.3.8\nxref: MetaCyc:ENOYL-COA-DELTA-ISOM-RXN\nxref: MetaCyc:RXN-7836\nxref: MetaCyc:RXN-7931\nxref: Reactome:R-HSA-109338 \"Isomerization of cis,cis-3,6-Dodecadienoyl-CoA to form trans,cis-Lauro-2,6-dienoyl-CoA\"\nxref: Reactome:R-HSA-6809808 \"ECI2 isomerizes 3Z-enoyl-CoA to 2E-enoyl-CoA\"\nxref: RHEA:23716\nxref: RHEA:29847\nxref: RHEA:45228\nxref: RHEA:45736\nxref: RHEA:45748\nxref: RHEA:45752\nxref: RHEA:45900\nxref: RHEA:46044\nxref: RHEA:46068\nxref: RHEA:47464\nxref: RHEA:47476\nxref: RHEA:49852\nxref: RHEA:49932\nxref: RHEA:77195\nxref: RHEA:83231\nxref: RHEA:84219\nxref: RHEA:84487\nxref: RHEA:84491\nxref: RHEA:84495\nxref: RHEA:84503\nxref: RHEA:84547\nxref: RHEA:84555\nxref: RHEA:84559\nxref: RHEA:84563\nxref: RHEA:84783\nxref: RHEA:84843\nxref: RHEA:84851\nxref: RHEA:84855\nis_a: GO:0016863 ! intramolecular oxidoreductase activity, transposing C=C bonds\nproperty_value: skos:exactMatch EC:5.3.3.8\nproperty_value: skos:exactMatch RHEA:45900\nproperty_value: skos:narrowMatch MetaCyc:ENOYL-COA-DELTA-ISOM-RXN\nproperty_value: skos:narrowMatch MetaCyc:RXN-7836\nproperty_value: skos:narrowMatch MetaCyc:RXN-7931\nproperty_value: skos:narrowMatch RHEA:23716\nproperty_value: skos:narrowMatch RHEA:29847\nproperty_value: skos:narrowMatch RHEA:45228\nproperty_value: skos:narrowMatch RHEA:45736\nproperty_value: skos:narrowMatch RHEA:45748\nproperty_value: skos:narrowMatch RHEA:45752\nproperty_value: skos:narrowMatch RHEA:46044\nproperty_value: skos:narrowMatch RHEA:46068\nproperty_value: skos:narrowMatch RHEA:47464\nproperty_value: skos:narrowMatch RHEA:47476\nproperty_value: skos:narrowMatch RHEA:49852\nproperty_value: skos:narrowMatch RHEA:49932\nproperty_value: skos:narrowMatch RHEA:77195\nproperty_value: skos:narrowMatch RHEA:83231\nproperty_value: skos:narrowMatch RHEA:84219\nproperty_value: skos:narrowMatch RHEA:84487\nproperty_value: skos:narrowMatch RHEA:84491\nproperty_value: skos:narrowMatch RHEA:84495\nproperty_value: skos:narrowMatch RHEA:84503\nproperty_value: skos:narrowMatch RHEA:84547\nproperty_value: skos:narrowMatch RHEA:84555\nproperty_value: skos:narrowMatch RHEA:84559\nproperty_value: skos:narrowMatch RHEA:84563\nproperty_value: skos:narrowMatch RHEA:84783\nproperty_value: skos:narrowMatch RHEA:84843\nproperty_value: skos:narrowMatch RHEA:84851\nproperty_value: skos:narrowMatch RHEA:84855\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004165",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 36710-36795",
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
  "excerpt": "[Term]\nid: GO:0008168\nname: methyltransferase activity\nnamespace: molecular_function\nalt_id: GO:0004480\ndef: \"Catalysis of the transfer of a methyl group to an acceptor molecule.\" [ISBN:0198506732]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"methylase\" BROAD []\nxref: EC:2.1.1.-\nxref: Reactome:R-HSA-212269 \"DNMT1,3A,3B:PRC2 methylates cytosine and histone H3\"\nxref: Reactome:R-HSA-379387 \"COMT transfers Met to DA to form 3MT\"\nxref: Reactome:R-HSA-379464 \"COMT transfers Met to DOPAC to form HVA\"\nxref: Reactome:R-HSA-5333608 \"GSSebGalNac is reduced and methylated to MeSebGalNac\"\nxref: Reactome:R-HSA-6800149 \"N6AMT1:TRMT112 transfers CH3 group from AdoMet to MMAIII\"\nxref: Reactome:R-HSA-71286 \"guanidinoacetate + S-adenosylmethionine => creatine + S-adenosylhomocysteine\"\nxref: Reactome:R-HSA-9710490 \"The GSDME gene promoter is hypermethylated\"\nis_a: GO:0016741 ! transferase activity, transferring one-carbon groups\nproperty_value: skos:exactMatch EC:2.1.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008168",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 80267-80287",
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
  "excerpt": "[Term]\nid: GO:0042277\nname: peptide binding\nnamespace: molecular_function\ndef: \"Binding to a peptide, an organic compound comprising two or more amino acids linked by peptide bonds.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_pir\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042277",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 235888-235896",
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
  "excerpt": "[Term]\nid: GO:0042826\nname: histone deacetylase binding\nnamespace: molecular_function\ndef: \"Binding to histone deacetylase.\" [GOC:jl]\nis_a: GO:0019899 ! enzyme binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042826",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 241324-241330",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
