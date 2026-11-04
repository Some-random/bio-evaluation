# GO_cellular_component_0158

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0158.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — nucleus

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTEHWGSLPAEDDGGQLTPDKYVPTAAKKLKLDEIRQRGDPQPQEKHHKLELRSALVTQTIEVMKQTEVLQSLIETYSNKNGSSNYLLNPCLMIPEVDFPPENAAELVGSQKFQKPIWFTPTVDTAYSRGDPEAYPEIPSSACRQAMRKVMCGMLRLAGFTDCSESAVQLLTDATEEFLRSFIGEYRGYYDSQPRLQNSTVLQLVPLERAHFAQTGTSLTQVHNYYKHKVLARNRAEIAEFNSVLQEYDKLMKESQSSMQKQHNEFNGHDFLNILDNSATGSSQSIGGMAMGDMLQDLGGSTGSSGTVSSQQMLYGLLDGQISSNTSNMTGTSGNGSTGGNGNGNGATISNFHATFET

[Multiple Choices]
A. lysosomal membrane
B. membrane
C. nucleus
D. cell tip
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

> The sequence matches the protein record, which reports a nuclear location with experimental evidence and a GO nucleus annotation with IDA evidence. This supports choice C, while the exact author source snapshot is unknown.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble SAGA/transcription-complex subunit: it lacks a long hydrophobic transmembrane segment or an evident secretory signal, and its folded, charged composition is compatible with a nuclear protein complex. Family-level knowledge that SAGA participates in eukaryotic transcription at chromatin favors the nucleus over membrane, lysosomal membrane, or cell tip.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from the sequence and the biology of transcription-complex subunits meaningfully distinguishes the nuclear choice from these alternatives. This supports a probabilistic prediction without relying on the target's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives distinguish nuclear localization from membrane-associated and cell-tip locations; no second option is comparably supported.


### Important caveats

