# EC_number_0197

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0197.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.18

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTISDNATFAPGPVINVADKKTFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQLSSITDKIRESANMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTSKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYISTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. 3.2.1.18
B. 3.2.1.20
C. 1.8.1.9
D. 2.3.1.312
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation assigns EC 3.2.1.18 and describes hydrolysis of terminal sialic-acid linkages. The annotation is explicitly transferred by similarity from another UniProt protein (ECO:0000250), so it supports the key as a database/computational annotation rather than establishing direct experimental evidence for this exact sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic membrane-anchor-like segment followed by a large extracellular enzyme domain, a pattern consistent with paramyxovirus hemagglutinin-neuraminidase (HN) proteins. Transferable knowledge of this protein family links its neuraminidase activity to EC 3.2.1.18, distinguishing A from the unrelated alpha-glucosidase choice B and the non-glycosidase choices C and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence architecture and known HN function meaningfully favors A without requiring recall of this exact protein's database record. The sequence alone may not make family identification certain, but the alternatives and transferable family knowledge support a defensible choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options classify distinct activities, and the HN-family inference favors the sialidase EC number rather than another listed choice.


### Important caveats

- The supplied source annotations are similarity-transferred, not direct experimental evidence for this exact protein.
- The source record matches the supplied sequence, but its annotation does not by itself establish the author's original source snapshot.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane-anchor-like segment followed by a large extracellular enzyme domain, a pattern consistent with paramyxovirus hemagglutinin-neuraminidase (HN) proteins. Transferable knowledge of this protein family links its neuraminidase activity to EC 3.2.1.18, distinguishing A from the unrelated alpha-glucosidase choice B and the non-glycosidase choices C and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence architecture and known HN function meaningfully favors A without requiring recall of this exact protein's database record. The sequence alone may not make family identification certain, but the alternatives and transferable family knowledge support a defensible choice."
  },
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.2.1.18 and describes hydrolysis of terminal sialic-acid linkages. The annotation is explicitly transferred by similarity from another UniProt protein (ECO:0000250), so it supports the key as a database/computational annotation rather than establishing direct experimental evidence for this exact sequence."
  },
  "important_caveats": [
    "The supplied source annotations are similarity-transferred, not direct experimental evidence for this exact protein.",
    "The source record matches the supplied sequence, but its annotation does not by itself establish the author's original source snapshot."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options classify distinct activities, and the HN-family inference favors the sialidase EC number rather than another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.2.1.18 and describes hydrolysis of terminal sialic-acid linkages. The annotation is explicitly transferred by similarity from another UniProt protein (ECO:0000250), so it supports the key as a database/computational annotation rather than establishing direct experimental evidence for this exact sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane-anchor-like segment followed by a large extracellular enzyme domain, a pattern consistent with paramyxovirus hemagglutinin-neuraminidase (HN) proteins. Transferable knowledge of this protein family links its neuraminidase activity to EC 3.2.1.18, distinguishing A from the unrelated alpha-glucosidase choice B and the non-glycosidase choices C and D.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence architecture and known HN function meaningfully favors A without requiring recall of this exact protein's database record. The sequence alone may not make family identification certain, but the alternatives and transferable family knowledge support a defensible choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options classify distinct activities, and the HN-family inference favors the sialidase EC number rather than another listed choice."
  },
  "important_caveats": [
    "The supplied source annotations are similarity-transferred, not direct experimental evidence for this exact protein.",
    "The source record matches the supplied sequence, but its annotation does not by itself establish the author's original source snapshot."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5SC51 (HN_MUMPZ) annotates this 582-aa sequence as Hemagglutinin-neuraminidase with EC 3.2.1.18. The annotation is based on similarity inference (ECO:0000250 from Q9WAF5, another mumps HN), not direct experimental measurement, but it is consistent across both current and historical entries and the catalytic activity description (hydrolysis of sialic acid glycosidic linkages) matches EC 3.2.1.18. The sequence match is confirmed.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTISDNATFAPGPVINVADKK), followed by a transmembrane anchor (TFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQ...), then a large C-terminal ectodomain with multiple N-glycosylation sequons. This architecture is a hallmark of paramyxovirus surface glycoproteins (HN and F), not of cytoplasmic/lysosomal enzymes like alpha-galactosidase (3.2.1.20), thioredoxin reductase (1.8.1.9), or acyltransferases (2.3.1.312). Within the ectodomain, degenerate but recognizable sialidase (GH33) motifs appear: 'FYFTG' as a variant of the canonical F-Y-G-R-Y motif (motif 2), and R-Y-Y patterns (e.g., 'RLLYYQRSTSWWPY') corresponding to the R-Y-R-Y motif 1. The ~582-aa length and heavy N-glycosylation are consistent with paramyxovirus HN. These features collectively distinguish 3.2.1.18 (sialidase, GH33 beta-propeller) from 3.2.1.20 (alpha-galactosidase, GH27/GH36, soluble, different fold), from 1.8.1.9 (FAD/NADPH oxidoreductase, cytoplasmic), and from 2.3.1.312 (acyltransferase, different EC class).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the type II membrane protein architecture characteristic of paramyxovirus HN proteins, identify degenerate sialidase motifs (FYFTG as FYGRY variant, R-Y-Y patterns) in the ectodomain, and use the overall size and glycosylation pattern to place this in the GH33 sialidase family. This family-level and architectural inference meaningfully distinguishes 3.2.1.18 from the other three options without requiring recall of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The type II membrane protein architecture and sialidase-like motifs clearly point to a paramyxovirus HN (3.2.1.18) over alpha-galactosidase (soluble, different fold), thioredoxin reductase (cytoplasmic oxidoreductase), or an acyltransferase (different EC class). No other option is defensible given the sequence features.


