# temperature_0030

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0030.txt)

**Task:** `temperature`  
**Expected answer:** **C** — 70

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRFSASLLLALTGSAAASPIRAEEEIRVYDLPISLFDDLQGLDAAMKAAGREYIGTSLTVRNDFQEQNIIRTEFGSITPENAQKWDATEPNRGQFTFGSADQHMDWARQNGKHVRCHTLVWYSQLPGWVSNSGFNNATLQQVMQNHINQVMGRYRGRCNHWDVVNEAPRLMAMRLQIGEAYIPIAFRMAAQADPSAKLYYNDYNLEYLGPKVEGAARIVRLVKQYGARIDGVGYQAHLVTEPTPTQSTPTPSEEDLIKALRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN

[Multiple Choices]
A. 45
B. 78
C. 70
D. 46
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

> The sequence-matched UniProt record reports an optimum temperature of 70°C with experimental evidence, supporting choice C. The archived record also matches the sequence and reports the same value.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a secreted enzyme, and transferable knowledge about enzyme families may suggest a broad temperature range. But such features do not meaningfully distinguish an optimum of 70°C from 78°C for this particular protein.


**Missing item-specific fact**

> The experimentally measured optimum temperature for this exact protein, which is not supplied with the sequence.


**Reason**

> Choosing among these close numerical alternatives depends on the target-specific measured optimum; broad sequence or family tendencies are not enough to select 70 over 78 with a meaningful basis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched experimental annotation identifies 70°C as the reported optimum.


### Important caveats

