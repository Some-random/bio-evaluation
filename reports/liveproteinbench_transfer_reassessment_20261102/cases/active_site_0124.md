# active_site_0124

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0124.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 154 (Acyl-thioester intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. Position 124 (Proton donor)
B. Position 154 (Acyl-thioester intermediate)
C. Position 58 (Proton donor)
D. Position 207 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation assigns position 154 the role “Acyl-thioester intermediate,” matching choice B. This is a computational PIRSR annotation, not direct residue-specific experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine at position 154 in a cysteine-containing motif. Transferable knowledge of aspartate-semialdehyde dehydrogenase and related enzyme chemistry supports a catalytic cysteine forming a thioester intermediate. That distinguishes B from the alternatives, which describe other positions as proton donors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence and mechanism inference provides a meaningful basis for choosing B; recalling this exact protein’s database annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only B pairs the catalytic cysteine position with the thioester-intermediate role supported by the family-level inference.


### Important caveats

- The reviewer-only annotation supports the key but is computationally inferred; the excerpts do not provide direct experimental confirmation of the residue’s role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine at position 154 in a cysteine-containing motif. Transferable knowledge of aspartate-semialdehyde dehydrogenase and related enzyme chemistry supports a catalytic cysteine forming a thioester intermediate. That distinguishes B from the alternatives, which describe other positions as proton donors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and mechanism inference provides a meaningful basis for choosing B; recalling this exact protein’s database annotation is not necessary."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the role “Acyl-thioester intermediate,” matching choice B. This is a computational PIRSR annotation, not direct residue-specific experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but is computationally inferred; the excerpts do not provide direct experimental confirmation of the residue’s role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B pairs the catalytic cysteine position with the thioester-intermediate role supported by the family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the role “Acyl-thioester intermediate,” matching choice B. This is a computational PIRSR annotation, not direct residue-specific experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine at position 154 in a cysteine-containing motif. Transferable knowledge of aspartate-semialdehyde dehydrogenase and related enzyme chemistry supports a catalytic cysteine forming a thioester intermediate. That distinguishes B from the alternatives, which describe other positions as proton donors.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and mechanism inference provides a meaningful basis for choosing B; recalling this exact protein’s database annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B pairs the catalytic cysteine position with the thioester-intermediate role supported by the family-level inference."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but is computationally inferred; the excerpts do not provide direct experimental confirmation of the residue’s role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WWR8 annotates position 154 as 'Acyl-thioester intermediate' active site (evidence: PIRSR000148-1, ECO:0000255). The residue at position 154 in the supplied sequence is C (Cysteine), which is biochemically consistent with forming a thioester intermediate. The protein is annotated as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism across many characterized homologs (E. coli, C. glutamicum, etc.) involves a conserved catalytic Cys attacking the hemithioacetal to form a thioester. A PDB structure (5JW6, 2.39 Å) provides structural context. The annotation is computational/curated (PIRSR) rather than directly experimental for this specific protein, but it is consistent with well-established family mechanism and structural data.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C17](#evidence-c17), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The question can be answered through fundamental enzyme mechanism knowledge and sequence analysis. (1) The sequence contains 'GATGSVG' at positions 13-19, a canonical Rossmann-fold NAD(P)-binding motif, identifying this as an NAD(P)-dependent dehydrogenase. (2) The phrase 'acyl-thioester intermediate' in option B uniquely requires a cysteine nucleophile (sulfur attacks a carbonyl to form R-S-C(=O)-R'), which is textbook biochemistry. (3) Reading the sequence at the four candidate positions: position 124 is Pro (P), position 154 is Cys (C), position 58 is Thr (T), position 207 is Gly (G). Only Cys can form a thioester. (4) The 'proton donor' role in options A, C, D is typically fulfilled by His, Asp, Glu, or Tyr—Pro, Gly, and (rarely) Thr are implausible as catalytic proton donors in dehydrogenase active sites. (5) The sequence context around position 154 ('GFLVCNSNCAVIGVVIPFAALQAKFGP') matches the conserved ASADH catalytic-domain signature seen in homologs. Thus, a model using family-level knowledge of ASADH and general mechanistic biochemistry can eliminate A, C, D and select B without memorizing this specific entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discriminating logic relies on: (a) recognizing the Rossmann fold to classify the enzyme, (b) the universal biochemical requirement that thioester intermediates require a Cys thiol, and (c) reading amino acid identities from the sequence to eliminate non-Cys options. All are transferable knowledge from enzyme mechanism and protein-family recognition, not lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 154 corresponds to a Cys residue, and only a Cys can form an acyl-thioester intermediate. The other three positions (Pro, Thr, Gly) are biochemically implausible as proton donors in a dehydrogenase active site. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for position 154 uses evidence code ECO:0000255 (PIRSR), which is computational/curated rather than direct experimental measurement on this exact protein. However, the mechanism is well-established across the ASADH family and supported by the 5JW6 crystal structure.
- The position numbering in the question matches the canonical UniProt coordinates (363-residue full-length sequence), confirmed by sequence match.
- The PDB structure 5JW6 (2.39 Å) provides structural evidence for this fungal ASADH but was not independently validated in this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The question can be answered through fundamental enzyme mechanism knowledge and sequence analysis. (1) The sequence contains 'GATGSVG' at positions 13-19, a canonical Rossmann-fold NAD(P)-binding motif, identifying this as an NAD(P)-dependent dehydrogenase. (2) The phrase 'acyl-thioester intermediate' in option B uniquely requires a cysteine nucleophile (sulfur attacks a carbonyl to form R-S-C(=O)-R'), which is textbook biochemistry. (3) Reading the sequence at the four candidate positions: position 124 is Pro (P), position 154 is Cys (C), position 58 is Thr (T), position 207 is Gly (G). Only Cys can form a thioester. (4) The 'proton donor' role in options A, C, D is typically fulfilled by His, Asp, Glu, or Tyr—Pro, Gly, and (rarely) Thr are implausible as catalytic proton donors in dehydrogenase active sites. (5) The sequence context around position 154 ('GFLVCNSNCAVIGVVIPFAALQAKFGP') matches the conserved ASADH catalytic-domain signature seen in homologs. Thus, a model using family-level knowledge of ASADH and general mechanistic biochemistry can eliminate A, C, D and select B without memorizing this specific entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discriminating logic relies on: (a) recognizing the Rossmann fold to classify the enzyme, (b) the universal biochemical requirement that thioester intermediates require a Cys thiol, and (c) reading amino acid identities from the sequence to eliminate non-Cys options. All are transferable knowledge from enzyme mechanism and protein-family recognition, not lookup of this specific entry's annotation."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C17",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WWR8 annotates position 154 as 'Acyl-thioester intermediate' active site (evidence: PIRSR000148-1, ECO:0000255). The residue at position 154 in the supplied sequence is C (Cysteine), which is biochemically consistent with forming a thioester intermediate. The protein is annotated as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism across many characterized homologs (E. coli, C. glutamicum, etc.) involves a conserved catalytic Cys attacking the hemithioacetal to form a thioester. A PDB structure (5JW6, 2.39 Å) provides structural context. The annotation is computational/curated (PIRSR) rather than directly experimental for this specific protein, but it is consistent with well-established family mechanism and structural data."
  },
  "important_caveats": [
    "The UniProt annotation for position 154 uses evidence code ECO:0000255 (PIRSR), which is computational/curated rather than direct experimental measurement on this exact protein. However, the mechanism is well-established across the ASADH family and supported by the 5JW6 crystal structure.",
    "The position numbering in the question matches the canonical UniProt coordinates (363-residue full-length sequence), confirmed by sequence match.",
    "The PDB structure 5JW6 (2.39 Å) provides structural evidence for this fungal ASADH but was not independently validated in this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 154 corresponds to a Cys residue, and only a Cys can form an acyl-thioester intermediate. The other three positions (Pro, Thr, Gly) are biochemically implausible as proton donors in a dehydrogenase active site. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WWR8 annotates position 154 as 'Acyl-thioester intermediate' active site (evidence: PIRSR000148-1, ECO:0000255). The residue at position 154 in the supplied sequence is C (Cysteine), which is biochemically consistent with forming a thioester intermediate. The protein is annotated as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism across many characterized homologs (E. coli, C. glutamicum, etc.) involves a conserved catalytic Cys attacking the hemithioacetal to form a thioester. A PDB structure (5JW6, 2.39 Å) provides structural context. The annotation is computational/curated (PIRSR) rather than directly experimental for this specific protein, but it is consistent with well-established family mechanism and structural data.",
    "evidence_ids": ["C5", "H4", "C17", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The question can be answered through fundamental enzyme mechanism knowledge and sequence analysis. (1) The sequence contains 'GATGSVG' at positions 13-19, a canonical Rossmann-fold NAD(P)-binding motif, identifying this as an NAD(P)-dependent dehydrogenase. (2) The phrase 'acyl-thioester intermediate' in option B uniquely requires a cysteine nucleophile (sulfur attacks a carbonyl to form R-S-C(=O)-R'), which is textbook biochemistry. (3) Reading the sequence at the four candidate positions: position 124 is Pro (P), position 154 is Cys (C), position 58 is Thr (T), position 207 is Gly (G). Only Cys can form a thioester. (4) The 'proton donor' role in options A, C, D is typically fulfilled by His, Asp, Glu, or Tyr—Pro, Gly, and (rarely) Thr are implausible as catalytic proton donors in dehydrogenase active sites. (5) The sequence context around position 154 ('GFLVCNSNCAVIGVVIPFAALQAKFGP') matches the conserved ASADH catalytic-domain signature seen in homologs. Thus, a model using family-level knowledge of ASADH and general mechanistic biochemistry can eliminate A, C, D and select B without memorizing this specific entry.",
    "missing_item_specific_fact": "",
    "reason": "The discriminating logic relies on: (a) recognizing the Rossmann fold to classify the enzyme, (b) the universal biochemical requirement that thioester intermediates require a Cys thiol, and (c) reading amino acid identities from the sequence to eliminate non-Cys options. All are transferable knowledge from enzyme mechanism and protein-family recognition, not lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 154 corresponds to a Cys residue, and only a Cys can form an acyl-thioester intermediate. The other three positions (Pro, Thr, Gly) are biochemically implausible as proton donors in a dehydrogenase active site. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 154 uses evidence code ECO:0000255 (PIRSR), which is computational/curated rather than direct experimental measurement on this exact protein. However, the mechanism is well-established across the ASADH family and supported by the 5JW6 crystal structure.",
    "The position numbering in the question matches the canonical UniProt coordinates (363-residue full-length sequence), confirmed by sequence match.",
    "The PDB structure 5JW6 (2.39 Å) provides structural evidence for this fungal ASADH but was not independently validated in this audit."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
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
  "requested_accession": "Q4WWR8",
  "selected_historical_entry_version": 118,
  "selected_historical_record_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "selected_historical_version": {
    "accession": "Q4WWR8",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WWR8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002530\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"AfASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Acyl-thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":15},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":17},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":18},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":43},\"start\":{\"modifier\":\"EXACT\",\"value\":43}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":341}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28045392\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x16020070\"}],\"citationType\":\"journal article\",\"firstPage\":\"36\",\"id\":\"28045392\",\"journal\":\"Acta Crystallogr. F\",\"lastPage\":\"44\",\"publicationDate\":\"2017\",\"title\":\"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5JW6\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_ASPFU              Reviewed;         363 AA.\nAC   Q4WWR8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\nGN   Name=hom2 {ECO:0000305};\nGN   ORFNames=AFUA_3G06830 {ECO:0000312|EMBL:EAL92885.1};\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879 {ECO:0000312|Proteomes:UP000002530};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5JW6}\nRP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=28045392; DOI=10.1107/s2053230x16020070;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from\nRT   Aspergillus fumigatus.\";\nRL   Acta Crystallogr. F 73:36-44(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Acyl-thioester intermediate\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 165-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        251\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-170",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         15\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         16\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-178",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         17\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 179-182",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         18\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 183-186",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 187-190",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         43\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 191-194",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         87\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 195-198",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 199-202",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         341\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 203-206",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
