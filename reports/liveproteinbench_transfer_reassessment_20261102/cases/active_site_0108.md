# active_site_0108

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0108.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 538 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYMLRPSSLLLATGLLNQGSSVLAAVISRASNQTFDYVIVGGGTAGLVLANRLTEDSSVTVAVVEAGTFPEDVVGNVTQVPAYAPQFEGAELDLEWNFTTTPQAGLGNIPVSYYRAKALGGCSDINFMAYGRTSKGAHQLWADLVGDDSYTYDNMVKYYKKTMNFSPPNAETRLANATPMYDTVDTSTGGGIDVTFPSFAQSWSTWVSKGLAAIGLPQAHSFVDGNLLGHSWQMVGITQSTGIRSSAQAGYLRPVMSRPNLTILNGTFAERIIFNGDAASGVEVTAKGQTYTLTSKKELILSAGVFQSPQLLMVSGVGPKALLDKFNIPVVKDLPGVGQNMVDHITVPLSYQVDVVTSSTLAGSSLEEAITEWNTHGTGPLSNNGGDYIGMEKAPAEFRANFSAETVKQLSALPEDWPELQYNVLPATVSSTSIGGEGSVLGGNYGSMLASVIAPQSRGNVSIASASMSDAPLINPNIFTAQADIDLLLTAFKRVRQALQSSAMAPIMIGDEFFPGPTVQTDEQILDYLTETVRPFSHGFATCKMGKSSDPDAVIDSHGKVYGIKNLRVVDASSFPFLPPGPAPQIQVYTLAEKLADDIKQTKY

[Multiple Choices]
A. Position 538 (Proton acceptor)
B. Position 1183 (Proton donor; for dehydratase activity 1)
C. Position 26 (Proton donor/acceptor)
D. Position 203 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates position 538 as an active-site proton acceptor. That annotation is transferred by similarity from a related protein (ECO:0000250), so it supports the key but is not direct experimental validation of this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s glycine-rich flavin-binding motif and overall features are consistent with a GMC-family FAD-dependent oxidoreductase. Family and homolog knowledge can guide alignment to a conserved catalytic proton-accepting residue in the catalytic region, making position 538 a defensible choice. Position 1183 is beyond the 604-residue sequence, and position 26 lies near the N-terminus rather than the expected catalytic region.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and transferable knowledge of homologous flavoprotein oxidoreductases meaningfully favors A. It need not reproduce the exact database annotation to distinguish the offered options, though the inference is not certain from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered position has comparable support; B is outside the sequence, and the sequence/family evidence favors A over the remaining alternatives.


### Important caveats

