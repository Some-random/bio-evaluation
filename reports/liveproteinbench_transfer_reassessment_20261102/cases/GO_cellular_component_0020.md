# GO_cellular_component_0020

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0020.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | uncertain | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MALVRFATIITVLCHLAIQDGAAKSFPHGEKAPFPLTLIHINDLHARFDETNQKSSTCTNSKECIAGIARVYHTIKQLKSEYKTKNPLYLNAGDNFQGTLWYNLLRWNVTAYFIKELPPDAMTLGNHEFDHSPKGLAPYLAELEKMKIPTVVANLEKNGEPALKDSKIARSIVLKVGNRKVGVIGALYDKTHLVAQTGMVTLTNSIEAVRKEAQELKKKNVNIIVVLSHCGLDGDKQLAEEAGDLIDVIVGAHSHSLLLNKDAKVPYDTKYDTIEGDYPLVVKKSNNHTVLITQARSFGKYVGRLTVNFDCEGEVQSWEGYPIYMNNSVKQDEEVLRELEPWRAEVKRLGTQVIGTTEVFLDRESCRWCECTLGDLIADAYADQYTNSTVQPVAFVQAGNFRNPIEKGDITNGLAIEAAPYGSSVDMIKLSGADLWSAIDHSFTLDDEFRYNTAQVSGMAVVADLSKKPYERVQSIDIVGANGAKTALKKDQIYYVVVPSYLADGKDGFAMLKKGTNRVTGPLDSDVLIEYVRKRQTIAKTMFQEKRVVIENHTNGTCSWDLDSQRYKPK

[Multiple Choices]
A. microvillus membrane
B. centrosome
C. plasma membrane
D. caveola
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched record assigns plasma membrane (GO:0005886), but the assignment is IBA, a phylogenetic inference rather than direct experimental localization. The same record reports experimental evidence for secretion, so the annotation supports the key without establishing plasma membrane as the protein’s exclusive or primary location.

