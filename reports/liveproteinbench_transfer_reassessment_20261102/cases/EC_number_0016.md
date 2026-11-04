# EC_number_0016

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0016.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVAFSSLFLGASIAATALAAPGELPGMHLNKRQTYTQSATGTHDGYYFSFWTDGGPNVRYTNEAGGQYSVTWSGNGNWVGGKGWNPGAARTINYTGTYQPNGNSYLAVYGWTRNPLVEYYVVENFGTYDPSTGAQRLGSINVDGSTYNVYRTRRTNAPSIEGTRSFDQYWSVRVNKRVGGSVDMNAHFNAWRQAGLTLGTHDYQIVATEGYFSSGSARINVGGGSTGGGNNGGGNNGGNPGGNPGGNPGGNPGGNCSPRWGQCGGQGWNGPTCCESGTTCRQQNQWYSQCL

[Multiple Choices]
A. 3.2.1.18
B. 2.7.7.43
C. 3.2.1.8
D. 1.8.1.9
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation reports EC 3.2.1.8 and the reaction as endohydrolysis of beta-D-xylosidic linkages in xylans, citing experimental evidence. This supports choice C, though the primary paper was not independently reviewed here.

Citations as saved: [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the following compact, aromatic-rich catalytic region has motifs characteristic of fungal GH11 xylanases. Recognition of that family from transferable sequence patterns supports an endo-1,4-beta-xylanase assignment, EC 3.2.1.8, distinguishing it from the other offered enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a meaningful family-level inference that distinguishes the xylanase option; identifying the exact database record is not necessary. The inference is probabilistic rather than a substitute for a direct activity assay.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-family inference and the supplied sequence-matched catalytic-activity annotation both support C; no other offered option is comparably supported.


### Important caveats

- The reviewer-only annotation cites experimental evidence, but that evidence was not part of the original model input.
- The family-level sequence inference supports the offered EC choice but does not independently verify substrate specificity experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the following compact, aromatic-rich catalytic region has motifs characteristic of fungal GH11 xylanases. Recognition of that family from transferable sequence patterns supports an endo-1,4-beta-xylanase assignment, EC 3.2.1.8, distinguishing it from the other offered enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a meaningful family-level inference that distinguishes the xylanase option; identifying the exact database record is not necessary. The inference is probabilistic rather than a substitute for a direct activity assay."
  },
  "case_id": "EC_number_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports EC 3.2.1.8 and the reaction as endohydrolysis of beta-D-xylosidic linkages in xylans, citing experimental evidence. This supports choice C, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation cites experimental evidence, but that evidence was not part of the original model input.",
    "The family-level sequence inference supports the offered EC choice but does not independently verify substrate specificity experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference and the supplied sequence-matched catalytic-activity annotation both support C; no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports EC 3.2.1.8 and the reaction as endohydrolysis of beta-D-xylosidic linkages in xylans, citing experimental evidence. This supports choice C, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the following compact, aromatic-rich catalytic region has motifs characteristic of fungal GH11 xylanases. Recognition of that family from transferable sequence patterns supports an endo-1,4-beta-xylanase assignment, EC 3.2.1.8, distinguishing it from the other offered enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a meaningful family-level inference that distinguishes the xylanase option; identifying the exact database record is not necessary. The inference is probabilistic rather than a substitute for a direct activity assay."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference and the supplied sequence-matched catalytic-activity annotation both support C; no other offered option is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotation cites experimental evidence, but that evidence was not part of the original model input.",
    "The family-level sequence inference supports the offered EC choice but does not independently verify substrate specificity experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0B5JC15 (XY11B_HUMIN, Endo-1,4-beta-xylanase 11B from Humicola insolens) carries EC 3.2.1.8 with experimental evidence (ECO:0000269, PubMed:25629035). The catalytic activity is described as endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans. The sequence match is confirmed (SHA256 identical, 291 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits multiple well-known hallmarks of fungal GH11 endo-1,4-beta-xylanases learned from other xylanases (e.g., Trichoderma, Aspergillus, Bacillus GH11 members): (1) an N-terminal hydrophobic signal peptide (MVAFSSLFLGASIAATALAAP) indicating a secreted enzyme; (2) a catalytic domain consistent with the beta-jelly roll fold of GH11 (rich in beta-strand-forming residues, conserved catalytic Glu pair visible in the 'EYYVVENFG' motif), which is structurally distinct from the (alpha/beta)-TIM barrel of GH13 alpha-amylases (option A); (3) a C-terminal linker containing multiple GGNPG repeats, a signature feature of fungal xylanases used for flexible tethering of accessory domains; (4) a C-terminal cysteine-rich region (CSPRWGQCGGQGWNGPTCCESGTTCRQQNQWYSQCL) characteristic of fungal xylanase linkers. None of these features appear in poly(ADP-ribose) polymerases (option B, a transferase) or thiosulfate reductases (option D, an oxidoreductase). The GH11 vs GH13 distinction is well-established from family-level knowledge: GH13 alpha-amylases have conserved 'NEFG' and 'DNE' motifs in a TIM barrel, absent here.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on protein families can recognize the GGNPG linker repeats, Cys-rich C-terminal tail, signal peptide, and beta-jelly-roll catalytic domain architecture as a composite fingerprint of fungal GH11 xylanases. These are transferable features shared across many xylanases, not unique to this exact protein. The alternatives are easily excluded: B and D are entirely different enzyme classes (transferase, oxidoreductase) with no sequence resemblance; A (GH13 alpha-amylase) has a fundamentally different fold and conserved motifs absent from this sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GGNPG linker repeats and Cys-rich C-terminal region are highly specific to fungal xylanases and do not appear in alpha-amylases, PARPs, or thiosulfate reductases. The catalytic domain fold is clearly GH11-like, not GH13. No alternative option is defensible.


