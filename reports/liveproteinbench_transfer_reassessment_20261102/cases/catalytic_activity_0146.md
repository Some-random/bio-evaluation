# catalytic_activity_0146

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0146.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHALRSSVLALWLCLHVSVRAWMTYRSANGLDEYEPEDRIIFLGTKWCGNGNVAEGPEDLGPLKETDACCREHDMCPDLIAAGQSKHGLTNTASYTRLNCGCDEKFYNCLKNSAETGSGAVRFTYFTVLGTKCYRNEHPLICVKKGWFSCSKYELDKSQPKRYQWFDVSSNFAFPRMLT

[Multiple Choices]
A. inosine(in) = inosine(out)
B. L-ornithine = L-proline + NH4(+)
C. K(+)(in) = K(+)(out)
D. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
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

> The sequence-matched UniProt entry annotates this protein as phospholipase A2 and gives the reaction in option D. The reaction annotation is computationally supported by a PROSITE rule, rather than being direct experimental evidence in the supplied excerpts, but it is consistent with the sequence and enzyme family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted precursor, and the short, cysteine-rich mature region is characteristic of secreted venom phospholipase A2 proteins. Transferable knowledge of this enzyme family supports hydrolysis of a phospholipid acyl ester, matching option D; the other choices describe unrelated transformations or no net reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features provide a meaningful basis for distinguishing D without needing this protein's exact database record. This is a credible inference, though not independent experimental confirmation of the particular substrate reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives are distinct, and the secreted phospholipase A2 family inference specifically favors D.


### Important caveats

- The cited catalytic-activity annotation is computationally supported by a PROSITE rule; the excerpts do not show a direct assay of this protein's catalytic activity.
- The sequence-matched entry identifies the protein in venom, but that source-specific information was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted precursor, and the short, cysteine-rich mature region is characteristic of secreted venom phospholipase A2 proteins. Transferable knowledge of this enzyme family supports hydrolysis of a phospholipid acyl ester, matching option D; the other choices describe unrelated transformations or no net reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features provide a meaningful basis for distinguishing D without needing this protein's exact database record. This is a credible inference, though not independent experimental confirmation of the particular substrate reaction."
  },
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as phospholipase A2 and gives the reaction in option D. The reaction annotation is computationally supported by a PROSITE rule, rather than being direct experimental evidence in the supplied excerpts, but it is consistent with the sequence and enzyme family."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is computationally supported by a PROSITE rule; the excerpts do not show a direct assay of this protein's catalytic activity.",
    "The sequence-matched entry identifies the protein in venom, but that source-specific information was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are distinct, and the secreted phospholipase A2 family inference specifically favors D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as phospholipase A2 and gives the reaction in option D. The reaction annotation is computationally supported by a PROSITE rule, rather than being direct experimental evidence in the supplied excerpts, but it is consistent with the sequence and enzyme family.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted precursor, and the short, cysteine-rich mature region is characteristic of secreted venom phospholipase A2 proteins. Transferable knowledge of this enzyme family supports hydrolysis of a phospholipid acyl ester, matching option D; the other choices describe unrelated transformations or no net reaction.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features provide a meaningful basis for distinguishing D without needing this protein's exact database record. This is a credible inference, though not independent experimental confirmation of the particular substrate reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are distinct, and the secreted phospholipase A2 family inference specifically favors D."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is computationally supported by a PROSITE rule; the excerpts do not show a direct assay of this protein's catalytic activity.",
    "The sequence-matched entry identifies the protein in venom, but that source-specific information was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXZ6 (PA2_XYLAR) annotates this exact sequence (179 aa, matched) as Phospholipase A2 (EC 3.1.1.4) with the catalytic reaction 'a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)', matching choice D verbatim. The evidence codes are ECO:0000250 (similarity to P00630) and ECO:0000255 (PROSITE-ProRule PRU10035), indicating a computational/similarity-based annotation rather than a direct enzymatic assay. The protein was identified by mass spectrometry from Xylocopa aruana venom gland (PubMed 36550366), but the specific catalytic activity is transferred by homology. The annotation is present and consistent with the sequence's PLA2-family features.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The mature region of the sequence contains multiple diagnostic motifs of the secretory phospholipase A2 (sPLA2) superfamily, recognizable from homologous proteins (pancreatic PLA2, snake venom PLA2s, bee/wasp venom PLA2s): (1) The 'GTKWCGNG' and 'GTKCYRNE' segments contain the 'CGNG' calcium-binding loop signature and the conserved 'GTK' motif found in virtually all sPLA2s. (2) A dense cysteine pattern (≥8 cysteines in the mature domain) forming the characteristic disulfide-bond framework of sPLA2. (3) An N-terminal hydrophobic signal peptide (MHALRSSVLALWLCLHVSVRAW) indicating a secreted protein, consistent with venom PLA2. (4) The overall mature length (~135 aa) matches the sPLA2 size range. These features are shared across the PLA2 family and are not present in the alternatives: choice A (inosine transporter) requires 10-12 transmembrane helices absent here; choice B (ornithine aminotransferase) requires a ~450-aa PLP-dependent fold with specific lysine/arginine motifs absent here; choice C (K+ channel) requires the TVGYG selectivity filter and multiple TM segments absent here. Family-level recognition of sPLA2 motifs learned from other PLA2s meaningfully and uniquely distinguishes choice D from all other offered options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sPLA2 catalytic and calcium-binding motifs (CGNG, GTK, CYRNE, dense cysteine pattern, signal peptide) are well-conserved across the PLA2 superfamily and can be recognized by comparison with other PLA2 sequences (e.g., pancreatic PLA2, snake venom PLA2s). This family-level pattern recognition, combined with the complete absence of features required by the other three choices (TM helices for transporters/channels, PLP-binding motifs for aminotransferases), provides a concrete and credible transferable inference that uniquely selects choice D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sPLA2 sequence motifs are highly specific and none of the other three choices (nucleoside transporter, aminotransferase, K+ channel) have any sequence or structural compatibility with this protein. Only choice D is defensible.


