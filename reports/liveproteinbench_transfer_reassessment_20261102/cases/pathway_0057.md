# pathway_0057

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0057.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. Alkaloid biosynthesis
B. protein glycosylation. .
C. Pyrimidine metabolism
D. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
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

> The sequence matches the protein in the supplied source evidence, whose pathway annotation assigns it to alkaloid and ajmaline biosynthesis with ECO:0000269 evidence. This supports choice A, though the underlying publication was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's specific substrate/product or functional-family assignment linking its reaction to alkaloid biosynthesis.


**Reason**

> The sequence has features consistent with an enzyme, but no clear feature in the input uniquely identifies an alkaloid-biosynthesis enzyme or distinguishes that pathway from the offered metabolic alternatives. A generic enzyme-fold or cofactor-binding inference would not establish the pathway; the specific functional assignment is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices name distinct pathways, and the reviewer evidence supports A; no second option is supported by the supplied evidence.


### Important caveats

- The pathway evidence is a curated annotation citing experimental evidence, not an independent review of the experiment.
- The target-specific annotation and identity were reviewer-only and do not count as information available in the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific substrate/product or functional-family assignment linking its reaction to alkaloid biosynthesis.",
    "reason": "The sequence has features consistent with an enzyme, but no clear feature in the input uniquely identifies an alkaloid-biosynthesis enzyme or distinguishes that pathway from the offered metabolic alternatives. A generic enzyme-fold or cofactor-binding inference would not establish the pathway; the specific functional assignment is needed."
  },
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein in the supplied source evidence, whose pathway annotation assigns it to alkaloid and ajmaline biosynthesis with ECO:0000269 evidence. This supports choice A, though the underlying publication was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway evidence is a curated annotation citing experimental evidence, not an independent review of the experiment.",
    "The target-specific annotation and identity were reviewer-only and do not count as information available in the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathways, and the reviewer evidence supports A; no second option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein in the supplied source evidence, whose pathway annotation assigns it to alkaloid and ajmaline biosynthesis with ECO:0000269 evidence. This supports choice A, though the underlying publication was not independently reviewed here.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's specific substrate/product or functional-family assignment linking its reaction to alkaloid biosynthesis.",
    "reason": "The sequence has features consistent with an enzyme, but no clear feature in the input uniquely identifies an alkaloid-biosynthesis enzyme or distinguishes that pathway from the offered metabolic alternatives. A generic enzyme-fold or cofactor-binding inference would not establish the pathway; the specific functional assignment is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathways, and the reviewer evidence supports A; no second option is supported by the supplied evidence."
  },
  "important_caveats": [
    "The pathway evidence is a curated annotation citing experimental evidence, not an independent review of the experiment.",
    "The target-specific annotation and identity were reviewer-only and do not count as information available in the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina is annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' (C5, ECO:0000269 experimental evidence from PubMed:38212296). The sequence matches the benchmark input exactly. The expected answer 'Alkaloid biosynthesis' is directly supported by the database annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'GGLGS' (around residue ~200) followed by a 'GAPETLFE' catalytic-region signature, identifying the protein as an NADPH-dependent oxidoreductase. This immediately eliminates option B (protein glycosylation), because glycosyltransferases use sugar-nucleotide binding motifs (e.g., DxD/HxD) and lack Rossmann folds. For options C (pyrimidine metabolism) and D (histidine biosynthesis), the principal enzymes are transferases, lyases, or non-Rossmann oxidoreductases (e.g., dihydroorotate dehydrogenase uses FMN, histidinol dehydrogenase is a zinc-dependent dehydrogenase), not NADPH-dependent Rossmann-fold reductases. In contrast, plant alkaloid biosynthesis (e.g., the ajmaline/serpentine pathway) is characterized by multiple NADPH-dependent reductases with Rossmann folds acting on indole/monoterpene intermediates. The 365-aa size and the overall sequence architecture are consistent with plant secondary-metabolism reductases rather than primary-metabolism enzymes. Thus, recognizing the Rossmann fold and the specific catalytic pattern, combined with general knowledge that plant alkaloid pathways heavily employ NADPH-dependent reductases, provides a concrete transferable inference favoring A over B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold motif is a well-known, transferable structural feature identifiable from the raw sequence. Combined with the general biological principle that NADPH-dependent Rossmann-fold reductases are hallmarks of plant secondary (alkaloid) metabolism rather than glycosylation, pyrimidine, or histidine biosynthesis, a knowledgeable model can meaningfully distinguish option A from the other three without recalling this protein's specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann fold clearly excludes glycosylation (B). The specific NADPH-dependent reductase architecture is inconsistent with the enzyme classes of pyrimidine (C) and histidine (D) pathways. Among the four offered choices, alkaloid biosynthesis (A) is the only pathway whose core enzymatic machinery matches the identified fold and cofactor dependence.


### Important caveats

- The Rossmann fold is widespread across many oxidoreductase families; the argument relies on the combination of fold, cofactor specificity, organism context (plant-like sequence), and the limited set of four options to reach a unique answer.
- The UniProt pathway annotation (C5) carries ECO:0000269 (experimental evidence), lending strong support to the key.
- The specific 'GAPETLFE' motif is suggestive of a particular reductase subfamily common in plant terpenoid/alkaloid biosynthesis but is not absolutely exclusive to that pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'GGLGS' (around residue ~200) followed by a 'GAPETLFE' catalytic-region signature, identifying the protein as an NADPH-dependent oxidoreductase. This immediately eliminates option B (protein glycosylation), because glycosyltransferases use sugar-nucleotide binding motifs (e.g., DxD/HxD) and lack Rossmann folds. For options C (pyrimidine metabolism) and D (histidine biosynthesis), the principal enzymes are transferases, lyases, or non-Rossmann oxidoreductases (e.g., dihydroorotate dehydrogenase uses FMN, histidinol dehydrogenase is a zinc-dependent dehydrogenase), not NADPH-dependent Rossmann-fold reductases. In contrast, plant alkaloid biosynthesis (e.g., the ajmaline/serpentine pathway) is characterized by multiple NADPH-dependent reductases with Rossmann folds acting on indole/monoterpene intermediates. The 365-aa size and the overall sequence architecture are consistent with plant secondary-metabolism reductases rather than primary-metabolism enzymes. Thus, recognizing the Rossmann fold and the specific catalytic pattern, combined with general knowledge that plant alkaloid pathways heavily employ NADPH-dependent reductases, provides a concrete transferable inference favoring A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold motif is a well-known, transferable structural feature identifiable from the raw sequence. Combined with the general biological principle that NADPH-dependent Rossmann-fold reductases are hallmarks of plant secondary (alkaloid) metabolism rather than glycosylation, pyrimidine, or histidine biosynthesis, a knowledgeable model can meaningfully distinguish option A from the other three without recalling this protein's specific database entry."
  },
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina is annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' (C5, ECO:0000269 experimental evidence from PubMed:38212296). The sequence matches the benchmark input exactly. The expected answer 'Alkaloid biosynthesis' is directly supported by the database annotation."
  },
  "important_caveats": [
    "The Rossmann fold is widespread across many oxidoreductase families; the argument relies on the combination of fold, cofactor specificity, organism context (plant-like sequence), and the limited set of four options to reach a unique answer.",
    "The UniProt pathway annotation (C5) carries ECO:0000269 (experimental evidence), lending strong support to the key.",
    "The specific 'GAPETLFE' motif is suggestive of a particular reductase subfamily common in plant terpenoid/alkaloid biosynthesis but is not absolutely exclusive to that pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann fold clearly excludes glycosylation (B). The specific NADPH-dependent reductase architecture is inconsistent with the enzyme classes of pyrimidine (C) and histidine (D) pathways. Among the four offered choices, alkaloid biosynthesis (A) is the only pathway whose core enzymatic machinery matches the identified fold and cofactor dependence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina is annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' (C5, ECO:0000269 experimental evidence from PubMed:38212296). The sequence matches the benchmark input exactly. The expected answer 'Alkaloid biosynthesis' is directly supported by the database annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'GGLGS' (around residue ~200) followed by a 'GAPETLFE' catalytic-region signature, identifying the protein as an NADPH-dependent oxidoreductase. This immediately eliminates option B (protein glycosylation), because glycosyltransferases use sugar-nucleotide binding motifs (e.g., DxD/HxD) and lack Rossmann folds. For options C (pyrimidine metabolism) and D (histidine biosynthesis), the principal enzymes are transferases, lyases, or non-Rossmann oxidoreductases (e.g., dihydroorotate dehydrogenase uses FMN, histidinol dehydrogenase is a zinc-dependent dehydrogenase), not NADPH-dependent Rossmann-fold reductases. In contrast, plant alkaloid biosynthesis (e.g., the ajmaline/serpentine pathway) is characterized by multiple NADPH-dependent reductases with Rossmann folds acting on indole/monoterpene intermediates. The 365-aa size and the overall sequence architecture are consistent with plant secondary-metabolism reductases rather than primary-metabolism enzymes. Thus, recognizing the Rossmann fold and the specific catalytic pattern, combined with general knowledge that plant alkaloid pathways heavily employ NADPH-dependent reductases, provides a concrete transferable inference favoring A over B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold motif is a well-known, transferable structural feature identifiable from the raw sequence. Combined with the general biological principle that NADPH-dependent Rossmann-fold reductases are hallmarks of plant secondary (alkaloid) metabolism rather than glycosylation, pyrimidine, or histidine biosynthesis, a knowledgeable model can meaningfully distinguish option A from the other three without recalling this protein's specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann fold clearly excludes glycosylation (B). The specific NADPH-dependent reductase architecture is inconsistent with the enzyme classes of pyrimidine (C) and histidine (D) pathways. Among the four offered choices, alkaloid biosynthesis (A) is the only pathway whose core enzymatic machinery matches the identified fold and cofactor dependence."
  },
  "important_caveats": [
    "The Rossmann fold is widespread across many oxidoreductase families; the argument relies on the combination of fold, cofactor specificity, organism context (plant-like sequence), and the limited set of four options to reach a unique answer.",
    "The UniProt pathway annotation (C5) carries ECO:0000269 (experimental evidence), lending strong support to the key.",
    "The specific 'GAPETLFE' motif is suggestive of a particular reductase subfamily common in plant terpenoid/alkaloid biosynthesis but is not absolutely exclusive to that pathway."
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
  "benchmark_sequence_length": 365,
  "benchmark_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 365,
  "current_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ1",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "selected_historical_source_sequence_length": 365,
  "selected_historical_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "selected_historical_version": {
    "accession": "P0DXJ1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GS_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsGS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61919.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"BIOTECHNOLOGY\",\"TISSUE SPECIFICITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   GS_RAUSE                Reviewed;         365 AA.\nAC   P0DXJ1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\nGN   Name=GS {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61919.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, BIOTECHNOLOGY, TISSUE SPECIFICITY,\nRP   AND PATHWAY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