### Important caveats

- The EC annotation in UniProt is based on similarity inference (ECO:0000250 from Q9WAF5), not direct experimental verification of this specific strain's sialidase activity.
- The sialidase motifs in this particular mumps strain (L-Zagreb vaccine) are somewhat degenerate (FYFTG rather than canonical FYGRY), making motif recognition less straightforward but still identifiable to someone familiar with paramyxovirus HN family variation.
- The identity of the protein as mumps HN was not provided to the evaluated model; the inference must come from sequence features and family knowledge alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTISDNATFAPGPVINVADKK), followed by a transmembrane anchor (TFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQ...), then a large C-terminal ectodomain with multiple N-glycosylation sequons. This architecture is a hallmark of paramyxovirus surface glycoproteins (HN and F), not of cytoplasmic/lysosomal enzymes like alpha-galactosidase (3.2.1.20), thioredoxin reductase (1.8.1.9), or acyltransferases (2.3.1.312). Within the ectodomain, degenerate but recognizable sialidase (GH33) motifs appear: 'FYFTG' as a variant of the canonical F-Y-G-R-Y motif (motif 2), and R-Y-Y patterns (e.g., 'RLLYYQRSTSWWPY') corresponding to the R-Y-R-Y motif 1. The ~582-aa length and heavy N-glycosylation are consistent with paramyxovirus HN. These features collectively distinguish 3.2.1.18 (sialidase, GH33 beta-propeller) from 3.2.1.20 (alpha-galactosidase, GH27/GH36, soluble, different fold), from 1.8.1.9 (FAD/NADPH oxidoreductase, cytoplasmic), and from 2.3.1.312 (acyltransferase, different EC class).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the type II membrane protein architecture characteristic of paramyxovirus HN proteins, identify degenerate sialidase motifs (FYFTG as FYGRY variant, R-Y-Y patterns) in the ectodomain, and use the overall size and glycosylation pattern to place this in the GH33 sialidase family. This family-level and architectural inference meaningfully distinguishes 3.2.1.18 from the other three options without requiring recall of this specific entry's annotation."
  },
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5SC51 (HN_MUMPZ) annotates this 582-aa sequence as Hemagglutinin-neuraminidase with EC 3.2.1.18. The annotation is based on similarity inference (ECO:0000250 from Q9WAF5, another mumps HN), not direct experimental measurement, but it is consistent across both current and historical entries and the catalytic activity description (hydrolysis of sialic acid glycosidic linkages) matches EC 3.2.1.18. The sequence match is confirmed."
  },
  "important_caveats": [
    "The EC annotation in UniProt is based on similarity inference (ECO:0000250 from Q9WAF5), not direct experimental verification of this specific strain's sialidase activity.",
    "The sialidase motifs in this particular mumps strain (L-Zagreb vaccine) are somewhat degenerate (FYFTG rather than canonical FYGRY), making motif recognition less straightforward but still identifiable to someone familiar with paramyxovirus HN family variation.",
    "The identity of the protein as mumps HN was not provided to the evaluated model; the inference must come from sequence features and family knowledge alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The type II membrane protein architecture and sialidase-like motifs clearly point to a paramyxovirus HN (3.2.1.18) over alpha-galactosidase (soluble, different fold), thioredoxin reductase (cytoplasmic oxidoreductase), or an acyltransferase (different EC class). No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5SC51 (HN_MUMPZ) annotates this 582-aa sequence as Hemagglutinin-neuraminidase with EC 3.2.1.18. The annotation is based on similarity inference (ECO:0000250 from Q9WAF5, another mumps HN), not direct experimental measurement, but it is consistent across both current and historical entries and the catalytic activity description (hydrolysis of sialic acid glycosidic linkages) matches EC 3.2.1.18. The sequence match is confirmed.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTISDNATFAPGPVINVADKK), followed by a transmembrane anchor (TFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQ...), then a large C-terminal ectodomain with multiple N-glycosylation sequons. This architecture is a hallmark of paramyxovirus surface glycoproteins (HN and F), not of cytoplasmic/lysosomal enzymes like alpha-galactosidase (3.2.1.20), thioredoxin reductase (1.8.1.9), or acyltransferases (2.3.1.312). Within the ectodomain, degenerate but recognizable sialidase (GH33) motifs appear: 'FYFTG' as a variant of the canonical F-Y-G-R-Y motif (motif 2), and R-Y-Y patterns (e.g., 'RLLYYQRSTSWWPY') corresponding to the R-Y-R-Y motif 1. The ~582-aa length and heavy N-glycosylation are consistent with paramyxovirus HN. These features collectively distinguish 3.2.1.18 (sialidase, GH33 beta-propeller) from 3.2.1.20 (alpha-galactosidase, GH27/GH36, soluble, different fold), from 1.8.1.9 (FAD/NADPH oxidoreductase, cytoplasmic), and from 2.3.1.312 (acyltransferase, different EC class).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the type II membrane protein architecture characteristic of paramyxovirus HN proteins, identify degenerate sialidase motifs (FYFTG as FYGRY variant, R-Y-Y patterns) in the ectodomain, and use the overall size and glycosylation pattern to place this in the GH33 sialidase family. This family-level and architectural inference meaningfully distinguishes 3.2.1.18 from the other three options without requiring recall of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The type II membrane protein architecture and sialidase-like motifs clearly point to a paramyxovirus HN (3.2.1.18) over alpha-galactosidase (soluble, different fold), thioredoxin reductase (cytoplasmic oxidoreductase), or an acyltransferase (different EC class). No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The EC annotation in UniProt is based on similarity inference (ECO:0000250 from Q9WAF5), not direct experimental verification of this specific strain's sialidase activity.",
    "The sialidase motifs in this particular mumps strain (L-Zagreb vaccine) are somewhat degenerate (FYFTG rather than canonical FYGRY), making motif recognition less straightforward but still identifiable to someone familiar with paramyxovirus HN family variation.",
    "The identity of the protein as mumps HN was not provided to the evaluated model; the inference must come from sequence features and family knowledge alone."
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
  "benchmark_sequence_sha256": "e96cff28d63a847ba629b286f3a32c333c53ea1cb31fc62f1e0624df41dc039e",
  "current_entry_audit": {
    "entryVersion": 107,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 582,
  "current_source_sequence_sha256": "e96cff28d63a847ba629b286f3a32c333c53ea1cb31fc62f1e0624df41dc039e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 105,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5SC51",
  "selected_historical_entry_version": 105,
  "selected_historical_record_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "selected_historical_source_sequence_length": 582,
  "selected_historical_source_sequence_sha256": "e96cff28d63a847ba629b286f3a32c333c53ea1cb31fc62f1e0624df41dc039e",
  "selected_historical_version": {
    "accession": "Q5SC51",
    "database": "Swiss-Prot",
    "entryVersion": 105,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPZ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5SC51\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":107,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"name\":\"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H1",
  "excerpt": "ID   HN_MUMPZ                Reviewed;         582 AA.\nAC   Q5SC51;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 105.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};\nGN   Name=HN;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-\nCC         (2->8)- glycosidic linkages of terminal sialic acid residues in\nCC         oligosaccharides, glycoproteins, glycolipids, colominic acid and\nCC         synthetic substrates.; EC=3.2.1.18;\nCC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 197. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
