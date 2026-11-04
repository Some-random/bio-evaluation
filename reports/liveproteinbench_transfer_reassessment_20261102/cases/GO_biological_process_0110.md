# GO_biological_process_0110

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0110.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — glycerophospholipid biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. regulation of transcription by RNA polymerase II
B. chromatin organization
C. response to muramyl dipeptide
D. glycerophospholipid biosynthetic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched record reports experimentally supported cardiolipin synthesis from CDP-diacylglycerol and phosphatidylglycerol (C5). Cardiolipin biosynthesis is a child of glycerophospholipid biosynthesis, so the broader option D is supported. The direct cardiolipin process annotation is IDA; the supplied record also has a glycerophospholipid-biosynthesis annotation with IBA evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6), [GO4](#evidence-go4), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 215-residue sequence is dominated by hydrophobic stretches consistent with a small multipass membrane protein, rather than a typical soluble transcription or chromatin regulator. In the context of these choices, that pattern favors a membrane-associated biosynthetic function such as glycerophospholipid synthesis over A or B; the sequence does not by itself establish the precise lipid pathway, so this is a probabilistic family-level inference rather than proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a meaningful, if not definitive, basis to distinguish D from the nuclear-process alternatives. The reviewer-only functional annotation corroborates the choice but is not needed to make the transferable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D among the offered options describes the relevant lipid-biosynthetic process; the more specific cardiolipin biosynthesis term is not offered.


### Important caveats

- Multipass membrane topology alone does not identify a protein's biological process or prove a lipid-biosynthesis role.
- The reviewer-only record's experimental evidence supports cardiolipin synthesis; the broader glycerophospholipid term is an ontology parent and also appears with IBA evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 215-residue sequence is dominated by hydrophobic stretches consistent with a small multipass membrane protein, rather than a typical soluble transcription or chromatin regulator. In the context of these choices, that pattern favors a membrane-associated biosynthetic function such as glycerophospholipid synthesis over A or B; the sequence does not by itself establish the precise lipid pathway, so this is a probabilistic family-level inference rather than proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful, if not definitive, basis to distinguish D from the nuclear-process alternatives. The reviewer-only functional annotation corroborates the choice but is not needed to make the transferable inference."
  },
  "case_id": "GO_biological_process_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H6",
      "GO4",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports experimentally supported cardiolipin synthesis from CDP-diacylglycerol and phosphatidylglycerol (C5). Cardiolipin biosynthesis is a child of glycerophospholipid biosynthesis, so the broader option D is supported. The direct cardiolipin process annotation is IDA; the supplied record also has a glycerophospholipid-biosynthesis annotation with IBA evidence."
  },
  "important_caveats": [
    "Multipass membrane topology alone does not identify a protein's biological process or prove a lipid-biosynthesis role.",
    "The reviewer-only record's experimental evidence supports cardiolipin synthesis; the broader glycerophospholipid term is an ontology parent and also appears with IBA evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D among the offered options describes the relevant lipid-biosynthetic process; the more specific cardiolipin biosynthesis term is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports experimentally supported cardiolipin synthesis from CDP-diacylglycerol and phosphatidylglycerol (C5). Cardiolipin biosynthesis is a child of glycerophospholipid biosynthesis, so the broader option D is supported. The direct cardiolipin process annotation is IDA; the supplied record also has a glycerophospholipid-biosynthesis annotation with IBA evidence.",
    "evidence_ids": ["C5", "C6", "H6", "GO4", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 215-residue sequence is dominated by hydrophobic stretches consistent with a small multipass membrane protein, rather than a typical soluble transcription or chromatin regulator. In the context of these choices, that pattern favors a membrane-associated biosynthetic function such as glycerophospholipid synthesis over A or B; the sequence does not by itself establish the precise lipid pathway, so this is a probabilistic family-level inference rather than proof.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful, if not definitive, basis to distinguish D from the nuclear-process alternatives. The reviewer-only functional annotation corroborates the choice but is not needed to make the transferable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D among the offered options describes the relevant lipid-biosynthetic process; the more specific cardiolipin biosynthesis term is not offered."
  },
  "important_caveats": [
    "Multipass membrane topology alone does not identify a protein's biological process or prove a lipid-biosynthesis role.",
    "The reviewer-only record's experimental evidence supports cardiolipin synthesis; the broader glycerophospholipid term is an ontology parent and also appears with IBA evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is annotated as cardiolipin synthase (CMP-forming, EC 2.7.8.41), which catalyzes the transfer of a phosphatidyl group from CDP-diacylglycerol to phosphatidylglycerol to form cardiolipin. Cardiolipin is a glycerophospholipid (diphosphatidylglycerol). The GO ontology hierarchy shows GO:0032049 (cardiolipin biosynthetic process) is_a GO:0006655 (phosphatidylglycerol biosynthetic process) is_a GO:0046474 (glycerophospholipid biosynthetic process). The UniProt entry directly assigns GO:0046474 via IBA evidence, and the primary experimental annotation (IDA, PubMed:19439403) is GO:0032049, a child of GO:0046474. Among the four offered options, D is the only one consistent with the protein's demonstrated enzymatic function in phospholipid synthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO4](#evidence-go4), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 215-aa sequence is a small, highly hydrophobic membrane protein with multiple predicted transmembrane helices (e.g., 'MARLAGVPLFLWLILR', 'WALLVLALSGVSDYLDGKLARR', 'YILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR', 'FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD'). This topology is characteristic of integral membrane lipid-metabolism enzymes, not nuclear transcription factors (A), chromatin remodelers (B), or large multi-domain immune receptors (C). Options A and B describe eukaryotic nuclear processes; the sequence lacks any DNA-binding domain, histone fold, or nuclear localization signal, and its composition is consistent with a bacterial membrane enzyme. Option C (response to muramyl dipeptide) involves NOD-like pattern-recognition receptors with NACHT, CARD, and LRR domains—none of which are present in this small TM-rich protein. The sequence contains a 'GSGW' motif within 'LLLSDGSGWIASLAAVFGW' reminiscent of the CDP-alcohol phosphotransferase superfamily (which includes CDP-diacylglycerol synthase, phosphatidylglycerophosphate synthase, and cardiolipin synthase), all of which participate in glycerophospholipid biosynthesis. Thus, family-level recognition of membrane-associated small lipid enzymes plus the CDP-alcohol phosphotransferase motif pattern meaningfully distinguishes D from A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The membrane topology, small size, absence of nuclear/immune domains, and the CDP-alcohol phosphotransferase-like motif provide a transferable biological argument from general knowledge of lipid-metabolism enzyme families and immune receptor architecture that distinguishes D from the other three options without requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B describe eukaryotic nuclear processes incompatible with a bacterial membrane protein. Option C requires large multi-domain immune receptors absent here. Option D is the only choice consistent with a small integral-membrane enzyme involved in phospholipid synthesis. No other option is defensible.


### Important caveats

- The most specific experimental annotation is GO:0032049 (cardiolipin biosynthetic process, IDA evidence); the offered option D (glycerophospholipid biosynthetic process, GO:0046474) is the broader parent term also directly annotated via IBA. Since 'cardiolipin biosynthetic process' is not among the choices, D is the best available answer.
- The CDP-alcohol phosphotransferase motif recognition is suggestive but not definitive from sequence alone; the primary discriminator is the overall membrane-protein topology and absence of features required by the other options.
- The UniProt entry also annotates GO:0007009 (plasma membrane organization, IMP), but this term is not among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 215-aa sequence is a small, highly hydrophobic membrane protein with multiple predicted transmembrane helices (e.g., 'MARLAGVPLFLWLILR', 'WALLVLALSGVSDYLDGKLARR', 'YILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR', 'FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD'). This topology is characteristic of integral membrane lipid-metabolism enzymes, not nuclear transcription factors (A), chromatin remodelers (B), or large multi-domain immune receptors (C). Options A and B describe eukaryotic nuclear processes; the sequence lacks any DNA-binding domain, histone fold, or nuclear localization signal, and its composition is consistent with a bacterial membrane enzyme. Option C (response to muramyl dipeptide) involves NOD-like pattern-recognition receptors with NACHT, CARD, and LRR domains—none of which are present in this small TM-rich protein. The sequence contains a 'GSGW' motif within 'LLLSDGSGWIASLAAVFGW' reminiscent of the CDP-alcohol phosphotransferase superfamily (which includes CDP-diacylglycerol synthase, phosphatidylglycerophosphate synthase, and cardiolipin synthase), all of which participate in glycerophospholipid biosynthesis. Thus, family-level recognition of membrane-associated small lipid enzymes plus the CDP-alcohol phosphotransferase motif pattern meaningfully distinguishes D from A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The membrane topology, small size, absence of nuclear/immune domains, and the CDP-alcohol phosphotransferase-like motif provide a transferable biological argument from general knowledge of lipid-metabolism enzyme families and immune receptor architecture that distinguishes D from the other three options without requiring recall of this specific protein's database annotation."
  },
  "case_id": "GO_biological_process_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H4",
      "H5",
      "H6",
      "GO4",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The protein is annotated as cardiolipin synthase (CMP-forming, EC 2.7.8.41), which catalyzes the transfer of a phosphatidyl group from CDP-diacylglycerol to phosphatidylglycerol to form cardiolipin. Cardiolipin is a glycerophospholipid (diphosphatidylglycerol). The GO ontology hierarchy shows GO:0032049 (cardiolipin biosynthetic process) is_a GO:0006655 (phosphatidylglycerol biosynthetic process) is_a GO:0046474 (glycerophospholipid biosynthetic process). The UniProt entry directly assigns GO:0046474 via IBA evidence, and the primary experimental annotation (IDA, PubMed:19439403) is GO:0032049, a child of GO:0046474. Among the four offered options, D is the only one consistent with the protein's demonstrated enzymatic function in phospholipid synthesis."
  },
  "important_caveats": [
    "The most specific experimental annotation is GO:0032049 (cardiolipin biosynthetic process, IDA evidence); the offered option D (glycerophospholipid biosynthetic process, GO:0046474) is the broader parent term also directly annotated via IBA. Since 'cardiolipin biosynthetic process' is not among the choices, D is the best available answer.",
    "The CDP-alcohol phosphotransferase motif recognition is suggestive but not definitive from sequence alone; the primary discriminator is the overall membrane-protein topology and absence of features required by the other options.",
    "The UniProt entry also annotates GO:0007009 (plasma membrane organization, IMP), but this term is not among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B describe eukaryotic nuclear processes incompatible with a bacterial membrane protein. Option C requires large multi-domain immune receptors absent here. Option D is the only choice consistent with a small integral-membrane enzyme involved in phospholipid synthesis. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is annotated as cardiolipin synthase (CMP-forming, EC 2.7.8.41), which catalyzes the transfer of a phosphatidyl group from CDP-diacylglycerol to phosphatidylglycerol to form cardiolipin. Cardiolipin is a glycerophospholipid (diphosphatidylglycerol). The GO ontology hierarchy shows GO:0032049 (cardiolipin biosynthetic process) is_a GO:0006655 (phosphatidylglycerol biosynthetic process) is_a GO:0046474 (glycerophospholipid biosynthetic process). The UniProt entry directly assigns GO:0046474 via IBA evidence, and the primary experimental annotation (IDA, PubMed:19439403) is GO:0032049, a child of GO:0046474. Among the four offered options, D is the only one consistent with the protein's demonstrated enzymatic function in phospholipid synthesis.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H4", "H5", "H6", "GO4", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 215-aa sequence is a small, highly hydrophobic membrane protein with multiple predicted transmembrane helices (e.g., 'MARLAGVPLFLWLILR', 'WALLVLALSGVSDYLDGKLARR', 'YILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR', 'FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD'). This topology is characteristic of integral membrane lipid-metabolism enzymes, not nuclear transcription factors (A), chromatin remodelers (B), or large multi-domain immune receptors (C). Options A and B describe eukaryotic nuclear processes; the sequence lacks any DNA-binding domain, histone fold, or nuclear localization signal, and its composition is consistent with a bacterial membrane enzyme. Option C (response to muramyl dipeptide) involves NOD-like pattern-recognition receptors with NACHT, CARD, and LRR domains—none of which are present in this small TM-rich protein. The sequence contains a 'GSGW' motif within 'LLLSDGSGWIASLAAVFGW' reminiscent of the CDP-alcohol phosphotransferase superfamily (which includes CDP-diacylglycerol synthase, phosphatidylglycerophosphate synthase, and cardiolipin synthase), all of which participate in glycerophospholipid biosynthesis. Thus, family-level recognition of membrane-associated small lipid enzymes plus the CDP-alcohol phosphotransferase motif pattern meaningfully distinguishes D from A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The membrane topology, small size, absence of nuclear/immune domains, and the CDP-alcohol phosphotransferase-like motif provide a transferable biological argument from general knowledge of lipid-metabolism enzyme families and immune receptor architecture that distinguishes D from the other three options without requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B describe eukaryotic nuclear processes incompatible with a bacterial membrane protein. Option C requires large multi-domain immune receptors absent here. Option D is the only choice consistent with a small integral-membrane enzyme involved in phospholipid synthesis. No other option is defensible."
  },
  "important_caveats": [
    "The most specific experimental annotation is GO:0032049 (cardiolipin biosynthetic process, IDA evidence); the offered option D (glycerophospholipid biosynthetic process, GO:0046474) is the broader parent term also directly annotated via IBA. Since 'cardiolipin biosynthetic process' is not among the choices, D is the best available answer.",
    "The CDP-alcohol phosphotransferase motif recognition is suggestive but not definitive from sequence alone; the primary discriminator is the overall membrane-protein topology and absence of features required by the other options.",
    "The UniProt entry also annotates GO:0007009 (plasma membrane organization, IMP), but this term is not among the offered choices."
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
  "benchmark_sequence_length": 215,
  "benchmark_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 215,
  "current_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9KZP3",
  "selected_historical_entry_version": 118,
  "selected_historical_record_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "selected_historical_source_sequence_length": 215,
  "selected_historical_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "selected_historical_version": {
    "accession": "Q9KZP3",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_STRCO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KZP3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001973\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\",\"Streptomyces albidoflavus group\"],\"scientificName\":\"Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145)\",\"taxonId\":100226}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19439403\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22409773\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the synthesis of cardiolipin (CL) (diphosphatidylglycerol) by specifically transferring a phosphatidyl group from CDP-diacylglycerol to phosphatidylglycerol (PG)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"id\":\"GO:0032049\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:cardiolipin biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"22409773\",\"source\":\"PubMed\"}],\"id\":\"GO:0007009\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:plasma membrane organization\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sandoval-Calderon M.\",\"Geiger O.\",\"Guan Z.\",\"Barona-Gomez F.\",\"Sohlenkamp C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19439403\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.006072\"}],\"citationType\":\"journal article\",\"firstPage\":\"17383\",\"id\":\"19439403\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"17390\",\"publicationDate\":\"2009\",\"title\":\"A eukaryote-like cardiolipin synthase is present in Streptomyces coelicolor and in most actinobacteria.\",\"volume\":\"284\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Jyothikumar V.\",\"Klanbut K.\",\"Tiong J.\",\"Roxburgh J.S.\",\"Hunter I.S.\",\"Smith T.K.\",\"Herron P.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22409773\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1365-2958.2012.08018.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"181\",\"id\":\"22409773\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"197\",\"publicationDate\":\"2012\",\"title\":\"Cardiolipin synthase is required for Streptomyces coelicolor morphogenesis.\",\"volume\":\"84\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H1",
  "excerpt": "ID   CRLS1_STRCO             Reviewed;         215 AA.\nAC   Q9KZP3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS {ECO:0000305};\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:19439403};\nGN   Name=clsA {ECO:0000303|PubMed:22409773};\nGN   OrderedLocusNames=SCO1389 {ECO:0000312|EMBL:CAB88885.1};\nGN   ORFNames=SC1A8A.09c {ECO:0000312|EMBL:CAB88885.1};\nOS   Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces; Streptomyces albidoflavus group.\nOX   NCBI_TaxID=100226 {ECO:0000312|Proteomes:UP000001973};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=19439403; DOI=10.1074/jbc.m109.006072;\nRA   Sandoval-Calderon M., Geiger O., Guan Z., Barona-Gomez F., Sohlenkamp C.;\nRT   \"A eukaryote-like cardiolipin synthase is present in Streptomyces\nRT   coelicolor and in most actinobacteria.\";\nRL   J. Biol. Chem. 284:17383-17390(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=22409773; DOI=10.1111/j.1365-2958.2012.08018.x;\nRA   Jyothikumar V., Klanbut K., Tiong J., Roxburgh J.S., Hunter I.S.,\nRA   Smith T.K., Herron P.R.;\nRT   \"Cardiolipin synthase is required for Streptomyces coelicolor\nRT   morphogenesis.\";\nRL   Mol. Microbiol. 84:181-197(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the synthesis of cardiolipin (CL)\nCC       (diphosphatidylglycerol) by specifically transferring a phosphatidyl\nCC       group from CDP-diacylglycerol to phosphatidylglycerol (PG).\nCC       {ECO:0000269|PubMed:19439403, ECO:0000269|PubMed:22409773}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0032049; P:cardiolipin biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0046474; P:glycerophospholipid biosynthetic process; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0007009; P:plasma membrane organization; IMP:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006325\nname: chromatin organization\nnamespace: biological_process\nalt_id: GO:0006333\nalt_id: GO:0006336\nalt_id: GO:0016568\nalt_id: GO:0031497\nalt_id: GO:0034724\ndef: \"The assembly or remodeling of chromatin composed of DNA complexed with histones, other associated proteins, and sometimes RNA.\" [PMID:20404130]\nsubset: goslim_generic\nsubset: goslim_pombe\nsubset: goslim_yeast\nsynonym: \"chromatin assembly\" NARROW []\nsynonym: \"chromatin assembly or disassembly\" RELATED []\nsynonym: \"chromatin assembly/disassembly\" RELATED []\nsynonym: \"chromatin maintenance\" BROAD []\nsynonym: \"chromatin modification\" RELATED []\nsynonym: \"chromatin organisation\" EXACT [GOC:mah]\nsynonym: \"DNA replication-independent chromatin assembly\" NARROW []\nsynonym: \"DNA replication-independent chromatin organization\" NARROW []\nsynonym: \"DNA replication-independent nucleosome organisation\" NARROW []\nsynonym: \"DNA replication-independent nuclesome assembly\" NARROW []\nsynonym: \"establishment of chromatin architecture\" EXACT [GOC:mah]\nsynonym: \"establishment or maintenance of chromatin architecture\" EXACT [GOC:mah]\nsynonym: \"transcription-coupled nucleosome assembly\" NARROW []\nxref: Reactome:R-HSA-4839726 \"Chromatin organization\"\nis_a: GO:0016043 ! cellular component organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006325",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 65125-65153",
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
  "excerpt": "[Term]\nid: GO:0006357\nname: regulation of transcription by RNA polymerase II\nnamespace: biological_process\nalt_id: GO:0006358\nalt_id: GO:0010551\ndef: \"Any process that modulates the frequency, rate or extent of transcription mediated by RNA polymerase II.\" [GOC:curators, GOC:txnOH]\nsynonym: \"global transcription regulation from Pol II promoter\" RELATED []\nsynonym: \"regulation of gene-specific transcription from RNA polymerase II promoter\" RELATED []\nsynonym: \"regulation of global transcription from Pol II promoter\" RELATED []\nsynonym: \"regulation of transcription from Pol II promoter\" EXACT []\nsynonym: \"regulation of transcription from RNA polymerase II promoter\" EXACT []\nsynonym: \"regulation of transcription from RNA polymerase II promoter, global\" RELATED []\nxref: Reactome:R-HSA-8864260 \"Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors\"\nis_a: GO:0006355 ! regulation of DNA-templated transcription\nrelationship: regulates GO:0006366 ! transcription by RNA polymerase II\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006357",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 65427-65443",
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
  "excerpt": "[Term]\nid: GO:0006655\nname: phosphatidylglycerol biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of phosphatidylglycerols, any of a class of phospholipids in which the phosphatidyl group is esterified to the hydroxyl group of glycerol.\" [ISBN:0198506732]\nsynonym: \"phosphatidylglycerol anabolism\" EXACT []\nsynonym: \"phosphatidylglycerol biosynthesis\" EXACT []\nsynonym: \"phosphatidylglycerol formation\" EXACT []\nsynonym: \"phosphatidylglycerol synthesis\" EXACT []\nxref: Reactome:R-HSA-1483148 \"Synthesis of PG\"\nis_a: GO:0046471 ! phosphatidylglycerol metabolic process\nis_a: GO:0046474 ! glycerophospholipid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006655",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 68783-68795",
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
  "excerpt": "[Term]\nid: GO:0032049\nname: cardiolipin biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of cardiolipin, 1,3-bis(3-phosphatidyl)glycerol.\" [GOC:mah]\nsynonym: \"diphosphatidylglycerol biosynthesis\" RELATED []\nsynonym: \"diphosphatidylglycerol biosynthetic process\" RELATED []\nxref: MetaCyc:PWY-5269\nxref: MetaCyc:PWY-5668\nxref: MetaCyc:PWY0-1545\nxref: Reactome:R-HSA-1483076 \"Synthesis of CL\"\nis_a: GO:0006655 ! phosphatidylglycerol biosynthetic process\nis_a: GO:0032048 ! cardiolipin metabolic process\nproperty_value: skos:narrowMatch MetaCyc:PWY-5269\nproperty_value: skos:narrowMatch MetaCyc:PWY-5668\nproperty_value: skos:narrowMatch MetaCyc:PWY0-1545\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032049",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 182251-182267",
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
  "excerpt": "[Term]\nid: GO:0032495\nname: response to muramyl dipeptide\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a muramyl dipeptide stimulus. Muramyl dipeptide is derived from peptidoglycan.\" [GOC:add]\nis_a: GO:1901698 ! response to nitrogen compound\nis_a: GO:1901700 ! response to oxygen-containing compound\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032495",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 186780-186787",
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
  "excerpt": "[Term]\nid: GO:0046474\nname: glycerophospholipid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of glycerophospholipids, any derivative of glycerophosphate that contains at least one O-acyl, O-alkyl, or O-alkenyl group attached to the glycerol residue.\" [ISBN:0198506732]\nsynonym: \"glycerophospholipid anabolism\" EXACT []\nsynonym: \"glycerophospholipid biosynthesis\" EXACT []\nsynonym: \"glycerophospholipid formation\" EXACT []\nsynonym: \"glycerophospholipid synthesis\" EXACT []\nsynonym: \"phosphoglyceride biosynthesis\" EXACT []\nsynonym: \"phosphoglyceride biosynthetic process\" EXACT []\nxref: Reactome:R-HSA-1483206 \"Glycerophospholipid biosynthesis\"\nis_a: GO:0006650 ! glycerophospholipid metabolic process\nis_a: GO:0008654 ! phospholipid biosynthetic process\nis_a: GO:0045017 ! glycerolipid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046474",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 277086-277101",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
