# temperature_0020

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0020.txt)

**Task:** `temperature`  
**Expected answer:** **D** — 55-60

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLQDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHIDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. 23-35
B. 49-55
C. 30-43
D. 55-60
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record reports an experimentally supported optimum temperature of 55–60 °C, which matches choice D. This supports the reported enzyme optimum, not necessarily a broader thermal-adaptation or stability range.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The measured temperature optimum for this particular enzyme.


**Reason**

> The input provides a sequence but no organism, enzyme annotation, assay result, or clear family-level clue that meaningfully distinguishes these narrow temperature intervals. Sequence-based stability tendencies are not enough to infer a specific optimum of 55–60 °C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reported 55–60 °C interval matches D; B shares only the 55 °C boundary.


### Important caveats

- The reviewer-only source reports the optimum with experimental evidence linked to a publication, and its sequence matches the supplied sequence.
- An enzyme's assay optimum is not equivalent to its full thermal stability range or a general thermal-adaptation category.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured temperature optimum for this particular enzyme.",
    "reason": "The input provides a sequence but no organism, enzyme annotation, assay result, or clear family-level clue that meaningfully distinguishes these narrow temperature intervals. Sequence-based stability tendencies are not enough to infer a specific optimum of 55–60 °C."
  },
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an experimentally supported optimum temperature of 55–60 °C, which matches choice D. This supports the reported enzyme optimum, not necessarily a broader thermal-adaptation or stability range."
  },
  "important_caveats": [
    "The reviewer-only source reports the optimum with experimental evidence linked to a publication, and its sequence matches the supplied sequence.",
    "An enzyme's assay optimum is not equivalent to its full thermal stability range or a general thermal-adaptation category."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported 55–60 °C interval matches D; B shares only the 55 °C boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an experimentally supported optimum temperature of 55–60 °C, which matches choice D. This supports the reported enzyme optimum, not necessarily a broader thermal-adaptation or stability range.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The measured temperature optimum for this particular enzyme.",
    "reason": "The input provides a sequence but no organism, enzyme annotation, assay result, or clear family-level clue that meaningfully distinguishes these narrow temperature intervals. Sequence-based stability tendencies are not enough to infer a specific optimum of 55–60 °C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported 55–60 °C interval matches D; B shares only the 55 °C boundary."
  },
  "important_caveats": [
    "The reviewer-only source reports the optimum with experimental evidence linked to a publication, and its sequence matches the supplied sequence.",
    "An enzyme's assay optimum is not equivalent to its full thermal stability range or a general thermal-adaptation category."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKM3 (Ipecoside beta-D-glucosidase IpeGLU1 from Carapichea ipecacuanha) explicitly records 'Optimum temperature is 55-60 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:18927081 (Nomura et al., J. Biol. Chem. 2008). The benchmark sequence matches the UniProt sequence exactly (SHA-256 confirmed). The expected answer D (55-60) directly corresponds to this experimentally measured value.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The experimentally measured in vitro optimum temperature of 55-60°C for this specific plant beta-glucosidase (IpeGLU1), reported in PubMed:18927081. This is a counterintuitive value for a plant enzyme that cannot be inferred from sequence features or general family knowledge.


**Reason**

> The protein is recognizably a GH1-family beta-glucosidase from a plant (tropical plant enzyme). General transferable knowledge strongly predicts a mesophilic optimum (20-45°C) for plant enzymes, as they function at ambient temperatures. The sequence lacks the extreme thermophilic signatures (very high charged-residue density, reduced thermolabile residues, enhanced proline content) that would distinguish it from typical mesophilic plant GH1 enzymes. A knowledgeable model using family-level and organism-level generalizations would most likely select A (23-35) or C (30-43), not D (55-60). The 55-60°C optimum is an unusual experimental measurement for a plant enzyme that contradicts general biological expectations. No sequence-derived feature or family-level inference meaningfully distinguishes 55-60°C from 30-43°C or 49-55°C for this protein without knowing the specific experimental result.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> From a sequence-only perspective using general biological knowledge, a plant GH1 beta-glucosidase would be expected to have a mesophilic optimum. Both A (23-35) and C (30-43) represent plausible mesophilic ranges for a plant enzyme, and neither can be definitively excluded over the other from sequence analysis alone. The expected answer D (55-60) is actually counterintuitive for a plant enzyme based on transferable knowledge.


### Important caveats

- The 55-60°C optimum is an in vitro enzymatic assay measurement (PubMed:18927081), not necessarily reflective of the organism's physiological temperature or the protein's in vivo stability range.
- The organism identity (Carapichea ipecacuanha, a tropical plant) was not provided in the original input; only the sequence was given. However, the sequence is recognizable as a plant GH1 beta-glucosidase.
- The question asks to classify thermal adaptation from sequence alone, but the correct answer depends on an experimental measurement that contradicts general expectations for plant enzymes, making it resistant to sequence-based reasoning.
- The distinction between B (49-55) and D (55-60) is a 5°C boundary that cannot be resolved from sequence features by any known method.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured in vitro optimum temperature of 55-60°C for this specific plant beta-glucosidase (IpeGLU1), reported in PubMed:18927081. This is a counterintuitive value for a plant enzyme that cannot be inferred from sequence features or general family knowledge.",
    "reason": "The protein is recognizably a GH1-family beta-glucosidase from a plant (tropical plant enzyme). General transferable knowledge strongly predicts a mesophilic optimum (20-45°C) for plant enzymes, as they function at ambient temperatures. The sequence lacks the extreme thermophilic signatures (very high charged-residue density, reduced thermolabile residues, enhanced proline content) that would distinguish it from typical mesophilic plant GH1 enzymes. A knowledgeable model using family-level and organism-level generalizations would most likely select A (23-35) or C (30-43), not D (55-60). The 55-60°C optimum is an unusual experimental measurement for a plant enzyme that contradicts general biological expectations. No sequence-derived feature or family-level inference meaningfully distinguishes 55-60°C from 30-43°C or 49-55°C for this protein without knowing the specific experimental result."
  },
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM3 (Ipecoside beta-D-glucosidase IpeGLU1 from Carapichea ipecacuanha) explicitly records 'Optimum temperature is 55-60 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:18927081 (Nomura et al., J. Biol. Chem. 2008). The benchmark sequence matches the UniProt sequence exactly (SHA-256 confirmed). The expected answer D (55-60) directly corresponds to this experimentally measured value."
  },
  "important_caveats": [
    "The 55-60°C optimum is an in vitro enzymatic assay measurement (PubMed:18927081), not necessarily reflective of the organism's physiological temperature or the protein's in vivo stability range.",
    "The organism identity (Carapichea ipecacuanha, a tropical plant) was not provided in the original input; only the sequence was given. However, the sequence is recognizable as a plant GH1 beta-glucosidase.",
    "The question asks to classify thermal adaptation from sequence alone, but the correct answer depends on an experimental measurement that contradicts general expectations for plant enzymes, making it resistant to sequence-based reasoning.",
    "The distinction between B (49-55) and D (55-60) is a 5°C boundary that cannot be resolved from sequence features by any known method."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "From a sequence-only perspective using general biological knowledge, a plant GH1 beta-glucosidase would be expected to have a mesophilic optimum. Both A (23-35) and C (30-43) represent plausible mesophilic ranges for a plant enzyme, and neither can be definitively excluded over the other from sequence analysis alone. The expected answer D (55-60) is actually counterintuitive for a plant enzyme based on transferable knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM3 (Ipecoside beta-D-glucosidase IpeGLU1 from Carapichea ipecacuanha) explicitly records 'Optimum temperature is 55-60 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:18927081 (Nomura et al., J. Biol. Chem. 2008). The benchmark sequence matches the UniProt sequence exactly (SHA-256 confirmed). The expected answer D (55-60) directly corresponds to this experimentally measured value.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The experimentally measured in vitro optimum temperature of 55-60°C for this specific plant beta-glucosidase (IpeGLU1), reported in PubMed:18927081. This is a counterintuitive value for a plant enzyme that cannot be inferred from sequence features or general family knowledge.",
    "reason": "The protein is recognizably a GH1-family beta-glucosidase from a plant (tropical plant enzyme). General transferable knowledge strongly predicts a mesophilic optimum (20-45°C) for plant enzymes, as they function at ambient temperatures. The sequence lacks the extreme thermophilic signatures (very high charged-residue density, reduced thermolabile residues, enhanced proline content) that would distinguish it from typical mesophilic plant GH1 enzymes. A knowledgeable model using family-level and organism-level generalizations would most likely select A (23-35) or C (30-43), not D (55-60). The 55-60°C optimum is an unusual experimental measurement for a plant enzyme that contradicts general biological expectations. No sequence-derived feature or family-level inference meaningfully distinguishes 55-60°C from 30-43°C or 49-55°C for this protein without knowing the specific experimental result."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "From a sequence-only perspective using general biological knowledge, a plant GH1 beta-glucosidase would be expected to have a mesophilic optimum. Both A (23-35) and C (30-43) represent plausible mesophilic ranges for a plant enzyme, and neither can be definitively excluded over the other from sequence analysis alone. The expected answer D (55-60) is actually counterintuitive for a plant enzyme based on transferable knowledge."
  },
  "important_caveats": [
    "The 55-60°C optimum is an in vitro enzymatic assay measurement (PubMed:18927081), not necessarily reflective of the organism's physiological temperature or the protein's in vivo stability range.",
    "The organism identity (Carapichea ipecacuanha, a tropical plant) was not provided in the original input; only the sequence was given. However, the sequence is recognizable as a plant GH1 beta-glucosidase.",
    "The question asks to classify thermal adaptation from sequence alone, but the correct answer depends on an experimental measurement that contradicts general expectations for plant enzymes, making it resistant to sequence-based reasoning.",
    "The distinction between B (49-55) and D (55-60) is a 5°C boundary that cannot be resolved from sequence features by any known method."
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
  "benchmark_sequence_length": 543,
  "benchmark_sequence_sha256": "ab13c398554479e37a5b23b4bb7283787edc8daa96c0ed91353c450298922f32",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 543,
  "current_source_sequence_sha256": "ab13c398554479e37a5b23b4bb7283787edc8daa96c0ed91353c450298922f32",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B6ZKM3",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831",
  "selected_historical_source_sequence_length": 543,
  "selected_historical_source_sequence_sha256": "ab13c398554479e37a5b23b4bb7283787edc8daa96c0ed91353c450298922f32",
  "selected_historical_version": {
    "accession": "B6ZKM3",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLU1_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B6ZKM3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:01.419788+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:01.419788+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:01.419788+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Ipecac alkaloid beta-glucosidase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02544.1\",\"source\":\"EMBL\"}],\"value\":\"IpeGLU1\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.105\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Strictosidine beta-glucosidase IpeGLU1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.220\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Ipecoside beta-D-glucosidase IpeGLU1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:01.419788+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with N-deacetylipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":25.577},{\"enzyme\":\"enzyme with N-deacetylisoipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":78.19},{\"enzyme\":\"enzyme with 6-O-methyl-N-deacetylipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":28.157},{\"enzyme\":\"enzyme with 6-O-methyl-N-deacetylisoipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":16.906},{\"enzyme\":\"enzyme with 7-O-methyl-N-deacetylipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":45.58},{\"enzyme\":\"enzyme with 7-O-methyl-N-deacetylisoipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":22.727},{\"enzyme\":\"enzyme with 6,7-O,O-dimethyl-N-deacetylipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":35.732},{\"enzyme\":\"enzyme with 6,7-O,O-Dimethyl-N-deacetylisoipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":21.989},{\"enzyme\":\"enzyme with ipecoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":46.729},{\"enzyme\":\"enzyme with strictosidine as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":1.945},{\"enzyme\":\"enzyme with vincoside as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":5.786},{\"enzyme\":\"enzyme with secologanin as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":30.303},{\"enzyme\":\"enzyme with loganin as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":19.881},{\"enzyme\":\"enzyme with galloyl-glucose as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":6.024},{\"enzyme\":\"enzyme with p-nitrophenyl-beta-glucose as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"unit\":\"nmol/min/mg\",\"velocity\":3.546}],\"michaelisConstants\":[{\"constant\":0.32,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"N-deacetylipecoside\",\"unit\":\"mM\"},{\"constant\":5.8,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"N-deacetylisoipecoside\",\"unit\":\"mM\"},{\"constant\":0.39,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"6-O-methyl-N-deacetylipecoside\",\"unit\":\"mM\"},{\"constant\":1.3,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"6-O-methyl-N-deacetylisoipecoside\",\"unit\":\"mM\"},{\"constant\":12.7,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"7-O-methyl-N-deacetylipecoside\",\"unit\":\"mM\"},{\"constant\":25.5,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"7-O-methyl-N-deacetylisoipecoside\",\"unit\":\"mM\"},{\"constant\":13.5,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"6,7-O,O-dimethyl-N-deacetylipecoside\",\"unit\":\"mM\"},{\"constant\":35.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"6,7-O,O-Dimethyl-N-deacetylisoipecoside\",\"unit\":\"mM\"},{\"constant\":0.1,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"ipecoside\",\"unit\":\"mM\"},{\"constant\":0.19,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"strictosidine\",\"unit\":\"mM\"},{\"constant\":0.29,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"vincoside\",\"unit\":\"mM\"},{\"constant\":26.5,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"secologanin\",\"unit\":\"mM\"},{\"constant\":33.2,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"loganin\",\"unit\":\"mM\"},{\"constant\":65.1,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"galloyl-glucose\",\"unit\":\"mM\"},{\"constant\":21.5,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"substrate\":\"p-nitrophenyl-beta-glucose\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"kcat is 28.2 sec(-1) with N-deacetylipecoside as substrate (PubMed:18927081). kcat is 86.3 sec(-1) with N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 31.1 sec(-1) with 6-O-methyl-N-deacetylipecoside as substrate (PubMed:18927081). kcat is 18.7 sec(-1) with 6-O-methyl-N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 50.3 sec(-1) with 7-O-methyl-N-deacetylipecoside as substrate (PubMed:18927081). kcat is 25.1 sec(-1) with 7-O-methyl-N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 39.4 sec(-1) with 6,7-O,O-dimethyl-N-deacetylipecoside as substrate (PubMed:18927081). kcat is 24.3 sec(-1) with 6,7-O,O-Dimethyl-N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 51.6 sec(-1) with ipecoside as substrate (PubMed:18927081). kcat is 2.1 sec(-1) with strictosidine as substrate (PubMed:18927081). kcat is 6.4 sec(-1) with vincoside as substrate (PubMed:18927081). kcat is 33.4 sec(-1) with secologanin as substrate (PubMed:18927081). kcat is 21.9 sec(-1) with loganin as substrate (PubMed:18927081). kcat is 6.6 sec(-1) with galloyl-glucose as substrate (PubMed:18927081). kcat is 3.9 sec(-1) with p-nitrophenyl-beta-glucose as substrate (PubMed:18927081).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 5 with N-deacetylisoipecoside and N-deacetylipecoside as substrates.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 55-60 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/8",
  "retrieved_utc": "2026-11-01T06:25:01.419788+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Quesada A.L.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18927081\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m806953200\"}],\"citationType\":\"journal article\",\"firstPage\":\"34650\",\"id\":\"18927081\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"34659\",\"publicationDate\":\"2008\",\"title\":\"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.\",\"volume\":\"283\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02544.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"},{\"type\":\"TISSUE\",\"value\":\"Shoot\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:01.419788+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   GLU1_CARIP              Reviewed;         543 AA.\nAC   B6ZKM3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2009, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Ipecoside beta-D-glucosidase IpeGLU1 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.220 {ECO:0000269|PubMed:18927081};\nDE   AltName: Full=Ipecac alkaloid beta-glucosidase 1 {ECO:0000303|PubMed:18927081};\nDE            Short=IpeGLU1 {ECO:0000303|PubMed:18927081, ECO:0000312|EMBL:BAH02544.1};\nDE   AltName: Full=Strictosidine beta-glucosidase IpeGLU1 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.105 {ECO:0000269|PubMed:18927081};\nGN   Name=GLU1 {ECO:0000303|PubMed:18927081};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:52.619495+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831",
  "url": "https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAH02544.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRC   TISSUE=Root, and Shoot;\nRX   PubMed=18927081; DOI=10.1074/jbc.m806953200;\nRA   Nomura T., Quesada A.L., Kutchan T.M.;\nRT   \"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis\nRT   in Psychotria ipecacuanha.\";\nRL   J. Biol. Chem. 283:34650-34659(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:52.619495+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831",
  "url": "https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=0.32 mM for N-deacetylipecoside {ECO:0000269|PubMed:18927081};\nCC         KM=5.8 mM for N-deacetylisoipecoside {ECO:0000269|PubMed:18927081};\nCC         KM=0.39 mM for 6-O-methyl-N-deacetylipecoside\nCC         {ECO:0000269|PubMed:18927081};\nCC         KM=1.3 mM for 6-O-methyl-N-deacetylisoipecoside\nCC         {ECO:0000269|PubMed:18927081};\nCC         KM=12.7 mM for 7-O-methyl-N-deacetylipecoside\nCC         {ECO:0000269|PubMed:18927081};\nCC         KM=25.5 mM for 7-O-methyl-N-deacetylisoipecoside\nCC         {ECO:0000269|PubMed:18927081};\nCC         KM=13.5 mM for 6,7-O,O-dimethyl-N-deacetylipecoside\nCC         {ECO:0000269|PubMed:18927081};\nCC         KM=35.0 mM for 6,7-O,O-Dimethyl-N-deacetylisoipecoside\nCC         {ECO:0000269|PubMed:18927081};\nCC         KM=0.10 mM for ipecoside {ECO:0000269|PubMed:18927081};\nCC         KM=0.19 mM for strictosidine {ECO:0000269|PubMed:18927081};\nCC         KM=0.29 mM for vincoside {ECO:0000269|PubMed:18927081};\nCC         KM=26.5 mM for secologanin {ECO:0000269|PubMed:18927081};\nCC         KM=33.2 mM for loganin {ECO:0000269|PubMed:18927081};\nCC         KM=65.1 mM for galloyl-glucose {ECO:0000269|PubMed:18927081};\nCC         KM=21.5 mM for p-nitrophenyl-beta-glucose\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=25.577 nmol/min/mg enzyme with N-deacetylipecoside as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=78.190 nmol/min/mg enzyme with N-deacetylisoipecoside as\nCC         substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=28.157 nmol/min/mg enzyme with 6-O-methyl-N-deacetylipecoside as\nCC         substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=16.906 nmol/min/mg enzyme with 6-O-methyl-N-deacetylisoipecoside\nCC         as substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=45.580 nmol/min/mg enzyme with 7-O-methyl-N-deacetylipecoside as\nCC         substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=22.727 nmol/min/mg enzyme with 7-O-methyl-N-deacetylisoipecoside\nCC         as substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=35.732 nmol/min/mg enzyme with 6,7-O,O-dimethyl-N-\nCC         deacetylipecoside as substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=21.989 nmol/min/mg enzyme with 6,7-O,O-Dimethyl-N-\nCC         deacetylisoipecoside as substrate {ECO:0000269|PubMed:18927081};\nCC         Vmax=46.729 nmol/min/mg enzyme with ipecoside as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=1.945 nmol/min/mg enzyme with strictosidine as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=5.786 nmol/min/mg enzyme with vincoside as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=30.303 nmol/min/mg enzyme with secologanin as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=19.881 nmol/min/mg enzyme with loganin as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=6.024 nmol/min/mg enzyme with galloyl-glucose as substrate\nCC         {ECO:0000269|PubMed:18927081};\nCC         Vmax=3.546 nmol/min/mg enzyme with p-nitrophenyl-beta-glucose as\nCC         substrate {ECO:0000269|PubMed:18927081};\nCC         Note=kcat is 28.2 sec(-1) with N-deacetylipecoside as substrate\nCC         (PubMed:18927081). kcat is 86.3 sec(-1) with N-deacetylisoipecoside\nCC         as substrate (PubMed:18927081). kcat is 31.1 sec(-1) with 6-O-methyl-\nCC         N-deacetylipecoside as substrate (PubMed:18927081). kcat is 18.7\nCC         sec(-1) with 6-O-methyl-N-deacetylisoipecoside as substrate\nCC         (PubMed:18927081). kcat is 50.3 sec(-1) with 7-O-methyl-N-\nCC         deacetylipecoside as substrate (PubMed:18927081). kcat is 25.1 sec(-\nCC         1) with 7-O-methyl-N-deacetylisoipecoside as substrate\nCC         (PubMed:18927081). kcat is 39.4 sec(-1) with 6,7-O,O-dimethyl-N-\nCC         deacetylipecoside as substrate (PubMed:18927081). kcat is 24.3 sec(-\nCC         1) with 6,7-O,O-Dimethyl-N-deacetylisoipecoside as substrate\nCC         (PubMed:18927081). kcat is 51.6 sec(-1) with ipecoside as substrate\nCC         (PubMed:18927081). kcat is 2.1 sec(-1) with strictosidine as\nCC         substrate (PubMed:18927081). kcat is 6.4 sec(-1) with vincoside as\nCC         substrate (PubMed:18927081). kcat is 33.4 sec(-1) with secologanin as\nCC         substrate (PubMed:18927081). kcat is 21.9 sec(-1) with loganin as\nCC         substrate (PubMed:18927081). kcat is 6.6 sec(-1) with galloyl-glucose\nCC         as substrate (PubMed:18927081). kcat is 3.9 sec(-1) with p-\nCC         nitrophenyl-beta-glucose as substrate (PubMed:18927081).\nCC         {ECO:0000269|PubMed:18927081};\nCC       pH dependence:\nCC         Optimum pH is 5 with N-deacetylisoipecoside and N-deacetylipecoside\nCC         as substrates. {ECO:0000269|PubMed:18927081};\nCC       Temperature dependence:\nCC         Optimum temperature is 55-60 degrees Celsius.\nCC         {ECO:0000269|PubMed:18927081};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:52.619495+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831",
  "url": "https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
