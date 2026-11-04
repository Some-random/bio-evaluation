# cofactor_0067

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0067.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — a divalent metal cation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLLYGLLILAFTRSCLVVGQCSINIPDDLKGEEAPVILVKTGNNVKLFRPEEKTTTFPKGTELLLACTGEGNGLKSNGQETTTLSCNGNQFESAAKEKLKDMSCKSMAKAVVEQTTKRCMGNDFNLYEAGYKVNGKFYGSVYDICYNGKGQSSGYTHNFIYGRTWKYKLPEKPYEHYSSRDPQAGKDLDKLYKEQKERFKNTKVNGKPLLDDEHYFTEGQLTPDTSIITGADKLSTYDYANIAPLFKDIYDGNIWRYENMTQELADQRQATFEEYTGGFYSYEVEKWKPIGLDNAEFPTHRVPKYIYKLVVDTESKDGIVFVTLNDPYHKSPASENLCKDICSEANINEPDFKNVEKGYTICCSYGDFGNRIRTLPKDIHVKGLLKY

[Multiple Choices]
A. Cu(2+)
B. a divalent metal cation
C. pyridoxal 5'-phosphate
D. Mo-bis(molybdopterin guanine dinucleotide)
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

> The sequence-matched UniProt record annotates the cofactor as “a divalent metal cation,” with experimental evidence attributed to the cited study. The historical record also matches the supplied sequence and gives the same annotation. This supports B, though the primary study was not independently reviewed here and the annotation does not identify a particular metal.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this protein's catalytic activity requires a divalent metal cation, as established by its biochemical characterization; the sequence alone does not identify that requirement or a specific metal.


**Reason**

> The N-terminal hydrophobic segment and cysteine-rich sequence suggest a secreted protein, but do not by themselves identify a catalytic family or cofactor requirement. General knowledge that some nucleases use divalent metals would not establish that this protein is one of them. The supplied choices also do not resolve the issue by sequence: there is no clear PLP- or molybdopterin-dependent enzyme signature, but that does not establish B over the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports the broad divalent-metal category but does not name a particular ion. Although Cu(2+) is itself a divalent metal, nothing supplied establishes copper as this protein's cofactor, so A is not independently supported.


### Important caveats

