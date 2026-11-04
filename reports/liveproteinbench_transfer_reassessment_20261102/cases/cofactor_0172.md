# cofactor_0172

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0172.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGQFRFLALIVAVLCFSVALFLPTADEPDQDSYSVPLNQSVNTSQPPSSEMVPSDIRLTPLPQPKRIHYMVKVGDTLSGIFAQLGVPYSILQKILSVDLDHLQLDMIQPGEELELMMDDMGQLSRLIYHMSIVEKAIYTRENDGSFSYDFQEISGEWREILFSGEINGSFSVSARRVGLTSSQVANITQVMKDKIDFSRSLRAGDRFDILVKQQYLGEHNTGNSEIKAISFKLAKGDVSAFLAEDGRFYDRAGNSLERAFNRYPVDKAYRQITSGFNPKRKHPVTGRVVPHNGTDFATPIGAPVYSTGDGKVIVVRKHPYAGNYLVIEHNSVYKTRYLHLDKILVKKGQLVKRGQKIALAGATGRLTGPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQANQQEVALDET

[Multiple Choices]
A. Fe(2+)
B. Zn(2+)
C. [2Fe-2S] cluster
D. Mn(2+)
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

> The sequence-matched record reports one Zn(2+) ion per subunit, with experimental evidence attributed to the cited study; the entry also describes a crystal structure determined in complex with zinc. This supports choice B for the supplied protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide, and the remaining sequence is compatible with a secreted peptidoglycan metallopeptidase. Transferable knowledge of lysostaphin/M23-like peptidases and their His-containing metal-binding active sites makes Zn(2+) a credible choice over Fe(2+), Mn(2+), or a &#91;2Fe-2S&#93; cluster. This is a family-level inference, not proof from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The options contrast a common metalloprotease cofactor with iron, manganese, and an iron-sulfur cluster. Recognition of the likely secreted peptidoglycan metallopeptidase family provides a meaningful basis for choosing zinc without knowing this exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference favors zinc among the listed choices, and the reviewer evidence supports that choice.


### Important caveats