### Important caveats

- The EC assignment in UniProt is backed by experimental evidence (ECO:0000269, PubMed:25629035), not merely computational annotation.
- The GGNPG linker and Cys-rich tail are strong family-level indicators but individual xylanase variants may lack them; their presence here strongly supports the GH11 xylanase assignment.
- The reviewer-only evidence confirms the exact protein identity (Humicola insolens Xyn11B) but this was not available to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits multiple well-known hallmarks of fungal GH11 endo-1,4-beta-xylanases learned from other xylanases (e.g., Trichoderma, Aspergillus, Bacillus GH11 members): (1) an N-terminal hydrophobic signal peptide (MVAFSSLFLGASIAATALAAP) indicating a secreted enzyme; (2) a catalytic domain consistent with the beta-jelly roll fold of GH11 (rich in beta-strand-forming residues, conserved catalytic Glu pair visible in the 'EYYVVENFG' motif), which is structurally distinct from the (alpha/beta)-TIM barrel of GH13 alpha-amylases (option A); (3) a C-terminal linker containing multiple GGNPG repeats, a signature feature of fungal xylanases used for flexible tethering of accessory domains; (4) a C-terminal cysteine-rich region (CSPRWGQCGGQGWNGPTCCESGTTCRQQNQWYSQCL) characteristic of fungal xylanase linkers. None of these features appear in poly(ADP-ribose) polymerases (option B, a transferase) or thiosulfate reductases (option D, an oxidoreductase). The GH11 vs GH13 distinction is well-established from family-level knowledge: GH13 alpha-amylases have conserved 'NEFG' and 'DNE' motifs in a TIM barrel, absent here.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein families can recognize the GGNPG linker repeats, Cys-rich C-terminal tail, signal peptide, and beta-jelly-roll catalytic domain architecture as a composite fingerprint of fungal GH11 xylanases. These are transferable features shared across many xylanases, not unique to this exact protein. The alternatives are easily excluded: B and D are entirely different enzyme classes (transferase, oxidoreductase) with no sequence resemblance; A (GH13 alpha-amylase) has a fundamentally different fold and conserved motifs absent from this sequence."
  },
  "case_id": "EC_number_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0B5JC15 (XY11B_HUMIN, Endo-1,4-beta-xylanase 11B from Humicola insolens) carries EC 3.2.1.8 with experimental evidence (ECO:0000269, PubMed:25629035). The catalytic activity is described as endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans. The sequence match is confirmed (SHA256 identical, 291 aa)."
  },
  "important_caveats": [
    "The EC assignment in UniProt is backed by experimental evidence (ECO:0000269, PubMed:25629035), not merely computational annotation.",
    "The GGNPG linker and Cys-rich tail are strong family-level indicators but individual xylanase variants may lack them; their presence here strongly supports the GH11 xylanase assignment.",
    "The reviewer-only evidence confirms the exact protein identity (Humicola insolens Xyn11B) but this was not available to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GGNPG linker repeats and Cys-rich C-terminal region are highly specific to fungal xylanases and do not appear in alpha-amylases, PARPs, or thiosulfate reductases. The catalytic domain fold is clearly GH11-like, not GH13. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0B5JC15 (XY11B_HUMIN, Endo-1,4-beta-xylanase 11B from Humicola insolens) carries EC 3.2.1.8 with experimental evidence (ECO:0000269, PubMed:25629035). The catalytic activity is described as endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans. The sequence match is confirmed (SHA256 identical, 291 aa).",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits multiple well-known hallmarks of fungal GH11 endo-1,4-beta-xylanases learned from other xylanases (e.g., Trichoderma, Aspergillus, Bacillus GH11 members): (1) an N-terminal hydrophobic signal peptide (MVAFSSLFLGASIAATALAAP) indicating a secreted enzyme; (2) a catalytic domain consistent with the beta-jelly roll fold of GH11 (rich in beta-strand-forming residues, conserved catalytic Glu pair visible in the 'EYYVVENFG' motif), which is structurally distinct from the (alpha/beta)-TIM barrel of GH13 alpha-amylases (option A); (3) a C-terminal linker containing multiple GGNPG repeats, a signature feature of fungal xylanases used for flexible tethering of accessory domains; (4) a C-terminal cysteine-rich region (CSPRWGQCGGQGWNGPTCCESGTTCRQQNQWYSQCL) characteristic of fungal xylanase linkers. None of these features appear in poly(ADP-ribose) polymerases (option B, a transferase) or thiosulfate reductases (option D, an oxidoreductase). The GH11 vs GH13 distinction is well-established from family-level knowledge: GH13 alpha-amylases have conserved 'NEFG' and 'DNE' motifs in a TIM barrel, absent here.",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein families can recognize the GGNPG linker repeats, Cys-rich C-terminal tail, signal peptide, and beta-jelly-roll catalytic domain architecture as a composite fingerprint of fungal GH11 xylanases. These are transferable features shared across many xylanases, not unique to this exact protein. The alternatives are easily excluded: B and D are entirely different enzyme classes (transferase, oxidoreductase) with no sequence resemblance; A (GH13 alpha-amylase) has a fundamentally different fold and conserved motifs absent from this sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GGNPG linker repeats and Cys-rich C-terminal region are highly specific to fungal xylanases and do not appear in alpha-amylases, PARPs, or thiosulfate reductases. The catalytic domain fold is clearly GH11-like, not GH13. No alternative option is defensible."
  },
  "important_caveats": [
    "The EC assignment in UniProt is backed by experimental evidence (ECO:0000269, PubMed:25629035), not merely computational annotation.",
    "The GGNPG linker and Cys-rich tail are strong family-level indicators but individual xylanase variants may lack them; their presence here strongly supports the GH11 xylanase assignment.",
    "The reviewer-only evidence confirms the exact protein identity (Humicola insolens Xyn11B) but this was not available to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge."
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
  "benchmark_sequence_sha256": "cd3a3423a03c858541b956741c23114bb67ae727771dfd47823e3d5c8afd1852",
  "current_entry_audit": {
    "entryVersion": 35,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-04-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 291,
  "current_source_sequence_sha256": "cd3a3423a03c858541b956741c23114bb67ae727771dfd47823e3d5c8afd1852",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 34,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0B5JC15",
  "selected_historical_entry_version": 34,
  "selected_historical_record_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "selected_historical_source_sequence_length": 291,
  "selected_historical_source_sequence_sha256": "cd3a3423a03c858541b956741c23114bb67ae727771dfd47823e3d5c8afd1852",
  "selected_historical_version": {
    "accession": "A0A0B5JC15",
    "database": "Swiss-Prot",
    "entryVersion": 34,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "XY11B_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0B5JC15\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":35,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-04-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase 11B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase 11B\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"value\":\"Xylanase 11B\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi P.\",\"Du Y.\",\"Yang H.\",\"Huang H.\",\"Zhang X.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25629035\"},{\"database\":\"DOI\",\"id\":\"10.1155/2015/149504\"}],\"citationType\":\"journal article\",\"firstPage\":\"149504\",\"id\":\"25629035\",\"journal\":\"Biomed. Res. Int.\",\"lastPage\":\"149504\",\"publicationDate\":\"2015\",\"title\":\"Molecular characterization of a new alkaline-tolerant xylanase from Humicola insolens Y1.\",\"volume\":\"2015\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"DOMAIN\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H1",
  "excerpt": "ID   XY11B_HUMIN             Reviewed;         291 AA.\nAC   A0A0B5JC15;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-APR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 34.\nDE   RecName: Full=Endo-1,4-beta-xylanase 11B {ECO:0000303|PubMed:25629035};\nDE            Short=Xylanase 11B {ECO:0000303|PubMed:25629035};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:25629035};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11B {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=Xyn11B {ECO:0000303|PubMed:25629035};\nGN   Synonyms=Xyl2 {ECO:0000303|PubMed:8190078};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase 11B {ECO:0000303|PubMed:25629035};\nDE            Short=Xylanase 11B {ECO:0000303|PubMed:25629035};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:25629035};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11B {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   DOMAIN, AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=25629035; DOI=10.1155/2015/149504;\nRA   Shi P., Du Y., Yang H., Huang H., Zhang X., Wang Y., Yao B.;\nRT   \"Molecular characterization of a new alkaline-tolerant xylanase from\nRT   Humicola insolens Y1.\";\nRL   Biomed. Res. Int. 2015:149504-149504(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION.\nRX   PubMed=8190078; DOI=10.1007/bf00301060;\nRA   Dalboege H., Hansen H.P.H.;\nRT   \"A novel method for efficient expression cloning of fungal enzyme genes.\";\nRL   Mol. Gen. Genet. 243:253-260(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:25629035};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
