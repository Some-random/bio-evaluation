# catalytic_activity_0021

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0021.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — Hydrolysis of alpha-(2-&gt;3)-, alpha-(2-&gt;6)-, alpha-(2-&gt;8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQLSSIADKIRESATMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATIRTGKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYISMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPTGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGNQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.
B. 4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)
C. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation assigns this protein the sialidase reaction in choice A and cites experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic membrane anchor followed by a long, glycosylation-rich extracellular protein region, consistent with a viral surface glycoprotein. Transferable knowledge of viral hemagglutinin-neuraminidase proteins links that kind of protein to removal of terminal sialic acid, as in A. This is a probabilistic family-level inference, not a definitive functional assignment from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence architecture and the known functions of related viral surface glycoproteins meaningfully favor A over the soluble Fe-S enzyme, lipid-transforming enzyme, and NAD-dependent sugar enzyme described in B-D; access to this exact protein's database entry is not required to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, A is the one consistent with the inferred viral membrane glycoprotein function.


### Important caveats

- The sequence-based family and function inference is not conclusive on its own; the reviewer-only annotation provides direct support for the key.
- The cited annotation is experimental-evidence-coded, but the underlying primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane anchor followed by a long, glycosylation-rich extracellular protein region, consistent with a viral surface glycoprotein. Transferable knowledge of viral hemagglutinin-neuraminidase proteins links that kind of protein to removal of terminal sialic acid, as in A. This is a probabilistic family-level inference, not a definitive functional assignment from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and the known functions of related viral surface glycoproteins meaningfully favor A over the soluble Fe-S enzyme, lipid-transforming enzyme, and NAD-dependent sugar enzyme described in B-D; access to this exact protein's database entry is not required to distinguish the offered choices."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the sialidase reaction in choice A and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence-based family and function inference is not conclusive on its own; the reviewer-only annotation provides direct support for the key.",
    "The cited annotation is experimental-evidence-coded, but the underlying primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, A is the one consistent with the inferred viral membrane glycoprotein function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the sialidase reaction in choice A and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane anchor followed by a long, glycosylation-rich extracellular protein region, consistent with a viral surface glycoprotein. Transferable knowledge of viral hemagglutinin-neuraminidase proteins links that kind of protein to removal of terminal sialic acid, as in A. This is a probabilistic family-level inference, not a definitive functional assignment from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and the known functions of related viral surface glycoproteins meaningfully favor A over the soluble Fe-S enzyme, lipid-transforming enzyme, and NAD-dependent sugar enzyme described in B-D; access to this exact protein's database entry is not required to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, A is the one consistent with the inferred viral membrane glycoprotein function."
  },
  "important_caveats": [
    "The sequence-based family and function inference is not conclusive on its own; the reviewer-only annotation provides direct support for the key.",
    "The cited annotation is experimental-evidence-coded, but the underlying primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9WAF5 (HN_MUMPV, Mumps orthorubulavirus Hemagglutinin-neuraminidase, EC 3.2.1.18) matches the supplied 582-aa sequence exactly (SHA-256 confirmed). The catalytic activity annotation (C5, H4) is stated verbatim as option A, supported by experimental evidence (ECO:0000269|PubMed:39088577). The sequence comparison is 'matched' in both current and historical snapshots.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQ) immediately followed by a hydrophobic transmembrane anchor. This topology is characteristic of paramyxovirus HN and F surface glycoproteins. The total length (~582 AA) matches paramyxovirus HN (influenza NA is ~470 AA; bacterial sialidases are typically soluble). In the C-terminal domain, the conserved 'RLLYY' motif (part of the neuraminidase active site in paramyxovirus HN) is clearly present, along with the characteristic C-terminal domain architecture of paramyxovirus neuraminidases. These features collectively identify the protein as a viral neuraminidase/sialidase (option A). Option B (taurine dioxygenase) requires Fe-S cluster motifs and is a small soluble enzyme. Option C (lipoxygenase-like) requires a different domain architecture and is typically >700 AA. Option D (fucose dehydrogenase) requires a Rossmann-fold NAD-binding motif (GxGxxG) and is a soluble cytoplasmic enzyme. None of these features are present. The type II membrane topology + ~580 AA length + RLLYY neuraminidase motif is a family-level pattern transferable from knowledge of other paramyxovirus HN proteins (NDV, measles, human parainfluenza) that meaningfully distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the type II membrane protein topology, the characteristic length, and the conserved neuraminidase catalytic motifs (RLLYY) from general knowledge of paramyxovirus HN proteins (e.g., NDV HN, measles HN). These family-level features are sufficient to select the sialidase/neuraminidase option over the three non-membrane, non-sialidase alternatives without recalling the specific UniProt entry for mumps HN.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (B, C, D) describe enzymes with fundamentally different topologies, sizes, and cofactor requirements that are clearly incompatible with the observed sequence features. Only option A is consistent with a type II membrane glycoprotein of ~580 AA bearing neuraminidase motifs.


### Important caveats

- The 'NPPY' catalytic tetrad characteristic of NDV HN is not perfectly conserved in mumps HN; however, the RLLYY motif and overall domain architecture are sufficient for family-level identification.
- The evidence for EC 3.2.1.18 assignment is experimental (PubMed:39088577, 2024), which is relatively recent; older annotations of mumps HN neuraminidase activity were primarily based on sequence similarity to other paramyxovirus HN proteins.
- The reviewer-only evidence confirms the identity but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable knowledge of paramyxovirus HN proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQ) immediately followed by a hydrophobic transmembrane anchor. This topology is characteristic of paramyxovirus HN and F surface glycoproteins. The total length (~582 AA) matches paramyxovirus HN (influenza NA is ~470 AA; bacterial sialidases are typically soluble). In the C-terminal domain, the conserved 'RLLYY' motif (part of the neuraminidase active site in paramyxovirus HN) is clearly present, along with the characteristic C-terminal domain architecture of paramyxovirus neuraminidases. These features collectively identify the protein as a viral neuraminidase/sialidase (option A). Option B (taurine dioxygenase) requires Fe-S cluster motifs and is a small soluble enzyme. Option C (lipoxygenase-like) requires a different domain architecture and is typically >700 AA. Option D (fucose dehydrogenase) requires a Rossmann-fold NAD-binding motif (GxGxxG) and is a soluble cytoplasmic enzyme. None of these features are present. The type II membrane topology + ~580 AA length + RLLYY neuraminidase motif is a family-level pattern transferable from knowledge of other paramyxovirus HN proteins (NDV, measles, human parainfluenza) that meaningfully distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the type II membrane protein topology, the characteristic length, and the conserved neuraminidase catalytic motifs (RLLYY) from general knowledge of paramyxovirus HN proteins (e.g., NDV HN, measles HN). These family-level features are sufficient to select the sialidase/neuraminidase option over the three non-membrane, non-sialidase alternatives without recalling the specific UniProt entry for mumps HN."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9WAF5 (HN_MUMPV, Mumps orthorubulavirus Hemagglutinin-neuraminidase, EC 3.2.1.18) matches the supplied 582-aa sequence exactly (SHA-256 confirmed). The catalytic activity annotation (C5, H4) is stated verbatim as option A, supported by experimental evidence (ECO:0000269|PubMed:39088577). The sequence comparison is 'matched' in both current and historical snapshots."
  },
  "important_caveats": [
    "The 'NPPY' catalytic tetrad characteristic of NDV HN is not perfectly conserved in mumps HN; however, the RLLYY motif and overall domain architecture are sufficient for family-level identification.",
    "The evidence for EC 3.2.1.18 assignment is experimental (PubMed:39088577, 2024), which is relatively recent; older annotations of mumps HN neuraminidase activity were primarily based on sequence similarity to other paramyxovirus HN proteins.",
    "The reviewer-only evidence confirms the identity but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable knowledge of paramyxovirus HN proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) describe enzymes with fundamentally different topologies, sizes, and cofactor requirements that are clearly incompatible with the observed sequence features. Only option A is consistent with a type II membrane glycoprotein of ~580 AA bearing neuraminidase motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9WAF5 (HN_MUMPV, Mumps orthorubulavirus Hemagglutinin-neuraminidase, EC 3.2.1.18) matches the supplied 582-aa sequence exactly (SHA-256 confirmed). The catalytic activity annotation (C5, H4) is stated verbatim as option A, supported by experimental evidence (ECO:0000269|PubMed:39088577). The sequence comparison is 'matched' in both current and historical snapshots.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQ) immediately followed by a hydrophobic transmembrane anchor. This topology is characteristic of paramyxovirus HN and F surface glycoproteins. The total length (~582 AA) matches paramyxovirus HN (influenza NA is ~470 AA; bacterial sialidases are typically soluble). In the C-terminal domain, the conserved 'RLLYY' motif (part of the neuraminidase active site in paramyxovirus HN) is clearly present, along with the characteristic C-terminal domain architecture of paramyxovirus neuraminidases. These features collectively identify the protein as a viral neuraminidase/sialidase (option A). Option B (taurine dioxygenase) requires Fe-S cluster motifs and is a small soluble enzyme. Option C (lipoxygenase-like) requires a different domain architecture and is typically >700 AA. Option D (fucose dehydrogenase) requires a Rossmann-fold NAD-binding motif (GxGxxG) and is a soluble cytoplasmic enzyme. None of these features are present. The type II membrane topology + ~580 AA length + RLLYY neuraminidase motif is a family-level pattern transferable from knowledge of other paramyxovirus HN proteins (NDV, measles, human parainfluenza) that meaningfully distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the type II membrane protein topology, the characteristic length, and the conserved neuraminidase catalytic motifs (RLLYY) from general knowledge of paramyxovirus HN proteins (e.g., NDV HN, measles HN). These family-level features are sufficient to select the sialidase/neuraminidase option over the three non-membrane, non-sialidase alternatives without recalling the specific UniProt entry for mumps HN."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) describe enzymes with fundamentally different topologies, sizes, and cofactor requirements that are clearly incompatible with the observed sequence features. Only option A is consistent with a type II membrane glycoprotein of ~580 AA bearing neuraminidase motifs."
  },
  "important_caveats": [
    "The 'NPPY' catalytic tetrad characteristic of NDV HN is not perfectly conserved in mumps HN; however, the RLLYY motif and overall domain architecture are sufficient for family-level identification.",
    "The evidence for EC 3.2.1.18 assignment is experimental (PubMed:39088577, 2024), which is relatively recent; older annotations of mumps HN neuraminidase activity were primarily based on sequence similarity to other paramyxovirus HN proteins.",
    "The reviewer-only evidence confirms the identity but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable knowledge of paramyxovirus HN proteins."
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
  "benchmark_sequence_length": 582,
  "benchmark_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "current_entry_audit": {
    "entryVersion": 132,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 582,
  "current_source_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 130,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9WAF5",
  "selected_historical_entry_version": 130,
  "selected_historical_record_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "selected_historical_source_sequence_length": 582,
  "selected_historical_source_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "selected_historical_version": {
    "accession": "Q9WAF5",
    "database": "Swiss-Prot",
    "entryVersion": 130,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9WAF5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":132,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\"],\"scientificName\":\"Mumps orthorubulavirus\",\"taxonId\":2560602}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39088577\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39088577\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Takahashi T.\",\"Kurebayashi Y.\",\"Otsubo T.\",\"Ikeda K.\",\"Konagaya K.\",\"Suzuki S.\",\"Yamazaki M.\",\"Suzuki K.\",\"Narimichi Y.\",\"Minami A.\",\"Takeuchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39088577\"},{\"database\":\"DOI\",\"id\":\"10.1093/glycob/cwae059\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39088577\",\"journal\":\"Glycobiology\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Novel sialidase inhibitors suppress mumps virus replication and infection.\",\"volume\":\"34\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"13V165E2\"}],\"referenceNumber\":6,\"referencePositions\":[\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H1",
  "excerpt": "ID   HN_MUMPV                Reviewed;         582 AA.\nAC   Q9WAF5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1999, sequence version 1.\nDT   28-JAN-2026, entry version 130.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};\nGN   Name=HN {ECO:0000312|EMBL:BAG84572.1};\nOS   Mumps orthorubulavirus (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis.\nOX   NCBI_TaxID=2560602;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H3",
  "excerpt": "RN   [6]\nRP   CATALYTIC ACTIVITY.\nRC   STRAIN=13V165E2;\nRX   PubMed=39088577; DOI=10.1093/glycob/cwae059;\nRA   Takahashi T., Kurebayashi Y., Otsubo T., Ikeda K., Konagaya K., Suzuki S.,\nRA   Yamazaki M., Suzuki K., Narimichi Y., Minami A., Takeuchi H.;\nRT   \"Novel sialidase inhibitors suppress mumps virus replication and\nRT   infection.\";\nRL   Glycobiology 34:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "entry_version": 130,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-\nCC         (2->8)- glycosidic linkages of terminal sialic acid residues in\nCC         oligosaccharides, glycoproteins, glycolipids, colominic acid and\nCC         synthetic substrates.; EC=3.2.1.18;\nCC         Evidence={ECO:0000269|PubMed:39088577};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
