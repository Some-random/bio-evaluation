# GO_cellular_component_0193

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0193.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — lysosomal membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTRPYIKRLSFTLLDSITDKDPMVQEQVCSALCSLGDAQPDETLHACEEYLRQHDKLAHPYRTKILRAMETVLSSHIHDLDKDTAGAVILLATSEMTRTKELDCDWQQAAGSVLVAVGKRFTNQVMEEVLSRFQPGMLPHSSVLHTLANLSVSNAFDMVPFLPSILSTMLPMLSMAKQDALKVVFCGALQHFSESILEYLANLDQAPDPTVRKDTFGADIFGAYDVLFHHWLQSRDAKLRLAVVAALGPMSHLLPSERLEEQLPKLLPAVLGLYKKHAEAFQISKSLGQILEAAVNVSSRTLEVQLDALLVALHAQICVPVESSSPLVMNSQKEVLRCFTVLACCSPDRLLAFLLPRLDTSNERLRVGTLQILRHIINSAAAQMEAKQPFILSSMRLPLLDTNDKVKRAVVQVISAMAHHGYLEQPGGEVMVEYIVQQCALPAEEPEKPGPDGEDLAADSVRAVSIRTLYLVSTTVDRMNSVLWPYLLEFLTPVRFTAALTPLCRSLVHLALKRQEAGADDFLIQYNANANLPSPFAMTTRLLVVSSNPYLGDGRGAASLRLLKVMHQNIHPFLGQRWETTMPMLLEYLDEHTEESLSLKEWEEKLLMFLRDTLAVVSDNIWICQLSQEMCKQLPSYSGTPQEKNFLYKCIGTTLGAASSKEVVRKHLRELLETARYQEEAEQEGLACCFGICAITHLEDTLAQLEDFVRSDVFRKSTGIFSIFKDRSEHEVERMKSCLILCYGHVAAQAPRELVLARVESDILRSMFQCFNTKVLGIKVETKDPALKLCLVQSLCMVSQAMCSSAQASSFHFLRKTELVTQMMEFIRAEPPDCLRTPIRKKAMLACTYLVNLEPALEEQTQADVVHSCLHSVMALPPEAEGGDGVGREPLYLDTVCALEDLLTRLLRQNMTPQGLQIMVEHLSPWIKSPRGHERARALGLGACLLEFFQEHLLVSTLVPFHNLGLLVGLFAPRCADTWTTTRQKAVGCVYSLLYLQLGYEGFSRDHRDDVAERLLTLQDGLVNADPTILFHTCHSIAQVIAKRLPSDQLISLLLTVFESLGDPDKNCSRAATVMINCLLKERGNVLLEKVPEIVSVLRAKLRDTQEEHVLPAAQHSVYLLASQHCEAVVSSLLGSPLPFDSHTCALWRALAVEPGLTAQVLELLLEKMSKDVPFKESRAFLLGSTADRVATLLPLAATCALYEVLSAPSSGTVVLELYPQLFAALLLRVSCTVGVQLPRNLQAKERRSTSPARAARNLDPCSSAVDALQALLLRSGSQDMLRCVELERGWELLKTSAGHEDGVAQLASSMAKYAGPRLPPVTKALACTQNSVYEIQRVTSTAFLAELLSSNVVNDLMLLEPLLDNLTARLKDSSASVRRLVLRGLANMASGSPDKVRAHGPQLLTAMVSGLDDGDEPHSPVALEAMVGLSRLLDLVEPWDLRLVLLHTTIRIRPFFDSEKVEFRTASIRLFGHLNKACHGDCEDVFLEQVVGGLVPLLLHLRDPQVPVASACKFALCMCVPHLECAELAAAFYKYLQEGRSVHFGEFLNSTCKHLMHHFPDLLGRLVSTNLFYFKSSWDDVRAAAPMFTGFLVLHAEPEQKTQVDLEQLIVALQLLLKDPVPGVREKAAETLGRLVKFA

[Multiple Choices]
A. nuclear pore
B. lysosomal membrane
C. SAGA complex
D. striated muscle dense body
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

> The sequence-matched historical UniProt entry annotates lysosome membrane localization and says the protein is recruited there by RAB7. The annotation is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein-specific or homolog-based annotation that this protein is recruited to the lysosomal membrane by RAB7.


