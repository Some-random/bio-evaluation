# cofactor_0031

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0031.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATDTAVTGAPETMQLRLASGNGPVTRTVLRTPLRDALPSEVPLIDISPIFSTSVADRKAVACKIHDAATNIGFFYIQNHRVPSRDTDMAYSASLDFFRQDMEAKMKADAKKGPFDSGYRGPGTQRVNPDEGADLRETYSILYDPMLDPTVPDPARIPEPASRFLHLGRAPFESTDTLPHFKDAFVRYFQACLALARALTRTFALSLDLPESAFDSKVQYPDASLEINFYPPISTGHAVSAPADPDTRVSIGSHTDFLLFTILWQDSNGGLQVLNREGQWIRASPVEGTFVVNIGDYLQRITNDKYVSTVHRAQNWSGRQRVSMPFFWGFGMHESCQVLESCCGEDGKSKYDEVRCVDWVSRRLGNLFDLSDKG

[Multiple Choices]
A. FAD
B. pantetheine 4'-phosphate
C. tungstopterin
D. Fe(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched annotation identifies this protein as a 2-oxoglutarate–Fe(II)-type oxidoreductase and assigns one Fe(2+) ion per subunit. The cofactor assignment is supported, though the cofactor annotation itself cites a PROSITE rule rather than a direct binding experiment in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an H-D-containing segment followed by another histidine (in the region around HDAA…QNH), compatible with the conserved His/carboxylate metal-binding motif of Fe(II)/2-oxoglutarate-dependent oxygenases. Family-level knowledge therefore makes Fe(2+) a meaningful choice over FAD, pantetheine 4'-phosphate, or tungstopterin.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence-and-family inference distinguishes the offered choices without needing the exact protein's database record. The motif is suggestive rather than proof of metal binding, but the alternatives make the Fe(II)-dependent-enzyme inference sufficiently discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, Fe(2+) is the defensible cofactor choice; the other candidates are not supported by the sequence-family inference.


### Important caveats

- The cofactor annotation is computationally assigned by a PROSITE rule; the cited research reference supports the enzyme's Fe(II)/2-oxoglutarate-dependent classification, but the excerpts do not show a direct metal-binding assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an H-D-containing segment followed by another histidine (in the region around HDAA…QNH), compatible with the conserved His/carboxylate metal-binding motif of Fe(II)/2-oxoglutarate-dependent oxygenases. Family-level knowledge therefore makes Fe(2+) a meaningful choice over FAD, pantetheine 4'-phosphate, or tungstopterin.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-and-family inference distinguishes the offered choices without needing the exact protein's database record. The motif is suggestive rather than proof of metal binding, but the alternatives make the Fe(II)-dependent-enzyme inference sufficiently discriminating."
  },
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as a 2-oxoglutarate–Fe(II)-type oxidoreductase and assigns one Fe(2+) ion per subunit. The cofactor assignment is supported, though the cofactor annotation itself cites a PROSITE rule rather than a direct binding experiment in the supplied excerpts."
  },
  "important_caveats": [
    "The cofactor annotation is computationally assigned by a PROSITE rule; the cited research reference supports the enzyme's Fe(II)/2-oxoglutarate-dependent classification, but the excerpts do not show a direct metal-binding assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, Fe(2+) is the defensible cofactor choice; the other candidates are not supported by the sequence-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as a 2-oxoglutarate–Fe(II)-type oxidoreductase and assigns one Fe(2+) ion per subunit. The cofactor assignment is supported, though the cofactor annotation itself cites a PROSITE rule rather than a direct binding experiment in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an H-D-containing segment followed by another histidine (in the region around HDAA…QNH), compatible with the conserved His/carboxylate metal-binding motif of Fe(II)/2-oxoglutarate-dependent oxygenases. Family-level knowledge therefore makes Fe(2+) a meaningful choice over FAD, pantetheine 4'-phosphate, or tungstopterin.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-and-family inference distinguishes the offered choices without needing the exact protein's database record. The motif is suggestive rather than proof of metal binding, but the alternatives make the Fe(II)-dependent-enzyme inference sufficiently discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, Fe(2+) is the defensible cofactor choice; the other candidates are not supported by the sequence-family inference."
  },
  "important_caveats": [
    "The cofactor annotation is computationally assigned by a PROSITE rule; the cited research reference supports the enzyme's Fe(II)/2-oxoglutarate-dependent classification, but the excerpts do not show a direct metal-binding assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C4, H2) identifies the protein as '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.-. The cofactor comment (C5, H5) explicitly states Fe(2+) with evidence code ECO:0000255 (PROSITE-ProRule PRU00805, family-based inference). Additionally, reference 2 (C7, H4, PubMed 38578094, JACS 2024) provides experimental evidence (ECO:0000269) that the PPZ cluster encodes 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes.' The expected answer D (Fe(2+)) is directly supported by both computational family annotation and experimental characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2-oxoglutarate/Fe(II)-dependent oxygenase superfamily is one of the most extensively characterized enzyme families in biology, with hundreds of experimentally validated members (prolyl hydroxylases, AlkB DNA repair enzymes, taurine dioxygenase, etc.). Its hallmark is the 2-His-1-carboxylate facial triad (HxD/E...H) that coordinates a single Fe(II) ion. In the supplied sequence, the 'HESCQVL' motif (His-Glu pair) and a downstream 'HRAQN' His are recognizable components of this degenerate but well-known triad, consistent with the PROSITE-ProRule PRU00805 signature. The overall ~374-aa length and domain architecture are typical of 2OG/Fe(II) oxygenases. Transferable elimination of the other options: (C) tungstopterin is restricted to anaerobic enzymes in thermophilic archaea/bacteria (e.g., formate dehydrogenase, aldehyde ferredoxin oxidoreductase) and is implausible in an aerobic filamentous fungus; (A) FAD requires a Rossmann-fold GxGxxG motif, which is absent from this sequence; (B) pantetheine 4'-phosphate is the prosthetic group of acyl-carrier/acyltransferase domains (ACP/PCP) in fatty acid or polyketide synthases, and no such domain architecture is present. Thus, family-level recognition of the HxD/E...H triad pattern plus elimination of cofactor classes incompatible with the sequence and organism context provides a concrete, transferable inference favoring Fe(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HxD/E...H facial triad is a textbook-level, highly transferable feature shared across hundreds of characterized 2OG/Fe(II) oxygenases. A knowledgeable model can recognize the HESC and downstream His pattern, apply the well-established family-level metal-binding logic, and eliminate FAD (no Rossmann fold), pantetheine 4'-phosphate (no ACP/PCP domain), and tungstopterin (anaerobic/archaeal cofactor incompatible with a fungal sequence) using general biochemistry and organism-level biology. This constitutes a credible transferable inference, not memorization of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct cofactor classes (flavin, acyl-carrier prosthetic group, anaerobic molybdenum/tungsten cofactor, divalent metal ion) that are mutually exclusive and distinguishable by sequence features and biological context. No two options are defensible for this sequence.


### Important caveats

- The PROSITE-ProRule PRU00805 annotation is a family-level computational inference (ECO:0000255), not direct experimental measurement of Fe(2+) binding to this exact protein. However, the 2024 JACS reference (PubMed 38578094) provides experimental functional evidence for Fe(II) dependence in the PPZ cluster enzymes.
- The HxD/E...H triad in raw sequence is degenerate and variable in spacing; recognition from sequence alone is probabilistic rather than deterministic, though the combination of motif, length, and elimination of alternatives strengthens the inference.
- The reviewer-only evidence confirms the sequence matches UniProt A0A455ZKR7 (Metarhizium majus ppzC), but this accession and organism identity were not provided to the evaluated model. The transferable argument relies only on sequence features and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2-oxoglutarate/Fe(II)-dependent oxygenase superfamily is one of the most extensively characterized enzyme families in biology, with hundreds of experimentally validated members (prolyl hydroxylases, AlkB DNA repair enzymes, taurine dioxygenase, etc.). Its hallmark is the 2-His-1-carboxylate facial triad (HxD/E...H) that coordinates a single Fe(II) ion. In the supplied sequence, the 'HESCQVL' motif (His-Glu pair) and a downstream 'HRAQN' His are recognizable components of this degenerate but well-known triad, consistent with the PROSITE-ProRule PRU00805 signature. The overall ~374-aa length and domain architecture are typical of 2OG/Fe(II) oxygenases. Transferable elimination of the other options: (C) tungstopterin is restricted to anaerobic enzymes in thermophilic archaea/bacteria (e.g., formate dehydrogenase, aldehyde ferredoxin oxidoreductase) and is implausible in an aerobic filamentous fungus; (A) FAD requires a Rossmann-fold GxGxxG motif, which is absent from this sequence; (B) pantetheine 4'-phosphate is the prosthetic group of acyl-carrier/acyltransferase domains (ACP/PCP) in fatty acid or polyketide synthases, and no such domain architecture is present. Thus, family-level recognition of the HxD/E...H triad pattern plus elimination of cofactor classes incompatible with the sequence and organism context provides a concrete, transferable inference favoring Fe(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HxD/E...H facial triad is a textbook-level, highly transferable feature shared across hundreds of characterized 2OG/Fe(II) oxygenases. A knowledgeable model can recognize the HESC and downstream His pattern, apply the well-established family-level metal-binding logic, and eliminate FAD (no Rossmann fold), pantetheine 4'-phosphate (no ACP/PCP domain), and tungstopterin (anaerobic/archaeal cofactor incompatible with a fungal sequence) using general biochemistry and organism-level biology. This constitutes a credible transferable inference, not memorization of this specific protein's record."
  },
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C4, H2) identifies the protein as '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.-. The cofactor comment (C5, H5) explicitly states Fe(2+) with evidence code ECO:0000255 (PROSITE-ProRule PRU00805, family-based inference). Additionally, reference 2 (C7, H4, PubMed 38578094, JACS 2024) provides experimental evidence (ECO:0000269) that the PPZ cluster encodes 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes.' The expected answer D (Fe(2+)) is directly supported by both computational family annotation and experimental characterization."
  },
  "important_caveats": [
    "The PROSITE-ProRule PRU00805 annotation is a family-level computational inference (ECO:0000255), not direct experimental measurement of Fe(2+) binding to this exact protein. However, the 2024 JACS reference (PubMed 38578094) provides experimental functional evidence for Fe(II) dependence in the PPZ cluster enzymes.",
    "The HxD/E...H triad in raw sequence is degenerate and variable in spacing; recognition from sequence alone is probabilistic rather than deterministic, though the combination of motif, length, and elimination of alternatives strengthens the inference.",
    "The reviewer-only evidence confirms the sequence matches UniProt A0A455ZKR7 (Metarhizium majus ppzC), but this accession and organism identity were not provided to the evaluated model. The transferable argument relies only on sequence features and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct cofactor classes (flavin, acyl-carrier prosthetic group, anaerobic molybdenum/tungsten cofactor, divalent metal ion) that are mutually exclusive and distinguishable by sequence features and biological context. No two options are defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C4, H2) identifies the protein as '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.-. The cofactor comment (C5, H5) explicitly states Fe(2+) with evidence code ECO:0000255 (PROSITE-ProRule PRU00805, family-based inference). Additionally, reference 2 (C7, H4, PubMed 38578094, JACS 2024) provides experimental evidence (ECO:0000269) that the PPZ cluster encodes 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes.' The expected answer D (Fe(2+)) is directly supported by both computational family annotation and experimental characterization.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2-oxoglutarate/Fe(II)-dependent oxygenase superfamily is one of the most extensively characterized enzyme families in biology, with hundreds of experimentally validated members (prolyl hydroxylases, AlkB DNA repair enzymes, taurine dioxygenase, etc.). Its hallmark is the 2-His-1-carboxylate facial triad (HxD/E...H) that coordinates a single Fe(II) ion. In the supplied sequence, the 'HESCQVL' motif (His-Glu pair) and a downstream 'HRAQN' His are recognizable components of this degenerate but well-known triad, consistent with the PROSITE-ProRule PRU00805 signature. The overall ~374-aa length and domain architecture are typical of 2OG/Fe(II) oxygenases. Transferable elimination of the other options: (C) tungstopterin is restricted to anaerobic enzymes in thermophilic archaea/bacteria (e.g., formate dehydrogenase, aldehyde ferredoxin oxidoreductase) and is implausible in an aerobic filamentous fungus; (A) FAD requires a Rossmann-fold GxGxxG motif, which is absent from this sequence; (B) pantetheine 4'-phosphate is the prosthetic group of acyl-carrier/acyltransferase domains (ACP/PCP) in fatty acid or polyketide synthases, and no such domain architecture is present. Thus, family-level recognition of the HxD/E...H triad pattern plus elimination of cofactor classes incompatible with the sequence and organism context provides a concrete, transferable inference favoring Fe(2+).",
    "missing_item_specific_fact": "",
    "reason": "The HxD/E...H facial triad is a textbook-level, highly transferable feature shared across hundreds of characterized 2OG/Fe(II) oxygenases. A knowledgeable model can recognize the HESC and downstream His pattern, apply the well-established family-level metal-binding logic, and eliminate FAD (no Rossmann fold), pantetheine 4'-phosphate (no ACP/PCP domain), and tungstopterin (anaerobic/archaeal cofactor incompatible with a fungal sequence) using general biochemistry and organism-level biology. This constitutes a credible transferable inference, not memorization of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct cofactor classes (flavin, acyl-carrier prosthetic group, anaerobic molybdenum/tungsten cofactor, divalent metal ion) that are mutually exclusive and distinguishable by sequence features and biological context. No two options are defensible for this sequence."
  },
  "important_caveats": [
    "The PROSITE-ProRule PRU00805 annotation is a family-level computational inference (ECO:0000255), not direct experimental measurement of Fe(2+) binding to this exact protein. However, the 2024 JACS reference (PubMed 38578094) provides experimental functional evidence for Fe(II) dependence in the PPZ cluster enzymes.",
    "The HxD/E...H triad in raw sequence is degenerate and variable in spacing; recognition from sequence alone is probabilistic rather than deterministic, though the combination of motif, length, and elimination of alternatives strengthens the inference.",
    "The reviewer-only evidence confirms the sequence matches UniProt A0A455ZKR7 (Metarhizium majus ppzC), but this accession and organism identity were not provided to the evaluated model. The transferable argument relies only on sequence features and general biology."
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
  "benchmark_sequence_length": 374,
  "benchmark_sequence_sha256": "15799a948141cc834792097224072e0866bb99a08601d2dffad614221d57bc06",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 374,
  "current_source_sequence_sha256": "15799a948141cc834792097224072e0866bb99a08601d2dffad614221d57bc06",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZKR7",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "selected_historical_source_sequence_length": 374,
  "selected_historical_source_sequence_sha256": "15799a948141cc834792097224072e0866bb99a08601d2dffad614221d57bc06",
  "selected_historical_version": {
    "accession": "A0A455ZKR7",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZC_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZKR7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2-oxoglutarate-Fe(II) type oxidoreductase ppzC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00805\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Fe(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00805\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Binds 1 Fe(2+) ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Rothchild K.W.\",\"Hagar M.\",\"Berry D.\",\"Ryan K.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38578094\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.4c01419\"}],\"citationType\":\"journal article\",\"firstPage\":\"10263\",\"id\":\"38578094\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"10267\",\"publicationDate\":\"2024\",\"title\":\"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\",\"volume\":\"146\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:16.380201+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   PPZC_METMF              Reviewed;         374 AA.\nAC   A0A455ZKR7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzC {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein C {ECO:0000303|PubMed:30452111};\nGN   Name=ppzC;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzC {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein C {ECO:0000303|PubMed:30452111};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00805};\nCC       Note=Binds 1 Fe(2+) ion per subunit. {ECO:0000255|PROSITE-\nCC       ProRule:PRU00805};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:18.441147+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca",
  "url": "https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