- The cofactor evidence is a database annotation attributed to an experimental study, not an independent review of that study's measurements.
- Reviewer-only protein identity and annotation were not available as original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this protein's catalytic activity requires a divalent metal cation, as established by its biochemical characterization; the sequence alone does not identify that requirement or a specific metal.",
    "reason": "The N-terminal hydrophobic segment and cysteine-rich sequence suggest a secreted protein, but do not by themselves identify a catalytic family or cofactor requirement. General knowledge that some nucleases use divalent metals would not establish that this protein is one of them. The supplied choices also do not resolve the issue by sequence: there is no clear PLP- or molybdopterin-dependent enzyme signature, but that does not establish B over the alternatives."
  },
  "case_id": "cofactor_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the cofactor as “a divalent metal cation,” with experimental evidence attributed to the cited study. The historical record also matches the supplied sequence and gives the same annotation. This supports B, though the primary study was not independently reviewed here and the annotation does not identify a particular metal."
  },
  "important_caveats": [
    "The cofactor evidence is a database annotation attributed to an experimental study, not an independent review of that study's measurements.",
    "Reviewer-only protein identity and annotation were not available as original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the broad divalent-metal category but does not name a particular ion. Although Cu(2+) is itself a divalent metal, nothing supplied establishes copper as this protein's cofactor, so A is not independently supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the cofactor as “a divalent metal cation,” with experimental evidence attributed to the cited study. The historical record also matches the supplied sequence and gives the same annotation. This supports B, though the primary study was not independently reviewed here and the annotation does not identify a particular metal.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this protein's catalytic activity requires a divalent metal cation, as established by its biochemical characterization; the sequence alone does not identify that requirement or a specific metal.",
    "reason": "The N-terminal hydrophobic segment and cysteine-rich sequence suggest a secreted protein, but do not by themselves identify a catalytic family or cofactor requirement. General knowledge that some nucleases use divalent metals would not establish that this protein is one of them. The supplied choices also do not resolve the issue by sequence: there is no clear PLP- or molybdopterin-dependent enzyme signature, but that does not establish B over the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the broad divalent-metal category but does not name a particular ion. Although Cu(2+) is itself a divalent metal, nothing supplied establishes copper as this protein's cofactor, so A is not independently supported."
  },
  "important_caveats": [
    "The cofactor evidence is a database annotation attributed to an experimental study, not an independent review of that study's measurements.",
    "Reviewer-only protein identity and annotation were not available as original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A3FMN3 (Salivary protein Tsal2A from Glossina morsitans morsitans) explicitly annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269, PubMed:23110062). The EC number 3.1.-.- (hydrolase acting on ester bonds, i.e., nuclease) is consistent with a metal-dependent hydrolysis mechanism. Both current and historical records confirm this annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'GDFG' motif (in 'CSYGDFGNRIRTLPKDIHVKGLLKY'), which is a hallmark of metal-dependent nucleases (e.g., DEDDh exonuclease family, ExoV/RecBCD-like nucleases). Transferable knowledge from hundreds of characterized nucleases (DNase I, RNase H, exonucleases, restriction enzymes) establishes that the GDFG/DEDDh-type active site coordinates a divalent metal cation (Mg2+, Mn2+, Ca2+, or Zn2+) essential for phosphodiester bond hydrolysis. The N-terminal hydrophobic signal peptide (MSLLYGLLILAFTRSC...) indicates a secreted protein, consistent with an insect salivary nuclease. Among the alternatives: (A) Cu(2+) is characteristic of oxidases (SOD, tyrosinase, laccase) with distinct His/Cys-rich copper-binding motifs absent here; (C) PLP-dependent enzymes (aminotransferases, decarboxylases) require a conserved active-site Lys forming a Schiff base, not present in this nuclease context; (D) Mo-bis(molybdopterin) cofactors are found in large redox enzymes (nitrate reductase, xanthine oxidase) far exceeding 388 residues and with completely different sequence signatures. The nuclease motif family knowledge meaningfully and strongly distinguishes option B from all three alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GDFG nuclease motif is a well-known, transferable family-level feature shared across many characterized nucleases, all of which require divalent metal cations. The absence of copper-binding, PLP-binding, or molybdenum-cofactor sequence signatures further eliminates the distractors. This constitutes legitimate generalization from other proteins in the same functional family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While Cu(2+) is technically a divalent cation, in cofactor annotation convention 'Cu(2+)' denotes copper-specific enzymes with distinct motifs, while 'a divalent metal cation' denotes the general metal-dependent nuclease class. The GDFG motif unambiguously places this protein in the latter category. No other option is defensible for a nuclease.


### Important caveats

- The specific identity of the divalent metal (Mg2+ vs Mn2+ vs Ca2+ vs Zn2+) is not resolved by sequence alone; however, the question only asks for the cofactor class, which is clearly 'a divalent metal cation.'
- The protein is annotated with 'residual nuclease activity,' suggesting its primary function may be nucleic acid binding rather than catalysis, but the experimental cofactor annotation still applies to the catalytic site.
- The historical UniProt entry was first released in 2026_01; the author's source snapshot date is unknown, but the sequence and annotation are consistent across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GDFG' motif (in 'CSYGDFGNRIRTLPKDIHVKGLLKY'), which is a hallmark of metal-dependent nucleases (e.g., DEDDh exonuclease family, ExoV/RecBCD-like nucleases). Transferable knowledge from hundreds of characterized nucleases (DNase I, RNase H, exonucleases, restriction enzymes) establishes that the GDFG/DEDDh-type active site coordinates a divalent metal cation (Mg2+, Mn2+, Ca2+, or Zn2+) essential for phosphodiester bond hydrolysis. The N-terminal hydrophobic signal peptide (MSLLYGLLILAFTRSC...) indicates a secreted protein, consistent with an insect salivary nuclease. Among the alternatives: (A) Cu(2+) is characteristic of oxidases (SOD, tyrosinase, laccase) with distinct His/Cys-rich copper-binding motifs absent here; (C) PLP-dependent enzymes (aminotransferases, decarboxylases) require a conserved active-site Lys forming a Schiff base, not present in this nuclease context; (D) Mo-bis(molybdopterin) cofactors are found in large redox enzymes (nitrate reductase, xanthine oxidase) far exceeding 388 residues and with completely different sequence signatures. The nuclease motif family knowledge meaningfully and strongly distinguishes option B from all three alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GDFG nuclease motif is a well-known, transferable family-level feature shared across many characterized nucleases, all of which require divalent metal cations. The absence of copper-binding, PLP-binding, or molybdenum-cofactor sequence signatures further eliminates the distractors. This constitutes legitimate generalization from other proteins in the same functional family."
  },
  "case_id": "cofactor_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A3FMN3 (Salivary protein Tsal2A from Glossina morsitans morsitans) explicitly annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269, PubMed:23110062). The EC number 3.1.-.- (hydrolase acting on ester bonds, i.e., nuclease) is consistent with a metal-dependent hydrolysis mechanism. Both current and historical records confirm this annotation."
  },
  "important_caveats": [
    "The specific identity of the divalent metal (Mg2+ vs Mn2+ vs Ca2+ vs Zn2+) is not resolved by sequence alone; however, the question only asks for the cofactor class, which is clearly 'a divalent metal cation.'",
    "The protein is annotated with 'residual nuclease activity,' suggesting its primary function may be nucleic acid binding rather than catalysis, but the experimental cofactor annotation still applies to the catalytic site.",
    "The historical UniProt entry was first released in 2026_01; the author's source snapshot date is unknown, but the sequence and annotation are consistent across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Cu(2+) is technically a divalent cation, in cofactor annotation convention 'Cu(2+)' denotes copper-specific enzymes with distinct motifs, while 'a divalent metal cation' denotes the general metal-dependent nuclease class. The GDFG motif unambiguously places this protein in the latter category. No other option is defensible for a nuclease."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A3FMN3 (Salivary protein Tsal2A from Glossina morsitans morsitans) explicitly annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269, PubMed:23110062). The EC number 3.1.-.- (hydrolase acting on ester bonds, i.e., nuclease) is consistent with a metal-dependent hydrolysis mechanism. Both current and historical records confirm this annotation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GDFG' motif (in 'CSYGDFGNRIRTLPKDIHVKGLLKY'), which is a hallmark of metal-dependent nucleases (e.g., DEDDh exonuclease family, ExoV/RecBCD-like nucleases). Transferable knowledge from hundreds of characterized nucleases (DNase I, RNase H, exonucleases, restriction enzymes) establishes that the GDFG/DEDDh-type active site coordinates a divalent metal cation (Mg2+, Mn2+, Ca2+, or Zn2+) essential for phosphodiester bond hydrolysis. The N-terminal hydrophobic signal peptide (MSLLYGLLILAFTRSC...) indicates a secreted protein, consistent with an insect salivary nuclease. Among the alternatives: (A) Cu(2+) is characteristic of oxidases (SOD, tyrosinase, laccase) with distinct His/Cys-rich copper-binding motifs absent here; (C) PLP-dependent enzymes (aminotransferases, decarboxylases) require a conserved active-site Lys forming a Schiff base, not present in this nuclease context; (D) Mo-bis(molybdopterin) cofactors are found in large redox enzymes (nitrate reductase, xanthine oxidase) far exceeding 388 residues and with completely different sequence signatures. The nuclease motif family knowledge meaningfully and strongly distinguishes option B from all three alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The GDFG nuclease motif is a well-known, transferable family-level feature shared across many characterized nucleases, all of which require divalent metal cations. The absence of copper-binding, PLP-binding, or molybdenum-cofactor sequence signatures further eliminates the distractors. This constitutes legitimate generalization from other proteins in the same functional family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Cu(2+) is technically a divalent cation, in cofactor annotation convention 'Cu(2+)' denotes copper-specific enzymes with distinct motifs, while 'a divalent metal cation' denotes the general metal-dependent nuclease class. The GDFG motif unambiguously places this protein in the latter category. No other option is defensible for a nuclease."
  },
  "important_caveats": [
    "The specific identity of the divalent metal (Mg2+ vs Mn2+ vs Ca2+ vs Zn2+) is not resolved by sequence alone; however, the question only asks for the cofactor class, which is clearly 'a divalent metal cation.'",
    "The protein is annotated with 'residual nuclease activity,' suggesting its primary function may be nucleic acid binding rather than catalysis, but the experimental cofactor annotation still applies to the catalytic site.",
    "The historical UniProt entry was first released in 2026_01; the author's source snapshot date is unknown, but the sequence and annotation are consistent across versions."
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
  "benchmark_sequence_length": 388,
  "benchmark_sequence_sha256": "629f9d1221c2be55e09d759195b67db01f2afd85556760be5f0ade9dae2beba4",
  "current_entry_audit": {
    "entryVersion": 44,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-03-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 388,
  "current_source_sequence_sha256": "629f9d1221c2be55e09d759195b67db01f2afd85556760be5f0ade9dae2beba4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 43,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A3FMN3",
  "selected_historical_entry_version": 43,
  "selected_historical_record_sha256": "536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5",
  "selected_historical_source_sequence_length": 388,
  "selected_historical_source_sequence_sha256": "629f9d1221c2be55e09d759195b67db01f2afd85556760be5f0ade9dae2beba4",
  "selected_historical_version": {
    "accession": "A3FMN3",
    "database": "Swiss-Prot",
    "entryVersion": 43,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SAL2A_GLOMM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A3FMN3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:55.735059+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "url": "https://rest.uniprot.org/uniprotkb/A3FMN3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":44,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-03-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:55.735059+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "url": "https://rest.uniprot.org/uniprotkb/A3FMN3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Savannah tsetse fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ABN58709.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Hippoboscoidea\",\"Glossinidae\",\"Glossina\"],\"scientificName\":\"Glossina morsitans morsitans\",\"taxonId\":37546}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:55.735059+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "url": "https://rest.uniprot.org/uniprotkb/A3FMN3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"value\":\"3.1.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ABN58709.1\",\"source\":\"EMBL\"}],\"value\":\"Tsal2 form A\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Salivary protein Tsal2A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:55.735059+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "url": "https://rest.uniprot.org/uniprotkb/A3FMN3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:60240\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"name\":\"a divalent metal cation\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:55.735059+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "url": "https://rest.uniprot.org/uniprotkb/A3FMN3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Caljon G.\",\"De Ridder K.\",\"Stijlemans B.\",\"Coosemans M.\",\"Magez S.\",\"De Baetselier P.\",\"Van Den Abbeele J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23110062\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0047233\"}],\"citationType\":\"journal article\",\"firstPage\":\"e47233\",\"id\":\"23110062\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e47233\",\"publicationDate\":\"2012\",\"title\":\"Tsetse salivary gland proteins 1 and 2 are high affinity nucleic acid binding proteins with residual nuclease activity.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:55.735059+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544",
  "url": "https://rest.uniprot.org/uniprotkb/A3FMN3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H1",
  "excerpt": "ID   SAL2A_GLOMM             Reviewed;         388 AA.\nAC   A3FMN3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-MAR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 43.\nDE   RecName: Full=Salivary protein Tsal2A {ECO:0000305};\nDE   AltName: Full=Tsal2 form A {ECO:0000312|EMBL:ABN58709.1};\nDE            EC=3.1.-.- {ECO:0000269|PubMed:23110062};\nDE   Flags: Precursor;\nGN   Name=Tsal2a {ECO:0000303|PubMed:23110062};\nOS   Glossina morsitans morsitans (Savannah tsetse fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Hippoboscoidea;\nOC   Glossinidae; Glossina.\nOX   NCBI_TaxID=37546 {ECO:0000312|EMBL:ABN58709.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:57.843760+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5",
  "url": "https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Salivary protein Tsal2A {ECO:0000305};\nDE   AltName: Full=Tsal2 form A {ECO:0000312|EMBL:ABN58709.1};\nDE            EC=3.1.-.- {ECO:0000269|PubMed:23110062};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:57.843760+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5",
  "url": "https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES,\nRP   SUBCELLULAR LOCATION, TISSUE SPECIFICITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=23110062; DOI=10.1371/journal.pone.0047233;\nRA   Caljon G., De Ridder K., Stijlemans B., Coosemans M., Magez S.,\nRA   De Baetselier P., Van Den Abbeele J.;\nRT   \"Tsetse salivary gland proteins 1 and 2 are high affinity nucleic acid\nRT   binding proteins with residual nuclease activity.\";\nRL   PLoS ONE 7:e47233-e47233(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:57.843760+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5",
  "url": "https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=a divalent metal cation; Xref=ChEBI:CHEBI:60240;\nCC         Evidence={ECO:0000269|PubMed:23110062};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:57.843760+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5",
  "url": "https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