- The sequence features support a probabilistic family-level inference; they do not independently establish the bound metal.
- The cofactor annotation and cited experimental evidence apply to the sequence-matched source record; the annotation is not itself a direct experimental report.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the remaining sequence is compatible with a secreted peptidoglycan metallopeptidase. Transferable knowledge of lysostaphin/M23-like peptidases and their His-containing metal-binding active sites makes Zn(2+) a credible choice over Fe(2+), Mn(2+), or a [2Fe-2S] cluster. This is a family-level inference, not proof from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The options contrast a common metalloprotease cofactor with iron, manganese, and an iron-sulfur cluster. Recognition of the likely secreted peptidoglycan metallopeptidase family provides a meaningful basis for choosing zinc without knowing this exact protein's recorded annotation."
  },
  "case_id": "cofactor_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports one Zn(2+) ion per subunit, with experimental evidence attributed to the cited study; the entry also describes a crystal structure determined in complex with zinc. This supports choice B for the supplied protein."
  },
  "important_caveats": [
    "The sequence features support a probabilistic family-level inference; they do not independently establish the bound metal.",
    "The cofactor annotation and cited experimental evidence apply to the sequence-matched source record; the annotation is not itself a direct experimental report."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors zinc among the listed choices, and the reviewer evidence supports that choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports one Zn(2+) ion per subunit, with experimental evidence attributed to the cited study; the entry also describes a crystal structure determined in complex with zinc. This supports choice B for the supplied protein.",
    "evidence_ids": ["C5", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the remaining sequence is compatible with a secreted peptidoglycan metallopeptidase. Transferable knowledge of lysostaphin/M23-like peptidases and their His-containing metal-binding active sites makes Zn(2+) a credible choice over Fe(2+), Mn(2+), or a [2Fe-2S] cluster. This is a family-level inference, not proof from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The options contrast a common metalloprotease cofactor with iron, manganese, and an iron-sulfur cluster. Recognition of the likely secreted peptidoglycan metallopeptidase family provides a meaningful basis for choosing zinc without knowing this exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors zinc among the listed choices, and the reviewer evidence supports that choice."
  },
  "important_caveats": [
    "The sequence features support a probabilistic family-level inference; they do not independently establish the bound metal.",
    "The cofactor annotation and cited experimental evidence apply to the sequence-matched source record; the annotation is not itself a direct experimental report."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9KUL5 (ShyB, Peptidoglycan DD-endopeptidase) explicitly annotates Zn(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:18498110), confirmed by X-ray crystallography at 1.90 Å in complex with zinc (PDB 2GU1). The EC number 3.4.24.- (metalloprotease) and the crystal structure paper title ('Crystal structure of a putative lysostaphin peptidase from Vibrio cholerae') all support Zn(2+) binding. The annotation states 'Binds 1 zinc ion per subunit.'

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish Zn(2+) from the alternatives: (1) The N-terminal hydrophobic stretch (MGQFRFLALIVAVLCFSVALFLPTA) indicates a signal peptide, marking this as a secreted protein—consistent with peptidoglycan-hydrolyzing enzymes. (2) The C-terminal domain contains multiple histidine residues in HxH and HxxH spacing patterns (e.g., 'KHPYAGNYLVIEHNSVYKTRYLHLDK' and 'GPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQ'), which are characteristic of zinc-coordination sites in metalloproteases. (3) The overall architecture (signal peptide + single globular domain ~350 residues) matches the M23 peptidase family (lysostaphin-type peptidoglycan endopeptidases), which are universally Zn-dependent across characterized members. (4) &#91;2Fe-2S&#93; clusters serve electron transfer, not hydrolysis, making them incompatible with a peptidase. (5) Fe(2+) is rare in peptidases and typically associated with oxygenases/hydroxylases with different sequence signatures. (6) While Mn(2+) appears in some peptidases (M24 aminopeptidases), those have different fold and coordination geometry; the M23 family and the His-rich C-terminal coordination pattern here specifically point to Zn.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the secreted peptidase architecture, identify the histidine-rich zinc-coordination motifs in the C-terminal domain, and apply family-level knowledge that peptidoglycan DD-endopeptidases (M23, M56, M74, M76, M78 families) are all Zn-dependent. The &#91;2Fe-2S&#93; option is excluded by function (electron transfer vs. hydrolysis), Fe(2+) by the absence of oxygenase-type motifs, and Mn(2+) by the specific His-coordination pattern and family context. This constitutes a credible multi-step inference from sequence features and transferable family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct cofactor classes: a mononuclear divalent cation (Zn, Fe, Mn) and a polynuclear cluster (&#91;2Fe-2S&#93;). The &#91;2Fe-2S&#93; option is functionally incompatible with a hydrolytic enzyme. Among the three mononuclear ions, the histidine-rich C-terminal domain and peptidoglycan-hydrolase architecture strongly favor Zn over Fe or Mn. No two options appear equally defensible given the sequence features.


### Important caveats

- The reviewer-only evidence confirms Zn(2+) experimentally via crystallography (PDB 2GU1), but this structural detail was not available to the evaluated model.
- Distinguishing Zn(2+) from Mn(2+) by sequence alone relies on family-level inference (M23 peptidase family) and coordination-geometry preferences rather than a unique sequence motif that unambiguously encodes 'Zn' vs 'Mn'.
- The protein was initially annotated as 'putative lysostaphin-type peptidase' before its DD-endopeptidase function was confirmed experimentally in 2013-2019; the family assignment is robust regardless of the exact substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish Zn(2+) from the alternatives: (1) The N-terminal hydrophobic stretch (MGQFRFLALIVAVLCFSVALFLPTA) indicates a signal peptide, marking this as a secreted protein—consistent with peptidoglycan-hydrolyzing enzymes. (2) The C-terminal domain contains multiple histidine residues in HxH and HxxH spacing patterns (e.g., 'KHPYAGNYLVIEHNSVYKTRYLHLDK' and 'GPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQ'), which are characteristic of zinc-coordination sites in metalloproteases. (3) The overall architecture (signal peptide + single globular domain ~350 residues) matches the M23 peptidase family (lysostaphin-type peptidoglycan endopeptidases), which are universally Zn-dependent across characterized members. (4) [2Fe-2S] clusters serve electron transfer, not hydrolysis, making them incompatible with a peptidase. (5) Fe(2+) is rare in peptidases and typically associated with oxygenases/hydroxylases with different sequence signatures. (6) While Mn(2+) appears in some peptidases (M24 aminopeptidases), those have different fold and coordination geometry; the M23 family and the His-rich C-terminal coordination pattern here specifically point to Zn.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the secreted peptidase architecture, identify the histidine-rich zinc-coordination motifs in the C-terminal domain, and apply family-level knowledge that peptidoglycan DD-endopeptidases (M23, M56, M74, M76, M78 families) are all Zn-dependent. The [2Fe-2S] option is excluded by function (electron transfer vs. hydrolysis), Fe(2+) by the absence of oxygenase-type motifs, and Mn(2+) by the specific His-coordination pattern and family context. This constitutes a credible multi-step inference from sequence features and transferable family knowledge."
  },
  "case_id": "cofactor_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9KUL5 (ShyB, Peptidoglycan DD-endopeptidase) explicitly annotates Zn(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:18498110), confirmed by X-ray crystallography at 1.90 Å in complex with zinc (PDB 2GU1). The EC number 3.4.24.- (metalloprotease) and the crystal structure paper title ('Crystal structure of a putative lysostaphin peptidase from Vibrio cholerae') all support Zn(2+) binding. The annotation states 'Binds 1 zinc ion per subunit.'"
  },
  "important_caveats": [
    "The reviewer-only evidence confirms Zn(2+) experimentally via crystallography (PDB 2GU1), but this structural detail was not available to the evaluated model.",
    "Distinguishing Zn(2+) from Mn(2+) by sequence alone relies on family-level inference (M23 peptidase family) and coordination-geometry preferences rather than a unique sequence motif that unambiguously encodes 'Zn' vs 'Mn'.",
    "The protein was initially annotated as 'putative lysostaphin-type peptidase' before its DD-endopeptidase function was confirmed experimentally in 2013-2019; the family assignment is robust regardless of the exact substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct cofactor classes: a mononuclear divalent cation (Zn, Fe, Mn) and a polynuclear cluster ([2Fe-2S]). The [2Fe-2S] option is functionally incompatible with a hydrolytic enzyme. Among the three mononuclear ions, the histidine-rich C-terminal domain and peptidoglycan-hydrolase architecture strongly favor Zn over Fe or Mn. No two options appear equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9KUL5 (ShyB, Peptidoglycan DD-endopeptidase) explicitly annotates Zn(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:18498110), confirmed by X-ray crystallography at 1.90 Å in complex with zinc (PDB 2GU1). The EC number 3.4.24.- (metalloprotease) and the crystal structure paper title ('Crystal structure of a putative lysostaphin peptidase from Vibrio cholerae') all support Zn(2+) binding. The annotation states 'Binds 1 zinc ion per subunit.'",
    "evidence_ids": ["C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish Zn(2+) from the alternatives: (1) The N-terminal hydrophobic stretch (MGQFRFLALIVAVLCFSVALFLPTA) indicates a signal peptide, marking this as a secreted protein—consistent with peptidoglycan-hydrolyzing enzymes. (2) The C-terminal domain contains multiple histidine residues in HxH and HxxH spacing patterns (e.g., 'KHPYAGNYLVIEHNSVYKTRYLHLDK' and 'GPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQ'), which are characteristic of zinc-coordination sites in metalloproteases. (3) The overall architecture (signal peptide + single globular domain ~350 residues) matches the M23 peptidase family (lysostaphin-type peptidoglycan endopeptidases), which are universally Zn-dependent across characterized members. (4) [2Fe-2S] clusters serve electron transfer, not hydrolysis, making them incompatible with a peptidase. (5) Fe(2+) is rare in peptidases and typically associated with oxygenases/hydroxylases with different sequence signatures. (6) While Mn(2+) appears in some peptidases (M24 aminopeptidases), those have different fold and coordination geometry; the M23 family and the His-rich C-terminal coordination pattern here specifically point to Zn.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the secreted peptidase architecture, identify the histidine-rich zinc-coordination motifs in the C-terminal domain, and apply family-level knowledge that peptidoglycan DD-endopeptidases (M23, M56, M74, M76, M78 families) are all Zn-dependent. The [2Fe-2S] option is excluded by function (electron transfer vs. hydrolysis), Fe(2+) by the absence of oxygenase-type motifs, and Mn(2+) by the specific His-coordination pattern and family context. This constitutes a credible multi-step inference from sequence features and transferable family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct cofactor classes: a mononuclear divalent cation (Zn, Fe, Mn) and a polynuclear cluster ([2Fe-2S]). The [2Fe-2S] option is functionally incompatible with a hydrolytic enzyme. Among the three mononuclear ions, the histidine-rich C-terminal domain and peptidoglycan-hydrolase architecture strongly favor Zn over Fe or Mn. No two options appear equally defensible given the sequence features."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms Zn(2+) experimentally via crystallography (PDB 2GU1), but this structural detail was not available to the evaluated model.",
    "Distinguishing Zn(2+) from Mn(2+) by sequence alone relies on family-level inference (M23 peptidase family) and coordination-geometry preferences rather than a unique sequence motif that unambiguously encodes 'Zn' vs 'Mn'.",
    "The protein was initially annotated as 'putative lysostaphin-type peptidase' before its DD-endopeptidase function was confirmed experimentally in 2013-2019; the family assignment is robust regardless of the exact substrate specificity."
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
  "benchmark_sequence_length": 426,
  "benchmark_sequence_sha256": "34584a20856bfb24b4e9d3cd47bf32ba3f960017eb05fdba40f5b8f0c5608054",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 426,
  "current_source_sequence_sha256": "34584a20856bfb24b4e9d3cd47bf32ba3f960017eb05fdba40f5b8f0c5608054",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9KUL5",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "selected_historical_source_sequence_length": 426,
  "selected_historical_source_sequence_sha256": "34584a20856bfb24b4e9d3cd47bf32ba3f960017eb05fdba40f5b8f0c5608054",
  "selected_historical_version": {
    "accession": "Q9KUL5",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHYB_VIBCH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KUL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF93673.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000584\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Vibrionales\",\"Vibrionaceae\",\"Vibrio\"],\"scientificName\":\"Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)\",\"taxonId\":243277}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Autolysin ShyB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18498110\",\"source\":\"PubMed\"}],\"value\":\"Putative lysostaphin-type peptidase P01\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Sidewall hydrolase B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Peptidoglycan DD-endopeptidase ShyB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18498110\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18498110\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Doerr T.\",\"Cava F.\",\"Lam H.\",\"Davis B.M.\",\"Waldor M.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23834664\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12323\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"23834664\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"962\",\"publicationDate\":\"2013\",\"title\":\"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.\",\"volume\":\"89\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Murphy S.G.\",\"Alvarez L.\",\"Adams M.C.\",\"Liu S.\",\"Chappie J.S.\",\"Cava F.\",\"Doerr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30782657\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02620-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30782657\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.\",\"volume\":\"10\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-372\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Ragumani S.\",\"Kumaran D.\",\"Burley S.K.\",\"Swaminathan S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18498110\"},{\"database\":\"DOI\",\"id\":\"10.1002/prot.22095\"}],\"citationType\":\"journal article\",\"firstPage\":\"1096\",\"id\":\"18498110\",\"journal\":\"Proteins\",\"lastPage\":\"1103\",\"publicationDate\":\"2008\",\"title\":\"Crystal structure of a putative lysostaphin peptidase from Vibrio cholerae.\",\"volume\":\"72\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"2GU1\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS) OF 63-412 IN COMPLEX WITH ZINC\",\"COFACTOR\",\"SUBUNIT\",\"REACTION MECHANISM\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:03.079631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KUL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   SHYB_VIBCH              Reviewed;         426 AA.\nAC   Q9KUL5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=Peptidoglycan DD-endopeptidase ShyB {ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};\nDE   AltName: Full=Autolysin ShyB {ECO:0000303|PubMed:30782657};\nDE   AltName: Full=Putative lysostaphin-type peptidase P01 {ECO:0000303|PubMed:18498110};\nDE   AltName: Full=Sidewall hydrolase B {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\nGN   Name=shyB {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nGN   OrderedLocusNames=VC_0503 {ECO:0000303|PubMed:23834664,\nGN   ECO:0000312|EMBL:AAF93673.1};\nOS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;\nOC   Vibrionaceae; Vibrio.\nOX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF93673.1, ECO:0000312|Proteomes:UP000000584};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Peptidoglycan DD-endopeptidase ShyB {ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};\nDE   AltName: Full=Autolysin ShyB {ECO:0000303|PubMed:30782657};\nDE   AltName: Full=Putative lysostaphin-type peptidase P01 {ECO:0000303|PubMed:18498110};\nDE   AltName: Full=Sidewall hydrolase B {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};\nRX   PubMed=23834664; DOI=10.1111/mmi.12323;\nRA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;\nRT   \"Substrate specificity of an elongation-specific peptidoglycan\nRT   endopeptidase and its implications for cell wall architecture and growth of\nRT   Vibrio cholerae.\";\nRL   Mol. Microbiol. 89:949-962(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, INDUCTION,\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-372.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};\nRX   PubMed=30782657; DOI=10.1128/mbio.02620-18;\nRA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,\nRA   Doerr T.;\nRT   \"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc\nRT   Starvation Response.\";\nRL   MBio 10:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H5",
  "excerpt": "RN   [4] {ECO:0007744|PDB:2GU1}\nRP   X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS) OF 63-412 IN COMPLEX WITH ZINC,\nRP   COFACTOR, SUBUNIT, AND REACTION MECHANISM.\nRX   PubMed=18498110; DOI=10.1002/prot.22095;\nRA   Ragumani S., Kumaran D., Burley S.K., Swaminathan S.;\nRT   \"Crystal structure of a putative lysostaphin peptidase from Vibrio\nRT   cholerae.\";\nRL   Proteins 72:1096-1103(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000269|PubMed:18498110};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000269|PubMed:18498110};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:12.389220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310",
  "url": "https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 172. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
