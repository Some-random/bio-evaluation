# GO_cellular_component_0129

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0129.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPNPKVFFDMTIGGQPAGRIVMELYADVTPSTAENFRALCTGEKGAGRSGKPLHYKGSSFHRVIPNFMCQGGDFTAGNGTGGESIYGAKFADENFVKKHTGPGILSMANAGPGTNGSQFFICTTKTEWLDGKHVVFGQVVEGMDVVKEIEKVGSSSGRTAKPVVVADCGQLS

[Multiple Choices]
A. presynaptic active zone
B. mitochondrial matrix
C. plasma membrane
D. microvillus membrane
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

> The sequence-matched UniProt record annotates cell membrane localization with experimental evidence, and separately assigns plasma membrane by IDA. This supports choice C as a location, though it does not establish that plasma membrane is the protein’s primary location over its also-annotated nuclear localization.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble cyclophilin-family PPIase and has no obvious transmembrane segment or clear N-terminal mitochondrial targeting peptide, making a mitochondrial-matrix assignment less compelling. The specialized presynaptic and microvillus choices also have no support from the sequence. But these features do not meaningfully predict plasma-membrane localization for a soluble protein; that distinction depends on a localization fact specific to this protein.


**Missing item-specific fact**

> Whether this particular cyclophilin is experimentally associated with the plasma membrane.


**Reason**

> Transferable family and targeting-signal knowledge can make some alternatives less plausible, but it does not supply a reliable basis for choosing plasma membrane over other non-mitochondrial possibilities. The key’s distinguishing support comes from this protein’s localization annotation, which was not in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the supplied sequence-matched evidence supports plasma membrane; the record’s additional nuclear localization is not an offered option. The evidence does not establish plasma membrane as the primary location, but it does not identify another offered choice as equally supported.


### Important caveats

