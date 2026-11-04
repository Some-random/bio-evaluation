# cofactor_0092

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0092.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. Mn(2+)
B. Fe cation
C. Fe(2+)
D. [4Fe-4S] cluster
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

> The sequence-matched UniProt record reports a &#91;4Fe-4S&#93; cluster per subunit, with evidence from cited studies; the cited crystallographic work also describes the protein in complex with an iron-sulfur cluster. This supports D as a cofactor, though the protein also binds tungstopterin, which is not among the choices.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long oxidoreductase-like sequence and its cysteine-containing region are consistent with an iron-sulfur-containing oxidoreductase family. Transferable knowledge about such enzymes supports a coordinated iron-sulfur cluster rather than manganese or an isolated iron ion; among the offered choices, the cluster-level answer is D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence patterns and the common use of iron-sulfur clusters in oxidoreductases provide a meaningful basis to distinguish D from the offered alternatives without recalling this exact protein's record. This is a probabilistic inference, not a sequence-only proof of the precise cluster.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered choice describing an iron-sulfur cluster. The protein has another cofactor, tungstopterin, but it is not an alternative in this question.


### Important caveats

- The source evidence supports the cluster as a cofactor but does not establish that it is the protein's only cofactor.
- The reviewer-only source identifies the exact enzyme; that identity was not part of the original input and is not relied on as the basis for answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long oxidoreductase-like sequence and its cysteine-containing region are consistent with an iron-sulfur-containing oxidoreductase family. Transferable knowledge about such enzymes supports a coordinated iron-sulfur cluster rather than manganese or an isolated iron ion; among the offered choices, the cluster-level answer is D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence patterns and the common use of iron-sulfur clusters in oxidoreductases provide a meaningful basis to distinguish D from the offered alternatives without recalling this exact protein's record. This is a probabilistic inference, not a sequence-only proof of the precise cluster."
  },
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports a [4Fe-4S] cluster per subunit, with evidence from cited studies; the cited crystallographic work also describes the protein in complex with an iron-sulfur cluster. This supports D as a cofactor, though the protein also binds tungstopterin, which is not among the choices."
  },
  "important_caveats": [
    "The source evidence supports the cluster as a cofactor but does not establish that it is the protein's only cofactor.",
    "The reviewer-only source identifies the exact enzyme; that identity was not part of the original input and is not relied on as the basis for answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice describing an iron-sulfur cluster. The protein has another cofactor, tungstopterin, but it is not an alternative in this question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports a [4Fe-4S] cluster per subunit, with evidence from cited studies; the cited crystallographic work also describes the protein in complex with an iron-sulfur cluster. This supports D as a cofactor, though the protein also binds tungstopterin, which is not among the choices.",
    "evidence_ids": ["C5", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long oxidoreductase-like sequence and its cysteine-containing region are consistent with an iron-sulfur-containing oxidoreductase family. Transferable knowledge about such enzymes supports a coordinated iron-sulfur cluster rather than manganese or an isolated iron ion; among the offered choices, the cluster-level answer is D.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence patterns and the common use of iron-sulfur clusters in oxidoreductases provide a meaningful basis to distinguish D from the offered alternatives without recalling this exact protein's record. This is a probabilistic inference, not a sequence-only proof of the precise cluster."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice describing an iron-sulfur cluster. The protein has another cofactor, tungstopterin, but it is not an alternative in this question."
  },
  "important_caveats": [
    "The source evidence supports the cluster as a cofactor but does not establish that it is the protein's only cofactor.",
    "The reviewer-only source identifies the exact enzyme; that identity was not part of the original input and is not relied on as the basis for answerability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (E7FHH1) annotates a &#91;4Fe-4S&#93; cluster as a cofactor with direct experimental evidence (ECO:0000269 from PubMed:16199576 and PubMed:36269456), confirmed by X-ray crystallography at 1.94 Å (PDB: 6X1O, 6X6U). The cluster has three cysteine ligands and one aspartic acid ligand. The protein also binds tungstopterin, but that is not among the offered choices. Among the four options, &#91;4Fe-4S&#93; cluster is the correct cofactor.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GAGGYSVG' motif, a hallmark of the DMSO reductase family of tungsten/molybdenum oxidoreductases. This family (including aldehyde oxidoreductase AOR, xanthine oxidoreductase, and DMSO reductase) is well-known to employ a &#91;4Fe-4S&#93; cluster as its electron-transfer cofactor, coordinated typically by cysteine residues. The sequence also shows a 'GCPVNCMKISYLRYG' motif with closely spaced cysteines consistent with &#91;4Fe-4S&#93; ligation. Family-level knowledge from many characterized members (e.g., Pyrococcus AOR, Desulfovibrio xanthine oxidoreductase) establishes that &#91;4Fe-4S&#93; clusters—not simple Fe²⁺/Fe³⁺ ions or Mn²⁺—are the standard electron-transfer cofactors in this enzyme superfamily. The distinction between a &#91;4Fe-4S&#93; cluster (a specific four-iron, four-sulfur molecular assembly) and free iron cations (options B, C) is a well-established biochemical distinction that family recognition resolves.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the GAGGYSVG motif as diagnostic of the DMSO reductase family, combined with the well-documented family-level fact that these tungsten/molybdenum oxidoreductases use &#91;4Fe-4S&#93; clusters for electron transfer, provides a concrete transferable inference that distinguishes option D from options A (Mn²⁺), B (Fe cation), and C (Fe²⁺). The cysteine-rich motifs in the sequence further corroborate &#91;4Fe-4S&#93; coordination rather than simple metal-ion binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (Fe cation) and C (Fe(2+)) are both simple iron species and are clearly distinguishable from the &#91;4Fe-4S&#93; cluster (a defined molecular assembly). Option A (Mn²⁺) is not a cofactor of the DMSO reductase family. Tungstopterin (the other cofactor of this enzyme) is not offered, so no ambiguity arises from the available choices. The &#91;4Fe-4S&#93; cluster is unambiguously the correct answer among the four options.


### Important caveats

- The protein also binds tungstopterin (a tungsten cofactor), which is arguably more directly 'required for catalytic activity' than the &#91;4Fe-4S&#93; cluster (which serves electron transfer). However, tungstopterin is not among the offered choices, so this does not create ambiguity within the question as posed.
- The &#91;4Fe-4S&#93; cluster annotation is supported by direct experimental evidence (X-ray crystallography at 1.94 Å), not merely computational prediction.
- The question wording 'specific cofactor required for catalytic activity' could be interpreted to favor tungstopterin over the &#91;4Fe-4S&#93; cluster, but since tungstopterin is absent from the options, D is the only valid choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GAGGYSVG' motif, a hallmark of the DMSO reductase family of tungsten/molybdenum oxidoreductases. This family (including aldehyde oxidoreductase AOR, xanthine oxidoreductase, and DMSO reductase) is well-known to employ a [4Fe-4S] cluster as its electron-transfer cofactor, coordinated typically by cysteine residues. The sequence also shows a 'GCPVNCMKISYLRYG' motif with closely spaced cysteines consistent with [4Fe-4S] ligation. Family-level knowledge from many characterized members (e.g., Pyrococcus AOR, Desulfovibrio xanthine oxidoreductase) establishes that [4Fe-4S] clusters—not simple Fe²⁺/Fe³⁺ ions or Mn²⁺—are the standard electron-transfer cofactors in this enzyme superfamily. The distinction between a [4Fe-4S] cluster (a specific four-iron, four-sulfur molecular assembly) and free iron cations (options B, C) is a well-established biochemical distinction that family recognition resolves.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the GAGGYSVG motif as diagnostic of the DMSO reductase family, combined with the well-documented family-level fact that these tungsten/molybdenum oxidoreductases use [4Fe-4S] clusters for electron transfer, provides a concrete transferable inference that distinguishes option D from options A (Mn²⁺), B (Fe cation), and C (Fe²⁺). The cysteine-rich motifs in the sequence further corroborate [4Fe-4S] coordination rather than simple metal-ion binding."
  },
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (E7FHH1) annotates a [4Fe-4S] cluster as a cofactor with direct experimental evidence (ECO:0000269 from PubMed:16199576 and PubMed:36269456), confirmed by X-ray crystallography at 1.94 Å (PDB: 6X1O, 6X6U). The cluster has three cysteine ligands and one aspartic acid ligand. The protein also binds tungstopterin, but that is not among the offered choices. Among the four options, [4Fe-4S] cluster is the correct cofactor."
  },
  "important_caveats": [
    "The protein also binds tungstopterin (a tungsten cofactor), which is arguably more directly 'required for catalytic activity' than the [4Fe-4S] cluster (which serves electron transfer). However, tungstopterin is not among the offered choices, so this does not create ambiguity within the question as posed.",
    "The [4Fe-4S] cluster annotation is supported by direct experimental evidence (X-ray crystallography at 1.94 Å), not merely computational prediction.",
    "The question wording 'specific cofactor required for catalytic activity' could be interpreted to favor tungstopterin over the [4Fe-4S] cluster, but since tungstopterin is absent from the options, D is the only valid choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (Fe cation) and C (Fe(2+)) are both simple iron species and are clearly distinguishable from the [4Fe-4S] cluster (a defined molecular assembly). Option A (Mn²⁺) is not a cofactor of the DMSO reductase family. Tungstopterin (the other cofactor of this enzyme) is not offered, so no ambiguity arises from the available choices. The [4Fe-4S] cluster is unambiguously the correct answer among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (E7FHH1) annotates a [4Fe-4S] cluster as a cofactor with direct experimental evidence (ECO:0000269 from PubMed:16199576 and PubMed:36269456), confirmed by X-ray crystallography at 1.94 Å (PDB: 6X1O, 6X6U). The cluster has three cysteine ligands and one aspartic acid ligand. The protein also binds tungstopterin, but that is not among the offered choices. Among the four options, [4Fe-4S] cluster is the correct cofactor.",
    "evidence_ids": ["C5", "C8", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GAGGYSVG' motif, a hallmark of the DMSO reductase family of tungsten/molybdenum oxidoreductases. This family (including aldehyde oxidoreductase AOR, xanthine oxidoreductase, and DMSO reductase) is well-known to employ a [4Fe-4S] cluster as its electron-transfer cofactor, coordinated typically by cysteine residues. The sequence also shows a 'GCPVNCMKISYLRYG' motif with closely spaced cysteines consistent with [4Fe-4S] ligation. Family-level knowledge from many characterized members (e.g., Pyrococcus AOR, Desulfovibrio xanthine oxidoreductase) establishes that [4Fe-4S] clusters—not simple Fe²⁺/Fe³⁺ ions or Mn²⁺—are the standard electron-transfer cofactors in this enzyme superfamily. The distinction between a [4Fe-4S] cluster (a specific four-iron, four-sulfur molecular assembly) and free iron cations (options B, C) is a well-established biochemical distinction that family recognition resolves.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the GAGGYSVG motif as diagnostic of the DMSO reductase family, combined with the well-documented family-level fact that these tungsten/molybdenum oxidoreductases use [4Fe-4S] clusters for electron transfer, provides a concrete transferable inference that distinguishes option D from options A (Mn²⁺), B (Fe cation), and C (Fe²⁺). The cysteine-rich motifs in the sequence further corroborate [4Fe-4S] coordination rather than simple metal-ion binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (Fe cation) and C (Fe(2+)) are both simple iron species and are clearly distinguishable from the [4Fe-4S] cluster (a defined molecular assembly). Option A (Mn²⁺) is not a cofactor of the DMSO reductase family. Tungstopterin (the other cofactor of this enzyme) is not offered, so no ambiguity arises from the available choices. The [4Fe-4S] cluster is unambiguously the correct answer among the four options."
  },
  "important_caveats": [
    "The protein also binds tungstopterin (a tungsten cofactor), which is arguably more directly 'required for catalytic activity' than the [4Fe-4S] cluster (which serves electron transfer). However, tungstopterin is not among the offered choices, so this does not create ambiguity within the question as posed.",
    "The [4Fe-4S] cluster annotation is supported by direct experimental evidence (X-ray crystallography at 1.94 Å), not merely computational prediction.",
    "The question wording 'specific cofactor required for catalytic activity' could be interpreted to favor tungstopterin over the [4Fe-4S] cluster, but since tungstopterin is absent from the options, D is the only valid choice."
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
  "benchmark_sequence_length": 624,
  "benchmark_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_entry_audit": {
    "entryVersion": 61,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 624,
  "current_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E7FHH1",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "selected_historical_source_sequence_length": 624,
  "selected_historical_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "selected_historical_version": {
    "accession": "E7FHH1",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASOR_PYRFU",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E7FHH1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":61,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Aliphatic sulfonate ferredoxin oxidoreductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"ASOR\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"Tungsten-containing aldehyde oxidoreductase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"WOR5\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5 large subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5-L\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aliphatic sulfonate oxidoreductase, WOR-like subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"[4Fe-4S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 [4Fe-4S] cluster per subunit (PubMed:16199576, PubMed:36269456). The [4Fe-4S] cluster has three cysteine ligands and one aspartic acid ligand (PubMed:36269456).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30402\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"tungstopterin\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 tungstopterin cofactor per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/8",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Bevers L.E.\",\"Bol E.\",\"Hagedoorn P.L.\",\"Hagen W.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16199576\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.20.7056-7061.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"7056\",\"id\":\"16199576\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"7061\",\"publicationDate\":\"2005\",\"title\":\"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus furiosus with a broad substrate specificity.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 43587 / DSM 3638 / JCM 8422 / Vc1\"}],\"referenceNumber\":3,\"referencePositions\":[\"PROTEIN SEQUENCE OF 1-21\",\"FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Mathew L.G.\",\"Haja D.K.\",\"Pritchett C.\",\"McCormick W.\",\"Zeineddine R.\",\"Fontenot L.S.\",\"Rivera M.E.\",\"Glushka J.\",\"Adams M.W.W.\",\"Lanzilotta W.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36269456\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00775-022-01965-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"747\",\"id\":\"36269456\",\"journal\":\"J. Biol. Inorg. Chem.\",\"lastPage\":\"758\",\"publicationDate\":\"2022\",\"title\":\"An unprecedented function for a tungsten-containing oxidoreductase.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X1O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X6U\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   ASOR_PYRFU              Reviewed;         624 AA.\nAC   E7FHH1; A0A5C0XQU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\nGN   Name=wor5 {ECO:0000303|PubMed:16199576};\nGN   OrderedLocusNames=PF1480 {ECO:0000312|EMBL:AAL81604.1};\nGN   ORFNames=PFDSM3638_07420 {ECO:0000312|EMBL:QEK79109.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   PROTEIN SEQUENCE OF 1-21, FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 43587 / DSM 3638 / JCM 8422 / Vc1;\nRX   PubMed=16199576; DOI=10.1128/jb.187.20.7056-7061.2005;\nRA   Bevers L.E., Bol E., Hagedoorn P.L., Hagen W.R.;\nRT   \"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus\nRT   furiosus with a broad substrate specificity.\";\nRL   J. Bacteriol. 187:7056-7061(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}\nRP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR\nRP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.\nRC   STRAIN=COM1;\nRX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;\nRA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,\nRA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;\nRT   \"An unprecedented function for a tungsten-containing oxidoreductase.\";\nRL   J. Biol. Inorg. Chem. 27:747-758(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;\nCC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nCC       Note=Binds 1 [4Fe-4S] cluster per subunit (PubMed:16199576,\nCC       PubMed:36269456). The [4Fe-4S] cluster has three cysteine ligands and\nCC       one aspartic acid ligand (PubMed:36269456).\nCC       {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=tungstopterin; Xref=ChEBI:CHEBI:30402;\nCC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nCC       Note=Binds 1 tungstopterin cofactor per subunit.\nCC       {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
