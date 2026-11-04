# pathway_0031

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0031.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Glycolipid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. Amino-acid biosynthesis
B. L-valine biosynthesis
C. Glycolipid biosynthesis
D. Glycan degradation
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

> The sequence-matched UniProt annotation places the protein in glycolipid biosynthesis, specifically GPI-anchor biosynthesis. The annotation identifies it as a GPI mannosyltransferase; the linked pathway annotation cites experimental evidence, although the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic with many likely transmembrane helices, consistent with an ER membrane glycosyltransferase rather than a typical soluble amino-acid biosynthesis enzyme. Transferable knowledge of multipass GT-C glycosyltransferases supports sugar transfer during assembly of membrane-associated glycoconjugates, including glycolipids; glycan-degradation enzymes are more typically hydrolases. This makes C meaningfully more plausible than the offered alternatives, though the sequence architecture alone is not definitive.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge of membrane glycosyltransferase families give a credible, if probabilistic, basis for choosing glycolipid biosynthesis without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, glycolipid biosynthesis best matches the inferred membrane glycosyltransferase function; no other option is comparably supported.


### Important caveats

- The multipass architecture is suggestive, not sufficient by itself to establish a specific pathway.
- The reviewer-only annotation supports the key, but its linked primary study was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic with many likely transmembrane helices, consistent with an ER membrane glycosyltransferase rather than a typical soluble amino-acid biosynthesis enzyme. Transferable knowledge of multipass GT-C glycosyltransferases supports sugar transfer during assembly of membrane-associated glycoconjugates, including glycolipids; glycan-degradation enzymes are more typically hydrolases. This makes C meaningfully more plausible than the offered alternatives, though the sequence architecture alone is not definitive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of membrane glycosyltransferase families give a credible, if probabilistic, basis for choosing glycolipid biosynthesis without needing the exact protein's database record."
  },
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the protein in glycolipid biosynthesis, specifically GPI-anchor biosynthesis. The annotation identifies it as a GPI mannosyltransferase; the linked pathway annotation cites experimental evidence, although the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The multipass architecture is suggestive, not sufficient by itself to establish a specific pathway.",
    "The reviewer-only annotation supports the key, but its linked primary study was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, glycolipid biosynthesis best matches the inferred membrane glycosyltransferase function; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the protein in glycolipid biosynthesis, specifically GPI-anchor biosynthesis. The annotation identifies it as a GPI mannosyltransferase; the linked pathway annotation cites experimental evidence, although the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic with many likely transmembrane helices, consistent with an ER membrane glycosyltransferase rather than a typical soluble amino-acid biosynthesis enzyme. Transferable knowledge of multipass GT-C glycosyltransferases supports sugar transfer during assembly of membrane-associated glycoconjugates, including glycolipids; glycan-degradation enzymes are more typically hydrolases. This makes C meaningfully more plausible than the offered alternatives, though the sequence architecture alone is not definitive.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of membrane glycosyltransferase families give a credible, if probabilistic, basis for choosing glycolipid biosynthesis without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, glycolipid biosynthesis best matches the inferred membrane glycosyltransferase function; no other option is comparably supported."
  },
  "important_caveats": [
    "The multipass architecture is suggestive, not sufficient by itself to establish a specific pathway.",
    "The reviewer-only annotation supports the key, but its linked primary study was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this exact sequence (A0A8C2M425, PIGV_CRIGR) explicitly annotates the pathway as 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis' with experimental evidence (ECO:0000269|PubMed:23694781, Hirata et al. J. Biochem. 2013). The protein is GPI alpha-1,6-mannosyltransferase 2 (PIGV/GPI-MT-II), a mannosyltransferase in the GPI-anchor biosynthetic pathway. This directly supports choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 494-residue sequence exhibits an extreme multi-transmembrane topology (approximately 8–10+ hydrophobic stretches spanning the sequence), characteristic of integral ER-membrane proteins involved in lipid/glycan biosynthesis (e.g., PIG enzymes, ceramide synthases, glucosylceramide synthase). This topology allows direct interaction with membrane-embedded lipid substrates (dolichol-phosphate mannose, GPI intermediates). In contrast: (A) amino-acid biosynthesis enzymes are soluble cytoplasmic enzymes (e.g., synthases, transaminases) without multi-TM architecture; (B) L-valine biosynthesis is a bacterial/fungal pathway absent in mammals, and its enzymes are also soluble; (D) glycan-degradation enzymes (glycosidases) are typically soluble cytosolic/lysosomal or single-pass membrane proteins, not 8+ TM integral membrane proteins. Thus, the pronounced multi-TM hydrophobic architecture plus glycosyltransferase-like conserved motifs (e.g., regions resembling DxH or HxxxD motifs common in retaining glycosyltransferases) meaningfully favor C (Glycolipid biosynthesis) over A, B, and D using general knowledge of membrane-protein topology and pathway compartmentalization learned from many other ER biosynthetic enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-TM topology visible directly from the sequence, combined with general knowledge that ER-membrane glycolipid biosynthetic enzymes are multi-pass integral membrane proteins while amino-acid biosynthesis enzymes and glycan-degradation glycosidases are soluble or single-pass, provides a concrete transferable inference that distinguishes C from the other three options without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The extreme multi-TM hydrophobicity of the sequence clearly excludes soluble-enzyme pathways (A, B) and typical glycosidase topology (D). Among the four offered choices, only C is consistent with an 8+ TM ER-membrane glycosyltransferase. No other option is genuinely defensible given the sequence architecture.


### Important caveats

- The UniProt annotation for GPI-MT-II relies partly on similarity-based transfer (ECO:0000250|UniProtKB:Q9NUD9) for the name and pathway assignment, though the experimental paper (PubMed:23694781) independently confirmed the mannosyltransferase activity and pathway role.
- The organism (Chinese hamster) is not provided in the original user input; however, the multi-TM topology argument does not depend on knowing the species.
- The sequence is 494 residues; the hydrophobicity profile is directly computable from the provided sequence without external lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 494-residue sequence exhibits an extreme multi-transmembrane topology (approximately 8–10+ hydrophobic stretches spanning the sequence), characteristic of integral ER-membrane proteins involved in lipid/glycan biosynthesis (e.g., PIG enzymes, ceramide synthases, glucosylceramide synthase). This topology allows direct interaction with membrane-embedded lipid substrates (dolichol-phosphate mannose, GPI intermediates). In contrast: (A) amino-acid biosynthesis enzymes are soluble cytoplasmic enzymes (e.g., synthases, transaminases) without multi-TM architecture; (B) L-valine biosynthesis is a bacterial/fungal pathway absent in mammals, and its enzymes are also soluble; (D) glycan-degradation enzymes (glycosidases) are typically soluble cytosolic/lysosomal or single-pass membrane proteins, not 8+ TM integral membrane proteins. Thus, the pronounced multi-TM hydrophobic architecture plus glycosyltransferase-like conserved motifs (e.g., regions resembling DxH or HxxxD motifs common in retaining glycosyltransferases) meaningfully favor C (Glycolipid biosynthesis) over A, B, and D using general knowledge of membrane-protein topology and pathway compartmentalization learned from many other ER biosynthetic enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-TM topology visible directly from the sequence, combined with general knowledge that ER-membrane glycolipid biosynthetic enzymes are multi-pass integral membrane proteins while amino-acid biosynthesis enzymes and glycan-degradation glycosidases are soluble or single-pass, provides a concrete transferable inference that distinguishes C from the other three options without needing to recall this specific protein's database annotation."
  },
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (A0A8C2M425, PIGV_CRIGR) explicitly annotates the pathway as 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis' with experimental evidence (ECO:0000269|PubMed:23694781, Hirata et al. J. Biochem. 2013). The protein is GPI alpha-1,6-mannosyltransferase 2 (PIGV/GPI-MT-II), a mannosyltransferase in the GPI-anchor biosynthetic pathway. This directly supports choice C."
  },
  "important_caveats": [
    "The UniProt annotation for GPI-MT-II relies partly on similarity-based transfer (ECO:0000250|UniProtKB:Q9NUD9) for the name and pathway assignment, though the experimental paper (PubMed:23694781) independently confirmed the mannosyltransferase activity and pathway role.",
    "The organism (Chinese hamster) is not provided in the original user input; however, the multi-TM topology argument does not depend on knowing the species.",
    "The sequence is 494 residues; the hydrophobicity profile is directly computable from the provided sequence without external lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The extreme multi-TM hydrophobicity of the sequence clearly excludes soluble-enzyme pathways (A, B) and typical glycosidase topology (D). Among the four offered choices, only C is consistent with an 8+ TM ER-membrane glycosyltransferase. No other option is genuinely defensible given the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (A0A8C2M425, PIGV_CRIGR) explicitly annotates the pathway as 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis' with experimental evidence (ECO:0000269|PubMed:23694781, Hirata et al. J. Biochem. 2013). The protein is GPI alpha-1,6-mannosyltransferase 2 (PIGV/GPI-MT-II), a mannosyltransferase in the GPI-anchor biosynthetic pathway. This directly supports choice C.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 494-residue sequence exhibits an extreme multi-transmembrane topology (approximately 8–10+ hydrophobic stretches spanning the sequence), characteristic of integral ER-membrane proteins involved in lipid/glycan biosynthesis (e.g., PIG enzymes, ceramide synthases, glucosylceramide synthase). This topology allows direct interaction with membrane-embedded lipid substrates (dolichol-phosphate mannose, GPI intermediates). In contrast: (A) amino-acid biosynthesis enzymes are soluble cytoplasmic enzymes (e.g., synthases, transaminases) without multi-TM architecture; (B) L-valine biosynthesis is a bacterial/fungal pathway absent in mammals, and its enzymes are also soluble; (D) glycan-degradation enzymes (glycosidases) are typically soluble cytosolic/lysosomal or single-pass membrane proteins, not 8+ TM integral membrane proteins. Thus, the pronounced multi-TM hydrophobic architecture plus glycosyltransferase-like conserved motifs (e.g., regions resembling DxH or HxxxD motifs common in retaining glycosyltransferases) meaningfully favor C (Glycolipid biosynthesis) over A, B, and D using general knowledge of membrane-protein topology and pathway compartmentalization learned from many other ER biosynthetic enzymes.",
    "missing_item_specific_fact": "",
    "reason": "The multi-TM topology visible directly from the sequence, combined with general knowledge that ER-membrane glycolipid biosynthetic enzymes are multi-pass integral membrane proteins while amino-acid biosynthesis enzymes and glycan-degradation glycosidases are soluble or single-pass, provides a concrete transferable inference that distinguishes C from the other three options without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The extreme multi-TM hydrophobicity of the sequence clearly excludes soluble-enzyme pathways (A, B) and typical glycosidase topology (D). Among the four offered choices, only C is consistent with an 8+ TM ER-membrane glycosyltransferase. No other option is genuinely defensible given the sequence architecture."
  },
  "important_caveats": [
    "The UniProt annotation for GPI-MT-II relies partly on similarity-based transfer (ECO:0000250|UniProtKB:Q9NUD9) for the name and pathway assignment, though the experimental paper (PubMed:23694781) independently confirmed the mannosyltransferase activity and pathway role.",
    "The organism (Chinese hamster) is not provided in the original user input; however, the multi-TM topology argument does not depend on knowing the species.",
    "The sequence is 494 residues; the hydrophobicity profile is directly computable from the provided sequence without external lookup."
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
  "benchmark_sequence_length": 494,
  "benchmark_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-01-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 494,
  "current_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8C2M425",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "selected_historical_source_sequence_length": 494,
  "selected_historical_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "selected_historical_version": {
    "accession": "A0A8C2M425",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PIGV_CRIGR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8C2M425\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chinese hamster\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Cricetidae\",\"Cricetinae\",\"Cricetulus\"],\"scientificName\":\"Cricetulus griseus\",\"synonyms\":[\"Cricetulus barabensis griseus\"],\"taxonId\":10029}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"GPI mannosyltransferase II\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI-MT-II\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphatidylinositol-glycan biosynthesis class V protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"PIG-V\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI alpha-1,6-mannosyltransferase 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hirata T.\",\"Fujita M.\",\"Kanzawa N.\",\"Murakami Y.\",\"Maeda Y.\",\"Kinoshita T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23694781\"},{\"database\":\"DOI\",\"id\":\"10.1093/jb/mvt045\"}],\"citationType\":\"journal article\",\"firstPage\":\"257\",\"id\":\"23694781\",\"journal\":\"J. Biochem.\",\"lastPage\":\"264\",\"publicationDate\":\"2013\",\"title\":\"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-phosphate mannose availability.\",\"volume\":\"154\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PIGV_CRIGR              Reviewed;         494 AA.\nAC   A0A8C2M425;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=GPI alpha-1,6-mannosyltransferase 2 {ECO:0000250|UniProtKB:Q9NUD9};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:23694781};\nDE   AltName: Full=GPI mannosyltransferase II;\nDE            Short=GPI-MT-II {ECO:0000250|UniProtKB:Q9NUD9};\nDE   AltName: Full=Phosphatidylinositol-glycan biosynthesis class V protein {ECO:0000250|UniProtKB:Q9NUD9};\nDE            Short=PIG-V {ECO:0000250|UniProtKB:Q9NUD9};\nGN   Name=PIGV {ECO:0000303|PubMed:23694781};\nOS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;\nOC   Cricetidae; Cricetinae; Cricetulus.\nOX   NCBI_TaxID=10029;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=23694781; DOI=10.1093/jb/mvt045;\nRA   Hirata T., Fujita M., Kanzawa N., Murakami Y., Maeda Y., Kinoshita T.;\nRT   \"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting\nRT   enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-\nRT   phosphate mannose availability.\";\nRL   J. Biochem. 154:257-264(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor\nCC       biosynthesis. {ECO:0000269|PubMed:23694781}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