Citations as saved: [C7](#evidence-c7), [H6](#evidence-h6), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal and apyrase-like sequence are consistent with an extracellular-pathway enzyme, but do not distinguish a soluble secreted protein from one localized at the plasma membrane. They provide no specific basis for microvillus membrane or caveola, and do not establish the broad plasma-membrane choice.


**Missing item-specific fact**

> Whether this exact protein is plasma-membrane-associated in addition to being secreted; the sequence alone does not establish that localization.


**Reason**

> Transferable family and sequence features support an extracellular or secretory-pathway destination, not a unique choice among the offered cellular locations. Choosing C depends on the exact protein’s plasma-membrane annotation or localization evidence, which was not included in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second offered option is comparably supported by the sequence. However, the experimentally supported secreted/extracellular location is not among the choices, and plasma-membrane association is not established by the sequence.


### Important caveats

- The supporting plasma-membrane annotation is computationally transferred (IBA); the supplied record also reports experimental secretion.
- The reviewer evidence is sequence-matched but was not available as input to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal and apyrase-like sequence are consistent with an extracellular-pathway enzyme, but do not distinguish a soluble secreted protein from one localized at the plasma membrane. They provide no specific basis for microvillus membrane or caveola, and do not establish the broad plasma-membrane choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this exact protein is plasma-membrane-associated in addition to being secreted; the sequence alone does not establish that localization.",
    "reason": "Transferable family and sequence features support an extracellular or secretory-pathway destination, not a unique choice among the offered cellular locations. Choosing C depends on the exact protein’s plasma-membrane annotation or localization evidence, which was not included in the original input."
  },
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H6",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record assigns plasma membrane (GO:0005886), but the assignment is IBA, a phylogenetic inference rather than direct experimental localization. The same record reports experimental evidence for secretion, so the annotation supports the key without establishing plasma membrane as the protein’s exclusive or primary location."
  },
  "important_caveats": [
    "The supporting plasma-membrane annotation is computationally transferred (IBA); the supplied record also reports experimental secretion.",
    "The reviewer evidence is sequence-matched but was not available as input to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option is comparably supported by the sequence. However, the experimentally supported secreted/extracellular location is not among the choices, and plasma-membrane association is not established by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record assigns plasma membrane (GO:0005886), but the assignment is IBA, a phylogenetic inference rather than direct experimental localization. The same record reports experimental evidence for secretion, so the annotation supports the key without establishing plasma membrane as the protein’s exclusive or primary location.",
    "evidence_ids": ["C7", "H6", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal and apyrase-like sequence are consistent with an extracellular-pathway enzyme, but do not distinguish a soluble secreted protein from one localized at the plasma membrane. They provide no specific basis for microvillus membrane or caveola, and do not establish the broad plasma-membrane choice.",
    "missing_item_specific_fact": "Whether this exact protein is plasma-membrane-associated in addition to being secreted; the sequence alone does not establish that localization.",
    "reason": "Transferable family and sequence features support an extracellular or secretory-pathway destination, not a unique choice among the offered cellular locations. Choosing C depends on the exact protein’s plasma-membrane annotation or localization evidence, which was not included in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option is comparably supported by the sequence. However, the experimentally supported secreted/extracellular location is not among the choices, and plasma-membrane association is not established by the sequence."
  },
  "important_caveats": [
    "The supporting plasma-membrane annotation is computationally transferred (IBA); the supplied record also reports experimental secretion.",
    "The reviewer evidence is sequence-matched but was not available as input to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: uncertain

> The author's answer 'plasma membrane' (GO:0005886) is present in the UniProt entry but only via IBA:GO_Central evidence, which is a computational inference propagated from biological-aspect annotations, not experimental data. The primary experimental annotation (ECO:0000269, direct assay, PubMed:39294191) records the subcellular location as 'Secreted' (SL-0243), and the GO cross-reference with IDA evidence is GO:0005576 'extracellular region.' The protein name includes 'ecto' (5' nucleotidase ecto), which is suggestive of membrane association but is a naming convention rather than a subcellular-location annotation. The experimental evidence points to a secreted/extracellular protein rather than a membrane-integral one, while the plasma membrane annotation is purely computational. The evidence is therefore mixed: the answer is not experimentally confirmed, nor is it clearly contradicted (secreted ecto-enzymes can transiently associate with the cell surface).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MALVRFATIITVLCHLAIQ' is a classic hydrophobic signal peptide (~20 residues), confirming entry into the secretory pathway. This immediately eliminates B (centrosome), which is a cytoplasmic/nuclear structure with no connection to the secretory pathway. The protein belongs to the ecto-nucleotidase/apyrase family (EC 3.6.1.5), whose defining characteristic is acting on extracellular substrates at the cell surface. Among the remaining membrane-associated choices: D (caveola) is a specialized lipid-raft microdomain primarily characterized in mammalian cells (adipocytes, endothelium) and requires caveolin proteins and specific lipid modifications; insects lack well-characterized caveolae, making this a weak candidate for an insect protein. A (microvillus membrane) is a highly specialized epithelial subdomain requiring specific targeting machinery and is not a default destination for secreted ecto-enzymes. C (plasma membrane) is the general cell-surface compartment where a secreted ecto-enzyme would reside, representing the most parsimonious localization for a signal-peptide-bearing, secretory-pathway ecto-nucleotidase without specialized targeting signals for caveolae or microvilli.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the signal peptide to eliminate the centrosome, recognize the ecto-nucleotidase family to infer cell-surface localization, and apply general biological knowledge (caveolae are primarily mammalian; microvillus targeting requires specific signals) to prefer the general plasma membrane over the specialized subdomain options. This is a legitimate chain of family-level and mechanism-level inference from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, plasma membrane (C) is clearly the best-supported answer. Centrosome (B) is eliminated by the signal peptide. Caveola (D) is a mammalian-specific structure unlikely for an insect protein. Microvillus membrane (A) is a highly specialized subdomain without supporting targeting features in the sequence. No two options are equally defensible.


### Important caveats

- The plasma membrane GO annotation in UniProt is IBA:GO_Central (computational inference), not experimental. The experimental evidence (direct assay) records 'Secreted' and GO:0005576 'extracellular region.'
- The 'ecto' in the protein name is a nomenclature convention, not an independent subcellular-location annotation, though it is strongly suggestive of cell-surface association.
- The benchmark author likely used the UniProt GO annotation (including IBA) as ground truth, which is a common practice in GO-prediction benchmarks.
- The sequence is from Anopheles gambiae (insect); caveolae are not well-characterized in insects, strengthening the elimination of option D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MALVRFATIITVLCHLAIQ' is a classic hydrophobic signal peptide (~20 residues), confirming entry into the secretory pathway. This immediately eliminates B (centrosome), which is a cytoplasmic/nuclear structure with no connection to the secretory pathway. The protein belongs to the ecto-nucleotidase/apyrase family (EC 3.6.1.5), whose defining characteristic is acting on extracellular substrates at the cell surface. Among the remaining membrane-associated choices: D (caveola) is a specialized lipid-raft microdomain primarily characterized in mammalian cells (adipocytes, endothelium) and requires caveolin proteins and specific lipid modifications; insects lack well-characterized caveolae, making this a weak candidate for an insect protein. A (microvillus membrane) is a highly specialized epithelial subdomain requiring specific targeting machinery and is not a default destination for secreted ecto-enzymes. C (plasma membrane) is the general cell-surface compartment where a secreted ecto-enzyme would reside, representing the most parsimonious localization for a signal-peptide-bearing, secretory-pathway ecto-nucleotidase without specialized targeting signals for caveolae or microvilli.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide to eliminate the centrosome, recognize the ecto-nucleotidase family to infer cell-surface localization, and apply general biological knowledge (caveolae are primarily mammalian; microvillus targeting requires specific signals) to prefer the general plasma membrane over the specialized subdomain options. This is a legitimate chain of family-level and mechanism-level inference from other proteins."
  },
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "cannot_determine",
    "reason": "The author's answer 'plasma membrane' (GO:0005886) is present in the UniProt entry but only via IBA:GO_Central evidence, which is a computational inference propagated from biological-aspect annotations, not experimental data. The primary experimental annotation (ECO:0000269, direct assay, PubMed:39294191) records the subcellular location as 'Secreted' (SL-0243), and the GO cross-reference with IDA evidence is GO:0005576 'extracellular region.' The protein name includes 'ecto' (5' nucleotidase ecto), which is suggestive of membrane association but is a naming convention rather than a subcellular-location annotation. The experimental evidence points to a secreted/extracellular protein rather than a membrane-integral one, while the plasma membrane annotation is purely computational. The evidence is therefore mixed: the answer is not experimentally confirmed, nor is it clearly contradicted (secreted ecto-enzymes can transiently associate with the cell surface)."
  },
  "important_caveats": [
    "The plasma membrane GO annotation in UniProt is IBA:GO_Central (computational inference), not experimental. The experimental evidence (direct assay) records 'Secreted' and GO:0005576 'extracellular region.'",
    "The 'ecto' in the protein name is a nomenclature convention, not an independent subcellular-location annotation, though it is strongly suggestive of cell-surface association.",
    "The benchmark author likely used the UniProt GO annotation (including IBA) as ground truth, which is a common practice in GO-prediction benchmarks.",
    "The sequence is from Anopheles gambiae (insect); caveolae are not well-characterized in insects, strengthening the elimination of option D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, plasma membrane (C) is clearly the best-supported answer. Centrosome (B) is eliminated by the signal peptide. Caveola (D) is a mammalian-specific structure unlikely for an insect protein. Microvillus membrane (A) is a highly specialized subdomain without supporting targeting features in the sequence. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The author's answer 'plasma membrane' (GO:0005886) is present in the UniProt entry but only via IBA:GO_Central evidence, which is a computational inference propagated from biological-aspect annotations, not experimental data. The primary experimental annotation (ECO:0000269, direct assay, PubMed:39294191) records the subcellular location as 'Secreted' (SL-0243), and the GO cross-reference with IDA evidence is GO:0005576 'extracellular region.' The protein name includes 'ecto' (5' nucleotidase ecto), which is suggestive of membrane association but is a naming convention rather than a subcellular-location annotation. The experimental evidence points to a secreted/extracellular protein rather than a membrane-integral one, while the plasma membrane annotation is purely computational. The evidence is therefore mixed: the answer is not experimentally confirmed, nor is it clearly contradicted (secreted ecto-enzymes can transiently associate with the cell surface).",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MALVRFATIITVLCHLAIQ' is a classic hydrophobic signal peptide (~20 residues), confirming entry into the secretory pathway. This immediately eliminates B (centrosome), which is a cytoplasmic/nuclear structure with no connection to the secretory pathway. The protein belongs to the ecto-nucleotidase/apyrase family (EC 3.6.1.5), whose defining characteristic is acting on extracellular substrates at the cell surface. Among the remaining membrane-associated choices: D (caveola) is a specialized lipid-raft microdomain primarily characterized in mammalian cells (adipocytes, endothelium) and requires caveolin proteins and specific lipid modifications; insects lack well-characterized caveolae, making this a weak candidate for an insect protein. A (microvillus membrane) is a highly specialized epithelial subdomain requiring specific targeting machinery and is not a default destination for secreted ecto-enzymes. C (plasma membrane) is the general cell-surface compartment where a secreted ecto-enzyme would reside, representing the most parsimonious localization for a signal-peptide-bearing, secretory-pathway ecto-nucleotidase without specialized targeting signals for caveolae or microvilli.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide to eliminate the centrosome, recognize the ecto-nucleotidase family to infer cell-surface localization, and apply general biological knowledge (caveolae are primarily mammalian; microvillus targeting requires specific signals) to prefer the general plasma membrane over the specialized subdomain options. This is a legitimate chain of family-level and mechanism-level inference from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, plasma membrane (C) is clearly the best-supported answer. Centrosome (B) is eliminated by the signal peptide. Caveola (D) is a mammalian-specific structure unlikely for an insect protein. Microvillus membrane (A) is a highly specialized subdomain without supporting targeting features in the sequence. No two options are equally defensible."
  },
  "important_caveats": [
    "The plasma membrane GO annotation in UniProt is IBA:GO_Central (computational inference), not experimental. The experimental evidence (direct assay) records 'Secreted' and GO:0005576 'extracellular region.'",
    "The 'ecto' in the protein name is a nomenclature convention, not an independent subcellular-location annotation, though it is strongly suggestive of cell-surface association.",
    "The benchmark author likely used the UniProt GO annotation (including IBA) as ground truth, which is a common practice in GO-prediction benchmarks.",
    "The sequence is from Anopheles gambiae (insect); caveolae are not well-characterized in insects, strengthening the elimination of option D."
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
  "benchmark_sequence_length": 570,
  "benchmark_sequence_sha256": "3683149afc9d326cb4fb66628aaf088737022753f738d7c8dc443028715694e1",
  "current_entry_audit": {
    "entryVersion": 122,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 570,
  "current_source_sequence_sha256": "3683149afc9d326cb4fb66628aaf088737022753f738d7c8dc443028715694e1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 120,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5TVM9",
  "selected_historical_entry_version": 120,
  "selected_historical_record_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "selected_historical_source_sequence_length": 570,
  "selected_historical_source_sequence_sha256": "3683149afc9d326cb4fb66628aaf088737022753f738d7c8dc443028715694e1",
  "selected_historical_version": {
    "accession": "Q5TVM9",
    "database": "Swiss-Prot",
    "entryVersion": 120,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "APY_ANOGA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5TVM9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":122,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"African malaria mosquito\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000007062\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Anophelinae\",\"Anopheles\"],\"scientificName\":\"Anopheles gambiae\",\"taxonId\":7165}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"5' nucleotidase ecto\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"Ag5'NTE\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10801886\",\"source\":\"PubMed\"}],\"value\":\"Apyrase-like 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10801886\",\"source\":\"PubMed\"}],\"value\":\"AgApyL1\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"3.6.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"Apyrase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"AgApy\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"17913537\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Lombardo F.\",\"Di Cristina M.\",\"Spanos L.\",\"Louis C.\",\"Coluzzi M.\",\"Arca B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10801886\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m909547199\"}],\"citationType\":\"journal article\",\"firstPage\":\"23861\",\"id\":\"10801886\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"23868\",\"publicationDate\":\"2000\",\"title\":\"Promoter sequences of the putative Anopheles gambiae apyrase confer salivary gland expression in Drosophila melanogaster.\",\"volume\":\"275\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB40347.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB40347.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"Gasua\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB40347.1\",\"source\":\"EMBL\"}],\"type\":\"TISSUE\",\"value\":\"Thorax\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"DEVELOPMENTAL STAGE\",\"INDUCTION BY BLOOD FEEDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Pala Z.R.\",\"Alves E Silva T.L.\",\"Minai M.\",\"Crews B.\",\"Patino-Martinez E.\",\"Carmona-Rivera C.\",\"Valenzuela Leon P.C.\",\"Martin-Martin I.\",\"Flores-Garcia Y.\",\"Cachau R.E.\",\"Muslinkina L.\",\"Gittis A.G.\",\"Srivastava N.\",\"Garboczi D.N.\",\"Alves D.A.\",\"Kaplan M.J.\",\"Fischer E.\",\"Calvo E.\",\"Vega-Rodriguez J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39294191\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-52502-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"8194\",\"id\":\"39294191\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"8194\",\"publicationDate\":\"2024\",\"title\":\"Mosquito salivary apyrase regulates blood meal hemostasis and facilitates malaria parasite transmission.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"FUNCTION\",\"FUNCTION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"INTERACTION WITH HUMAN PLAT\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H1",
  "excerpt": "ID   APY_ANOGA               Reviewed;         570 AA.\nAC   Q5TVM9; Q9UB34;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 120.\nDE   RecName: Full=Apyrase {ECO:0000303|PubMed:39294191};\nDE            Short=AgApy {ECO:0000303|PubMed:39294191};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:39294191};\nDE   AltName: Full=5' nucleotidase ecto {ECO:0000303|PubMed:39294191};\nDE            Short=Ag5'NTE {ECO:0000303|PubMed:39294191};\nDE   AltName: Full=Apyrase-like 1 {ECO:0000303|PubMed:10801886};\nDE            Short=AgApyL1 {ECO:0000303|PubMed:10801886};\nDE   Flags: Precursor;\nGN   ORFNames=AgaP_AGAP011026 {ECO:0000312|EMBL:EAA05427.2};\nOS   Anopheles gambiae (African malaria mosquito).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Anophelinae; Anopheles.\nOX   NCBI_TaxID=7165 {ECO:0000312|Proteomes:UP000007062};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB40347.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], DEVELOPMENTAL STAGE, AND INDUCTION BY BLOOD\nRP   FEEDING.\nRC   STRAIN=Gasua {ECO:0000312|EMBL:CAB40347.1};\nRC   TISSUE=Thorax {ECO:0000312|EMBL:CAB40347.1};\nRX   PubMed=10801886; DOI=10.1074/jbc.m909547199;\nRA   Lombardo F., Di Cristina M., Spanos L., Louis C., Coluzzi M., Arca B.;\nRT   \"Promoter sequences of the putative Anopheles gambiae apyrase confer\nRT   salivary gland expression in Drosophila melanogaster.\";\nRL   J. Biol. Chem. 275:23861-23868(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   IDENTIFICATION BY MASS SPECTROMETRY, FUNCTION, FUNCTION (MICROBIAL\nRP   INFECTION), CATALYTIC ACTIVITY, COFACTOR, INTERACTION WITH HUMAN PLAT,\nRP   SUBCELLULAR LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=39294191; DOI=10.1038/s41467-024-52502-3;\nRA   Pala Z.R., Alves E Silva T.L., Minai M., Crews B., Patino-Martinez E.,\nRA   Carmona-Rivera C., Valenzuela Leon P.C., Martin-Martin I.,\nRA   Flores-Garcia Y., Cachau R.E., Muslinkina L., Gittis A.G., Srivastava N.,\nRA   Garboczi D.N., Alves D.A., Kaplan M.J., Fischer E., Calvo E.,\nRA   Vega-Rodriguez J.;\nRT   \"Mosquito salivary apyrase regulates blood meal hemostasis and facilitates\nRT   malaria parasite transmission.\";\nRL   Nat. Commun. 15:8194-8194(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:39294191}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005615; C:extracellular space; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-154",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 155-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005813\nname: centrosome\nnamespace: cellular_component\ndef: \"A structure comprised of a core structure (in most organisms, a pair of centrioles) and peripheral material from which a microtubule-based structure, such as a spindle apparatus, is organized. Centrosomes occur close to the nucleus during interphase in many eukaryotic cells, though in animal cells it changes continually during the cell-division cycle.\" [GOC:mah, ISBN:0198547684]\nsubset: goslim_pir\nxref: Wikipedia:Centrosome\nis_a: GO:0005815 ! microtubule organizing center\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005813",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59790-59798",
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
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0005901\nname: caveola\nnamespace: cellular_component\nalt_id: GO:0016599\ndef: \"A membrane raft that forms small pit, depression, or invagination that communicates with the outside of a cell and extends inward, indenting the cytoplasm and the cell membrane. Examples include flask-shaped invaginations of the plasma membrane in adipocytes associated with caveolin proteins, and minute pits or incuppings of the cell membrane formed during pinocytosis. Caveolae may be pinched off to form free vesicles within the cytoplasm.\" [GOC:mah, ISBN:0721662544, PMID:16645198]\nsynonym: \"caveolae\" EXACT []\nsynonym: \"caveolar membrane\" RELATED []\nxref: Wikipedia:Caveolae\nis_a: GO:0044853 ! plasma membrane raft\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005901",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60572-60582",
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
  "excerpt": "[Term]\nid: GO:0031528\nname: microvillus membrane\nnamespace: cellular_component\ndef: \"The portion of the plasma membrane surrounding a microvillus.\" [GOC:mah]\nis_a: GO:0031253 ! cell projection membrane\nrelationship: part_of GO:0005902 ! microvillus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031528",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 177423-177430",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