### Important caveats

- The UniProt catalytic activity annotation uses evidence codes ECO:0000250 (similarity) and ECO:0000255 (PROSITE-ProRule), meaning it is a computational transfer rather than a direct enzymatic assay on this specific protein.
- The protein was identified by mass spectrometry from venom gland tissue but the specific hydrolytic reaction was not experimentally demonstrated on this exact sequence in the cited reference.
- The sequence is a precursor (includes signal peptide); the mature PLA2 domain begins after the signal peptide.
- The annotation was first published in 2025 (entry integrated 05-FEB-2025), so the benchmark question was constructed from a very recent Swiss-Prot entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The mature region of the sequence contains multiple diagnostic motifs of the secretory phospholipase A2 (sPLA2) superfamily, recognizable from homologous proteins (pancreatic PLA2, snake venom PLA2s, bee/wasp venom PLA2s): (1) The 'GTKWCGNG' and 'GTKCYRNE' segments contain the 'CGNG' calcium-binding loop signature and the conserved 'GTK' motif found in virtually all sPLA2s. (2) A dense cysteine pattern (≥8 cysteines in the mature domain) forming the characteristic disulfide-bond framework of sPLA2. (3) An N-terminal hydrophobic signal peptide (MHALRSSVLALWLCLHVSVRAW) indicating a secreted protein, consistent with venom PLA2. (4) The overall mature length (~135 aa) matches the sPLA2 size range. These features are shared across the PLA2 family and are not present in the alternatives: choice A (inosine transporter) requires 10-12 transmembrane helices absent here; choice B (ornithine aminotransferase) requires a ~450-aa PLP-dependent fold with specific lysine/arginine motifs absent here; choice C (K+ channel) requires the TVGYG selectivity filter and multiple TM segments absent here. Family-level recognition of sPLA2 motifs learned from other PLA2s meaningfully and uniquely distinguishes choice D from all other offered options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sPLA2 catalytic and calcium-binding motifs (CGNG, GTK, CYRNE, dense cysteine pattern, signal peptide) are well-conserved across the PLA2 superfamily and can be recognized by comparison with other PLA2 sequences (e.g., pancreatic PLA2, snake venom PLA2s). This family-level pattern recognition, combined with the complete absence of features required by the other three choices (TM helices for transporters/channels, PLP-binding motifs for aminotransferases), provides a concrete and credible transferable inference that uniquely selects choice D."
  },
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ6 (PA2_XYLAR) annotates this exact sequence (179 aa, matched) as Phospholipase A2 (EC 3.1.1.4) with the catalytic reaction 'a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)', matching choice D verbatim. The evidence codes are ECO:0000250 (similarity to P00630) and ECO:0000255 (PROSITE-ProRule PRU10035), indicating a computational/similarity-based annotation rather than a direct enzymatic assay. The protein was identified by mass spectrometry from Xylocopa aruana venom gland (PubMed 36550366), but the specific catalytic activity is transferred by homology. The annotation is present and consistent with the sequence's PLA2-family features."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation uses evidence codes ECO:0000250 (similarity) and ECO:0000255 (PROSITE-ProRule), meaning it is a computational transfer rather than a direct enzymatic assay on this specific protein.",
    "The protein was identified by mass spectrometry from venom gland tissue but the specific hydrolytic reaction was not experimentally demonstrated on this exact sequence in the cited reference.",
    "The sequence is a precursor (includes signal peptide); the mature PLA2 domain begins after the signal peptide.",
    "The annotation was first published in 2025 (entry integrated 05-FEB-2025), so the benchmark question was constructed from a very recent Swiss-Prot entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sPLA2 sequence motifs are highly specific and none of the other three choices (nucleoside transporter, aminotransferase, K+ channel) have any sequence or structural compatibility with this protein. Only choice D is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ6 (PA2_XYLAR) annotates this exact sequence (179 aa, matched) as Phospholipase A2 (EC 3.1.1.4) with the catalytic reaction 'a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)', matching choice D verbatim. The evidence codes are ECO:0000250 (similarity to P00630) and ECO:0000255 (PROSITE-ProRule PRU10035), indicating a computational/similarity-based annotation rather than a direct enzymatic assay. The protein was identified by mass spectrometry from Xylocopa aruana venom gland (PubMed 36550366), but the specific catalytic activity is transferred by homology. The annotation is present and consistent with the sequence's PLA2-family features.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The mature region of the sequence contains multiple diagnostic motifs of the secretory phospholipase A2 (sPLA2) superfamily, recognizable from homologous proteins (pancreatic PLA2, snake venom PLA2s, bee/wasp venom PLA2s): (1) The 'GTKWCGNG' and 'GTKCYRNE' segments contain the 'CGNG' calcium-binding loop signature and the conserved 'GTK' motif found in virtually all sPLA2s. (2) A dense cysteine pattern (≥8 cysteines in the mature domain) forming the characteristic disulfide-bond framework of sPLA2. (3) An N-terminal hydrophobic signal peptide (MHALRSSVLALWLCLHVSVRAW) indicating a secreted protein, consistent with venom PLA2. (4) The overall mature length (~135 aa) matches the sPLA2 size range. These features are shared across the PLA2 family and are not present in the alternatives: choice A (inosine transporter) requires 10-12 transmembrane helices absent here; choice B (ornithine aminotransferase) requires a ~450-aa PLP-dependent fold with specific lysine/arginine motifs absent here; choice C (K+ channel) requires the TVGYG selectivity filter and multiple TM segments absent here. Family-level recognition of sPLA2 motifs learned from other PLA2s meaningfully and uniquely distinguishes choice D from all other offered options.",
    "missing_item_specific_fact": "",
    "reason": "The sPLA2 catalytic and calcium-binding motifs (CGNG, GTK, CYRNE, dense cysteine pattern, signal peptide) are well-conserved across the PLA2 superfamily and can be recognized by comparison with other PLA2 sequences (e.g., pancreatic PLA2, snake venom PLA2s). This family-level pattern recognition, combined with the complete absence of features required by the other three choices (TM helices for transporters/channels, PLP-binding motifs for aminotransferases), provides a concrete and credible transferable inference that uniquely selects choice D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sPLA2 sequence motifs are highly specific and none of the other three choices (nucleoside transporter, aminotransferase, K+ channel) have any sequence or structural compatibility with this protein. Only choice D is defensible."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation uses evidence codes ECO:0000250 (similarity) and ECO:0000255 (PROSITE-ProRule), meaning it is a computational transfer rather than a direct enzymatic assay on this specific protein.",
    "The protein was identified by mass spectrometry from venom gland tissue but the specific hydrolytic reaction was not experimentally demonstrated on this exact sequence in the cited reference.",
    "The sequence is a precursor (includes signal peptide); the mature PLA2 domain begins after the signal peptide.",
    "The annotation was first published in 2025 (entry integrated 05-FEB-2025), so the benchmark question was constructed from a very recent Swiss-Prot entry."
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
  "benchmark_sequence_length": 179,
  "benchmark_sequence_sha256": "50594be59aa7852dcdccd4fd13825b239fed46dff2ce31a488ef868edb881b3b",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 179,
  "current_source_sequence_sha256": "50594be59aa7852dcdccd4fd13825b239fed46dff2ce31a488ef868edb881b3b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXZ6",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "selected_historical_source_sequence_length": 179,
  "selected_historical_source_sequence_sha256": "50594be59aa7852dcdccd4fd13825b239fed46dff2ce31a488ef868edb881b3b",
  "selected_historical_version": {
    "accession": "P0DXZ6",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PA2_XYLAR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXZ6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Great carpenter bee\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Hymenoptera\",\"Apocrita\",\"Aculeata\",\"Apoidea\",\"Anthophila\",\"Apidae\",\"Xylocopa\",\"Koptortosoma\"],\"scientificName\":\"Xylocopa aruana\",\"taxonId\":135674}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Phosphatidylcholine 2-acylhydrolase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00630\",\"source\":\"UniProtKB\"}],\"value\":\"3.1.1.4\"}],\"fullName\":{\"value\":\"Phospholipase A2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PA2\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36550366\",\"source\":\"PubMed\"}],\"value\":\"PLA2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.1.1.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10035\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15801\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28868\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57643\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58168\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi N.\",\"Szanto T.G.\",\"He J.\",\"Schroeder C.I.\",\"Walker A.A.\",\"Deuis J.R.\",\"Vetter I.\",\"Panyi G.\",\"King G.F.\",\"Robinson S.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36550366\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-022-26867-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"22168\",\"id\":\"36550366\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"22168\",\"publicationDate\":\"2022\",\"title\":\"Venom composition and pain-causing toxins of the Australian great carpenter bee Xylocopa aruana.\",\"volume\":\"12\"},\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom\"},{\"type\":\"TISSUE\",\"value\":\"Venom gland\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   PA2_XYLAR               Reviewed;         179 AA.\nAC   P0DXZ6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Phospholipase A2;\nDE            Short=PA2 {ECO:0000305};\nDE            Short=PLA2 {ECO:0000303|PubMed:36550366};\nDE            EC=3.1.1.4 {ECO:0000250|UniProtKB:P00630};\nDE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;\nDE   Flags: Precursor;\nOS   Xylocopa aruana (Great carpenter bee).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;\nOC   Anthophila; Apidae; Xylocopa; Koptortosoma.\nOX   NCBI_TaxID=135674;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phospholipase A2;\nDE            Short=PA2 {ECO:0000305};\nDE            Short=PLA2 {ECO:0000303|PubMed:36550366};\nDE            EC=3.1.1.4 {ECO:0000250|UniProtKB:P00630};\nDE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], IDENTIFICATION BY MASS SPECTROMETRY, AND\nRP   SUBCELLULAR LOCATION.\nRC   TISSUE=Venom, and Venom gland;\nRX   PubMed=36550366; DOI=10.1038/s41598-022-26867-8;\nRA   Shi N., Szanto T.G., He J., Schroeder C.I., Walker A.A., Deuis J.R.,\nRA   Vetter I., Panyi G., King G.F., Robinson S.D.;\nRT   \"Venom composition and pain-causing toxins of the Australian great\nRT   carpenter bee Xylocopa aruana.\";\nRL   Sci. Rep. 12:22168-22168(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-\nCC         glycero-3-phosphocholine + a fatty acid + H(+); Xref=Rhea:RHEA:15801,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:28868,\nCC         ChEBI:CHEBI:57643, ChEBI:CHEBI:58168; EC=3.1.1.4;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10035};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
