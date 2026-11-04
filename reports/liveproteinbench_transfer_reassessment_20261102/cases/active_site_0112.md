# active_site_0112

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0112.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 511 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. Position 2059 (For beta-ketoacyl synthase 2 activity)
B. Position 251 (Proton acceptor)
C. Position 511 (Proton acceptor)
D. Position 215 (Charge relay system)
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

> The sequence-matched UniProt annotation identifies residue 511 as a proton acceptor; the historical record also contains this annotation. Its evidence is transfer by similarity from another UniProt protein, so it supports the key as a homology-based annotation, not as direct experimental verification on this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the Fe-S-dependent dihydroxy-acid dehydratase/IlvD family. Transferable family knowledge and alignment to related enzymes can locate the conserved catalytic proton-accepting residue in the homologous C-terminal region, supporting position 511 rather than the other offered proton-acceptor position, 251. Position 2059 is outside this 598-residue sequence, and the charge-relay option does not fit this family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Selecting the exact coordinate requires family recognition and residue mapping, but those can be inferred from transferable knowledge of related dehydratases; the task is not necessarily dependent on recalling this protein's own database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although two options describe a proton acceptor, they specify different positions; the family-level residue mapping favors position 511.


### Important caveats

- The supplied evidence supports a similarity-transferred annotation, not direct experimental confirmation for this sequence.
- The reviewer-only source identification and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the Fe-S-dependent dihydroxy-acid dehydratase/IlvD family. Transferable family knowledge and alignment to related enzymes can locate the conserved catalytic proton-accepting residue in the homologous C-terminal region, supporting position 511 rather than the other offered proton-acceptor position, 251. Position 2059 is outside this 598-residue sequence, and the charge-relay option does not fit this family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Selecting the exact coordinate requires family recognition and residue mapping, but those can be inferred from transferable knowledge of related dehydratases; the task is not necessarily dependent on recalling this protein's own database record."
  },
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 511 as a proton acceptor; the historical record also contains this annotation. Its evidence is transfer by similarity from another UniProt protein, so it supports the key as a homology-based annotation, not as direct experimental verification on this exact protein."
  },
  "important_caveats": [
    "The supplied evidence supports a similarity-transferred annotation, not direct experimental confirmation for this sequence.",
    "The reviewer-only source identification and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although two options describe a proton acceptor, they specify different positions; the family-level residue mapping favors position 511."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 511 as a proton acceptor; the historical record also contains this annotation. Its evidence is transfer by similarity from another UniProt protein, so it supports the key as a homology-based annotation, not as direct experimental verification on this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the Fe-S-dependent dihydroxy-acid dehydratase/IlvD family. Transferable family knowledge and alignment to related enzymes can locate the conserved catalytic proton-accepting residue in the homologous C-terminal region, supporting position 511 rather than the other offered proton-acceptor position, 251. Position 2059 is outside this 598-residue sequence, and the charge-relay option does not fit this family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "Selecting the exact coordinate requires family recognition and residue mapping, but those can be inferred from transferable knowledge of related dehydratases; the task is not necessarily dependent on recalling this protein's own database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although two options describe a proton acceptor, they specify different positions; the family-level residue mapping favors position 511."
  },
  "important_caveats": [
    "The supplied evidence supports a similarity-transferred annotation, not direct experimental confirmation for this sequence.",
    "The reviewer-only source identification and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Saved visible final text:** empty string (`""`).

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 598,
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 598,
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG9",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_length": 598,
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":511},\"start\":{\"modifier\":\"EXACT\",\"value\":511}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:190135\",\"name\":\"[2Fe-2S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":86},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":118}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:190135\",\"name\":\"[2Fe-2S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":159}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":160},\"start\":{\"modifier\":\"EXACT\",\"value\":160}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:190135\",\"name\":\"[2Fe-2S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":232},\"start\":{\"modifier\":\"EXACT\",\"value\":232}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":485},\"start\":{\"modifier\":\"EXACT\",\"value\":485}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        511\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 155-157",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         86\nFT                   /ligand=\"[2Fe-2S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:190135\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 158-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         118\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         159\nFT                   /ligand=\"[2Fe-2S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:190135\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         160\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 170-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         232\nFT                   /ligand=\"[2Fe-2S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:190135\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 174-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         485\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-181",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
