# cofactor_0024

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0024.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASGQMAPSLLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTSPAPQLSASHQHQAQQQQQQTKQPQQPYDPQQDQVPSTSTASSSKPAADPVYNLPNAVSVARLVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK

[Multiple Choices]
A. Fe cation
B. tungstopterin
C. pyridoxal 5'-phosphate
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

> The sequence-matched UniProt record annotates Mn(2+) as the cofactor. The annotation is transferred by similarity to another UniProt protein, so it supports the key but is not direct experimental evidence for this sequence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s long hydrophobic regions are consistent with an integral-membrane enzyme involved in lipid metabolism. Transferable knowledge of membrane phospholipid-synthase families makes a divalent metal such as Mn(2+) more plausible than PLP or tungstopterin; Fe is a less typical choice for this kind of catalytic chemistry. Thus D is meaningfully favored among these options, though the sequence alone does not prove the metal identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the choices can favor Mn(2+) without recalling this exact protein’s annotation. The inference is probabilistic, not a substitute for direct cofactor characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is as well supported by the transferable family-level inference, although the sequence alone does not establish Mn(2+) with certainty.


### Important caveats

- The cited cofactor annotation is similarity-based (ECO:0000250), not direct experimental evidence for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s long hydrophobic regions are consistent with an integral-membrane enzyme involved in lipid metabolism. Transferable knowledge of membrane phospholipid-synthase families makes a divalent metal such as Mn(2+) more plausible than PLP or tungstopterin; Fe is a less typical choice for this kind of catalytic chemistry. Thus D is meaningfully favored among these options, though the sequence alone does not prove the metal identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the choices can favor Mn(2+) without recalling this exact protein’s annotation. The inference is probabilistic, not a substitute for direct cofactor characterization."
  },
  "case_id": "cofactor_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mn(2+) as the cofactor. The annotation is transferred by similarity to another UniProt protein, so it supports the key but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The cited cofactor annotation is similarity-based (ECO:0000250), not direct experimental evidence for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is as well supported by the transferable family-level inference, although the sequence alone does not establish Mn(2+) with certainty."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mn(2+) as the cofactor. The annotation is transferred by similarity to another UniProt protein, so it supports the key but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s long hydrophobic regions are consistent with an integral-membrane enzyme involved in lipid metabolism. Transferable knowledge of membrane phospholipid-synthase families makes a divalent metal such as Mn(2+) more plausible than PLP or tungstopterin; Fe is a less typical choice for this kind of catalytic chemistry. Thus D is meaningfully favored among these options, though the sequence alone does not prove the metal identity.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the choices can favor Mn(2+) without recalling this exact protein’s annotation. The inference is probabilistic, not a substitute for direct cofactor characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is as well supported by the transferable family-level inference, although the sequence alone does not establish Mn(2+) with certainty."
  },
  "important_caveats": [
    "The cited cofactor annotation is similarity-based (ECO:0000250), not direct experimental evidence for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0A2K3D1C8) annotates the protein as Cardiolipin synthase (CMP-forming), EC 2.7.8.41, with cofactor Mn(2+) (ChEBI:CHEBI:29035). The evidence code is ECO:0000250 (inferred by similarity from Q93YW7), so this is a computational/transferred annotation rather than direct experimental evidence on this exact protein. However, the annotation is consistent with the broader literature on CMP-forming cardiolipin synthases, which are known to require Mn(2+). The EC assignment itself is supported by PubMed:26793177 (functional characterization in Chlamydomonas reinhardtii). The sequence matches the benchmark exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches (e.g., 'LVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK'), strongly indicating a membrane-associated enzyme, likely involved in lipid metabolism. Among the four choices: (B) tungstopterin is restricted to specific oxidoreductase families (formate dehydrogenases, aldehyde oxidoreductases) with characteristic Cys-rich motifs absent here; (C) PLP-dependent enzymes require a specific lysine in a conserved context and motifs like 'GGG' in aminotransferase folds, which are not present. This leaves A (Fe) and D (Mn2+). The absence of redox-associated motifs (no Cys clusters for Fe-S, no His-rich iron-binding sites, no oxygenase signatures) argues against Fe. Membrane-associated phospholipid-metabolizing enzymes (phospholipases, lipid phosphatases, phosphatidyltransferases, cardiolipin synthases) predominantly use divalent cations, especially Mn(2+) or Mg(2+), as learned from numerous family members. Among the offered choices, Mn(2+) is the only divalent cation and the cofactor most associated with phospholipid-related membrane enzymes. This family-level inference meaningfully distinguishes D from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the membrane-associated character of the sequence (multiple TM-like hydrophobic segments), the absence of PLP/tungstopterin/iron-specific motifs, and the well-established pattern that phospholipid-related membrane enzymes preferentially use Mn(2+) to select D over A, B, and C. The inference relies on family-level knowledge of lipid-metabolizing enzymes and cofactor preferences, not on memorizing this exact protein's annotation. The limitation is that positively identifying the protein as a cardiolipin synthase specifically from sequence is uncertain; the argument operates at the level of 'membrane lipid-metabolizing enzyme' rather than 'CLS family member.' Nevertheless, this broader family-level inference is sufficient to distinguish among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (tungstopterin) and C (PLP) can be confidently excluded by the absence of their characteristic motifs. Option A (Fe) is less likely given the membrane-lipid enzyme context and absence of redox motifs. Mn(2+) is the most defensible choice among the four. No two options are equally supported by the available sequence evidence.


### Important caveats

- The UniProt cofactor annotation (ECO:0000250) is transferred by similarity from Q93YW7, not directly experimentally determined for this exact protein. The EC assignment (2.7.8.41) is supported by PubMed:26793177, but the specific Mn(2+) dependence is inferred.
- The sequence-to-family identification (cardiolipin synthase) is not trivially obvious from sequence motifs alone; the reasoning operates at the broader level of 'membrane-associated phospholipid enzyme' rather than precise CLS family recognition.
- The distinction between Mn(2+) and Mg(2+) (the latter not offered) is not addressed by the choices, but this does not affect the answerability among the given options.
- The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., 'LVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK'), strongly indicating a membrane-associated enzyme, likely involved in lipid metabolism. Among the four choices: (B) tungstopterin is restricted to specific oxidoreductase families (formate dehydrogenases, aldehyde oxidoreductases) with characteristic Cys-rich motifs absent here; (C) PLP-dependent enzymes require a specific lysine in a conserved context and motifs like 'GGG' in aminotransferase folds, which are not present. This leaves A (Fe) and D (Mn2+). The absence of redox-associated motifs (no Cys clusters for Fe-S, no His-rich iron-binding sites, no oxygenase signatures) argues against Fe. Membrane-associated phospholipid-metabolizing enzymes (phospholipases, lipid phosphatases, phosphatidyltransferases, cardiolipin synthases) predominantly use divalent cations, especially Mn(2+) or Mg(2+), as learned from numerous family members. Among the offered choices, Mn(2+) is the only divalent cation and the cofactor most associated with phospholipid-related membrane enzymes. This family-level inference meaningfully distinguishes D from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the membrane-associated character of the sequence (multiple TM-like hydrophobic segments), the absence of PLP/tungstopterin/iron-specific motifs, and the well-established pattern that phospholipid-related membrane enzymes preferentially use Mn(2+) to select D over A, B, and C. The inference relies on family-level knowledge of lipid-metabolizing enzymes and cofactor preferences, not on memorizing this exact protein's annotation. The limitation is that positively identifying the protein as a cardiolipin synthase specifically from sequence is uncertain; the argument operates at the level of 'membrane lipid-metabolizing enzyme' rather than 'CLS family member.' Nevertheless, this broader family-level inference is sufficient to distinguish among the four offered choices."
  },
  "case_id": "cofactor_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A2K3D1C8) annotates the protein as Cardiolipin synthase (CMP-forming), EC 2.7.8.41, with cofactor Mn(2+) (ChEBI:CHEBI:29035). The evidence code is ECO:0000250 (inferred by similarity from Q93YW7), so this is a computational/transferred annotation rather than direct experimental evidence on this exact protein. However, the annotation is consistent with the broader literature on CMP-forming cardiolipin synthases, which are known to require Mn(2+). The EC assignment itself is supported by PubMed:26793177 (functional characterization in Chlamydomonas reinhardtii). The sequence matches the benchmark exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt cofactor annotation (ECO:0000250) is transferred by similarity from Q93YW7, not directly experimentally determined for this exact protein. The EC assignment (2.7.8.41) is supported by PubMed:26793177, but the specific Mn(2+) dependence is inferred.",
    "The sequence-to-family identification (cardiolipin synthase) is not trivially obvious from sequence motifs alone; the reasoning operates at the broader level of 'membrane-associated phospholipid enzyme' rather than precise CLS family recognition.",
    "The distinction between Mn(2+) and Mg(2+) (the latter not offered) is not addressed by the choices, but this does not affect the answerability among the given options.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (tungstopterin) and C (PLP) can be confidently excluded by the absence of their characteristic motifs. Option A (Fe) is less likely given the membrane-lipid enzyme context and absence of redox motifs. Mn(2+) is the most defensible choice among the four. No two options are equally supported by the available sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A2K3D1C8) annotates the protein as Cardiolipin synthase (CMP-forming), EC 2.7.8.41, with cofactor Mn(2+) (ChEBI:CHEBI:29035). The evidence code is ECO:0000250 (inferred by similarity from Q93YW7), so this is a computational/transferred annotation rather than direct experimental evidence on this exact protein. However, the annotation is consistent with the broader literature on CMP-forming cardiolipin synthases, which are known to require Mn(2+). The EC assignment itself is supported by PubMed:26793177 (functional characterization in Chlamydomonas reinhardtii). The sequence matches the benchmark exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., 'LVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK'), strongly indicating a membrane-associated enzyme, likely involved in lipid metabolism. Among the four choices: (B) tungstopterin is restricted to specific oxidoreductase families (formate dehydrogenases, aldehyde oxidoreductases) with characteristic Cys-rich motifs absent here; (C) PLP-dependent enzymes require a specific lysine in a conserved context and motifs like 'GGG' in aminotransferase folds, which are not present. This leaves A (Fe) and D (Mn2+). The absence of redox-associated motifs (no Cys clusters for Fe-S, no His-rich iron-binding sites, no oxygenase signatures) argues against Fe. Membrane-associated phospholipid-metabolizing enzymes (phospholipases, lipid phosphatases, phosphatidyltransferases, cardiolipin synthases) predominantly use divalent cations, especially Mn(2+) or Mg(2+), as learned from numerous family members. Among the offered choices, Mn(2+) is the only divalent cation and the cofactor most associated with phospholipid-related membrane enzymes. This family-level inference meaningfully distinguishes D from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the membrane-associated character of the sequence (multiple TM-like hydrophobic segments), the absence of PLP/tungstopterin/iron-specific motifs, and the well-established pattern that phospholipid-related membrane enzymes preferentially use Mn(2+) to select D over A, B, and C. The inference relies on family-level knowledge of lipid-metabolizing enzymes and cofactor preferences, not on memorizing this exact protein's annotation. The limitation is that positively identifying the protein as a cardiolipin synthase specifically from sequence is uncertain; the argument operates at the level of 'membrane lipid-metabolizing enzyme' rather than 'CLS family member.' Nevertheless, this broader family-level inference is sufficient to distinguish among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (tungstopterin) and C (PLP) can be confidently excluded by the absence of their characteristic motifs. Option A (Fe) is less likely given the membrane-lipid enzyme context and absence of redox motifs. Mn(2+) is the most defensible choice among the four. No two options are equally supported by the available sequence evidence."
  },
  "important_caveats": [
    "The UniProt cofactor annotation (ECO:0000250) is transferred by similarity from Q93YW7, not directly experimentally determined for this exact protein. The EC assignment (2.7.8.41) is supported by PubMed:26793177, but the specific Mn(2+) dependence is inferred.",
    "The sequence-to-family identification (cardiolipin synthase) is not trivially obvious from sequence motifs alone; the reasoning operates at the broader level of 'membrane-associated phospholipid enzyme' rather than precise CLS family recognition.",
    "The distinction between Mn(2+) and Mg(2+) (the latter not offered) is not addressed by the choices, but this does not affect the answerability among the given options.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model."
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
  "benchmark_sequence_length": 351,
  "benchmark_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-03-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 351,
  "current_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
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
  "requested_accession": "A0A2K3D1C8",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "selected_historical_source_sequence_length": 351,
  "selected_historical_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "selected_historical_version": {
    "accession": "A0A2K3D1C8",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_CHLRE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2K3D1C8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-03-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chlamydomonas smithii\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000006906\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Chlorophyta\",\"core chlorophytes\",\"Chlorophyceae\",\"CS clade\",\"Chlamydomonadales\",\"Chlamydomonadaceae\",\"Chlamydomonas\"],\"scientificName\":\"Chlamydomonas reinhardtii\",\"taxonId\":3055}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26793177\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93YW7\",\"source\":\"UniProtKB\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hung C.H.\",\"Kobayashi K.\",\"Wada H.\",\"Nakamura Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26793177\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2015.01542\"}],\"citationType\":\"journal article\",\"firstPage\":\"1542\",\"id\":\"26793177\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"1542\",\"publicationDate\":\"2015\",\"title\":\"Functional Specificity of Cardiolipin Synthase Revealed by the Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas reinhardtii.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   CRLS1_CHLRE             Reviewed;         351 AA.\nAC   A0A2K3D1C8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-MAR-2018, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS;\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};\nDE   Flags: Precursor;\nGN   ORFNames=CHLRE_13g604700v5 {ECO:0000312|EMBL:PNW74341.1};\nOS   Chlamydomonas reinhardtii (Chlamydomonas smithii).\nOC   Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae;\nOC   CS clade; Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas.\nOX   NCBI_TaxID=3055 {ECO:0000312|Proteomes:UP000006906};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS;\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=26793177; DOI=10.3389/fmicb.2015.01542;\nRA   Hung C.H., Kobayashi K., Wada H., Nakamura Y.;\nRT   \"Functional Specificity of Cardiolipin Synthase Revealed by the\nRT   Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas\nRT   reinhardtii.\";\nRL   Front. Microbiol. 6:1542-1542(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000250|UniProtKB:Q93YW7};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