**Reason**

> The sequence is long and rich in helical-repeat-like regions, but that general architecture does not meaningfully distinguish lysosomal membrane localization from the offered alternatives. It has no obvious membrane-spanning segment; peripheral recruitment is possible, but the RAB7-dependent lysosomal localization is not established by the provided sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied annotation supports B, and the other choices are not established as plausible alternative locations by the original input.


### Important caveats

- The supporting localization annotation is similarity-based rather than direct experimental evidence for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific or homolog-based annotation that this protein is recruited to the lysosomal membrane by RAB7.",
    "reason": "The sequence is long and rich in helical-repeat-like regions, but that general architecture does not meaningfully distinguish lysosomal membrane localization from the offered alternatives. It has no obvious membrane-spanning segment; peripheral recruitment is possible, but the RAB7-dependent lysosomal localization is not established by the provided sequence alone."
  },
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates lysosome membrane localization and says the protein is recruited there by RAB7. The annotation is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting localization annotation is similarity-based rather than direct experimental evidence for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports B, and the other choices are not established as plausible alternative locations by the original input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates lysosome membrane localization and says the protein is recruited there by RAB7. The annotation is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein-specific or homolog-based annotation that this protein is recruited to the lysosomal membrane by RAB7.",
    "reason": "The sequence is long and rich in helical-repeat-like regions, but that general architecture does not meaningfully distinguish lysosomal membrane localization from the offered alternatives. It has no obvious membrane-spanning segment; peripheral recruitment is possible, but the RAB7-dependent lysosomal localization is not established by the provided sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports B, and the other choices are not established as plausible alternative locations by the original input."
  },
  "important_caveats": [
    "The supporting localization annotation is similarity-based rather than direct experimental evidence for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (E0CZ22, MROH1_MOUSE) annotates GO:0005765 (C:lysosomal membrane) with evidence code ISS:UniProtKB, inferred from sequence similarity to human MROH1 (Q8NDA8). The subcellular location comment states 'Lysosome membrane' with the note 'Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B).' This is a computational inference from orthology rather than direct experimental evidence for the mouse protein, but it is the recorded annotation and supports choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model could partially eliminate options A, C, and D by domain architecture: nuclear pore proteins typically contain FG-repeats and nucleoporin-specific domains absent here; SAGA complex subunits contain HAT, DUB, or specific scaffold domains not present in this Maestro heat-like repeat protein; striated muscle dense body proteins are vinculin/talin/alpha-actinin-type with actin-binding domains, which this sequence lacks. However, this negative elimination does not positively identify lysosomal membrane. The Maestro heat-like repeat family is not a family with a well-known general lysosomal localization; the RAB7-dependent recruitment to the lysosome membrane is a specific finding for MROH1 (and its human ortholog Q8NDA8), not a general property transferable from other Maestro repeat proteins. No obvious sequence features (transmembrane helices, lipid modifications, RAB-binding motifs, mannose-6-phosphate signals) in the provided sequence positively indicate lysosomal membrane residence.


**Missing item-specific fact**

> The specific annotation that MROH1 is recruited to the lysosomal membrane by RAB7 (RAB7A/RAB7B), which is a protein-specific finding (ISS from human Q8NDA8) rather than a general Maestro-repeat family property. Without this annotation or knowledge of the RAB7-interaction literature, the sequence alone does not positively indicate lysosomal membrane over other cytoplasmic or peripheral-membrane localizations.


**Reason**

> While elimination of A, C, and D by domain architecture is feasible, it is negative reasoning that merely removes alternatives without positively identifying B. The positive assignment to lysosomal membrane requires the specific MROH1 annotation (recruitment by RAB7), which is a fact about this particular protein (inferred from its human ortholog) and is not derivable from general Maestro-repeat family knowledge or sequence features visible in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D can be reasonably excluded by domain architecture (no FG repeats, no HAT/DUB/SAGA domains, no muscle-specific actin-binding domains). Among the four given choices, B is the only remaining option, though the positive justification for lysosomal membrane is weak from sequence alone.


### Important caveats

- The UniProt annotation for lysosomal membrane is ISS (Inferred from Sequence or structural Similarity) from human MROH1 (Q8NDA8), not direct experimental evidence for the mouse protein.
- The Maestro heat-like repeat family is relatively obscure; general family-level transfer of localization is not well-established beyond MROH1 itself.
- The elimination argument (not A, not C, not D) provides some narrowing but is not a positive identification of lysosomal membrane.
- The protein is also annotated GO:0005737 (C:cytoplasm; IBA:GO_Central) in the historical record, indicating it may have a cytoplasmic pool as well.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could partially eliminate options A, C, and D by domain architecture: nuclear pore proteins typically contain FG-repeats and nucleoporin-specific domains absent here; SAGA complex subunits contain HAT, DUB, or specific scaffold domains not present in this Maestro heat-like repeat protein; striated muscle dense body proteins are vinculin/talin/alpha-actinin-type with actin-binding domains, which this sequence lacks. However, this negative elimination does not positively identify lysosomal membrane. The Maestro heat-like repeat family is not a family with a well-known general lysosomal localization; the RAB7-dependent recruitment to the lysosome membrane is a specific finding for MROH1 (and its human ortholog Q8NDA8), not a general property transferable from other Maestro repeat proteins. No obvious sequence features (transmembrane helices, lipid modifications, RAB-binding motifs, mannose-6-phosphate signals) in the provided sequence positively indicate lysosomal membrane residence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation that MROH1 is recruited to the lysosomal membrane by RAB7 (RAB7A/RAB7B), which is a protein-specific finding (ISS from human Q8NDA8) rather than a general Maestro-repeat family property. Without this annotation or knowledge of the RAB7-interaction literature, the sequence alone does not positively indicate lysosomal membrane over other cytoplasmic or peripheral-membrane localizations.",
    "reason": "While elimination of A, C, and D by domain architecture is feasible, it is negative reasoning that merely removes alternatives without positively identifying B. The positive assignment to lysosomal membrane requires the specific MROH1 annotation (recruitment by RAB7), which is a fact about this particular protein (inferred from its human ortholog) and is not derivable from general Maestro-repeat family knowledge or sequence features visible in the input."
  },
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (E0CZ22, MROH1_MOUSE) annotates GO:0005765 (C:lysosomal membrane) with evidence code ISS:UniProtKB, inferred from sequence similarity to human MROH1 (Q8NDA8). The subcellular location comment states 'Lysosome membrane' with the note 'Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B).' This is a computational inference from orthology rather than direct experimental evidence for the mouse protein, but it is the recorded annotation and supports choice B."
  },
  "important_caveats": [
    "The UniProt annotation for lysosomal membrane is ISS (Inferred from Sequence or structural Similarity) from human MROH1 (Q8NDA8), not direct experimental evidence for the mouse protein.",
    "The Maestro heat-like repeat family is relatively obscure; general family-level transfer of localization is not well-established beyond MROH1 itself.",
    "The elimination argument (not A, not C, not D) provides some narrowing but is not a positive identification of lysosomal membrane.",
    "The protein is also annotated GO:0005737 (C:cytoplasm; IBA:GO_Central) in the historical record, indicating it may have a cytoplasmic pool as well."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D can be reasonably excluded by domain architecture (no FG repeats, no HAT/DUB/SAGA domains, no muscle-specific actin-binding domains). Among the four given choices, B is the only remaining option, though the positive justification for lysosomal membrane is weak from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (E0CZ22, MROH1_MOUSE) annotates GO:0005765 (C:lysosomal membrane) with evidence code ISS:UniProtKB, inferred from sequence similarity to human MROH1 (Q8NDA8). The subcellular location comment states 'Lysosome membrane' with the note 'Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B).' This is a computational inference from orthology rather than direct experimental evidence for the mouse protein, but it is the recorded annotation and supports choice B.",
    "evidence_ids": ["C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model could partially eliminate options A, C, and D by domain architecture: nuclear pore proteins typically contain FG-repeats and nucleoporin-specific domains absent here; SAGA complex subunits contain HAT, DUB, or specific scaffold domains not present in this Maestro heat-like repeat protein; striated muscle dense body proteins are vinculin/talin/alpha-actinin-type with actin-binding domains, which this sequence lacks. However, this negative elimination does not positively identify lysosomal membrane. The Maestro heat-like repeat family is not a family with a well-known general lysosomal localization; the RAB7-dependent recruitment to the lysosome membrane is a specific finding for MROH1 (and its human ortholog Q8NDA8), not a general property transferable from other Maestro repeat proteins. No obvious sequence features (transmembrane helices, lipid modifications, RAB-binding motifs, mannose-6-phosphate signals) in the provided sequence positively indicate lysosomal membrane residence.",
    "missing_item_specific_fact": "The specific annotation that MROH1 is recruited to the lysosomal membrane by RAB7 (RAB7A/RAB7B), which is a protein-specific finding (ISS from human Q8NDA8) rather than a general Maestro-repeat family property. Without this annotation or knowledge of the RAB7-interaction literature, the sequence alone does not positively indicate lysosomal membrane over other cytoplasmic or peripheral-membrane localizations.",
    "reason": "While elimination of A, C, and D by domain architecture is feasible, it is negative reasoning that merely removes alternatives without positively identifying B. The positive assignment to lysosomal membrane requires the specific MROH1 annotation (recruitment by RAB7), which is a fact about this particular protein (inferred from its human ortholog) and is not derivable from general Maestro-repeat family knowledge or sequence features visible in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D can be reasonably excluded by domain architecture (no FG repeats, no HAT/DUB/SAGA domains, no muscle-specific actin-binding domains). Among the four given choices, B is the only remaining option, though the positive justification for lysosomal membrane is weak from sequence alone."
  },
  "important_caveats": [
    "The UniProt annotation for lysosomal membrane is ISS (Inferred from Sequence or structural Similarity) from human MROH1 (Q8NDA8), not direct experimental evidence for the mouse protein.",
    "The Maestro heat-like repeat family is relatively obscure; general family-level transfer of localization is not well-established beyond MROH1 itself.",
    "The elimination argument (not A, not C, not D) provides some narrowing but is not a positive identification of lysosomal membrane.",
    "The protein is also annotated GO:0005737 (C:cytoplasm; IBA:GO_Central) in the historical record, indicating it may have a cytoplasmic pool as well."
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
  "benchmark_sequence_length": 1640,
  "benchmark_sequence_sha256": "935c243be9edd13819d4b8ea088b7d29b7698bfcf4baf50c2369cd3fa82b77e8",
  "current_entry_audit": {
    "entryVersion": 95,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-10-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1640,
  "current_source_sequence_sha256": "935c243be9edd13819d4b8ea088b7d29b7698bfcf4baf50c2369cd3fa82b77e8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 93,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E0CZ22",
  "selected_historical_entry_version": 93,
  "selected_historical_record_sha256": "ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316",
  "selected_historical_source_sequence_length": 1640,
  "selected_historical_source_sequence_sha256": "935c243be9edd13819d4b8ea088b7d29b7698bfcf4baf50c2369cd3fa82b77e8",
  "selected_historical_version": {
    "accession": "E0CZ22",
    "database": "Swiss-Prot",
    "entryVersion": 93,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MROH1_MOUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E0CZ22\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:53.277334+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "url": "https://rest.uniprot.org/uniprotkb/E0CZ22.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":95,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-10-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:53.277334+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "url": "https://rest.uniprot.org/uniprotkb/E0CZ22.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:53.277334+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "url": "https://rest.uniprot.org/uniprotkb/E0CZ22.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"Maestro heat-like repeat-containing protein family member 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:53.277334+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "url": "https://rest.uniprot.org/uniprotkb/E0CZ22.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NDA8\",\"source\":\"UniProtKB\"}],\"value\":\"Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B)\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NDA8\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0157\",\"value\":\"Lysosome membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:53.277334+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "url": "https://rest.uniprot.org/uniprotkb/E0CZ22.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005765\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:lysosomal membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/43",
  "retrieved_utc": "2026-11-02T04:27:53.277334+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0",
  "url": "https://rest.uniprot.org/uniprotkb/E0CZ22.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)

```json
{
  "entry_version": 93,
  "evidence_id": "H1",
  "excerpt": "ID   MROH1_MOUSE             Reviewed;        1640 AA.\nAC   E0CZ22; D3Z624; E0CYC5; Q80T84;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-OCT-2010, sequence version 1.\nDT   28-JAN-2026, entry version 93.\nDE   RecName: Full=Maestro heat-like repeat-containing protein family member 1;\nGN   Name=Mroh1 {ECO:0000312|MGI:MGI:2442558}; Synonyms=Kiaa1833;\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.152074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316",
  "url": "https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)

```json
{
  "entry_version": 93,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Lysosome membrane {ECO:0000250|UniProtKB:Q8NDA8}.\nCC       Note=Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B).\nCC       {ECO:0000250|UniProtKB:Q8NDA8}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.152074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316",
  "url": "https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)

```json
{
  "entry_version": 93,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.152074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316",
  "url": "https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)

```json
{
  "entry_version": 93,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005765; C:lysosomal membrane; ISS:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.152074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316",
  "url": "https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000124\nname: SAGA complex\nnamespace: cellular_component\nalt_id: GO:0000125\nalt_id: GO:0030914\ndef: \"A SAGA-type histone acetyltransferase complex that deubiquitinates H2A and/or H2B. This complex is organized into several functional submodules: a structural core including the activator binding module and consisting of ADA1 or a homolog, members of the SPT and TAF protein families as well as promotor recruitment factor TRRAP/TRA1, a histone acetyltransferase (HAT) module consisting of GCN5/KAT2A or PCAF/KAT2B, ADA2, ADA3/NGG1, and SGF29 or homologues thereof, a histone deubiquitinase (DUB) module consisting of ATXN7/SGF73, ATXN7L3/SGF11, ENY2/SUS1 and USP22/UBP8 or homologues thereof, and in some taxa a splicing module consisting of SF3B3 and SF3B5 or homologues thereof (not in fungi). In budding yeast also contains Spt8 which distinguishes it from SAGA-like (SLIK) complex (GO:0046695).\" [PMID:10637607, PMID:17337012, PMID:19056896, PMID:20838651, PMID:33004486]\nsynonym: \"PCAF complex\" NARROW []\nsynonym: \"PCAF histone acetylase-associated complex\" NARROW []\nsynonym: \"Spt-Ada-Gcn5-acetyltransferase complex\" EXACT []\nsynonym: \"SPT3-TAF9-GCN5 acetylase complex\" RELATED [GOC:rl, PMID:18838386]\nsynonym: \"SPT3-TAF9-PCAF acetylase complex\" NARROW [PMID:18838386]\nsynonym: \"STAGA coactivator complex\" RELATED []\nsynonym: \"STAGA complex\" RELATED [PMID:32616828, PMID:33004486, PMID:34112237]\nis_a: GO:0070461 ! SAGA-type complex\nis_a: GO:1905368 ! peptidase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000124",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1252-1268",
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
  "excerpt": "[Term]\nid: GO:0005643\nname: nuclear pore\nnamespace: cellular_component\nalt_id: GO:0005644\ndef: \"A protein complex providing a discrete opening in the nuclear envelope of a eukaryotic cell, where the inner and outer nuclear membranes are joined.\" [ISBN:0198547684]\nsubset: goslim_pir\nsynonym: \"NPC\" EXACT []\nsynonym: \"nuclear pore complex\" EXACT []\nsynonym: \"nuclear pore membrane protein\" NARROW []\nsynonym: \"nucleopore\" EXACT [GOC:al, PMID:7603572]\nxref: NIF_Subcellular:sao220861693\nxref: Wikipedia:Nuclear_pore\nis_a: GO:0140513 ! nuclear protein-containing complex\nrelationship: part_of GO:0005635 ! nuclear envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005643",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58104-58119",
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
  "excerpt": "[Term]\nid: GO:0005765\nname: lysosomal membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the lysosome and separating its contents from the cell cytoplasm.\" [GOC:ai]\nsynonym: \"lysosome membrane\" EXACT []\nis_a: GO:0098852 ! lytic vacuole membrane\nrelationship: part_of GO:0005764 ! lysosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005765",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59259-59267",
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
  "excerpt": "[Term]\nid: GO:0055120\nname: striated muscle dense body\nnamespace: cellular_component\ndef: \"A vinculin-containing myofibril attachment structure of striated muscle that connects sarcomeres to the extracellular matrix. In nematode body wall muscle, the dense body performs the dual role of Z-disk and costamere.\" [GOC:kmv, PMID:17492481]\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0043292 ! contractile muscle fiber\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0055120",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 343547-343554",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 193. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