- The supplied source annotation is similarity-based, not evidence of direct experimental determination for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s glycine-rich flavin-binding motif and overall features are consistent with a GMC-family FAD-dependent oxidoreductase. Family and homolog knowledge can guide alignment to a conserved catalytic proton-accepting residue in the catalytic region, making position 538 a defensible choice. Position 1183 is beyond the 604-residue sequence, and position 26 lies near the N-terminus rather than the expected catalytic region.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and transferable knowledge of homologous flavoprotein oxidoreductases meaningfully favors A. It need not reproduce the exact database annotation to distinguish the offered options, though the inference is not certain from sequence alone."
  },
  "case_id": "active_site_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 538 as an active-site proton acceptor. That annotation is transferred by similarity from a related protein (ECO:0000250), so it supports the key but is not direct experimental validation of this protein."
  },
  "important_caveats": [
    "The supplied source annotation is similarity-based, not evidence of direct experimental determination for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered position has comparable support; B is outside the sequence, and the sequence/family evidence favors A over the remaining alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 538 as an active-site proton acceptor. That annotation is transferred by similarity from a related protein (ECO:0000250), so it supports the key but is not direct experimental validation of this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s glycine-rich flavin-binding motif and overall features are consistent with a GMC-family FAD-dependent oxidoreductase. Family and homolog knowledge can guide alignment to a conserved catalytic proton-accepting residue in the catalytic region, making position 538 a defensible choice. Position 1183 is beyond the 604-residue sequence, and position 26 lies near the N-terminus rather than the expected catalytic region.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and transferable knowledge of homologous flavoprotein oxidoreductases meaningfully favors A. It need not reproduce the exact database annotation to distinguish the offered options, though the inference is not certain from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered position has comparable support; B is outside the sequence, and the sequence/family evidence favors A over the remaining alternatives."
  },
  "important_caveats": [
    "The supplied source annotation is similarity-based, not evidence of direct experimental determination for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY22 annotates position 538 as 'Proton acceptor' active site (evidence ECO:0000250, inferred by similarity to E4QP00, a related GMC oxidoreductase). The sequence is 604 residues, so position 538 is valid. The residue at position 538 is Histidine (H), embedded in the conserved 'FSHGFAT' motif characteristic of the glucose-methanol-choline (GMC) oxidoreductase family. The annotation is homology-based rather than directly experimental for this protein, but it is consistent with the well-established catalytic mechanism of the family. The other options are either out of range (position 1183 exceeds the 604-residue length) or correspond to non-catalytic residues (Val at 26, Ser at 203).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two highly diagnostic features of the GMC oxidoreductase family: (1) the Rossmann-fold FAD-binding motif 'GGGTAG' near position 41-46, and (2) the catalytic 'FSHGFAT' motif near the C-terminus. In every well-characterized GMC oxidoreductase (glucose oxidase from A. niger with His516, methanol oxidase, choline oxidase), the histidine immediately preceding 'GFAT' in the 'FSHG' context is the catalytic base acting as a proton acceptor that abstracts a proton from the substrate hydroxyl group. Position 538 corresponds to this histidine. Option B (position 1183) is immediately eliminated because the protein is only 604 residues. Option C (position 26 = Val) and option D (position 203 = Ser) do not correspond to any known catalytic residue in this family. The family-level inference from the conserved FSHGFAT motif and the FAD-binding Rossmann fold is a textbook example of transferable knowledge from glucose oxidase and related enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the GMC oxidoreductase family from the GGGTAG Rossmann-fold motif and the FSHGFAT catalytic motif, both visible in the raw sequence. Family-level knowledge from glucose oxidase, methanol oxidase, and choline oxidase establishes that the His in FSHG is the catalytic proton acceptor. The protein length (604) eliminates option B. The residues at positions 26 and 203 are non-catalytic for this family. No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A corresponds to the conserved catalytic histidine in the FSHGFAT motif. Option B is impossible (position exceeds sequence length). Options C and D correspond to Val and Ser, which are not catalytic residues in GMC oxidoreductases. No ambiguity exists.


### Important caveats

- The UniProt annotation for position 538 is based on homology (ECO:0000250 to E4QP00), not direct experimental characterization of this specific protein. However, the FSHGFAT motif is so highly conserved across the GMC family that the inference is robust.
- The protein was characterized in a 2024 publication (PubMed 38404388) as part of a polyketide-terpenoid biosynthetic cluster, but the catalytic residue assignment relies on family-level mechanistic knowledge rather than a dedicated mutagenesis study of this enzyme.
- The reviewer-only evidence confirms the sequence matches P0DY22 (604 AA) and the active-site annotation, but these were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two highly diagnostic features of the GMC oxidoreductase family: (1) the Rossmann-fold FAD-binding motif 'GGGTAG' near position 41-46, and (2) the catalytic 'FSHGFAT' motif near the C-terminus. In every well-characterized GMC oxidoreductase (glucose oxidase from A. niger with His516, methanol oxidase, choline oxidase), the histidine immediately preceding 'GFAT' in the 'FSHG' context is the catalytic base acting as a proton acceptor that abstracts a proton from the substrate hydroxyl group. Position 538 corresponds to this histidine. Option B (position 1183) is immediately eliminated because the protein is only 604 residues. Option C (position 26 = Val) and option D (position 203 = Ser) do not correspond to any known catalytic residue in this family. The family-level inference from the conserved FSHGFAT motif and the FAD-binding Rossmann fold is a textbook example of transferable knowledge from glucose oxidase and related enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GMC oxidoreductase family from the GGGTAG Rossmann-fold motif and the FSHGFAT catalytic motif, both visible in the raw sequence. Family-level knowledge from glucose oxidase, methanol oxidase, and choline oxidase establishes that the His in FSHG is the catalytic proton acceptor. The protein length (604) eliminates option B. The residues at positions 26 and 203 are non-catalytic for this family. No target-specific database lookup is required."
  },
  "case_id": "active_site_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY22 annotates position 538 as 'Proton acceptor' active site (evidence ECO:0000250, inferred by similarity to E4QP00, a related GMC oxidoreductase). The sequence is 604 residues, so position 538 is valid. The residue at position 538 is Histidine (H), embedded in the conserved 'FSHGFAT' motif characteristic of the glucose-methanol-choline (GMC) oxidoreductase family. The annotation is homology-based rather than directly experimental for this protein, but it is consistent with the well-established catalytic mechanism of the family. The other options are either out of range (position 1183 exceeds the 604-residue length) or correspond to non-catalytic residues (Val at 26, Ser at 203)."
  },
  "important_caveats": [
    "The UniProt annotation for position 538 is based on homology (ECO:0000250 to E4QP00), not direct experimental characterization of this specific protein. However, the FSHGFAT motif is so highly conserved across the GMC family that the inference is robust.",
    "The protein was characterized in a 2024 publication (PubMed 38404388) as part of a polyketide-terpenoid biosynthetic cluster, but the catalytic residue assignment relies on family-level mechanistic knowledge rather than a dedicated mutagenesis study of this enzyme.",
    "The reviewer-only evidence confirms the sequence matches P0DY22 (604 AA) and the active-site annotation, but these were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A corresponds to the conserved catalytic histidine in the FSHGFAT motif. Option B is impossible (position exceeds sequence length). Options C and D correspond to Val and Ser, which are not catalytic residues in GMC oxidoreductases. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY22 annotates position 538 as 'Proton acceptor' active site (evidence ECO:0000250, inferred by similarity to E4QP00, a related GMC oxidoreductase). The sequence is 604 residues, so position 538 is valid. The residue at position 538 is Histidine (H), embedded in the conserved 'FSHGFAT' motif characteristic of the glucose-methanol-choline (GMC) oxidoreductase family. The annotation is homology-based rather than directly experimental for this protein, but it is consistent with the well-established catalytic mechanism of the family. The other options are either out of range (position 1183 exceeds the 604-residue length) or correspond to non-catalytic residues (Val at 26, Ser at 203).",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two highly diagnostic features of the GMC oxidoreductase family: (1) the Rossmann-fold FAD-binding motif 'GGGTAG' near position 41-46, and (2) the catalytic 'FSHGFAT' motif near the C-terminus. In every well-characterized GMC oxidoreductase (glucose oxidase from A. niger with His516, methanol oxidase, choline oxidase), the histidine immediately preceding 'GFAT' in the 'FSHG' context is the catalytic base acting as a proton acceptor that abstracts a proton from the substrate hydroxyl group. Position 538 corresponds to this histidine. Option B (position 1183) is immediately eliminated because the protein is only 604 residues. Option C (position 26 = Val) and option D (position 203 = Ser) do not correspond to any known catalytic residue in this family. The family-level inference from the conserved FSHGFAT motif and the FAD-binding Rossmann fold is a textbook example of transferable knowledge from glucose oxidase and related enzymes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GMC oxidoreductase family from the GGGTAG Rossmann-fold motif and the FSHGFAT catalytic motif, both visible in the raw sequence. Family-level knowledge from glucose oxidase, methanol oxidase, and choline oxidase establishes that the His in FSHG is the catalytic proton acceptor. The protein length (604) eliminates option B. The residues at positions 26 and 203 are non-catalytic for this family. No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A corresponds to the conserved catalytic histidine in the FSHGFAT motif. Option B is impossible (position exceeds sequence length). Options C and D correspond to Val and Ser, which are not catalytic residues in GMC oxidoreductases. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt annotation for position 538 is based on homology (ECO:0000250 to E4QP00), not direct experimental characterization of this specific protein. However, the FSHGFAT motif is so highly conserved across the GMC family that the inference is robust.",
    "The protein was characterized in a 2024 publication (PubMed 38404388) as part of a polyketide-terpenoid biosynthetic cluster, but the catalytic residue assignment relies on family-level mechanistic knowledge rather than a dedicated mutagenesis study of this enzyme.",
    "The reviewer-only evidence confirms the sequence matches P0DY22 (604 AA) and the active-site annotation, but these were not available to the evaluated model."
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
  "benchmark_sequence_length": 604,
  "benchmark_sequence_sha256": "d3b91763b1aeec6909489107b5227811c4fdd9c5bc992119ac925d983d2d88ca",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 604,
  "current_source_sequence_sha256": "d3b91763b1aeec6909489107b5227811c4fdd9c5bc992119ac925d983d2d88ca",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DY22",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "selected_historical_source_sequence_length": 604,
  "selected_historical_source_sequence_sha256": "d3b91763b1aeec6909489107b5227811c4fdd9c5bc992119ac925d983d2d88ca",
  "selected_historical_version": {
    "accession": "P0DY22",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMG_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY22\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein G\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.1.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Glucose-methanol-choline family oxidoreductase mfmG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E4QP00\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":538},\"start\":{\"modifier\":\"EXACT\",\"value\":538}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E4QP00\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":45},\"start\":{\"modifier\":\"EXACT\",\"value\":44}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E4QP00\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":66},\"start\":{\"modifier\":\"EXACT\",\"value\":65}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E4QP00\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":126}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E4QP00\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":572},\"start\":{\"modifier\":\"EXACT\",\"value\":572}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E4QP00\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":585},\"start\":{\"modifier\":\"EXACT\",\"value\":584}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:17.365835+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY22.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMG_ANNMO              Reviewed;         604 AA.\nAC   P0DY22;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Glucose-methanol-choline family oxidoreductase mfmG {ECO:0000303|PubMed:38404388};\nDE            EC=1.1.-.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein G {ECO:0000303|PubMed:38404388};\nDE   Flags: Precursor;\nGN   Name=mfmG {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_30153;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        538\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:E4QP00\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         44..45\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:E4QP00\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         65..66\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:E4QP00\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         126..129\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:E4QP00\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         572\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:E4QP00\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         584..585\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:E4QP00\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.566799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337",
  "url": "https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