- The family-level identification is an inference from the sequence, not an explicit input annotation.
- The source record supports nuclear localization but does not establish that the protein resides exclusively in the nucleus.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble SAGA/transcription-complex subunit: it lacks a long hydrophobic transmembrane segment or an evident secretory signal, and its folded, charged composition is compatible with a nuclear protein complex. Family-level knowledge that SAGA participates in eukaryotic transcription at chromatin favors the nucleus over membrane, lysosomal membrane, or cell tip.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the sequence and the biology of transcription-complex subunits meaningfully distinguishes the nuclear choice from these alternatives. This supports a probabilistic prediction without relying on the target's recorded annotation."
  },
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein record, which reports a nuclear location with experimental evidence and a GO nucleus annotation with IDA evidence. This supports choice C, while the exact author source snapshot is unknown."
  },
  "important_caveats": [
    "The family-level identification is an inference from the sequence, not an explicit input annotation.",
    "The source record supports nuclear localization but does not establish that the protein resides exclusively in the nucleus."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives distinguish nuclear localization from membrane-associated and cell-tip locations; no second option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein record, which reports a nuclear location with experimental evidence and a GO nucleus annotation with IDA evidence. This supports choice C, while the exact author source snapshot is unknown.",
    "evidence_ids": ["C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble SAGA/transcription-complex subunit: it lacks a long hydrophobic transmembrane segment or an evident secretory signal, and its folded, charged composition is compatible with a nuclear protein complex. Family-level knowledge that SAGA participates in eukaryotic transcription at chromatin favors the nucleus over membrane, lysosomal membrane, or cell tip.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the sequence and the biology of transcription-complex subunits meaningfully distinguishes the nuclear choice from these alternatives. This supports a probabilistic prediction without relying on the target's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives distinguish nuclear localization from membrane-associated and cell-tip locations; no second option is comparably supported."
  },
  "important_caveats": [
    "The family-level identification is an inference from the sequence, not an explicit input annotation.",
    "The source record supports nuclear localization but does not establish that the protein resides exclusively in the nucleus."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VX12 (Spt7, SAGA complex subunit, Drosophila melanogaster) records subcellular localization as Nucleus with direct experimental evidence (ECO:0000269, PubMed:20008933 and PubMed:24493646, both reporting SUBCELLULAR LOCATION). The GO annotation GO:0005634 (C:nucleus) is supported by IDA:FlyBase (evidence codes ECO:0000314 from PubMed:16980620 and PubMed:21764853). The SAGA complex is a well-characterized nuclear transcriptional coactivator complex, and multiple independent experimental studies confirm nuclear localization. The expected answer C is strongly supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [C11](#evidence-c11), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits several features that, combined with well-established family-level knowledge, distinguish nucleus from the other options: (1) The N-terminal ~150 residues contain a histone-fold domain (HFD) pattern (alpha-helix-loop-alpha-helix with charged residues, e.g., 'KLELRSALVTQTIEVMKQTEVLQSLIETYSNKNGSSNYLLNPCLMIPEVDFPPENAAELVGSQKFQKPIWFTPTVDTAYSRGDPEAYPEIPSSACRQAMRKVMCGMLRLAGFTDCSESAVQLLTDATEEFLRSFIGEYRGYYDSQPRLQNSTVLQLVPLERAHFAQTGTSLTQVHNYYKHKVLARNRAEIAEFNSVLQEYDKLMKESQSSMQKQHNEFNGHDFLNILDNSATGSSQSIGGMAMGDMLQDLGGSTGSSGTVSSQQMLYGLLDGQISSNTSNMTGTSGNGSTGGNGNGNGATISNFHATFET'), characteristic of SAGA/TFIID complex subunits. (2) The middle region shows WD40 repeat-like patterns (pairs of Trp/Asp in beta-sheet-forming arrangements). (3) The C-terminus is extremely serine/threonine-rich with multiple phosphorylation sites, typical of transcription coactivators. (4) Critically, the sequence lacks any hydrophobic stretch of 20+ residues that would indicate a transmembrane domain, effectively ruling out membrane (B) and lysosomal membrane (A). (5) The SAGA complex is one of the most well-studied transcriptional coactivator complexes in eukaryotic biology; all its subunits (Spt3, Spt5, Spt7, Spt8, Spt20, Ada2, Ada3, Gcn5, etc.) are nuclear proteins involved in histone acetylation and transcription. This family-level knowledge is extensively documented across yeast, human, and Drosophila literature. (6) 'Cell tip' (D) is a term primarily used for yeast/fungal cell biology and is not applicable to Drosophila proteins. Together, the HFD + WD40 architecture, absence of TM domains, and the universal nuclear localization of SAGA complex members provide a strong, transferable inference to nucleus.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence contains recognizable histone-fold domain and WD40 repeat motifs, lacks transmembrane domains, and has a serine-rich C-terminus. Combined with the well-established, extensively documented fact that all SAGA complex subunits are nuclear transcriptional coactivators (known from yeast, human, and other Drosophila SAGA components), a knowledgeable model can meaningfully distinguish nucleus from membrane, lysosomal membrane, and cell tip without needing to look up this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated. Membrane (B) and lysosomal membrane (A) are excluded by the absence of transmembrane domains. Cell tip (D) is a yeast-specific term inapplicable to Drosophila proteins. Nucleus (C) is the only option consistent with the HFD/WD40 architecture and the universal nuclear localization of transcription coactivator complexes.


### Important caveats

- The reviewer identified the protein as Q9VX12 (Spt7_DROME) from dataset metadata, but this accession was not provided to the evaluated model. The model must rely on sequence features and family-level knowledge.
- The histone-fold domain and WD40 repeat identification from sequence alone is approximate without structural data, but these are well-known motifs in transcription complex biology.
- The SAGA complex nuclear localization is supported by multiple independent experimental studies (PubMed:20008933, PubMed:24493646) with direct assay evidence codes.
- The GO term 'membrane' (GO:0016020) is very broad in the ontology, but the protein's lack of TM domains makes it inapplicable as the primary localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits several features that, combined with well-established family-level knowledge, distinguish nucleus from the other options: (1) The N-terminal ~150 residues contain a histone-fold domain (HFD) pattern (alpha-helix-loop-alpha-helix with charged residues, e.g., 'KLELRSALVTQTIEVMKQTEVLQSLIETYSNKNGSSNYLLNPCLMIPEVDFPPENAAELVGSQKFQKPIWFTPTVDTAYSRGDPEAYPEIPSSACRQAMRKVMCGMLRLAGFTDCSESAVQLLTDATEEFLRSFIGEYRGYYDSQPRLQNSTVLQLVPLERAHFAQTGTSLTQVHNYYKHKVLARNRAEIAEFNSVLQEYDKLMKESQSSMQKQHNEFNGHDFLNILDNSATGSSQSIGGMAMGDMLQDLGGSTGSSGTVSSQQMLYGLLDGQISSNTSNMTGTSGNGSTGGNGNGNGATISNFHATFET'), characteristic of SAGA/TFIID complex subunits. (2) The middle region shows WD40 repeat-like patterns (pairs of Trp/Asp in beta-sheet-forming arrangements). (3) The C-terminus is extremely serine/threonine-rich with multiple phosphorylation sites, typical of transcription coactivators. (4) Critically, the sequence lacks any hydrophobic stretch of 20+ residues that would indicate a transmembrane domain, effectively ruling out membrane (B) and lysosomal membrane (A). (5) The SAGA complex is one of the most well-studied transcriptional coactivator complexes in eukaryotic biology; all its subunits (Spt3, Spt5, Spt7, Spt8, Spt20, Ada2, Ada3, Gcn5, etc.) are nuclear proteins involved in histone acetylation and transcription. This family-level knowledge is extensively documented across yeast, human, and Drosophila literature. (6) 'Cell tip' (D) is a term primarily used for yeast/fungal cell biology and is not applicable to Drosophila proteins. Together, the HFD + WD40 architecture, absence of TM domains, and the universal nuclear localization of SAGA complex members provide a strong, transferable inference to nucleus.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable histone-fold domain and WD40 repeat motifs, lacks transmembrane domains, and has a serine-rich C-terminus. Combined with the well-established, extensively documented fact that all SAGA complex subunits are nuclear transcriptional coactivators (known from yeast, human, and other Drosophila SAGA components), a knowledgeable model can meaningfully distinguish nucleus from membrane, lysosomal membrane, and cell tip without needing to look up this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9",
      "C11",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VX12 (Spt7, SAGA complex subunit, Drosophila melanogaster) records subcellular localization as Nucleus with direct experimental evidence (ECO:0000269, PubMed:20008933 and PubMed:24493646, both reporting SUBCELLULAR LOCATION). The GO annotation GO:0005634 (C:nucleus) is supported by IDA:FlyBase (evidence codes ECO:0000314 from PubMed:16980620 and PubMed:21764853). The SAGA complex is a well-characterized nuclear transcriptional coactivator complex, and multiple independent experimental studies confirm nuclear localization. The expected answer C is strongly supported by experimental evidence."
  },
  "important_caveats": [
    "The reviewer identified the protein as Q9VX12 (Spt7_DROME) from dataset metadata, but this accession was not provided to the evaluated model. The model must rely on sequence features and family-level knowledge.",
    "The histone-fold domain and WD40 repeat identification from sequence alone is approximate without structural data, but these are well-known motifs in transcription complex biology.",
    "The SAGA complex nuclear localization is supported by multiple independent experimental studies (PubMed:20008933, PubMed:24493646) with direct assay evidence codes.",
    "The GO term 'membrane' (GO:0016020) is very broad in the ontology, but the protein's lack of TM domains makes it inapplicable as the primary localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated. Membrane (B) and lysosomal membrane (A) are excluded by the absence of transmembrane domains. Cell tip (D) is a yeast-specific term inapplicable to Drosophila proteins. Nucleus (C) is the only option consistent with the HFD/WD40 architecture and the universal nuclear localization of transcription coactivator complexes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VX12 (Spt7, SAGA complex subunit, Drosophila melanogaster) records subcellular localization as Nucleus with direct experimental evidence (ECO:0000269, PubMed:20008933 and PubMed:24493646, both reporting SUBCELLULAR LOCATION). The GO annotation GO:0005634 (C:nucleus) is supported by IDA:FlyBase (evidence codes ECO:0000314 from PubMed:16980620 and PubMed:21764853). The SAGA complex is a well-characterized nuclear transcriptional coactivator complex, and multiple independent experimental studies confirm nuclear localization. The expected answer C is strongly supported by experimental evidence.",
    "evidence_ids": ["C5", "C6", "C9", "C11", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits several features that, combined with well-established family-level knowledge, distinguish nucleus from the other options: (1) The N-terminal ~150 residues contain a histone-fold domain (HFD) pattern (alpha-helix-loop-alpha-helix with charged residues, e.g., 'KLELRSALVTQTIEVMKQTEVLQSLIETYSNKNGSSNYLLNPCLMIPEVDFPPENAAELVGSQKFQKPIWFTPTVDTAYSRGDPEAYPEIPSSACRQAMRKVMCGMLRLAGFTDCSESAVQLLTDATEEFLRSFIGEYRGYYDSQPRLQNSTVLQLVPLERAHFAQTGTSLTQVHNYYKHKVLARNRAEIAEFNSVLQEYDKLMKESQSSMQKQHNEFNGHDFLNILDNSATGSSQSIGGMAMGDMLQDLGGSTGSSGTVSSQQMLYGLLDGQISSNTSNMTGTSGNGSTGGNGNGNGATISNFHATFET'), characteristic of SAGA/TFIID complex subunits. (2) The middle region shows WD40 repeat-like patterns (pairs of Trp/Asp in beta-sheet-forming arrangements). (3) The C-terminus is extremely serine/threonine-rich with multiple phosphorylation sites, typical of transcription coactivators. (4) Critically, the sequence lacks any hydrophobic stretch of 20+ residues that would indicate a transmembrane domain, effectively ruling out membrane (B) and lysosomal membrane (A). (5) The SAGA complex is one of the most well-studied transcriptional coactivator complexes in eukaryotic biology; all its subunits (Spt3, Spt5, Spt7, Spt8, Spt20, Ada2, Ada3, Gcn5, etc.) are nuclear proteins involved in histone acetylation and transcription. This family-level knowledge is extensively documented across yeast, human, and Drosophila literature. (6) 'Cell tip' (D) is a term primarily used for yeast/fungal cell biology and is not applicable to Drosophila proteins. Together, the HFD + WD40 architecture, absence of TM domains, and the universal nuclear localization of SAGA complex members provide a strong, transferable inference to nucleus.",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable histone-fold domain and WD40 repeat motifs, lacks transmembrane domains, and has a serine-rich C-terminus. Combined with the well-established, extensively documented fact that all SAGA complex subunits are nuclear transcriptional coactivators (known from yeast, human, and other Drosophila SAGA components), a knowledgeable model can meaningfully distinguish nucleus from membrane, lysosomal membrane, and cell tip without needing to look up this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated. Membrane (B) and lysosomal membrane (A) are excluded by the absence of transmembrane domains. Cell tip (D) is a yeast-specific term inapplicable to Drosophila proteins. Nucleus (C) is the only option consistent with the HFD/WD40 architecture and the universal nuclear localization of transcription coactivator complexes."
  },
  "important_caveats": [
    "The reviewer identified the protein as Q9VX12 (Spt7_DROME) from dataset metadata, but this accession was not provided to the evaluated model. The model must rely on sequence features and family-level knowledge.",
    "The histone-fold domain and WD40 repeat identification from sequence alone is approximate without structural data, but these are well-known motifs in transcription complex biology.",
    "The SAGA complex nuclear localization is supported by multiple independent experimental studies (PubMed:20008933, PubMed:24493646) with direct assay evidence codes.",
    "The GO term 'membrane' (GO:0016020) is very broad in the ontology, but the protein's lack of TM domains makes it inapplicable as the primary localization."
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
  "benchmark_sequence_length": 359,
  "benchmark_sequence_sha256": "24c8d7f5d596b66562cea83bbe3bbdd5cccf1afe472e54ce1802596000891e36",
  "current_entry_audit": {
    "entryVersion": 169,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-02-07",
    "sequenceVersion": 3
  },
  "current_record_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 359,
  "current_source_sequence_sha256": "24c8d7f5d596b66562cea83bbe3bbdd5cccf1afe472e54ce1802596000891e36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 167,
      "exact_sequence_comparison": "matched",
      "sequence_version": 3
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VX12",
  "selected_historical_entry_version": 167,
  "selected_historical_record_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "selected_historical_source_sequence_length": 359,
  "selected_historical_source_sequence_sha256": "24c8d7f5d596b66562cea83bbe3bbdd5cccf1afe472e54ce1802596000891e36",
  "selected_historical_version": {
    "accession": "Q9VX12",
    "database": "Swiss-Prot",
    "entryVersion": 167,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SPT7_DROME",
    "sequenceVersion": 3
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VX12\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":169,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-02-07\",\"sequenceVersion\":3}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"SAGA complex subunit Spt7\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20008933\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24493646\",\"source\":\"PubMed\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"16980620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"21764853\",\"source\":\"PubMed\"}],\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/27",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"16980620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"21764853\",\"source\":\"PubMed\"}],\"id\":\"GO:0000124\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:SAGA complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/28",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Guelman S.\",\"Suganuma T.\",\"Florens L.\",\"Weake V.\",\"Swanson S.K.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16980620\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.00130-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"7178\",\"id\":\"16980620\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"7189\",\"publicationDate\":\"2006\",\"title\":\"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.\",\"volume\":\"26\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Swanson S.K.\",\"Mushegian A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20008933\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.1846409\"}],\"citationType\":\"journal article\",\"firstPage\":\"2818\",\"id\":\"20008933\",\"journal\":\"Genes Dev.\",\"lastPage\":\"2823\",\"publicationDate\":\"2009\",\"title\":\"A novel histone fold domain-containing protein that replaces TAF6 in Drosophila SAGA is required for SAGA-dependent gene expression.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Dyer J.O.\",\"Seidel C.\",\"Box A.\",\"Swanson S.K.\",\"Peak A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21764853\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.2046211\"}],\"citationType\":\"journal article\",\"firstPage\":\"1499\",\"id\":\"21764853\",\"journal\":\"Genes Dev.\",\"lastPage\":\"1509\",\"publicationDate\":\"2011\",\"title\":\"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.\",\"volume\":\"25\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"DEVELOPMENTAL STAGE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Mohan R.D.\",\"Dialynas G.\",\"Weake V.M.\",\"Liu J.\",\"Martin-Brown S.\",\"Florens L.\",\"Washburn M.P.\",\"Workman J.L.\",\"Abmayr S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24493646\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.225151.113\"}],\"citationType\":\"journal article\",\"firstPage\":\"259\",\"id\":\"24493646\",\"journal\":\"Genes Dev.\",\"lastPage\":\"272\",\"publicationDate\":\"2014\",\"title\":\"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:45.135468+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VX12.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H1",
  "excerpt": "ID   SPT7_DROME              Reviewed;         359 AA.\nAC   Q9VX12; Q8MSV3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-FEB-2006, sequence version 3.\nDT   28-JAN-2026, entry version 167.\nDE   RecName: Full=SAGA complex subunit Spt7 {ECO:0000305};\nGN   Name=Spt7 {ECO:0000303|PubMed:16980620, ECO:0000312|FlyBase:FBgn0030874};\nGN   ORFNames=CG6506 {ECO:0000312|FlyBase:FBgn0030874};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=16980620; DOI=10.1128/mcb.00130-06;\nRA   Guelman S., Suganuma T., Florens L., Weake V., Swanson S.K., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA\nRT   required for histone H3 acetylation.\";\nRL   Mol. Cell. Biol. 26:7178-7189(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=20008933; DOI=10.1101/gad.1846409;\nRA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"A novel histone fold domain-containing protein that replaces TAF6 in\nRT   Drosophila SAGA is required for SAGA-dependent gene expression.\";\nRL   Genes Dev. 23:2818-2823(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H4",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=24493646; DOI=10.1101/gad.225151.113;\nRA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,\nRA   Washburn M.P., Workman J.L., Abmayr S.M.;\nRT   \"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination\nRT   and leads to neural and retinal degeneration.\";\nRL   Genes Dev. 28:259-272(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H5",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:20008933,\nCC       ECO:0000269|PubMed:24493646}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 141-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-172",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)

```json
{
  "entry_version": 167,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0000124; C:SAGA complex; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:49.946751+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071",
  "url": "https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005634\nname: nucleus\nnamespace: cellular_component\ndef: \"A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cell's chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent.\" [GOC:curators]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"cell nucleus\" EXACT []\nsynonym: \"horsetail nucleus\" NARROW [GOC:al, GOC:mah, GOC:vw, PMID:15030757]\nxref: NIF_Subcellular:sao1702920020\nxref: Wikipedia:Cell_nucleus\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005634",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58002-58025",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0016020\nname: membrane\nnamespace: cellular_component\nalt_id: GO:0016021\nalt_id: GO:0098589\nalt_id: GO:0098805\ndef: \"A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it.\" [GOC:dos, GOC:mah, ISBN:0815316194]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"integral component of membrane\" NARROW []\nsynonym: \"integral to membrane\" NARROW []\nsynonym: \"membrane region\" NARROW []\nsynonym: \"region of membrane\" NARROW []\nsynonym: \"transmembrane\" RELATED [GOC:mah]\nsynonym: \"whole membrane\" NARROW []\nxref: Wikipedia:Biological_membrane\nxref: Wikipedia:Transmembrane_protein\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 122626-122650",
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
  "excerpt": "[Term]\nid: GO:0051286\nname: cell tip\nnamespace: cellular_component\ndef: \"The region at the end of the longest axis of a cylindrical or elongated cell.\" [GOC:ai, GOC:mah]\ncomment: Note that this term differs from 'cell pole ; GO:0060187' in that it is applicable to the thin ends of elongated cells, such as the ends of axons or dendrites.\nsynonym: \"cell end\" EXACT [GOC:mah]\nis_a: GO:0060187 ! cell pole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051286",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 325114-325122",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
