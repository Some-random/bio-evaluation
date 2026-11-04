# active_site_0063

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0063.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 148 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. Position 94 (Nucleophile)
B. Position 146 (Proton acceptor)
C. Position 502 (Nucleophile)
D. Position 148 (Proton acceptor)
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

> The sequence-matched UniProt record annotates position 148 as the proton acceptor, matching choice D. This annotation is transferred by similarity rather than shown here to be a direct experimental determination for this protein.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich dinucleotide-binding motif consistent with an NAD-dependent enzyme, and position 148 is Tyr whereas position 146 is Trp. In this enzyme-family context, a conserved Tyr is a plausible proton-transfer residue; Trp is a poor proton acceptor. Position 502 is beyond the 321-residue sequence, and position 94 is Glu, not the characteristic Tyr proton-transfer candidate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the local sequence distinguish the offered Tyr148 proton-acceptor choice from the nearby Trp146 distractor without needing the exact protein's recorded annotation. The precise catalytic assignment remains an inference, not proof from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only D offers the plausible Tyr proton-acceptor residue at position 148.


### Important caveats

- The source annotation cites similarity evidence, so it should not be presented as direct experimental confirmation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding motif consistent with an NAD-dependent enzyme, and position 148 is Tyr whereas position 146 is Trp. In this enzyme-family context, a conserved Tyr is a plausible proton-transfer residue; Trp is a poor proton acceptor. Position 502 is beyond the 321-residue sequence, and position 94 is Glu, not the characteristic Tyr proton-transfer candidate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the local sequence distinguish the offered Tyr148 proton-acceptor choice from the nearby Trp146 distractor without needing the exact protein's recorded annotation. The precise catalytic assignment remains an inference, not proof from sequence alone."
  },
  "case_id": "active_site_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 148 as the proton acceptor, matching choice D. This annotation is transferred by similarity rather than shown here to be a direct experimental determination for this protein."
  },
  "important_caveats": [
    "The source annotation cites similarity evidence, so it should not be presented as direct experimental confirmation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D offers the plausible Tyr proton-acceptor residue at position 148."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 148 as the proton acceptor, matching choice D. This annotation is transferred by similarity rather than shown here to be a direct experimental determination for this protein.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding motif consistent with an NAD-dependent enzyme, and position 148 is Tyr whereas position 146 is Trp. In this enzyme-family context, a conserved Tyr is a plausible proton-transfer residue; Trp is a poor proton acceptor. Position 502 is beyond the 321-residue sequence, and position 94 is Glu, not the characteristic Tyr proton-transfer candidate.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the local sequence distinguish the offered Tyr148 proton-acceptor choice from the nearby Trp146 distractor without needing the exact protein's recorded annotation. The precise catalytic assignment remains an inference, not proof from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D offers the plausible Tyr proton-acceptor residue at position 148."
  },
  "important_caveats": [
    "The source annotation cites similarity evidence, so it should not be presented as direct experimental confirmation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5/H3) explicitly lists position 148 as 'Proton acceptor' active site. The evidence code is ECO:0000250 (similarity-based inference from Q8NBZ7), making this a computational transfer rather than direct experimental validation for this exact protein. The sequence at position 148 is Tyrosine (Y), consistent with the proton-acceptor role in NAD+-dependent decarboxylases. The annotation is supported but with the caveat that it is a similarity-based assignment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable features distinguish the options: (1) Option C (position 502) is eliminated because the protein is only 321 residues long. (2) Option B (position 146, W/Tryptophan as proton acceptor) is chemically implausible—tryptophan is not a recognized proton acceptor in any known enzymatic catalytic mechanism. (3) The sequence contains a Rossmann-fold motif 'GGAGFIG' (positions 10-16) and 'YGDG' near position 207-210, hallmarks of NAD+-dependent enzymes. In the well-characterized family of NAD+-dependent decarboxylases (EC 4.1.1.x, including UDP-glucuronate decarboxylase and related UDP-sugar decarboxylases), the canonical catalytic mechanism employs a tyrosine residue as the proton acceptor that abstracts a proton from the substrate's C4 hydroxyl to facilitate decarboxylation. Position 148 is Tyrosine (Y), fitting this family mechanism. (4) Option A (position 94, E/Glutamate as nucleophile) is inconsistent with the established mechanism of this enzyme family, where the catalytic step is proton abstraction by Tyr, not nucleophilic attack by Glu. Thus, family-level knowledge of NAD+-dependent decarboxylase catalysis meaningfully distinguishes D from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use: sequence-length counting to eliminate C; basic amino-acid chemistry to eliminate B (Trp cannot serve as proton acceptor); recognition of the Rossmann fold and NAD+-binding architecture from the sequence; and well-established family knowledge that NAD+-dependent decarboxylases use a catalytic tyrosine as proton acceptor to select D over A. This is a concrete, transferable inference from protein-family mechanisms learned from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is eliminated by sequence length (321 aa < 502). Option B is eliminated by amino-acid chemistry (Trp is not a proton acceptor). Between A and D, the NAD+-dependent decarboxylase family mechanism (Tyr proton acceptor) clearly favors D. No two options are equally defensible.


### Important caveats

- The UniProt active-site annotation is based on similarity (ECO:0000250 from Q8NBZ7), not direct experimental mutagenesis or kinetics on this specific protein.
- The protein was identified by the reviewer as A7GKX7 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase, EC 4.1.1.128) from Bacillus cytotoxicus, but this identity was not provided to the evaluated model.
- The family-level reasoning about NAD+-dependent decarboxylases using catalytic Tyr is well-supported across multiple characterized members of this enzyme superfamily.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable features distinguish the options: (1) Option C (position 502) is eliminated because the protein is only 321 residues long. (2) Option B (position 146, W/Tryptophan as proton acceptor) is chemically implausible—tryptophan is not a recognized proton acceptor in any known enzymatic catalytic mechanism. (3) The sequence contains a Rossmann-fold motif 'GGAGFIG' (positions 10-16) and 'YGDG' near position 207-210, hallmarks of NAD+-dependent enzymes. In the well-characterized family of NAD+-dependent decarboxylases (EC 4.1.1.x, including UDP-glucuronate decarboxylase and related UDP-sugar decarboxylases), the canonical catalytic mechanism employs a tyrosine residue as the proton acceptor that abstracts a proton from the substrate's C4 hydroxyl to facilitate decarboxylation. Position 148 is Tyrosine (Y), fitting this family mechanism. (4) Option A (position 94, E/Glutamate as nucleophile) is inconsistent with the established mechanism of this enzyme family, where the catalytic step is proton abstraction by Tyr, not nucleophilic attack by Glu. Thus, family-level knowledge of NAD+-dependent decarboxylase catalysis meaningfully distinguishes D from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: sequence-length counting to eliminate C; basic amino-acid chemistry to eliminate B (Trp cannot serve as proton acceptor); recognition of the Rossmann fold and NAD+-binding architecture from the sequence; and well-established family knowledge that NAD+-dependent decarboxylases use a catalytic tyrosine as proton acceptor to select D over A. This is a concrete, transferable inference from protein-family mechanisms learned from other proteins."
  },
  "case_id": "active_site_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H3) explicitly lists position 148 as 'Proton acceptor' active site. The evidence code is ECO:0000250 (similarity-based inference from Q8NBZ7), making this a computational transfer rather than direct experimental validation for this exact protein. The sequence at position 148 is Tyrosine (Y), consistent with the proton-acceptor role in NAD+-dependent decarboxylases. The annotation is supported but with the caveat that it is a similarity-based assignment."
  },
  "important_caveats": [
    "The UniProt active-site annotation is based on similarity (ECO:0000250 from Q8NBZ7), not direct experimental mutagenesis or kinetics on this specific protein.",
    "The protein was identified by the reviewer as A7GKX7 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase, EC 4.1.1.128) from Bacillus cytotoxicus, but this identity was not provided to the evaluated model.",
    "The family-level reasoning about NAD+-dependent decarboxylases using catalytic Tyr is well-supported across multiple characterized members of this enzyme superfamily."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is eliminated by sequence length (321 aa < 502). Option B is eliminated by amino-acid chemistry (Trp is not a proton acceptor). Between A and D, the NAD+-dependent decarboxylase family mechanism (Tyr proton acceptor) clearly favors D. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H3) explicitly lists position 148 as 'Proton acceptor' active site. The evidence code is ECO:0000250 (similarity-based inference from Q8NBZ7), making this a computational transfer rather than direct experimental validation for this exact protein. The sequence at position 148 is Tyrosine (Y), consistent with the proton-acceptor role in NAD+-dependent decarboxylases. The annotation is supported but with the caveat that it is a similarity-based assignment.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable features distinguish the options: (1) Option C (position 502) is eliminated because the protein is only 321 residues long. (2) Option B (position 146, W/Tryptophan as proton acceptor) is chemically implausible—tryptophan is not a recognized proton acceptor in any known enzymatic catalytic mechanism. (3) The sequence contains a Rossmann-fold motif 'GGAGFIG' (positions 10-16) and 'YGDG' near position 207-210, hallmarks of NAD+-dependent enzymes. In the well-characterized family of NAD+-dependent decarboxylases (EC 4.1.1.x, including UDP-glucuronate decarboxylase and related UDP-sugar decarboxylases), the canonical catalytic mechanism employs a tyrosine residue as the proton acceptor that abstracts a proton from the substrate's C4 hydroxyl to facilitate decarboxylation. Position 148 is Tyrosine (Y), fitting this family mechanism. (4) Option A (position 94, E/Glutamate as nucleophile) is inconsistent with the established mechanism of this enzyme family, where the catalytic step is proton abstraction by Tyr, not nucleophilic attack by Glu. Thus, family-level knowledge of NAD+-dependent decarboxylase catalysis meaningfully distinguishes D from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: sequence-length counting to eliminate C; basic amino-acid chemistry to eliminate B (Trp cannot serve as proton acceptor); recognition of the Rossmann fold and NAD+-binding architecture from the sequence; and well-established family knowledge that NAD+-dependent decarboxylases use a catalytic tyrosine as proton acceptor to select D over A. This is a concrete, transferable inference from protein-family mechanisms learned from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is eliminated by sequence length (321 aa < 502). Option B is eliminated by amino-acid chemistry (Trp is not a proton acceptor). Between A and D, the NAD+-dependent decarboxylase family mechanism (Tyr proton acceptor) clearly favors D. No two options are equally defensible."
  },
  "important_caveats": [
    "The UniProt active-site annotation is based on similarity (ECO:0000250 from Q8NBZ7), not direct experimental mutagenesis or kinetics on this specific protein.",
    "The protein was identified by the reviewer as A7GKX7 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase, EC 4.1.1.128) from Bacillus cytotoxicus, but this identity was not provided to the evaluated model.",
    "The family-level reasoning about NAD+-dependent decarboxylases using catalytic Tyr is well-supported across multiple characterized members of this enzyme superfamily."
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
  "benchmark_sequence_length": 321,
  "benchmark_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_entry_audit": {
    "entryVersion": 96,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 321,
  "current_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 94,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7GKX7",
  "selected_historical_entry_version": 94,
  "selected_historical_record_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "selected_historical_source_sequence_length": 321,
  "selected_historical_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "selected_historical_version": {
    "accession": "A7GKX7",
    "database": "Swiss-Prot",
    "entryVersion": 94,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UXNAS_BACCN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7GKX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":96,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-XylNAc synthase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.128\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAcA decarboxylase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":148},\"start\":{\"modifier\":\"EXACT\",\"value\":148}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":12},\"start\":{\"modifier\":\"EXACT\",\"value\":12}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":13},\"start\":{\"modifier\":\"EXACT\",\"value\":13}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":14},\"start\":{\"modifier\":\"EXACT\",\"value\":14}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":33},\"start\":{\"modifier\":\"EXACT\",\"value\":33}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":34},\"start\":{\"modifier\":\"EXACT\",\"value\":34}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":36},\"start\":{\"modifier\":\"EXACT\",\"value\":36}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":38},\"start\":{\"modifier\":\"EXACT\",\"value\":38}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":76},\"start\":{\"modifier\":\"EXACT\",\"value\":76}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":95},\"start\":{\"modifier\":\"EXACT\",\"value\":95}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":117},\"start\":{\"modifier\":\"EXACT\",\"value\":117}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":148},\"start\":{\"modifier\":\"EXACT\",\"value\":148}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8NBZ7\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":152},\"start\":{\"modifier\":\"EXACT\",\"value\":152}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43880.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H1",
  "excerpt": "ID   UXNAS_BACCN             Reviewed;         321 AA.\nAC   A7GKX7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 94.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};\nDE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};\nDE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};\nDE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};\nGN   Name=UXNAcS {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0430 {ECO:0000312|EMBL:ABS20785.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43880.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        148\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         12\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         13\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         14\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         33\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         34\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         36\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         38\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         76\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         95\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         117\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         148\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         152\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8NBZ7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