- The experimental support is reported through UniProt evidence linked to a cited publication; the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted enzyme, and transferable knowledge about enzyme families may suggest a broad temperature range. But such features do not meaningfully distinguish an optimum of 70°C from 78°C for this particular protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature for this exact protein, which is not supplied with the sequence.",
    "reason": "Choosing among these close numerical alternatives depends on the target-specific measured optimum; broad sequence or family tendencies are not enough to select 70 over 78 with a meaningful basis."
  },
  "case_id": "temperature_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 70°C with experimental evidence, supporting choice C. The archived record also matches the sequence and reports the same value."
  },
  "important_caveats": [
    "The experimental support is reported through UniProt evidence linked to a cited publication; the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched experimental annotation identifies 70°C as the reported optimum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 70°C with experimental evidence, supporting choice C. The archived record also matches the sequence and reports the same value.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a secreted enzyme, and transferable knowledge about enzyme families may suggest a broad temperature range. But such features do not meaningfully distinguish an optimum of 70°C from 78°C for this particular protein.",
    "missing_item_specific_fact": "The experimentally measured optimum temperature for this exact protein, which is not supplied with the sequence.",
    "reason": "Choosing among these close numerical alternatives depends on the target-specific measured optimum; broad sequence or family tendencies are not enough to select 70 over 78 with a meaningful basis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched experimental annotation identifies 70°C as the reported optimum."
  },
  "important_caveats": [
    "The experimental support is reported through UniProt evidence linked to a cited publication; the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MLB5 (XYNB_HUMIN) explicitly states 'Optimum temperature is 70 degrees Celsius' with evidence code ECO:0000269 (direct assay) from PubMed:23306124. The benchmark sequence matches the source sequence exactly (SHA256 match confirmed). The expected answer of 70°C is directly supported by experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two transferable inferences narrow the choices: (1) Amino acid composition analysis — the sequence shows elevated charged-residue density (many D, E, K, R), reduced thermolabile residues (few C, N, Q relative to length), and features consistent with salt-bridge-rich thermophilic proteins, which distinguishes thermophilic optima (70, 78) from mesophilic ones (45, 46). (2) The N-terminal sequence MRFSASLLLALTGSAAASPIRA is a canonical eukaryotic signal peptide (hydrophobic h-region, AXA cleavage motif), identifying this as a secreted eukaryotic enzyme. Eukaryotic thermophiles (thermophilic fungi, algae) have maximum growth temperatures around 55–65°C and their secreted enzymes typically have optima up to ~70°C; optima of 78°C are characteristic of hyperthermophilic prokaryotes (archaea, thermophilic bacteria), not eukaryotes. This family/kingdom-level biological regularity distinguishes 70 from 78 without needing the specific experimental record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of thermophilic sequence signatures (eliminating 45 and 46) and the eukaryotic signal peptide indicating a fungal/eukaryotic origin (whose enzymes rarely exceed ~70°C optimum, eliminating 78) provides a concrete, transferable inference from general biology of thermophiles across kingdoms. This does not require knowing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While 70 and 78 are both thermophilic, the eukaryotic signal peptide provides a principled reason to prefer 70 over 78 based on known thermal limits of eukaryotic organisms. 45 and 46 are clearly mesophilic and inconsistent with the thermophilic sequence signatures. No pair of choices is truly indistinguishable given the available reasoning.


### Important caveats

- The distinction between 70 and 78°C relies on the general principle that eukaryotic thermophiles have lower thermal limits than prokaryotic hyperthermophiles. While well-supported, this is a probabilistic/biological-tendency argument rather than an absolute rule.
- The specific 70°C value was experimentally measured (ECO:0000269); sequence-based prediction cannot achieve single-degree accuracy in general. The question's multiple-choice format (70 vs 78) makes the kingdom-level distinction sufficient to select the correct option.
- The reviewer-only UniProt evidence confirms the answer but was not available to the evaluated model; the transferable argument stands independently.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two transferable inferences narrow the choices: (1) Amino acid composition analysis — the sequence shows elevated charged-residue density (many D, E, K, R), reduced thermolabile residues (few C, N, Q relative to length), and features consistent with salt-bridge-rich thermophilic proteins, which distinguishes thermophilic optima (70, 78) from mesophilic ones (45, 46). (2) The N-terminal sequence MRFSASLLLALTGSAAASPIRA is a canonical eukaryotic signal peptide (hydrophobic h-region, AXA cleavage motif), identifying this as a secreted eukaryotic enzyme. Eukaryotic thermophiles (thermophilic fungi, algae) have maximum growth temperatures around 55–65°C and their secreted enzymes typically have optima up to ~70°C; optima of 78°C are characteristic of hyperthermophilic prokaryotes (archaea, thermophilic bacteria), not eukaryotes. This family/kingdom-level biological regularity distinguishes 70 from 78 without needing the specific experimental record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of thermophilic sequence signatures (eliminating 45 and 46) and the eukaryotic signal peptide indicating a fungal/eukaryotic origin (whose enzymes rarely exceed ~70°C optimum, eliminating 78) provides a concrete, transferable inference from general biology of thermophiles across kingdoms. This does not require knowing the specific UniProt annotation for this exact protein."
  },
  "case_id": "temperature_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MLB5 (XYNB_HUMIN) explicitly states 'Optimum temperature is 70 degrees Celsius' with evidence code ECO:0000269 (direct assay) from PubMed:23306124. The benchmark sequence matches the source sequence exactly (SHA256 match confirmed). The expected answer of 70°C is directly supported by experimental measurement."
  },
  "important_caveats": [
    "The distinction between 70 and 78°C relies on the general principle that eukaryotic thermophiles have lower thermal limits than prokaryotic hyperthermophiles. While well-supported, this is a probabilistic/biological-tendency argument rather than an absolute rule.",
    "The specific 70°C value was experimentally measured (ECO:0000269); sequence-based prediction cannot achieve single-degree accuracy in general. The question's multiple-choice format (70 vs 78) makes the kingdom-level distinction sufficient to select the correct option.",
    "The reviewer-only UniProt evidence confirms the answer but was not available to the evaluated model; the transferable argument stands independently."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 70 and 78 are both thermophilic, the eukaryotic signal peptide provides a principled reason to prefer 70 over 78 based on known thermal limits of eukaryotic organisms. 45 and 46 are clearly mesophilic and inconsistent with the thermophilic sequence signatures. No pair of choices is truly indistinguishable given the available reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MLB5 (XYNB_HUMIN) explicitly states 'Optimum temperature is 70 degrees Celsius' with evidence code ECO:0000269 (direct assay) from PubMed:23306124. The benchmark sequence matches the source sequence exactly (SHA256 match confirmed). The expected answer of 70°C is directly supported by experimental measurement.",
    "evidence_ids": ["C5", "H3", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two transferable inferences narrow the choices: (1) Amino acid composition analysis — the sequence shows elevated charged-residue density (many D, E, K, R), reduced thermolabile residues (few C, N, Q relative to length), and features consistent with salt-bridge-rich thermophilic proteins, which distinguishes thermophilic optima (70, 78) from mesophilic ones (45, 46). (2) The N-terminal sequence MRFSASLLLALTGSAAASPIRA is a canonical eukaryotic signal peptide (hydrophobic h-region, AXA cleavage motif), identifying this as a secreted eukaryotic enzyme. Eukaryotic thermophiles (thermophilic fungi, algae) have maximum growth temperatures around 55–65°C and their secreted enzymes typically have optima up to ~70°C; optima of 78°C are characteristic of hyperthermophilic prokaryotes (archaea, thermophilic bacteria), not eukaryotes. This family/kingdom-level biological regularity distinguishes 70 from 78 without needing the specific experimental record.",
    "missing_item_specific_fact": "",
    "reason": "The combination of thermophilic sequence signatures (eliminating 45 and 46) and the eukaryotic signal peptide indicating a fungal/eukaryotic origin (whose enzymes rarely exceed ~70°C optimum, eliminating 78) provides a concrete, transferable inference from general biology of thermophiles across kingdoms. This does not require knowing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 70 and 78 are both thermophilic, the eukaryotic signal peptide provides a principled reason to prefer 70 over 78 based on known thermal limits of eukaryotic organisms. 45 and 46 are clearly mesophilic and inconsistent with the thermophilic sequence signatures. No pair of choices is truly indistinguishable given the available reasoning."
  },
  "important_caveats": [
    "The distinction between 70 and 78°C relies on the general principle that eukaryotic thermophiles have lower thermal limits than prokaryotic hyperthermophiles. While well-supported, this is a probabilistic/biological-tendency argument rather than an absolute rule.",
    "The specific 70°C value was experimentally measured (ECO:0000269); sequence-based prediction cannot achieve single-degree accuracy in general. The question's multiple-choice format (70 vs 78) makes the kingdom-level distinction sufficient to select the correct option.",
    "The reviewer-only UniProt evidence confirms the answer but was not available to the evaluated model; the transferable argument stands independently."
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
  "benchmark_sequence_length": 358,
  "benchmark_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 358,
  "current_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MLB5",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "selected_historical_source_sequence_length": 358,
  "selected_historical_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "selected_historical_version": {
    "accession": "M4MLB5",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNB_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MLB5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme towards birchwood xylan\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":306.8}],\"michaelisConstants\":[{\"constant\":1.1,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"substrate\":\"birchwood xylan\",\"unit\":\"mM\"}]},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7.0.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 70 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNB_HUMIN              Reviewed;         358 AA.\nAC   M4MLB5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynB {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=1.1 mM for birchwood xylan {ECO:0000269|PubMed:23306124};\nCC         Vmax=306.8 umol/min/mg enzyme towards birchwood xylan\nCC         {ECO:0000269|PubMed:23306124};\nCC       pH dependence:\nCC         Optimum pH is 7.0. {ECO:0000269|PubMed:23306124};\nCC       Temperature dependence:\nCC         Optimum temperature is 70 degrees Celsius.\nCC         {ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
