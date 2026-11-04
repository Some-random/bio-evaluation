# GO_cellular_component_0113

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0113.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — virion component

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSQIKIPLPKPPDSDSQRLNAFPVIMAQEGKGRLLRQIRLRKILSGDPSDQQITFVNTYGFIRATPETSEFISESSQQKVTPVVTACMLSFGAGPVLEDPQHMLKALDQTDIRVRKTASDKEQILFEINRIPNLFRHYQISADHLIQASSDKYVKSPAKLIAGVNYIYCVTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEILLRVTCKKDSQMAKSMLNDPDGEGCIASVWFHLCNLCKGRNKLRSYDENYFASKCRKMNLTVSIGDMWGPTILVHAGGHIPTTAKPFFNSRGWVCHPIHQSSPSLAKTLWSSGCEIKAASAILQGSDYASLAKTDDIIYSKIKVDKDAANYKGVSWSPFRKSASMRNL

[Multiple Choices]
A. rhoptry
B. caveola
C. early endosome membrane
D. virion component
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

> The sequence-matched UniProt record reports Virion as the subcellular location with experimental evidence (ECO:0000269, PubMed 26768080). It also has a viral-envelope GO annotation, which is a descendant of virion component. The latter is computationally inferred, but the location annotation supports the keyed choice.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2), [GO5](#evidence-go5), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 375-residue sequence has no obvious N-terminal secretion signal or long hydrophobic transmembrane segment. Transferable knowledge that viral matrix proteins are often soluble or peripheral structural proteins incorporated into virions makes D plausible, while the membrane-oriented caveola and early-endosome choices fit less well; rhoptry proteins are generally associated with secretory targeting in apicomplexan parasites. This is a probabilistic sequence-based distinction, not a definitive identification.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The absence of membrane-targeting features and the expected properties of viral matrix proteins provide a meaningful, though limited, basis for preferring D among these alternatives. The sequence alone does not establish the protein’s identity or localization with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence-level inference or the reviewer evidence.


### Important caveats

- The sequence does not contain an unmistakable localization signal that proves virion incorporation.
- The direct location evidence supports Virion; the viral-envelope GO annotation is computationally inferred and more specific.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 375-residue sequence has no obvious N-terminal secretion signal or long hydrophobic transmembrane segment. Transferable knowledge that viral matrix proteins are often soluble or peripheral structural proteins incorporated into virions makes D plausible, while the membrane-oriented caveola and early-endosome choices fit less well; rhoptry proteins are generally associated with secretory targeting in apicomplexan parasites. This is a probabilistic sequence-based distinction, not a definitive identification.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The absence of membrane-targeting features and the expected properties of viral matrix proteins provide a meaningful, though limited, basis for preferring D among these alternatives. The sequence alone does not establish the protein’s identity or localization with certainty."
  },
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "GO2",
      "GO5",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports Virion as the subcellular location with experimental evidence (ECO:0000269, PubMed 26768080). It also has a viral-envelope GO annotation, which is a descendant of virion component. The latter is computationally inferred, but the location annotation supports the keyed choice."
  },
  "important_caveats": [
    "The sequence does not contain an unmistakable localization signal that proves virion incorporation.",
    "The direct location evidence supports Virion; the viral-envelope GO annotation is computationally inferred and more specific."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level inference or the reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports Virion as the subcellular location with experimental evidence (ECO:0000269, PubMed 26768080). It also has a viral-envelope GO annotation, which is a descendant of virion component. The latter is computationally inferred, but the location annotation supports the keyed choice.",
    "evidence_ids": ["C5", "C6", "GO2", "GO5", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 375-residue sequence has no obvious N-terminal secretion signal or long hydrophobic transmembrane segment. Transferable knowledge that viral matrix proteins are often soluble or peripheral structural proteins incorporated into virions makes D plausible, while the membrane-oriented caveola and early-endosome choices fit less well; rhoptry proteins are generally associated with secretory targeting in apicomplexan parasites. This is a probabilistic sequence-based distinction, not a definitive identification.",
    "missing_item_specific_fact": "",
    "reason": "The absence of membrane-targeting features and the expected properties of viral matrix proteins provide a meaningful, though limited, basis for preferring D among these alternatives. The sequence alone does not establish the protein’s identity or localization with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level inference or the reviewer evidence."
  },
  "important_caveats": [
    "The sequence does not contain an unmistakable localization signal that proves virion incorporation.",
    "The direct location evidence supports Virion; the viral-envelope GO annotation is computationally inferred and more specific."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9J4L4 (Mumps virus Matrix protein, strain Jeryl-Lynn) explicitly annotates the subcellular location as 'Virion' with experimental evidence (ECO:0000269, PubMed:26768080, mass spectrometry identification in virion particles). The GO annotation GO:0019031 (viral envelope) is a child of GO:0036338 (viral membrane), which is itself a child of GO:0044423 (virion component). Thus the expected answer 'virion component' is directly supported by experimental annotation. The sequence in the question matches the canonical entry exactly (375 aa, SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [GO5](#evidence-go5), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 375-aa sequence lacks any canonical eukaryotic targeting signals: no N-terminal signal peptide (rules out secretory pathway/organelle entry), no nuclear localization signal, no mitochondrial targeting presequence, and no ER-retention or endosomal sorting motifs (dileucine, tyrosine-based). The central hydrophobic stretch (~40 residues, VTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEILLRVTCKK) is flanked by hydrophilic domains and resembles the membrane-binding amphipathic region of paramyxovirus matrix proteins (known from measles, Nipah, Sendai virus M proteins) that associates with the inner leaflet of the viral envelope rather than spanning a bilayer as a trafficking TM domain. The small size, single hydrophobic membrane-interaction region, and absence of caveolin-like hairpin topology (rules out B), absence of apicomplexan secretory/organellar features (rules out A), and absence of endosomal trafficking motifs or multi-TM architecture (rules out C) collectively favor a viral structural protein interpretation. A model trained on viral structural biology can recognize this domain architecture from homologous matrix proteins in other paramyxoviruses and paramyxovirid viruses.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use family-level knowledge of paramyxovirus matrix proteins (measles M, Nipah M, Sendai M) to recognize the characteristic architecture: small size, central hydrophobic membrane-binding region flanked by hydrophilic domains, no signal peptide, no eukaryotic trafficking motifs. This pattern is transferable from other viral matrix proteins and meaningfully distinguishes 'virion component' from the three eukaryotic-compartment distractors, each of which requires specific structural or sequence features absent here.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct biological contexts (apicomplexan secretory organelle, mammalian plasma-membrane invagination, eukaryotic endosomal membrane, viral particle constituent). The sequence lacks features specific to any of the three eukaryotic options and its architecture is most consistent with a viral structural protein. No ambiguity among the offered choices.


### Important caveats

- The inference from sequence to 'viral matrix protein' is probabilistic and relies on family-level pattern recognition from other paramyxoviruses; it does not constitute a definitive proof from first principles.
- The GO annotation in UniProt is GO:0019031 (viral envelope, IEA keyword-derived), while the experimental evidence supports 'Virion' location. The option 'virion component' (GO:0044423) is the parent of viral envelope, so it is correct but less specific than the annotated term.
- The reviewer identified the protein as Mumps virus Matrix protein via accession Q9J4L4; this identity was not provided to the evaluated model and the model must rely on sequence features and transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 375-aa sequence lacks any canonical eukaryotic targeting signals: no N-terminal signal peptide (rules out secretory pathway/organelle entry), no nuclear localization signal, no mitochondrial targeting presequence, and no ER-retention or endosomal sorting motifs (dileucine, tyrosine-based). The central hydrophobic stretch (~40 residues, VTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEILLRVTCKK) is flanked by hydrophilic domains and resembles the membrane-binding amphipathic region of paramyxovirus matrix proteins (known from measles, Nipah, Sendai virus M proteins) that associates with the inner leaflet of the viral envelope rather than spanning a bilayer as a trafficking TM domain. The small size, single hydrophobic membrane-interaction region, and absence of caveolin-like hairpin topology (rules out B), absence of apicomplexan secretory/organellar features (rules out A), and absence of endosomal trafficking motifs or multi-TM architecture (rules out C) collectively favor a viral structural protein interpretation. A model trained on viral structural biology can recognize this domain architecture from homologous matrix proteins in other paramyxoviruses and paramyxovirid viruses.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family-level knowledge of paramyxovirus matrix proteins (measles M, Nipah M, Sendai M) to recognize the characteristic architecture: small size, central hydrophobic membrane-binding region flanked by hydrophilic domains, no signal peptide, no eukaryotic trafficking motifs. This pattern is transferable from other viral matrix proteins and meaningfully distinguishes 'virion component' from the three eukaryotic-compartment distractors, each of which requires specific structural or sequence features absent here."
  },
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "GO5",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9J4L4 (Mumps virus Matrix protein, strain Jeryl-Lynn) explicitly annotates the subcellular location as 'Virion' with experimental evidence (ECO:0000269, PubMed:26768080, mass spectrometry identification in virion particles). The GO annotation GO:0019031 (viral envelope) is a child of GO:0036338 (viral membrane), which is itself a child of GO:0044423 (virion component). Thus the expected answer 'virion component' is directly supported by experimental annotation. The sequence in the question matches the canonical entry exactly (375 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "The inference from sequence to 'viral matrix protein' is probabilistic and relies on family-level pattern recognition from other paramyxoviruses; it does not constitute a definitive proof from first principles.",
    "The GO annotation in UniProt is GO:0019031 (viral envelope, IEA keyword-derived), while the experimental evidence supports 'Virion' location. The option 'virion component' (GO:0044423) is the parent of viral envelope, so it is correct but less specific than the annotated term.",
    "The reviewer identified the protein as Mumps virus Matrix protein via accession Q9J4L4; this identity was not provided to the evaluated model and the model must rely on sequence features and transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct biological contexts (apicomplexan secretory organelle, mammalian plasma-membrane invagination, eukaryotic endosomal membrane, viral particle constituent). The sequence lacks features specific to any of the three eukaryotic options and its architecture is most consistent with a viral structural protein. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9J4L4 (Mumps virus Matrix protein, strain Jeryl-Lynn) explicitly annotates the subcellular location as 'Virion' with experimental evidence (ECO:0000269, PubMed:26768080, mass spectrometry identification in virion particles). The GO annotation GO:0019031 (viral envelope) is a child of GO:0036338 (viral membrane), which is itself a child of GO:0044423 (virion component). Thus the expected answer 'virion component' is directly supported by experimental annotation. The sequence in the question matches the canonical entry exactly (375 aa, SHA256 confirmed).",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "GO5", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 375-aa sequence lacks any canonical eukaryotic targeting signals: no N-terminal signal peptide (rules out secretory pathway/organelle entry), no nuclear localization signal, no mitochondrial targeting presequence, and no ER-retention or endosomal sorting motifs (dileucine, tyrosine-based). The central hydrophobic stretch (~40 residues, VTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEILLRVTCKK) is flanked by hydrophilic domains and resembles the membrane-binding amphipathic region of paramyxovirus matrix proteins (known from measles, Nipah, Sendai virus M proteins) that associates with the inner leaflet of the viral envelope rather than spanning a bilayer as a trafficking TM domain. The small size, single hydrophobic membrane-interaction region, and absence of caveolin-like hairpin topology (rules out B), absence of apicomplexan secretory/organellar features (rules out A), and absence of endosomal trafficking motifs or multi-TM architecture (rules out C) collectively favor a viral structural protein interpretation. A model trained on viral structural biology can recognize this domain architecture from homologous matrix proteins in other paramyxoviruses and paramyxovirid viruses.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family-level knowledge of paramyxovirus matrix proteins (measles M, Nipah M, Sendai M) to recognize the characteristic architecture: small size, central hydrophobic membrane-binding region flanked by hydrophilic domains, no signal peptide, no eukaryotic trafficking motifs. This pattern is transferable from other viral matrix proteins and meaningfully distinguishes 'virion component' from the three eukaryotic-compartment distractors, each of which requires specific structural or sequence features absent here."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct biological contexts (apicomplexan secretory organelle, mammalian plasma-membrane invagination, eukaryotic endosomal membrane, viral particle constituent). The sequence lacks features specific to any of the three eukaryotic options and its architecture is most consistent with a viral structural protein. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The inference from sequence to 'viral matrix protein' is probabilistic and relies on family-level pattern recognition from other paramyxoviruses; it does not constitute a definitive proof from first principles.",
    "The GO annotation in UniProt is GO:0019031 (viral envelope, IEA keyword-derived), while the experimental evidence supports 'Virion' location. The option 'virion component' (GO:0044423) is the parent of viral envelope, so it is correct but less specific than the annotated term.",
    "The reviewer identified the protein as Mumps virus Matrix protein via accession Q9J4L4; this identity was not provided to the evaluated model and the model must rely on sequence features and transferable knowledge."
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
  "benchmark_sequence_length": 375,
  "benchmark_sequence_sha256": "b3a155418446b9b5ab5bc76d6d8a68f5e1e01726a681e8e97145eed8171d2ca0",
  "current_entry_audit": {
    "entryVersion": 49,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 375,
  "current_source_sequence_sha256": "b3a155418446b9b5ab5bc76d6d8a68f5e1e01726a681e8e97145eed8171d2ca0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 48,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9J4L4",
  "selected_historical_entry_version": 48,
  "selected_historical_record_sha256": "4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8",
  "selected_historical_source_sequence_length": 375,
  "selected_historical_source_sequence_sha256": "b3a155418446b9b5ab5bc76d6d8a68f5e1e01726a681e8e97145eed8171d2ca0",
  "selected_historical_version": {
    "accession": "Q9J4L4",
    "database": "Swiss-Prot",
    "entryVersion": 48,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MATRX_MUMPJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9J4L4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":49,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype A (strain Jeryl-Lynn)\",\"taxonId\":11168}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"Matrix protein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26768080\",\"source\":\"PubMed\"}],\"id\":\"SL-0274\",\"value\":\"Virion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0019031\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:viral envelope\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Brgles M.\",\"Bonta M.\",\"Santak M.\",\"Jagusic M.\",\"Forcic D.\",\"Halassy B.\",\"Allmaier G.\",\"Marchetti-Deschmann M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26768080\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12985-016-0463-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"9\",\"id\":\"26768080\",\"journal\":\"Virol. J.\",\"lastPage\":\"9\",\"publicationDate\":\"2016\",\"title\":\"Identification of mumps virus protein and lipid composition by mass spectrometry.\",\"volume\":\"13\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Jeryl-Lynn 5\"}],\"referenceNumber\":3,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:51.770411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807",
  "url": "https://rest.uniprot.org/uniprotkb/Q9J4L4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)

```json
{
  "entry_version": 48,
  "evidence_id": "H1",
  "excerpt": "ID   MATRX_MUMPJ             Reviewed;         375 AA.\nAC   Q9J4L4; Q77IS4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 48.\nDE   RecName: Full=Matrix protein;\nGN   Name=M;\nOS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=11168;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:56.031444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8",
  "url": "https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)

```json
{
  "entry_version": 48,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.\nRC   STRAIN=Jeryl-Lynn 5;\nRX   PubMed=26768080; DOI=10.1186/s12985-016-0463-0;\nRA   Brgles M., Bonta M., Santak M., Jagusic M., Forcic D., Halassy B.,\nRA   Allmaier G., Marchetti-Deschmann M.;\nRT   \"Identification of mumps virus protein and lipid composition by mass\nRT   spectrometry.\";\nRL   Virol. J. 13:9-9(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:56.031444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8",
  "url": "https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)

```json
{
  "entry_version": 48,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000269|PubMed:26768080}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:56.031444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8",
  "url": "https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)

```json
{
  "entry_version": 48,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0019031; C:viral envelope; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:56.031444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8",
  "url": "https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005901\nname: caveola\nnamespace: cellular_component\nalt_id: GO:0016599\ndef: \"A membrane raft that forms small pit, depression, or invagination that communicates with the outside of a cell and extends inward, indenting the cytoplasm and the cell membrane. Examples include flask-shaped invaginations of the plasma membrane in adipocytes associated with caveolin proteins, and minute pits or incuppings of the cell membrane formed during pinocytosis. Caveolae may be pinched off to form free vesicles within the cytoplasm.\" [GOC:mah, ISBN:0721662544, PMID:16645198]\nsynonym: \"caveolae\" EXACT []\nsynonym: \"caveolar membrane\" RELATED []\nxref: Wikipedia:Caveolae\nis_a: GO:0044853 ! plasma membrane raft\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005901",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60572-60582",
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
  "excerpt": "[Term]\nid: GO:0019031\nname: viral envelope\nnamespace: cellular_component\ndef: \"The lipid bilayer of a virion that surrounds the protein capsid. May also contain glycoproteins.\" [GOC:bf, GOC:bm, GOC:jl, ISBN:0781718325, Wikipedia:Viral_envelope]\nsubset: goslim_chembl\nsynonym: \"viral glycoprotein\" RELATED []\nsynonym: \"viral outside membrane\" EXACT []\nxref: Wikipedia:Viral_envelope\nis_a: GO:0036338 ! viral membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019031",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 144681-144691",
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
  "excerpt": "[Term]\nid: GO:0020008\nname: rhoptry\nnamespace: cellular_component\ndef: \"A large, club-shaped secretory organelle that forms part of the apical complex of an apicomplexan parasite, and consists of a bulbous body and a narrow electron-dense neck that extends through the conoid at the apical tip of the parasite. The rhoptry necks serve as ducts through which the contents of the rhoptries are secreted after attachment to the host has been completed and at the commencement of invasion. Rhoptry proteins function in the biogenesis and host organellar association of the parasitophorous vacuole.\" [ISBN:0521664470, PMID:11801218, PMID:16002398]\nsynonym: \"paired organelles\" RELATED []\nsynonym: \"toxoneme\" RELATED []\nxref: Wikipedia:Rhoptry\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0020007 ! apical complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020008",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155180-155190",
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
  "excerpt": "[Term]\nid: GO:0031901\nname: early endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an early endosome.\" [GOC:pz]\nis_a: GO:0010008 ! endosome membrane\nrelationship: part_of GO:0005769 ! early endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031901",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 180777-180784",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0036338\nname: viral membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer of a virion, a complete fully infectious extracellular virus particle.\" [GOC:bm]\nis_a: GO:0044423 ! virion component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0036338",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 226661-226667",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0044423\nname: virion component\nnamespace: cellular_component\nalt_id: GO:0019012\ndef: \"Any constituent part of a virion, a complete fully infectious extracellular virus particle.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"complete virus particle\" RELATED []\nsynonym: \"virion\" RELATED []\nsynonym: \"virion part\" EXACT []\nxref: Wikipedia:Virus\nis_a: GO:0005575 ! cellular_component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044423",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 257048-257062",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