- The record annotates both cell membrane/plasma membrane and nucleus, so the word “primary” is not resolved by the supplied localization evidence.
- The evidence supports localization but does not independently establish the fraction of protein at each location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble cyclophilin-family PPIase and has no obvious transmembrane segment or clear N-terminal mitochondrial targeting peptide, making a mitochondrial-matrix assignment less compelling. The specialized presynaptic and microvillus choices also have no support from the sequence. But these features do not meaningfully predict plasma-membrane localization for a soluble protein; that distinction depends on a localization fact specific to this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular cyclophilin is experimentally associated with the plasma membrane.",
    "reason": "Transferable family and targeting-signal knowledge can make some alternatives less plausible, but it does not supply a reliable basis for choosing plasma membrane over other non-mitochondrial possibilities. The key’s distinguishing support comes from this protein’s localization annotation, which was not in the original input."
  },
  "case_id": "GO_cellular_component_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cell membrane localization with experimental evidence, and separately assigns plasma membrane by IDA. This supports choice C as a location, though it does not establish that plasma membrane is the protein’s primary location over its also-annotated nuclear localization."
  },
  "important_caveats": [
    "The record annotates both cell membrane/plasma membrane and nucleus, so the word “primary” is not resolved by the supplied localization evidence.",
    "The evidence supports localization but does not independently establish the fraction of protein at each location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the supplied sequence-matched evidence supports plasma membrane; the record’s additional nuclear localization is not an offered option. The evidence does not establish plasma membrane as the primary location, but it does not identify another offered choice as equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cell membrane localization with experimental evidence, and separately assigns plasma membrane by IDA. This supports choice C as a location, though it does not establish that plasma membrane is the protein’s primary location over its also-annotated nuclear localization.",
    "evidence_ids": ["C5", "C7", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble cyclophilin-family PPIase and has no obvious transmembrane segment or clear N-terminal mitochondrial targeting peptide, making a mitochondrial-matrix assignment less compelling. The specialized presynaptic and microvillus choices also have no support from the sequence. But these features do not meaningfully predict plasma-membrane localization for a soluble protein; that distinction depends on a localization fact specific to this protein.",
    "missing_item_specific_fact": "Whether this particular cyclophilin is experimentally associated with the plasma membrane.",
    "reason": "Transferable family and targeting-signal knowledge can make some alternatives less plausible, but it does not supply a reliable basis for choosing plasma membrane over other non-mitochondrial possibilities. The key’s distinguishing support comes from this protein’s localization annotation, which was not in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the supplied sequence-matched evidence supports plasma membrane; the record’s additional nuclear localization is not an offered option. The evidence does not establish plasma membrane as the primary location, but it does not identify another offered choice as equally supported."
  },
  "important_caveats": [
    "The record annotates both cell membrane/plasma membrane and nucleus, so the word “primary” is not resolved by the supplied localization evidence.",
    "The evidence supports localization but does not independently establish the fraction of protein at each location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A0R0H9T5, Peptidyl-prolyl cis-trans isomerase 2 / Cyclophilin 2 from Glycine max) lists 'Cell membrane' (GO:0005886, plasma membrane) with ECO:0000269 (experimental) and IDA:UniProtKB evidence. The GO term GO:0005886 (plasma membrane) is directly annotated. The annotation also includes nucleus (GO:0005634, IDA), but since nucleus is not among the offered choices, the expected answer 'plasma membrane' is supported by the experimental annotation for this protein.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark cyclophilin/PPIase motifs (IGG near N-terminus, GAGR, GGDFTAGNGTGG), identifying it as a member of the cyclophilin peptidyl-prolyl isomerase family. Transferable knowledge about this family and cell biology enables elimination of three distractors: (1) Option A (presynaptic active zone) is a neuron-specific structure; cyclophilins are ubiquitous soluble enzymes with no neuronal targeting features, and the sequence lacks any synaptic protein motifs. (2) Option B (mitochondrial matrix) requires an N-terminal amphipathic mitochondrial targeting presequence rich in arginine and hydroxylated residues; this sequence begins MPNPKVFFDMTIGG with no such targeting signal, and most cyclophilins are cytosolic/nuclear. (3) Option D (microvillus membrane) describes a specialized animal-cell surface structure; microvillus membrane proteins typically possess transmembrane domains or GPI anchors, neither of which is present in this 172-aa soluble enzyme. Additionally, plants lack microvilli. By elimination, C (plasma membrane) remains as the only viable option among the four. While cyclophilins are classically soluble, peripheral membrane association without a TM domain is a known phenomenon for some family members, making C the least inconsistent choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination argument relies on recognizing the cyclophilin family from conserved sequence motifs, knowing that mitochondrial matrix proteins require targeting signals absent here, knowing presynaptic active zones are neuron-specific, and knowing microvillus membrane proteins require membrane anchors absent here. This is standard transferable knowledge about protein families and cell biology that meaningfully distinguishes C from A, B, and D without requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt annotation also lists nucleus (GO:0005634), nucleus is not among the four offered choices. Among the presented alternatives (presynaptic active zone, mitochondrial matrix, plasma membrane, microvillus membrane), only plasma membrane is defensible after applying family-level and structural reasoning. No ambiguity exists among the given options.


### Important caveats

- The protein is also annotated in the nucleus (IDA), which would be a competing 'primary' location if offered as a choice; the question's phrasing 'primary Cellular Component' could be debatable if nucleus were an option.
- The plasma membrane association is unusual for a cyclophilin and was determined experimentally (Ref.2, ECO:0000269); sequence-based prediction alone would more typically suggest cytoplasm or nucleus for this family.
- The organism identity (Glycine max / plant) is not given in the original input; elimination of option D (microvillus membrane) partially relies on recognizing that plants lack microvilli, though the absence of membrane anchors in the sequence provides an independent argument against D.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark input and UniProt entry A0A0R0H9T5.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark cyclophilin/PPIase motifs (IGG near N-terminus, GAGR, GGDFTAGNGTGG), identifying it as a member of the cyclophilin peptidyl-prolyl isomerase family. Transferable knowledge about this family and cell biology enables elimination of three distractors: (1) Option A (presynaptic active zone) is a neuron-specific structure; cyclophilins are ubiquitous soluble enzymes with no neuronal targeting features, and the sequence lacks any synaptic protein motifs. (2) Option B (mitochondrial matrix) requires an N-terminal amphipathic mitochondrial targeting presequence rich in arginine and hydroxylated residues; this sequence begins MPNPKVFFDMTIGG with no such targeting signal, and most cyclophilins are cytosolic/nuclear. (3) Option D (microvillus membrane) describes a specialized animal-cell surface structure; microvillus membrane proteins typically possess transmembrane domains or GPI anchors, neither of which is present in this 172-aa soluble enzyme. Additionally, plants lack microvilli. By elimination, C (plasma membrane) remains as the only viable option among the four. While cyclophilins are classically soluble, peripheral membrane association without a TM domain is a known phenomenon for some family members, making C the least inconsistent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination argument relies on recognizing the cyclophilin family from conserved sequence motifs, knowing that mitochondrial matrix proteins require targeting signals absent here, knowing presynaptic active zones are neuron-specific, and knowing microvillus membrane proteins require membrane anchors absent here. This is standard transferable knowledge about protein families and cell biology that meaningfully distinguishes C from A, B, and D without requiring recall of this specific protein's database annotation."
  },
  "case_id": "GO_cellular_component_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A0R0H9T5, Peptidyl-prolyl cis-trans isomerase 2 / Cyclophilin 2 from Glycine max) lists 'Cell membrane' (GO:0005886, plasma membrane) with ECO:0000269 (experimental) and IDA:UniProtKB evidence. The GO term GO:0005886 (plasma membrane) is directly annotated. The annotation also includes nucleus (GO:0005634, IDA), but since nucleus is not among the offered choices, the expected answer 'plasma membrane' is supported by the experimental annotation for this protein."
  },
  "important_caveats": [
    "The protein is also annotated in the nucleus (IDA), which would be a competing 'primary' location if offered as a choice; the question's phrasing 'primary Cellular Component' could be debatable if nucleus were an option.",
    "The plasma membrane association is unusual for a cyclophilin and was determined experimentally (Ref.2, ECO:0000269); sequence-based prediction alone would more typically suggest cytoplasm or nucleus for this family.",
    "The organism identity (Glycine max / plant) is not given in the original input; elimination of option D (microvillus membrane) partially relies on recognizing that plants lack microvilli, though the absence of membrane anchors in the sequence provides an independent argument against D.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark input and UniProt entry A0A0R0H9T5."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt annotation also lists nucleus (GO:0005634), nucleus is not among the four offered choices. Among the presented alternatives (presynaptic active zone, mitochondrial matrix, plasma membrane, microvillus membrane), only plasma membrane is defensible after applying family-level and structural reasoning. No ambiguity exists among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A0R0H9T5, Peptidyl-prolyl cis-trans isomerase 2 / Cyclophilin 2 from Glycine max) lists 'Cell membrane' (GO:0005886, plasma membrane) with ECO:0000269 (experimental) and IDA:UniProtKB evidence. The GO term GO:0005886 (plasma membrane) is directly annotated. The annotation also includes nucleus (GO:0005634, IDA), but since nucleus is not among the offered choices, the expected answer 'plasma membrane' is supported by the experimental annotation for this protein.",
    "evidence_ids": ["C5", "C7", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark cyclophilin/PPIase motifs (IGG near N-terminus, GAGR, GGDFTAGNGTGG), identifying it as a member of the cyclophilin peptidyl-prolyl isomerase family. Transferable knowledge about this family and cell biology enables elimination of three distractors: (1) Option A (presynaptic active zone) is a neuron-specific structure; cyclophilins are ubiquitous soluble enzymes with no neuronal targeting features, and the sequence lacks any synaptic protein motifs. (2) Option B (mitochondrial matrix) requires an N-terminal amphipathic mitochondrial targeting presequence rich in arginine and hydroxylated residues; this sequence begins MPNPKVFFDMTIGG with no such targeting signal, and most cyclophilins are cytosolic/nuclear. (3) Option D (microvillus membrane) describes a specialized animal-cell surface structure; microvillus membrane proteins typically possess transmembrane domains or GPI anchors, neither of which is present in this 172-aa soluble enzyme. Additionally, plants lack microvilli. By elimination, C (plasma membrane) remains as the only viable option among the four. While cyclophilins are classically soluble, peripheral membrane association without a TM domain is a known phenomenon for some family members, making C the least inconsistent choice.",
    "missing_item_specific_fact": "",
    "reason": "The elimination argument relies on recognizing the cyclophilin family from conserved sequence motifs, knowing that mitochondrial matrix proteins require targeting signals absent here, knowing presynaptic active zones are neuron-specific, and knowing microvillus membrane proteins require membrane anchors absent here. This is standard transferable knowledge about protein families and cell biology that meaningfully distinguishes C from A, B, and D without requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt annotation also lists nucleus (GO:0005634), nucleus is not among the four offered choices. Among the presented alternatives (presynaptic active zone, mitochondrial matrix, plasma membrane, microvillus membrane), only plasma membrane is defensible after applying family-level and structural reasoning. No ambiguity exists among the given options."
  },
  "important_caveats": [
    "The protein is also annotated in the nucleus (IDA), which would be a competing 'primary' location if offered as a choice; the question's phrasing 'primary Cellular Component' could be debatable if nucleus were an option.",
    "The plasma membrane association is unusual for a cyclophilin and was determined experimentally (Ref.2, ECO:0000269); sequence-based prediction alone would more typically suggest cytoplasm or nucleus for this family.",
    "The organism identity (Glycine max / plant) is not given in the original input; elimination of option D (microvillus membrane) partially relies on recognizing that plants lack microvilli, though the absence of membrane anchors in the sequence provides an independent argument against D.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark input and UniProt entry A0A0R0H9T5."
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
  "benchmark_sequence_length": 172,
  "benchmark_sequence_sha256": "15f4f693a49e94758c12a146f81dfe672d4a7a350d20925457cc6e0fb22324ba",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-01-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 172,
  "current_source_sequence_sha256": "15f4f693a49e94758c12a146f81dfe672d4a7a350d20925457cc6e0fb22324ba",
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
  "requested_accession": "A0A0R0H9T5",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66",
  "selected_historical_source_sequence_length": 172,
  "selected_historical_source_sequence_sha256": "15f4f693a49e94758c12a146f81dfe672d4a7a350d20925457cc6e0fb22324ba",
  "selected_historical_version": {
    "accession": "A0A0R0H9T5",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CYP2_SOYBN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0R0H9T5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-01-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"Cyclophilin 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"GmCYP2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P62937\",\"source\":\"UniProtKB\"}],\"value\":\"5.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O49886\",\"source\":\"UniProtKB\"}],\"value\":\"Peptidyl-prolyl cis-trans isomerase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O49886\",\"source\":\"UniProtKB\"}],\"value\":\"PPIase 2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-02T04:24:20.433774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   CYP2_SOYBN              Reviewed;         172 AA.\nAC   A0A0R0H9T5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-JAN-2016, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Peptidyl-prolyl cis-trans isomerase 2 {ECO:0000250|UniProtKB:O49886};\nDE            Short=PPIase 2 {ECO:0000250|UniProtKB:O49886};\nDE            EC=5.2.1.8 {ECO:0000250|UniProtKB:P62937};\nDE   AltName: Full=Cyclophilin 2 {ECO:0000303|Ref.2};\nDE            Short=GmCYP2 {ECO:0000303|Ref.2};\nGN   Name=CYP2 {ECO:0000303|Ref.2};\nGN   ORFNames=GLYMA_12G024700 {ECO:0000312|EMBL:KRH24153.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:22.440712+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66",
  "url": "https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|Ref.2}. Nucleus\nCC       {ECO:0000269|Ref.2}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:22.440712+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66",
  "url": "https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:22.440712+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66",
  "url": "https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:22.440712+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66",
  "url": "https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:22.440712+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66",
  "url": "https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005759\nname: mitochondrial matrix\nnamespace: cellular_component\nalt_id: GO:0031980\ndef: \"The gel-like material, with considerable fine structure, that lies in the matrix space, or lumen, of a mitochondrion. It contains the enzymes of the tricarboxylic acid cycle and, in some organisms, the enzymes concerned with fatty acid oxidation.\" [GOC:as, ISBN:0198506732]\nsynonym: \"mitochondrial lumen\" EXACT []\nsynonym: \"mitochondrial stroma\" NARROW []\nxref: NIF_Subcellular:sao1804523077\nxref: Wikipedia:Mitochondrial_matrix\nis_a: GO:0070013 ! intracellular organelle lumen\nrelationship: part_of GO:0005739 ! mitochondrion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005759",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59194-59206",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0048786\nname: presynaptic active zone\nnamespace: cellular_component\ndef: \"A specialized region of the plasma membrane and cell cortex of a presynaptic neuron; encompasses a region of the plasma membrane where synaptic vesicles dock and fuse, and a specialized cortical cytoskeletal matrix.\" [GOC:dh, GOC:dl, GOC:ef, GOC:jid, GOC:pr, PMID:3152289]\nsubset: goslim_synapse\nsynonym: \"pre-synaptic active zone\" EXACT []\nsynonym: \"pre-synaptic active zone component\" NARROW [NIF_Subcellular:sao1911631652]\nsynonym: \"presynaptic specialization\" EXACT []\nxref: NIF_Subcellular:sao792027222\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0098793 ! presynapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048786",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 306510-306522",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
